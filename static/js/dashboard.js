// ─── STATE ────────────────────────────────────────────────────
let selectedStyle = 'infantil';
let selectedPackStyle = 'infantil';
let stickerCount = 9;
let currentSVG = null;
let currentStickers = [];
let currentPack = null;

// ─── TAB SWITCHING ────────────────────────────────────────────
function switchTab(tabName, linkEl) {
  // Hide all tabs
  document.querySelectorAll('.tab-content').forEach(t => t.style.display = 'none');
  // Show selected
  const target = document.getElementById('tab-' + tabName);
  if (target) target.style.display = 'block';
  
  // Update sidebar links
  document.querySelectorAll('.sidebar-link').forEach(l => l.classList.remove('active'));
  if (linkEl) linkEl.classList.add('active');

  // Update header title
  const titles = {
    drawing: '🎨 Gerador de Desenhos',
    stickers: '🧷 Cartela de Figurinhas',
    pack: '📦 Pacote Comercial',
    history: '📋 Histórico'
  };
  const h = document.getElementById('dash-title');
  if (h) h.textContent = titles[tabName] || 'Painel';

  return false;
}

// ─── STYLE SELECTION ──────────────────────────────────────────
function selectStyle(btn) {
  document.querySelectorAll('#tab-drawing .style-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  selectedStyle = btn.dataset.style;
}

function selectPackStyle(btn) {
  document.querySelectorAll('#tab-pack .style-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  selectedPackStyle = btn.dataset.style;
}

// ─── STICKER COUNT ────────────────────────────────────────────
function changeCount(delta) {
  stickerCount = Math.max(3, Math.min(12, stickerCount + delta));
  const el = document.getElementById('sticker-count');
  if (el) el.textContent = stickerCount;
}

// ─── GENERATE DRAWING ─────────────────────────────────────────
async function generateDrawing() {
  const prompt = document.getElementById('draw-prompt').value.trim();
  if (!prompt) {
    showNotif('Digite uma descrição para o desenho!', 'error');
    return;
  }

  const btn = document.getElementById('btn-generate');
  const btnText = document.getElementById('gen-btn-text');
  const spinner = document.getElementById('gen-spinner');

  btn.disabled = true;
  btnText.style.display = 'none';
  spinner.style.display = 'block';

  try {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, style: selectedStyle, category: selectedStyle, type: 'drawing' })
    });
    const data = await res.json();

    if (data.success) {
      currentSVG = data.svg;
      displayDrawing(data.svg, data.prompt);
      showNotif('✨ Desenho gerado com sucesso!', 'success');
      updateUsageBar();
    } else {
      if (data.upgrade) {
        showUpgradeModal();
      } else {
        showNotif(data.error || 'Erro ao gerar. Tente novamente.', 'error');
      }
    }
  } catch(e) {
    showNotif('Erro de conexão. Tente novamente.', 'error');
  } finally {
    btn.disabled = false;
    btnText.style.display = 'inline';
    spinner.style.display = 'none';
  }
}

function displayDrawing(svg, prompt) {
  document.getElementById('draw-placeholder').style.display = 'none';
  const result = document.getElementById('draw-result');
  result.style.display = 'block';
  
  const container = document.getElementById('result-image-container');
  container.innerHTML = svg;
  
  const label = document.getElementById('result-label');
  if (label) label.textContent = prompt ? `"${prompt}"` : 'Desenho gerado';
}

// ─── GENERATE STICKERS ────────────────────────────────────────
async function generateStickers() {
  const prompt = document.getElementById('sticker-prompt').value.trim();
  if (!prompt) {
    showNotif('Digite o tema das figurinhas!', 'error');
    return;
  }

  const btnText = document.getElementById('stk-btn-text');
  const spinner = document.getElementById('stk-spinner');
  btnText.style.display = 'none';
  spinner.style.display = 'block';

  const border = document.getElementById('border-toggle').checked;

  try {
    const res = await fetch('/api/generate-stickers', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, count: stickerCount, border })
    });
    const data = await res.json();

    if (data.success) {
      currentStickers = data.stickers;
      displayStickers(data.stickers, border);
      showNotif('🧷 Cartela criada com sucesso!', 'success');
      updateUsageBar();
    } else {
      if (data.upgrade) showUpgradeModal();
      else showNotif(data.error || 'Erro ao gerar.', 'error');
    }
  } catch(e) {
    showNotif('Erro de conexão. Tente novamente.', 'error');
  } finally {
    btnText.style.display = 'inline';
    spinner.style.display = 'none';
  }
}

function displayStickers(stickers, border) {
  document.getElementById('sticker-placeholder').style.display = 'none';
  document.getElementById('sticker-result').style.display = 'block';
  
  const grid = document.getElementById('sticker-grid');
  grid.innerHTML = '';
  
  stickers.forEach((stickerG, i) => {
    const item = document.createElement('div');
    item.className = 'sticker-item';
    
    const svg = `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">${stickerG}</svg>`;
    item.innerHTML = svg;
    grid.appendChild(item);
  });
}

// ─── GENERATE COMMERCIAL PACK ─────────────────────────────────
async function generatePack() {
  const prompt = document.getElementById('pack-prompt').value.trim();
  if (!prompt) {
    showNotif('Digite o tema do pacote!', 'error');
    return;
  }

  const btnText = document.getElementById('pack-btn-text');
  const spinner = document.getElementById('pack-spinner');
  btnText.style.display = 'none';
  spinner.style.display = 'block';

  try {
    const res = await fetch('/api/generate-pack', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, category: selectedPackStyle })
    });
    const data = await res.json();

    if (data.success) {
      currentPack = data;
      displayPack(data);
      showNotif('📦 Pacote comercial gerado!', 'success');
    } else {
      if (data.upgrade) showUpgradeModal();
      else showNotif(data.error || 'Erro ao gerar pacote.', 'error');
    }
  } catch(e) {
    showNotif('Erro de conexão. Tente novamente.', 'error');
  } finally {
    btnText.style.display = 'inline';
    spinner.style.display = 'none';
  }
}

function displayPack(data) {
  document.getElementById('pack-placeholder').style.display = 'none';
  document.getElementById('pack-result').style.display = 'block';

  const meta = document.getElementById('pack-meta');
  meta.innerHTML = `
    <div class="pack-product-name">📦 ${data.product_name}</div>
    
    <div class="pack-section-title">📝 Descrição para Etsy/KDP</div>
    <div class="pack-description">${data.description}</div>
    
    <div class="pack-section-title">🏷️ Tags SEO (${data.tags.length})</div>
    <div class="pack-tags-wrap">
      ${data.tags.map(t => `<span class="pack-tag">#${t}</span>`).join('')}
    </div>
    
    <button class="pack-copy-btn" onclick="copyPackInfo()">📋 Copiar Tudo para Área de Transferência</button>
  `;

  const grid = document.getElementById('pack-drawings-grid');
  grid.innerHTML = '';
  data.drawings.forEach((svg, i) => {
    const item = document.createElement('div');
    item.className = 'pack-drawing-item';
    item.innerHTML = `${svg}<div style="text-align:center;font-size:0.75rem;color:var(--text-muted);padding:6px 0">Desenho ${i+1}</div>`;
    grid.appendChild(item);
  });
}

function copyPackInfo() {
  if (!currentPack) return;
  const text = `NOME DO PRODUTO:\n${currentPack.product_name}\n\nDESCRIÇÃO:\n${currentPack.description}\n\nTAGS:\n${currentPack.tags.join(', ')}`;
  navigator.clipboard.writeText(text).then(() => {
    showNotif('📋 Copiado para a área de transferência!', 'success');
  });
}

// ─── DOWNLOAD FUNCTIONS ───────────────────────────────────────
function downloadSVG() {
  if (!currentSVG) return;
  const blob = new Blob([currentSVG], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'colorIA-desenho.svg';
  a.click();
  URL.revokeObjectURL(url);
  showNotif('✅ Imagem baixada com sucesso!', 'success');
}

function downloadPDF() {
  if (!currentSVG) return;
  const win = window.open('', '_blank');
  win.document.write(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>ColorIA - Desenho para Colorir</title>
      <style>
        body { margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        @page { size: A4; margin: 20mm; }
        @media print { body { margin: 0; } }
        .page { width: 170mm; padding: 10mm; text-align: center; }
        h2 { font-family: Arial, sans-serif; color: #7c3aed; font-size: 16px; margin-bottom: 20px; }
        svg { max-width: 100%; height: auto; }
        footer { margin-top: 20px; font-size: 11px; color: #666; font-family: Arial, sans-serif; }
      </style>
    </head>
    <body>
      <div class="page">
        <h2>✦ ColorIA — Desenho para Colorir</h2>
        ${currentSVG}
        <footer>Gerado em ColorIA.com.br | Imprima e divirta-se!</footer>
      </div>
    </body>
    </html>
  `);
  win.document.close();
  setTimeout(() => { win.print(); }, 500);
  showNotif('📄 Abrindo para impressão/PDF...', 'success');
}

function downloadStickerPDF() {
  if (!currentStickers.length) return;
  const stickerItems = currentStickers.map((g, i) => `
    <div class="sticker">
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        ${g}
      </svg>
    </div>
  `).join('');

  const win = window.open('', '_blank');
  win.document.write(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>ColorIA - Cartela de Figurinhas</title>
      <style>
        body { margin: 0; padding: 20mm; font-family: Arial, sans-serif; }
        @page { size: A4; margin: 15mm; }
        h2 { color: #7c3aed; text-align: center; margin-bottom: 20px; font-size: 16px; }
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .sticker { border: 2px dashed #ccc; border-radius: 50%; padding: 15px; aspect-ratio: 1; display: flex; align-items: center; justify-content: center; }
        .sticker svg { width: 100%; height: 100%; }
        footer { text-align: center; margin-top: 20px; font-size: 10px; color: #999; }
      </style>
    </head>
    <body>
      <h2>✦ ColorIA — Cartela de Figurinhas</h2>
      <div class="grid">${stickerItems}</div>
      <footer>Recorte ao longo das linhas pontilhadas | ColorIA.com.br</footer>
    </body>
    </html>
  `);
  win.document.close();
  setTimeout(() => win.print(), 500);
  showNotif('📄 Abrindo cartela para impressão...', 'success');
}

// ─── HISTORY ──────────────────────────────────────────────────
async function loadHistory() {
  const grid = document.getElementById('history-grid');
  grid.innerHTML = '<div class="loading-history">Carregando histórico...</div>';

  try {
    const res = await fetch('/api/history');
    const data = await res.json();

    if (data.success && data.generations.length > 0) {
      grid.innerHTML = '';
      data.generations.forEach(gen => {
        const item = document.createElement('div');
        item.className = 'history-item';
        item.onclick = () => {
          switchTab('drawing', document.querySelector('[data-tab="drawing"]'));
          currentSVG = gen.svg;
          displayDrawing(gen.svg, gen.prompt);
        };
        
        const date = new Date(gen.created_at).toLocaleDateString('pt-BR');
        item.innerHTML = `
          ${gen.svg}
          <div class="history-item-meta">
            <div class="history-item-prompt">${gen.prompt || 'Sem título'}</div>
            <div class="history-item-date">${date}</div>
          </div>
        `;
        grid.appendChild(item);
      });
    } else {
      grid.innerHTML = '<div class="loading-history">Nenhuma geração encontrada. Crie seu primeiro desenho!</div>';
    }
  } catch(e) {
    grid.innerHTML = '<div class="loading-history">Erro ao carregar histórico.</div>';
  }
}

// ─── UI HELPERS ───────────────────────────────────────────────
function showUpgradeModal() {
  document.getElementById('upgrade-modal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('upgrade-modal').style.display = 'none';
}

function showNotif(msg, type = 'success') {
  const existing = document.querySelector('.notif');
  if (existing) existing.remove();

  const notif = document.createElement('div');
  notif.className = `notif ${type}`;
  notif.innerHTML = `<span>${msg}</span>`;
  document.body.appendChild(notif);
  setTimeout(() => notif.remove(), 3500);
}

function updateUsageBar() {
  const fill = document.querySelector('.usage-fill');
  const label = document.querySelector('.usage-label');
  if (!fill || !label) return;
  
  const match = label.textContent.match(/(\d+)\/(\d+)/);
  if (match) {
    const current = parseInt(match[1]) + 1;
    const max = parseInt(match[2]);
    label.textContent = `${current}/${max} hoje`;
    fill.style.width = `${Math.min((current / max) * 100, 100)}%`;
  }
}

// ─── KEYBOARD SHORTCUTS ───────────────────────────────────────
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
    const activeTab = document.querySelector('.tab-content[style*="block"]');
    if (activeTab && activeTab.id === 'tab-drawing') generateDrawing();
    if (activeTab && activeTab.id === 'tab-stickers') generateStickers();
    if (activeTab && activeTab.id === 'tab-pack') generatePack();
  }
});

// Tip: Ctrl+Enter to generate
document.querySelectorAll('textarea').forEach(ta => {
  ta.title = 'Dica: Ctrl+Enter para gerar rapidamente';
});
