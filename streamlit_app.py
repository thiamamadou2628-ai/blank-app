import streamlit as st
import urllib.parse

# ─── CONFIGURATION DE LA PAGE ────────────────────────────────────────────────
st.set_page_config(page_title="Forge IA", page_icon="🤖", layout="wide")

# ─── INJECTION DES STYLES CSS COMPLETS (VERSION FONDS IMAGES & ANIMATIONS) ───
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght=400;700;900&family=Syne:wght=400;700;800&display=swap');
    
    /* FOND GLOBAL */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
    [data-testid="stMainBlockContainer"] {
        background: #060912 !important;
        background-image: radial-gradient(circle at 20% 50%, rgba(56, 189, 248, 0.08) 0%, transparent 60%), 
                          radial-gradient(circle at 80% 20%, rgba(129, 140, 248, 0.08) 0%, transparent 60%) !important;
        color: #e2e8f0 !important;
        font-family: 'Syne', sans-serif !important;
    }

    /* LOGO ROBOT SOURIANT ANIMÉ */
    .logo-container {
        text-align: center;
        padding: 20px 0;
        filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.5));
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    .robot-logo { font-size: 80px; margin-bottom: 0; }

    /* TITRES & TEXTES */
    .hero-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 55px; font-weight: 900 !important; text-align: center;
        letter-spacing: -1px; line-height: 1.1; margin: 10px 0;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #f472b6);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .hero-sub {
        color: #94a3b8; text-align: center; font-size: 17px; font-weight: 500;
        max-width: 600px; margin: 0 auto 40px auto; font-family: 'Syne', sans-serif;
    }

    /* BARRE DE NAVIGATION (TABS) */
    div[data-baseweb="tab-list"] {
        gap: 12px !important;
        background: rgba(15, 23, 42, 0.9) !important;
        padding: 12px !important;
        border-radius: 20px !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        justify-content: center !important;
    }
    button[data-baseweb="tab"] {
        font-family: 'Orbitron', sans-serif !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        color: #94a3b8 !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        font-size: 13px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #38bdf8 !important;
        background: rgba(56, 189, 248, 0.08) !important;
        transform: translateY(-2px);
    }
    button[aria-selected="true"] {
        background: rgba(56, 189, 248, 0.15) !important;
        color: #38bdf8 !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.25) !important;
        border: 1px solid rgba(56, 189, 248, 0.5) !important;
    }

    /* CARTES DES AGENTS AVEC IMAGES DE FOND ET HOVER */
    .agent-card {
        position: relative !important;
        background-size: cover !important;
        background-position: center !important;
        border: 1px solid #1e2d4a !important;
        border-radius: 18px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        display: flex !important; flex-direction: column !important;
        justify-content: space-between !important; min-height: 420px;
        overflow: hidden !important;
        z-index: 1;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* FILTRE ASSOMBREUR POUR LA LISIBILITÉ DU TEXTE */
    .agent-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(180deg, rgba(10, 16, 32, 0.88) 0%, rgba(6, 9, 18, 0.96) 100%) !important;
        z-index: -1;
        transition: all 0.3s ease;
    }
    
    .agent-card:hover { 
        transform: translateY(-8px) scale(1.01); 
        border-color: #38bdf8 !important;
        box-shadow: 0 10px 30px rgba(56, 189, 248, 0.2) !important;
    }
    
    .agent-card:hover::before {
        background: linear-gradient(180deg, rgba(10, 16, 32, 0.78) 0%, rgba(6, 9, 18, 0.92) 100%) !important;
    }

    .agent-card.premium {
        border: 1px solid rgba(129, 140, 248, 0.3) !important;
    }
    .agent-card.premium:hover {
        border-color: #818cf8 !important;
        box-shadow: 0 10px 30px rgba(129, 140, 248, 0.25) !important;
    }
    
    .agent-title { font-family: 'Orbitron', sans-serif; font-size: 19px; font-weight: 700; color: #fff; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
    .agent-dom { font-size: 10px; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 1.5px; }
    .agent-desc { color: #cbd5e1; font-size: 13px; line-height: 1.6; margin: 10px 0; text-shadow: 0 1px 2px rgba(0,0,0,0.6); }

    /* BOUTONS */
    .btn-wa {
        display: block; text-align: center; font-family: 'Orbitron', sans-serif;
        background: linear-gradient(135deg, #38bdf8, #818cf8);
        color: #060912 !important; font-weight: 900; font-size: 12px;
        padding: 12px 0; border-radius: 10px; text-decoration: none; margin-top: 15px;
        transition: all 0.3s ease;
    }
    .btn-wa:hover {
        transform: scale(1.03);
        box-shadow: 0 0 15px rgba(129, 140, 248, 0.4);
    }
    .btn-free {
        display: block; text-align: center; font-family: 'Orbitron', sans-serif;
        background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4);
        color: #10b981 !important; font-weight: 900; font-size: 12px;
        padding: 12px 0; border-radius: 10px; text-decoration: none; margin-top: 15px;
        transition: all 0.3s ease;
    }
    .btn-free:hover {
        background: rgba(16, 185, 129, 0.25) !important;
        transform: scale(1.02);
    }
    
    .skill-tag {
        display: inline-block; background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 6px; padding: 2px 8px; font-size: 11px;
        color: #fff; margin: 2px;
    }

    /* PORTFOLIO ANIMÉ */
    .portfolio-card { 
        background: #0a1020; border: 1px solid #1e2d4a; border-radius: 20px; 
        overflow: hidden; height: 100%; margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .portfolio-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: #f472b6 !important;
        box-shadow: 0 15px 35px rgba(244, 114, 182, 0.2) !important;
    }
    .portfolio-img { width: 100%; height: 220px; object-fit: cover; transition: transform 0.5s ease; }
    .portfolio-card:hover .portfolio-img { transform: scale(1.06); }
    .portfolio-content { padding: 22px; }
    .portfolio-content h4 { font-family: 'Orbitron', sans-serif; color: #fff; margin-bottom: 8px; font-size: 17px; }
    .portfolio-content p { color: #94a3b8; font-size: 13px; line-height: 1.6; margin: 0; }

    /* AVIS */
    .review-card { background: #0a1020; border: 1px solid #1e2d4a; border-radius: 16px; padding: 20px; transition: all 0.3s ease; }
    .review-card:hover { transform: translateY(-5px); border-color: #38bdf8; box-shadow: 0 8px 25px rgba(56, 189, 248, 0.1); }
    .avatar-circle { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #38bdf8, #818cf8); display: flex; align-items: center; justify-content: center; font-weight: 900; color: #060912; }

    /* FOOTER */
    .footer-container { text-align: center; margin-top: 80px; padding: 40px; border-top: 1px solid rgba(56, 189, 248, 0.15); }
    .footer-email { font-family: 'Orbitron', sans-serif; color: #38bdf8; font-weight: 700; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

# ─── CONFIGURATION DES VARIABLES GLOBALES ────────────────────────────────────
WHATSAPP = "221771122598"
PRIX = "10 $"

TEMOIGNAGES = [
    {"nom": "Karim B.", "role": "CEO Startup", "texte": "L'Avocat IA m'a économisé 3000$ en frais juridiques dès le premier mois. Incroyable.", "avatar": "K", "stars": "★★★★★"},
    {"nom": "Sophie L.", "role": "E-commerçante", "texte": "Mon CA a bondi de +40% grâce à l'Expert Shopify. ROI immédiat sur l'investissement.", "avatar": "S", "stars": "★★★★★"},
    {"nom": "Marcus T.", "role": "Trader Crypto", "texte": "L'Analyste Web3 m'alerte avant les mouvements de marché. Un must-have absolu.", "avatar": "M", "stars": "★★★★★"},
    {"nom": "Aïda F.", "role": "DRH Tech", "texte": "Le Recruteur IA analyse 200 CVs en 30 secondes. Mon équipe RH adore.", "avatar": "A", "stars": "★★★★☆"}
]

# Liens d'images thématiques de fond pour le catalogue
IMG_MARKETING = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500&q=60"
IMG_DEV = "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500&q=60"
IMG_SPORT = "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=500&q=60"
IMG_DESIGN = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500&q=60"
IMG_LOGISTIQUE = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=500&q=60"
IMG_JURIDIQUE = "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=500&q=60"
IMG_FINANCE = "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?w=500&q=60"
IMG_RH = "https://images.unsplash.com/photo-1521737711867-e3b90473bd58?w=500&q=60"
IMG_ECOMMERCE = "https://images.unsplash.com/photo-1556742044-3c52d6e88c62?w=500&q=60"
IMG_SANTE = "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=500&q=60"
IMG_EDUCATION = "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=500&q=60"

CATALOGUE = [
    # GRATUITS
    {"type": "FREE", "dom": "MARKETING", "bg": IMG_MARKETING, "t": "Ambassadeur Growth", "badge": "populaire", "badge_label": "🔥 Populaire", "rating": "4.8", "users": "1 240", "d": "Stratégies SEO et visibilité digitale. Génère des plans de contenu viraux.", "skills": ["SEO", "Content"]},
    {"type": "FREE", "dom": "MARKETING", "bg": IMG_MARKETING, "t": "Rédacteur Copywriter", "badge": "gratuit", "badge_label": "✨ Offert", "rating": "4.6", "users": "850", "d": "Conçoit des accroches publicitaires et des scripts de vente percutants.", "skills": ["Ads", "Sales"]},
    {"type": "FREE", "dom": "DÉVELOPPEMENT", "bg": IMG_DEV, "t": "Architecte Python", "badge": "populaire", "badge_label": "⭐ Top", "rating": "4.9", "users": "980", "d": "Scripts automatisés et APIs REST. Debug express inclus.", "skills": ["Python", "API"]},
    {"type": "FREE", "dom": "DÉVELOPPEMENT", "bg": IMG_DEV, "t": "Débuggeur JS", "badge": "gratuit", "badge_label": "✨ Offert", "rating": "4.7", "users": "640", "d": "Analyse et corrige vos bugs front-end en un temps record.", "skills": ["JavaScript", "Debug"]},
    {"type": "FREE", "dom": "MARKETING", "bg": IMG_DESIGN, "t": "Créatif Visuel", "badge": "gratuit", "badge_label": "🎨 Design", "rating": "4.8", "users": "1 100", "d": "Générateur de prompts ultra-précis pour Midjourney et Stable Diffusion.", "skills": ["Prompts", "Design"]},
    
    # PREMIUM
    {"type": "PREMIUM", "dom": "SPORT", "bg": IMG_SPORT, "t": "Analyste Sportif IA", "badge": "populaire", "badge_label": "⚽ Paris & Stats", "rating": "4.8", "users": "580", "d": "Analyse algorithmique des ligues de football et stratégies de paris.", "skills": ["Football", "Stats"]},
    {"type": "PREMIUM", "dom": "DESIGN", "bg": IMG_DESIGN, "t": "Studio Avatar Pro", "badge": "bestseller", "badge_label": "📸 Studio", "rating": "4.9", "users": "890", "d": "Portraits photo-réalistes IA pro pour CV et réseaux sociaux.", "skills": ["Portraits", "Pro"]},
    {"type": "PREMIUM", "dom": "DÉVELOPPEMENT", "bg": IMG_DEV, "t": "Développeur Jeux 2D", "badge": "tendance", "badge_label": "🎮 Gaming", "rating": "4.9", "users": "210", "d": "Scripts de mouvement et modélisation 2D complète (Sir Galette).", "skills": ["Gaming", "Unity"]},
    {"type": "PREMIUM", "dom": "LOGISTIQUE", "bg": IMG_LOGISTIQUE, "t": "Maître Logistique", "badge": "populaire", "badge_label": "💎 Premium", "rating": "4.7", "users": "430", "d": "Optimisation de flottes et gestion de chaîne d'approvisionnement.", "skills": ["Supply", "Fleet"]},
    {"type": "PREMIUM", "dom": "JURIDIQUE", "bg": IMG_JURIDIQUE, "t": "Avocat IA", "badge": "populaire", "badge_label": "💎 Premium", "rating": "4.9", "users": "312", "d": "Analyse de contrats et conformité RGPD internationale.", "skills": ["Contrats", "RGPD"]},
    {"type": "PREMIUM", "dom": "FINANCE", "bg": IMG_FINANCE, "t": "Analyste Web3", "badge": "tendance", "badge_label": "🚀 DeFi", "rating": "4.6", "users": "520", "d": "Audit de smart contracts et analyse on-chain.", "skills": ["DeFi", "Crypto"]},
    {"type": "PREMIUM", "dom": "RH", "bg": IMG_RH, "t": "Recruteur Tech", "badge": "populaire", "badge_label": "💎 Premium", "rating": "4.8", "users": "275", "d": "Sourcing de talents et scoring de CVs automatisé.", "skills": ["Sourcing", "HR"]},
    {"type": "PREMIUM", "dom": "E-COMMERCE", "bg": IMG_ECOMMERCE, "t": "Expert Shopify", "badge": "bestseller", "badge_label": "💰 Profit", "rating": "4.7", "users": "610", "d": "Boutiques haute conversion et optimisation des funnels Gumroad.", "skills": ["Shopify", "Sales"]},
    {"type": "PREMIUM", "dom": "SANTÉ", "bg": IMG_SANTE, "t": "Coach Santé IA", "badge": "bestseller", "badge_label": "❤️ Zen", "rating": "4.9", "users": "380", "d": "Plans nutritionnels et suivi de soins préventifs.", "skills": ["Santé", "Food"]},
    {"type": "PREMIUM", "dom": "ÉDUCATION", "bg": IMG_EDUCATION, "t": "Tuteur Universel", "badge": "populaire", "badge_label": "🎓 Éducation", "rating": "4.8", "users": "720", "d": "Cours adaptatifs et parcours d'apprentissage personnalisé.", "skills": ["IA", "Cours"]}
]

# ─── HEADER AVEC LOGO ────────────────────────────────────────────────────────
st.markdown('<div class="logo-container"><div class="robot-logo">🤖</div></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">FORGE IA : L\'ARMÉE<br>DES AGENTS FUTURISTES</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Propulsez vos projets avec des intelligences taillées pour la performance. Sélectionnez votre expert et commencez l\'aventure.</div>', unsafe_allow_html=True)

# ─── NAVIGATION PRINCIPALE ───────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🤖 CATALOGUE", "🖼️ PORTFOLIO", "⭐ AVIS", "❓ FAQ", "💬 CONSEILLER"])

with tab1:
    c_f1, c_f2 = st.columns([2, 1])
    search = c_f1.text_input("🔍 Rechercher un agent...", "")
    filtre = c_f2.selectbox("Filtre", ["TOUS", "MARKETING", "DÉVELOPPEMENT", "LOGISTIQUE", "JURIDIQUE", "FINANCE", "RH", "E-COMMERCE", "SPORT", "DESIGN"])

    agents_filtres = [a for a in CATALOGUE if (filtre == "TOUS" or a["dom"] == filtre) and (search.lower() in a["t"].lower() or search.lower() in a["d"].lower())]

    if agents_filtres:
        for i in range(0, len(agents_filtres), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(agents_filtres):
                    agent = agents_filtres[i + j]
                    with cols[j]:
                        skills_html = "".join([f'<span class="skill-tag">{s}</span>' for s in agent["skills"]])
                        if agent["type"] == "PREMIUM":
                            msg = urllib.parse.quote(f"Bonjour, je veux l'agent Premium : {agent['t']}")
                            btn_html = f'<a class="btn-wa" href="https://wa.me/{WHATSAPP}?text={msg}" target="_blank">🛒 ACHETER — {PRIX}</a>'
                        else:
                            btn_html = f'<a class="btn-free" href="#">🚀 ACCÈS GRATUIT</a>'
                        
                        st.markdown(f"""
                        <div class="agent-card {'premium' if agent['type'] == 'PREMIUM' else ''}" style="background-image: url('{agent['bg']}');">
                            <div>
                                <span class="badge-tag badge-{agent['badge']}">{agent['badge_label']}</span>
                                <div class="agent-dom">{agent['dom']}</div>
                                <div class="agent-title">{agent['t']}</div>
                                <div class="agent-desc">{agent['d']}</div>
                                <div style="font-size: 11px; color: #a1a1aa; font-weight: 700;">⭐ {agent['rating']} | 👥 {agent['users']} users</div>
                            </div>
                            <div>
                                <div style="margin: 10px 0;">{skills_html}</div>
                                {btn_html}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 🖼️ GALERIE DE PROJETS HAUTE PERFORMANCE")
    st.write("Survolez les projets ci-dessous pour découvrir la puissance de nos agents en action.")
    
    p_cols1 = st.columns(2)
    with p_cols1[0]:
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600">
            <div class="portfolio-content">
                <h4>🎮 Logique & Ennemis de Jeu 2D (Sir Galette)</h4>
                <p>Développement complet de la structure d'un jeu de tir 2D d'arcade. Modélisation comportementale des ennemis (patrouille, attaques de zone) et nettoyage intégral du code principal pour assurer un gameplay fluide à 60 FPS.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=600">
            <div class="portfolio-content">
                <h4>📸 Studio Photo IA & Avatars Professionnels</h4>
                <p>Génération de portraits d'affaires hyper-réalistes à partir de selfies ordinaires pour des profils LinkedIn et des CV. Ajustement chirurgical de la symétrie des yeux, de l'expression du visage et intégration d'habits pros sur-mesure.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600">
            <div class="portfolio-content">
                <h4>⚽ Analyse Prédictive : Les Grands Classicos</h4>
                <p>Algorithme d'analyse croisant les historiques de matchs, l'état de forme des joueurs clés et la dynamique de grands chocs (comme les derbys et les Classicos). Génération de statistiques pré-match d'une précision chirurgicale.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=600">
            <div class="portfolio-content">
                <h4>🔐 Audit de Contrats Web3 Securisés</h4>
                <p>Analyse de lignes de code de smart contracts sur Ethereum et Solana. Repérage immédiat des failles de sécurité critiques et optimisation des coûts de gaz avant le déploiement sur les réseaux de test.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with p_cols1[1]:
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600">
            <div class="portfolio-content">
                <h4>💰 Tunnel de Vente E-Commerce Intégré</h4>
                <p>Déploiement d'une structure automatisée pour boutiques en ligne. Intégration de plateformes de produits digitaux comme Gumroad et gestion de l'hébergement sécurisé sur GitHub Pages, doublant le taux de conversion.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=600">
            <div class="portfolio-content">
                <h4>🐍 Script d'Automatisation Python & API</h4>
                <p>Création d'un outil complet d'extraction et de traitement de données connecté à des applications de messagerie. Extraction automatique de fichiers volumineux, tri intelligent et stockage structuré sans aucune action humaine.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?w=600">
            <div class="portfolio-content">
                <h4>👔 Automatisation des Procédés RH</h4>
                <p>Interface IA capable de trier, catégoriser et évaluer la pertinence de profils complexes de candidats (par exemple pour des postes d'encadrement en service client). Réduction du temps de sélection initial de 75%.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="portfolio-card">
            <img class="portfolio-img" src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600">
            <div class="portfolio-content">
                <h4>✍️ Générateur de Contenu & Copywriting Viral</h4>
                <p>Conception automatique de textes publicitaires persuasifs et de plans éditoriaux pour les réseaux sociaux. Adapté instantanément au ton de l'entreprise pour maximiser l'engagement et le clic.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    for i in range(0, len(TEMOIGNAGES), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(TEMOIGNAGES):
                item = TEMOIGNAGES[i + j]
                with cols[j]:
                    st.markdown(f'<div class="review-card"><div style="display:flex; gap:10px; align-items:center;"><div class="avatar-circle">{item["avatar"]}</div><div><h4 style="margin:0; font-family:Orbitron;">{item["nom"]}</h4><p style="margin:0; font-size:12px; color:#64748b;">{item["role"]}</p></div></div><div style="color:#f59e0b; margin:10px 0;">{item["stars"]}</div><p style="font-style:italic; font-size:14px; color:#94a3b8;">"{item["texte"]}"</p></div>', unsafe_allow_html=True)

with tab4:
    with st.expander("Comment se passe l'achat ?"): st.write("Cliquez sur Acheter, contactez-nous sur WhatsApp, et recevez votre agent prêt à l'emploi.")
    with st.expander("Support technique ?"): st.write("Nous offrons un support 7j/7 pour vous aider à déployer vos agents.")

with tab5:
    st.info("🤖 Besoin d'un conseil ? Posez-moi votre question !")
    if "msgs" not in st.session_state: st.session_state.msgs = [{"role": "assistant", "content": "Salut ! Quel type d'agent peut t'aider aujourd'hui ?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]): st.write(m["content"])
    if p := st.chat_input("Message..."):
        st.session_state.msgs.append({"role": "user", "content": p})
        with st.chat_message("user"): st.write(p)
        r = "Super projet ! Contactez Amadou par mail ou WhatsApp pour une démo personnalisée. 🚀"
        st.session_state.msgs.append({"role": "assistant", "content": r})
        with st.chat_message("assistant"): st.write(r)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="footer-container">
        <a class="footer-email" href="mailto:amadouthiam579@gmail.com">📩 amadouthiam579@gmail.com</a>
        <p style="color: #334155; font-size: 11px; margin-top: 25px;">© 2026 FORGE IA — L'EXCELLENCE ARTIFICIELLE</p>
    </div>
""", unsafe_allow_html=True)