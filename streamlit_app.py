import streamlit as st
import urllib.parse

# ─── CONFIGURATION DE LA PAGE ────────────────────────────────────────────────
st.set_page_config(page_title="Forge IA", page_icon="⚒️", layout="wide")

# ─── INJECTION DES STYLES CSS COMPLETS ───────────────────────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght=400;700;800;900&display=swap');
    
    /* FOND GLOBAL DE LA PAGE */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
    [data-testid="stMainBlockContainer"] {
        background: #060912 !important;
        background-image: radial-gradient(circle at 20% 50%, rgba(56, 189, 248, 0.06) 0%, transparent 60%), 
                          radial-gradient(circle at 80% 20%, rgba(129, 140, 248, 0.06) 0%, transparent 60%) !important;
        color: #e2e8f0 !important;
        font-family: 'Syne', sans-serif !important;
    }

    /* EN-TÊTE PLATFORME */
    .hero-badge-container {
        text-align: center;
        margin-top: 15px;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.3);
        color: #38bdf8;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .hero-title {
        font-size: 50px;
        font-weight: 900 !important;
        text-align: center;
        letter-spacing: -2px;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 10px;
        margin-top: 10px;
    }
    .hero-sub {
        color: #94a3b8;
        text-align: center;
        font-size: 16px;
        font-weight: 700 !important;
        max-width: 560px;
        margin: 0 auto 30px auto;
    }

    /* CARTES DES AGENTS */
    .agent-card {
        background: #0a1020 !important;
        border: 1px solid #1e2d4a !important;
        border-radius: 16px !important;
        padding: 22px !important;
        margin-bottom: 20px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        min-height: 400px;
        box-sizing: border-box;
    }
    .agent-card.premium {
        background: linear-gradient(145deg, #0d1526, #111827) !important;
        border: 1px solid rgba(129, 140, 248, 0.3) !important;
        box-shadow: 0 4px 30px rgba(129, 140, 248, 0.08) !important;
    }
    .agent-title {
        font-size: 18px;
        font-weight: 800 !important;
        color: #f1f5f9 !important;
        margin: 6px 0 4px 0 !important;
    }
    .agent-dom {
        font-size: 11px;
        font-weight: 700 !important;
        color: #38bdf8 !important;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .agent-desc {
        color: #94a3b8 !important;
        font-size: 13px !important;
        line-height: 1.6 !important;
        margin: 10px 0 !important;
    }
    .agent-meta {
        font-size: 12px;
        color: #64748b;
        margin-bottom: 10px;
    }

    /* BADGES INTERNES DES CARTES */
    .badge-tag {
        display: inline-block;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .badge-populaire { background: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.2); }
    .badge-tendance { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-bestseller { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-gratuit { background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.25); }
    
    /* SKILLS TAGS */
    .skill-tag {
        display: inline-block !important;
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid #1e2d4a !important;
        border-radius: 6px !important;
        padding: 2px 8px !important;
        font-size: 11px !important;
        color: #cbd5e1 !important;
        margin-right: 4px !important;
        margin-bottom: 4px !important;
    }

    /* BOUTONS D'ACTION ACTIONNABLES */
    .btn-wa {
        display: block !important;
        text-align: center !important;
        background: linear-gradient(135deg, #38bdf8, #818cf8) !important;
        color: #060912 !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        padding: 10px 0 !important;
        border-radius: 10px !important;
        text-decoration: none !important;
        margin-top: 14px !important;
        transition: transform 0.2s ease, opacity 0.2s ease;
    }
    .btn-wa:hover {
        transform: translateY(-2px);
        opacity: 0.9;
        color: #060912 !important;
    }
    .btn-free {
        display: block !important;
        text-align: center !important;
        background: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        color: #10b981 !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        padding: 10px 0 !important;
        border-radius: 10px !important;
        text-decoration: none !important;
        margin-top: 14px !important;
    }

    /* AVIS CLIENTS */
    .review-card {
        background: #0a1020;
        border: 1px solid #1e2d4a;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        height: 100%;
    }
    .review-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    .avatar-circle {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, #38bdf8, #818cf8);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        color: #060912;
        font-size: 18px;
    }
    .review-info h4 {
        margin: 0;
        color: #f1f5f9;
        font-size: 15px;
    }
    .review-info p {
        margin: 0;
        color: #64748b;
        font-size: 12px;
    }
    .review-stars {
        color: #f59e0b;
        margin-bottom: 8px;
    }

    /* STYLE DES TABS NATIVES STREAMLIT */
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        letter-spacing: 0.5px;
    }

    /* FOOTER DE LA PAGE */
    .footer-container {
        text-align: center;
        margin-top: 60px;
        padding-top: 20px;
        border-top: 1px solid #1e2d4a;
    }
    .footer-email {
        color: #94a3b8;
        font-size: 14px;
        font-weight: 700;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .footer-email:hover {
        color: #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

# ─── CONFIGURATION DES VARIABLES GLOBALES ────────────────────────────────────
WHATSAPP = "221771122598"
PRIX = "10 $"

CATALOGUE = [
    # AGENTS GRATUITS
    {"type": "FREE", "dom": "MARKETING", "t": "Ambassadeur Growth", "badge": "populaire", "badge_label": "🔥 Populaire", "rating": "★★★★★ 4.8", "users": "1 240", "d": "Expert en stratégies SEO, growth hacking et visibilité digitale. Génère des plans de contenu viraux.", "skills": ["SEO", "Content", "Social Media"]},
    {"type": "FREE", "dom": "MARKETING", "t": "Rédacteur Copywriter", "badge": "gratuit", "badge_label": "✨ Offert", "rating": "★★★★☆ 4.6", "users": "850", "d": "Conçoit des accroches publicitaires percutantes, des pages de capture et des scripts de vente optimisés.", "skills": ["Copywriting", "Ads", "Sales"]},
    {"type": "FREE", "dom": "DÉVELOPPEMENT", "t": "Architecte Python", "badge": "populaire", "badge_label": "⭐ Top noté", "rating": "★★★★★ 4.9", "users": "980", "d": "Spécialiste en scripts automatisés, APIs REST et backend scalable. Debug express inclus.", "skills": ["Python", "API", "Automation"]},
    {"type": "FREE", "dom": "DÉVELOPPEMENT", "t": "Débuggeur JavaScript", "badge": "gratuit", "badge_label": "✨ Offert", "rating": "★★★★☆ 4.7", "users": "640", "d": "Analyse vos scripts JS/TypeScript, corrige les bugs front-end et optimise la vitesse de chargement.", "skills": ["JavaScript", "Debug", "Front-end"]},
    {"type": "FREE", "dom": "MARKETING", "t": "Créatif Visuel", "badge": "gratuit", "badge_label": "🎨 Design", "rating": "★★★★★ 4.8", "users": "1 100", "d": "Générateur de prompts ultra-précis pour Midjourney et Stable Diffusion. Crée des chartes graphiques.", "skills": ["Prompts", "Midjourney", "Design AI"]},

    # AGENTS PREMIUM
    {"type": "PREMIUM", "dom": "LOGISTIQUE", "t": "Maître Logistique", "badge": "populaire", "badge_label": "💎 Premium", "rating": "★★★★☆ 4.7", "users": "430", "d": "Optimisation de flottes, gestion de chaîne d'approvisionnement et prévision de stocks en temps réel.", "skills": ["Supply Chain", "Fleet", "Stock AI"]},
    {"type": "PREMIUM", "dom": "JURIDIQUE", "t": "Avocat IA", "badge": "populaire", "badge_label": "💎 Premium", "rating": "★★★★★ 4.9", "users": "312", "d": "Analyse de contrats, conformité RGPD et juridique internationale. Rédaction de clauses sur-mesure.", "skills": ["Contrats", "RGPD", "Compliance"]},
    {"type": "PREMIUM", "dom": "FINANCE", "t": "Analyste Web3", "badge": "tendance", "badge_label": "🚀 Tendance", "rating": "★★★★☆ 4.6", "users": "520", "d": "Audit de smart contracts, analyse on-chain et tendances DeFi. Alertes personnalisées en temps réel.", "skills": ["DeFi", "Smart Contracts", "On-chain"]},
    {"type": "PREMIUM", "dom": "RH", "t": "Recruteur Tech", "badge": "populaire", "badge_label": "💎 Premium", "rating": "★★★★☆ 4.8", "users": "275", "d": "Sourcing de talents, scoring de CVs par IA et évaluation de compétences techniques en profondeur.", "skills": ["Sourcing", "CV Scoring", "Interview AI"]},
    {"type": "PREMIUM", "dom": "E-COMMERCE", "t": "Expert Shopify", "badge": "bestseller", "badge_label": "💰 Best-seller", "rating": "★★★★☆ 4.7", "users": "610", "d": "Configuration de boutiques haute conversion, A/B testing produits et optimisation des funnels.", "skills": ["Shopify", "Conversion", "Funnel"]},
    {"type": "PREMIUM", "dom": "SANTÉ", "t": "Coach Santé IA", "badge": "bestseller", "badge_label": "❤️ Bien-être", "rating": "★★★★★ 4.9", "users": "380", "d": "Plans nutritionnels personnalisés, suivi de symptômes et recommandations de soins préventifs.", "skills": ["Nutrition", "Symptômes", "Prévention"]},
    {"type": "PREMIUM", "dom": "ÉDUCATION", "t": "Tuteur Universel", "badge": "populaire", "badge_label": "🎓 Éducation", "rating": "★★★★☆ 4.8", "users": "720", "d": "Cours adaptatifs, quiz génératifs et parcours d'apprentissage personnalisé pour toute discipline.", "skills": ["Cours IA", "Quiz", "Parcours"]}
]

TEMOIGNAGES = [
    {"nom": "Karim B.", "role": "CEO Startup", "texte": "L'Avocat IA m'a économisé 3000$ en frais juridiques dès le premier mois. Incroyable.", "avatar": "K", "stars": "★★★★★"},
    {"nom": "Sophie L.", "role": "E-commerçante", "texte": "Mon CA a bondi de +40% grâce à l'Expert Shopify. ROI immédiat sur l'investissement.", "avatar": "S", "stars": "★★★★★"},
    {"nom": "Marcus T.", "role": "Trader Crypto", "texte": "L'Analyste Web3 m'alerte avant les mouvements de marché. Un must-have absolu.", "avatar": "M", "stars": "★★★★★"},
    {"nom": "Aïda F.", "role": "DRH Tech", "texte": "Le Recruteur IA analyse 200 CVs en 30 secondes. Mon équipe RH adore.", "avatar": "A", "stars": "★★★★☆"}
]

# ─── HERO HEADER ─────────────────────────────────────────────────────────────
st.markdown('<div class="hero-badge-container"><span class="hero-badge">⚒️ Forge IA — Plateforme Agents</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Des agents IA taillés<br>pour vos ambitions</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Choisissez, testez en direct et déployez des agents spécialisés pour booster chaque aspect de votre business.</div>', unsafe_allow_html=True)

# ─── NAVIGATION PRINCIPALE ───────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🤖 Catalogue", "⭐ Avis clients", "❓ FAQ"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("🔍 Rechercher un agent...", "")
    with col2:
        filtre = st.selectbox("Domaines", ["TOUS", "MARKETING", "DÉVELOPPEMENT", "LOGISTIQUE", "JURIDIQUE", "FINANCE", "RH", "E-COMMERCE", "SANTÉ", "ÉDUCATION"])

    # Filtrer les agents
    agents_filtres = [a for a in CATALOGUE if (filtre == "TOUS" or a["dom"] == filtre) and (search.lower() in a["t"].lower() or search.lower() in a["d"].lower() or search.lower() in a["dom"].lower())]

    # Grille à deux colonnes stable
    if agents_filtres:
        for i in range(0, len(agents_filtres), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(agents_filtres):
                    agent = agents_filtres[i + j]
                    with cols[j]:
                        skills_html = "".join([f'<span class="skill-tag">{s}</span>' for s in agent["skills"]])
                        
                        # Configuration du bouton d'action selon le type d'agent
                        if agent["type"] == "PREMIUM":
                            msg = f"Bonjour, je souhaite acquérir l'agent Premium : {agent['t']}"
                            link = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
                            btn_html = f'<a class="btn-wa" href="{link}" target="_blank">💳 Acquérir — {PRIX}</a>'
                        else:
                            btn_html = f'<a class="btn-free" href="#">🚀 Agent Gratuit (Disponible)</a>'
                        
                        card_style = "agent-card premium" if agent["type"] == "PREMIUM" else "agent-card"
                        
                        # Rendu HTML complet de la carte
                        st.markdown(f"""
                        <div class="{card_style}">
                            <div>
                                <span class="badge-tag badge-{agent['badge']}">{agent['badge_label']}</span>
                                <div class="agent-dom">{agent['dom']}</div>
                                <div class="agent-title">{agent['t']}</div>
                                <div class="agent-desc">{agent['d']}</div>
                                <div class="agent-meta">⭐ {agent['rating']} | 👥 {agent['users']} utilisateurs</div>
                            </div>
                            <div>
                                <div style="margin-top: 10px; margin-bottom: 5px;">{skills_html}</div>
                                {btn_html}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("Aucun agent ne correspond à votre recherche.")

with tab2:
    # Affichage des témoignages clients sous forme de grille (2 colonnes)
    for i in range(0, len(TEMOIGNAGES), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(TEMOIGNAGES):
                item = TEMOIGNAGES[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="review-card">
                        <div class="review-header">
                            <div class="avatar-circle">{item['avatar']}</div>
                            <div class="review-info">
                                <h4>{item['nom']}</h4>
                                <p>{item['role']}</p>
                            </div>
                        </div>
                        <div class="review-stars">{item['stars']}</div>
                        <div style="color: #94a3b8; font-style: italic; font-size: 14px;">"{item['texte']}"</div>
                    </div>
                    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### ❓ Questions Fréquentes")
    with st.expander("Comment se passe le déploiement des agents ?"):
        st.write("Une fois l'acquisition validée sur WhatsApp, nous configurons l'agent selon vos besoins et vous recevez un lien d'accès direct ou un script d'intégration en moins de 24 heures.")
    with st.expander("Les agents gratuits restent-ils gratuits à vie ?"):
        st.write("Oui, tous les agents marqués comme gratuits restent accessibles sans frais pour les fonctionnalités de base.")
    with st.expander("Puis-je demander un agent sur-mesure ?"):
        st.write("Absolument. Contactez-nous directement via le bouton d'un agent Premium pour discuter d'un développement spécifique pour votre business.")

# ─── FOOTER CONTACT GMAIL ───────────────────────────────────────────────────
st.markdown("""
    <div class="footer-container">
        <p style="margin-bottom: 5px; color: #64748b; font-size: 13px;">Une question ou un besoin sur-mesure ?</p>
        <a class="footer-email" href="mailto:amadouthiam579@gmail.com">📩 Contactez-nous : amadouthiam579@gmail.com</a>
        <p style="margin-top: 15px; margin-bottom: 0; color: #334155; font-size: 11px;">© 2026 Forge IA. Tous droits réservés.</p>
    </div>
""", unsafe_allow_html=True)