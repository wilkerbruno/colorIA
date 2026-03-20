# ✦ ColorIA — Gerador de Desenhos para Colorir com IA

Plataforma SaaS completa para gerar, baixar e vender desenhos para colorir e figurinhas imprimíveis.

---

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
- Python 3.9+
- pip

### 2. Instalar dependências
```bash
cd colorIA
pip install -r requirements.txt
```

### 3. Rodar o servidor
```bash
python app.py
```

### 4. Acessar
Abra o navegador em: **http://localhost:5000**

---

## 📁 Estrutura do Projeto

```
colorIA/
├── app.py                    # Backend Flask + API + banco de dados
├── requirements.txt          # Dependências Python
├── colorIA.db               # Banco de dados SQLite (criado automaticamente)
├── templates/
│   ├── index.html           # Landing page
│   ├── login.html           # Login + Cadastro
│   ├── dashboard.html       # Painel do usuário (app principal)
│   └── pricing.html         # Página de preços
└── static/
    ├── css/
    │   ├── main.css         # Estilos globais + landing + auth + pricing
    │   └── dashboard.css    # Estilos do painel do usuário
    └── js/
        ├── main.js          # JavaScript da landing page
        └── dashboard.js     # JavaScript do painel (interatividade completa)
```

---

## 💡 Funcionalidades Implementadas

### 🎨 Gerador de Desenhos
- Campo de texto para descrever o desenho
- 4 categorias: Infantil, Animais, Personagens, Educativo
- Geração de SVG vetorial (preto e branco, contornos fortes)
- Download em SVG/PNG e PDF (impressão A4)

### 🧷 Cartela de Figurinhas
- Gera de 3 a 12 figurinhas por cartela
- Borda tracejada para recorte
- Download em PDF pronto para impressão

### 📦 Pacote Comercial (Premium)
- Gera 10 desenhos relacionados ao tema
- Nome do produto otimizado
- Descrição completa para Etsy/KDP
- 13 tags SEO automaticamente geradas
- Botão para copiar tudo para a área de transferência

### 👤 Sistema de Usuário
- Cadastro e login com senha hasheada (SHA-256)
- Sessões seguras com Flask
- Histórico de todas as gerações
- Plano gratuito (5 gerações/dia) e Premium (ilimitado)

### 💰 Monetização
- Limite diário para usuários gratuitos
- Modal de upgrade quando o limite é atingido
- Página de preços com comparativo de planos
- Endpoint `/api/upgrade` (conectar ao Stripe/Mercado Pago)

---

## 🔌 Integrar com Stripe (Pagamento Real)

1. Instale: `pip install stripe`
2. No `app.py`, substitua a rota `/api/upgrade`:

```python
import stripe
stripe.api_key = 'sk_live_...'

@app.route('/api/create-checkout', methods=['POST'])
@login_required
def create_checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_XXXX',  # seu Price ID do Stripe
            'quantity': 1,
        }],
        mode='subscription',
        success_url='https://seusite.com/upgrade-success',
        cancel_url='https://seusite.com/pricing',
    )
    return jsonify({'url': session.url})
```

## 🔌 Integrar com Mercado Pago

```python
import mercadopago
sdk = mercadopago.SDK("seu_access_token")

preference_data = {
    "items": [{"title": "ColorIA Premium", "quantity": 1, "unit_price": 29.00}],
    "back_urls": {"success": "https://seusite.com/upgrade-success"},
    "auto_return": "approved",
}
preference = sdk.preference().create(preference_data)
```

---

## 🌐 Deploy em Produção

### Opção 1: Railway.app (recomendado, grátis para começar)
```bash
pip install gunicorn
# Adicione ao requirements.txt: gunicorn>=21.0.0
# railway up
```

### Opção 2: Render.com
- Start Command: `gunicorn app:app`
- Environment: Python 3

### Opção 3: VPS (DigitalOcean, Contabo)
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## 🎯 Melhorias Futuras

### Curto Prazo
- [ ] Integração com DALL-E 3 ou Stable Diffusion para geração real de imagens
- [ ] Integração real com Stripe para pagamentos
- [ ] Email de confirmação ao cadastrar
- [ ] Recuperação de senha

### Médio Prazo  
- [ ] Galeria pública de desenhos populares
- [ ] Sistema de categorias e tags
- [ ] API para desenvolvedores
- [ ] App mobile (PWA)

### Longo Prazo
- [ ] Marketplace interno (vender no próprio site)
- [ ] Plano de agência (múltiplos usuários)
- [ ] Geração de vídeos time-lapse do desenho
- [ ] Integração direta com Etsy via API

---

## 💰 Estratégia de Monetização

1. **Freemium**: 5 gerações/dia grátis → converte bem
2. **Premium R$ 29/mês**: Ilimitado + pacotes comerciais
3. **Anual R$ 249/ano**: Desconto de 28%
4. **Pacotes avulsos**: R$ 9,90 por pacote de 10 desenhos

### Canais de Aquisição
- SEO: "desenho para colorir grátis", "gerador de figurinhas"
- Pinterest: compartilhar exemplos de desenhos
- YouTube: tutoriais de "como ganhar dinheiro com Etsy"
- TikTok: mostrar o processo de geração

---

## 📊 Métricas para Acompanhar

- Taxa de conversão gratuito → premium
- Gerações por usuário ativo
- Churn rate mensal
- LTV (Lifetime Value) por usuário

---

Feito com ❤️ para criadores brasileiros que querem ganhar dinheiro online.
