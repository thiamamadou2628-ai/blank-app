import streamlit as st
import json
import random
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="FORGE AGENT IA | MARKETPLACE", layout="wide")

# --- 2. ENGINE DE DESIGN AVANCÉ ---
def inject_vanguard_ui():
    icons = ["🤖", "⚙️", "💻", "🧠", "⚛️", "🛡️", "⚡", "🌐", "💾", "🔑", "📈", "🛒"]
    html_icons = "".join([f'<div class="bg-icon" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(10, 25)}s; animation-delay:{random.randint(0, 10)}s;">{random.choice(icons)}</div>' for _ in range(25)])
    
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&family=Fira+Code:wght@400;500&display=swap');
        
        .stApp {{ background-color: #010103; color: #f0f0f0; font-family: 'Rajdhani', sans-serif; }}
        
        /* Background */
        @keyframes fall {{ 0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 0; }} 15% {{ opacity: 0.1; }} 100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }} }}
        .bg-icon {{ position: fixed; top: -10%; z-index: 0; pointer-events: none; animation: fall linear infinite; font-size: 20px; }}

        /* TITRE : FORGE AGENT IA */
        .title-container {{ text-align: center; margin-bottom: 40px; padding: 20px; }}
        .main-title {{ 
            font-family: 'Orbitron'; font-weight: 900; font-size: 3.8rem;
            background: linear-gradient(to bottom, #ffffff 30%, #00f2fe 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-transform: uppercase; letter-spacing: 8px;
            filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.3));
            margin-bottom: 0;
        }}
        .sub-logo {{ width: 60px; height: 5px; background: #00f2fe; margin: 10px auto; border-radius: 5px; box-shadow: 0 0 15px #00f2fe; }}

        /* TICKER */
        .ticker-wrapper {{ width: 100%; overflow: hidden; background: rgba(0, 242, 254, 0.03); border-y: 1px solid rgba(0, 242, 254, 0.1); padding: 12px 0; margin-bottom: 40px; }}
        .ticker-text {{ display: inline-block; white-space: nowrap; animation: ticker 60s linear infinite; font-family: 'Orbitron'; font-size: 0.65rem; color: #00f2fe; opacity: 0.8; letter-spacing: 2px; text-transform: uppercase; }}
        @keyframes ticker {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}

        /* --- CARTES CYBER-PLATE --- */
        .agent-card {{ 
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(0, 242, 254, 0.1);
            clip-path: polygon(0% 0%, 90% 0%, 100% 12%, 100% 100%, 10% 100%, 0% 88%);
            padding: 30px; margin-bottom: 25px; transition: 0.4s;
            height: 280px; display: flex; flex-direction: column; justify-content: space-between;
            position: relative;
        }}
        .agent-card::before {{
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(45deg, transparent 95%, rgba(0, 242, 254, 0.2) 100%);
        }}
        .agent-card:hover {{ 
            border-color: #00f2fe; background: rgba(0, 242, 254, 0.05);
            transform: scale(1.02) rotate(0.5deg);
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(0, 242, 254, 0.1);
        }}
        .premium-border {{ border: 1px solid rgba(255, 215, 0, 0.3) !important; }}
        .premium-border::before {{ background: linear-gradient(45deg, transparent 95%, rgba(255, 215, 0, 0.2) 100%); }}
        .premium-border:hover {{ border-color: #ffd700 !important; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(255, 215, 0, 0.1); }}

        .tag {{ font-family: 'Orbitron'; font-size: 0.6rem; color: #666; letter-spacing: 2px; text-transform: uppercase; }}
        .name {{ font-family: 'Orbitron'; font-size: 1.3rem; color: #fff; font-weight: 700; margin-top: 10px; }}
        .desc {{ color: #888; font-size: 0.9rem; margin-top: 10px; line-height: 1.5; }}
        .price {{ font-family: 'Orbitron'; font-size: 1.3rem; font-weight: 900; margin-top: 15px; }}

        /* --- BOUTON WHATSAPP GÉANT --- */
        .wa-container {{
            margin-top: 60px; text-align: center; padding: 50px 20px;
            background: radial-gradient(circle at center, rgba(37, 211, 102, 0.08) 0%, transparent 60%);
            border-radius: 20px;
        }}
        .wa-btn {{
            display: inline-block; padding: 22px 60px;
            background: linear-gradient(90deg, #25D366 0%, #128C7E 100%);
            color: white !important; font-family: 'Orbitron'; font-weight: 900;
            text-decoration: none; border-radius: 50px;
            font-size: 1.3rem; letter-spacing: 2px;
            box-shadow: 0 0 30px rgba(37, 211, 102, 0.4);
            transition: 0.3s; animation: pulseWA 2s infinite;
        }}
        .wa-btn:hover {{ transform: scale(1.05); box-shadow: 0 0 60px rgba(37, 211, 102, 0.7); }}
        @keyframes pulseWA {{ 0% {{ box-shadow: 0 0 20px rgba(37, 211, 102, 0.4); }} 50% {{ box-shadow: 0 0 45px rgba(37, 211, 102, 0.8); }} 100% {{ box-shadow: 0 0 20px rgba(37, 211, 102, 0.4); }} }}

        .matrix-box {{ background: #000; color: #00ff41; font-family: 'Fira Code'; padding: 30px; border: 1px solid #00f2fe; border-radius: 4px; font-size: 1.1rem; }}
        </style>
        
        {html_icons}
        
        <div class="title-container">
            <h1 class="main-title">FORGE AGENT IA</h1>
            <div class="sub-logo"></div>
        </div>

        <div class="ticker-wrapper">
            <div class="ticker-text">
                STATUT SYSTÈME : OPTIMISÉ -- RÉSEAU GLOBAL ACTIF -- NOUVELLES UNITÉS CHARGÉES -- DÉPLOIEMENT DES RÉSEAUX NEURONAUX -- ⚡ FORGE RÉCENTE : EXPERT LOGISTIQUE (DAKAR) -- 💎 ACHAT RÉCENT : STRATÈGE WEB3 (PARIS) -- ⚡ 3,450+ AGENTS EN LIGNE...
            </div>
        </div>
    """, unsafe_allow_html=True)

inject_vanguard_ui()

# --- 3. CATALOGUE MASSIF ---
CATALOGUE = [
    # --- AGENTS GRATUITS (8) ---
    {"id": "amb", "type": "FREE", "dom": "MARKETING", "t": "Ambassadeur Growth", "p": "GRATUIT", "d": "Protocoles de croissance virale et stratégies SEO à haute conversion."},
    {"id": "py", "type": "FREE", "dom": "DÉVELOPPEMENT", "t": "Architecte Python", "p": "GRATUIT", "d": "Génération de code full-stack et débogage neuronal avancé."},
    {"id": "edu", "type": "FREE", "dom": "ÉDUCATION", "t": "Tuteur Universel", "p": "GRATUIT", "d": "Assistance académique multidisciplinaire et méthodes d'apprentissage."},
    {"id": "food", "type": "FREE", "dom": "GASTRONOMIE", "t": "Chef Étoilé IA", "p": "GRATUIT", "d": "Création de recettes fusion internationales et gestion des stocks."},
    {"id": "copy", "type": "FREE", "dom": "RÉDACTION", "t": "Plume Virtuelle", "p": "GRATUIT", "d": "Correction orthographique, reformulation et copywriting percutant."},
    {"id": "fit", "type": "FREE", "dom": "SANTÉ", "t": "Coach Sportif Pro", "p": "GRATUIT", "d": "Programmes d'entraînement sur mesure et plans nutritionnels optimisés."},
    {"id": "data", "type": "FREE", "dom": "ANALYSE", "t": "Maître Excel", "p": "GRATUIT", "d": "Génération de macros, formules complexes et nettoyage de données."},
    {"id": "idea", "type": "FREE", "dom": "ENTREPRENEURIAT", "t": "Générateur d'Idées", "p": "GRATUIT", "d": "Brainstorming de startups, noms de marques et business models."},

    # --- AGENTS PREMIUM (14) ---
    {"id": "log", "type": "PREMIUM", "dom": "LOGISTIQUE", "t": "Maître de la Logistique", "p": "4.99 €", "d": "Optimisation des itinéraires de livraison et gestion de flottes internationales.", "link": "https://gumroad.com/l/link1"},
    {"id": "law", "type": "PREMIUM", "dom": "JURIDIQUE", "t": "Avocat d'Affaires IA", "p": "8.50 €", "d": "Analyse de contrats internationaux et protection de la propriété intellectuelle.", "link": "https://gumroad.com/l/link2"},
    {"id": "crypto", "type": "PREMIUM", "dom": "FINANCE", "t": "Analyste Web3 & Crypto", "p": "9.99 €", "d": "Audit blockchain en temps réel, signaux de trading et tendances du marché.", "link": "https://gumroad.com/l/link3"},
    {"id": "hr", "type": "PREMIUM", "dom": "RESSOURCES HUMAINES", "t": "Chasseur de Têtes Elite", "p": "3.50 €", "d": "Sourcing automatisé et évaluation technique des développeurs mondiaux.", "link": "https://gumroad.com/l/link4"},
    {"id": "ecom", "type": "PREMIUM", "dom": "E-COMMERCE", "t": "Stratège Shopify", "p": "5.99 €", "d": "Optimisation du taux de conversion, descriptions de produits et tunnel de vente.", "link": "https://gumroad.com/l/link5"},
    {"id": "ads", "type": "PREMIUM", "dom": "PUBLICITÉ", "t": "Sniper Facebook Ads", "p": "6.50 €", "d": "Création d'angles publicitaires, ciblage d'audience et gestion de budget ROI.", "link": "https://gumroad.com/l/link6"},
    {"id": "cloud", "type": "PREMIUM", "dom": "INFRASTRUCTURE", "t": "Architecte Cloud AWS", "p": "8.99 €", "d": "Conception de serveurs scalables, sécurité réseau et réduction des coûts cloud.", "link": "https://gumroad.com/l/link7"},
    {"id": "ux", "type": "PREMIUM", "dom": "DESIGN", "t": "Directeur UX/UI", "p": "4.50 €", "d": "Critique d'interfaces, psychologie des couleurs et conception de wireframes.", "link": "https://gumroad.com/l/link8"},
    {"id": "forex", "type": "PREMIUM", "dom": "TRADING", "t": "Algo-Trader Forex", "p": "9.50 €", "d": "Analyse technique approfondie, gestion des risques et stratégies scalping.", "link": "https://gumroad.com/l/link9"},
    {"id": "admin", "type": "PREMIUM", "dom": "ADMINISTRATION", "t": "Assistante Virtuelle", "p": "3.99 €", "d": "Gestion des emails, priorisation des agendas et automatisation des tâches.", "link": "https://gumroad.com/l/link10"},
    {"id": "sec", "type": "PREMIUM", "dom": "CYBERSÉCURITÉ", "t": "Pentester Cyber", "p": "7.99 €", "d": "Audit de vulnérabilités, protection contre les failles et sécurisation de données.", "link": "https://gumroad.com/l/link11"},
    {"id": "lang", "type": "PREMIUM", "dom": "TRADUCTION", "t": "Linguiste Polyglotte", "p": "3.50 €", "d": "Traduction native avec contexte culturel dans plus de 20 langues courantes.", "link": "https://gumroad.com/l/link12"},
    {"id": "media", "type": "PREMIUM", "dom": "CRÉATION VIDÉO", "t": "Réalisateur TikTok/Reels", "p": "5.50 €", "d": "Scripts viraux, accroches hypnotiques (hooks) et directives de montage.", "link": "https://gumroad.com/l/link13"},
    {"id": "immo", "type": "PREMIUM", "dom": "IMMOBILIER", "t": "Investisseur Immo", "p": "6.99 €", "d": "Calcul de rentabilité locative, analyse de marché et montage de dossiers bancaires.", "link": "https://gumroad.com/l/link14"}
]

if "view" not in st.session_state: st.session_state.view = "market"

# --- 4. MARKETPLACE ---
if st.session_state.view == "market":
    st.write("<center style='color:#666; margin-bottom:40px; letter-spacing:1px; font-size:1.1rem;'>SÉLECTIONNEZ UNE UNITÉ. INITIALISEZ LA FORGE. DÉPLOYEZ.</center>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, item in enumerate(CATALOGUE):
        is_p = item["type"] == "PREMIUM"
        accent = "#ffd700" if is_p else "#00f2fe"
        with cols[i % 2]:
            st.markdown(f"""
            <div class="agent-card {'premium-border' if is_p else ''}">
                <div>
                    <div class="tag">{item['dom']} {'★ PREMIUM' if is_p else '● LIBRE'}</div>
                    <div class="name">{item['t']}</div>
                    <div class="desc">{item['d']}</div>
                </div>
                <div class="price" style="color:{accent};">{item['p']}</div>
            </div>
            """, unsafe_allow_html=True)
            if is_p:
                st.link_button("💎 ACQUÉRIR L'UNITÉ", item['link'], use_container_width=True)
            else:
                if st.button(f"⚒️ INITIALISER LA FORGE", key=f"f_{i}", use_container_width=True):
                    st.session_state.selected_item = item
                    st.session_state.view = "forge_custom"
                    st.rerun()

    # --- SECTION WHATSAPP GÉANTE (EN FRANÇAIS) ---
    st.markdown(f"""
        <div class="wa-container">
            <h2 style="font-family:'Orbitron'; font-size:1.8rem; margin-bottom:15px; color:#fff;">BESOIN D'UNE IA SUR MESURE ?</h2>
            <p style="color:#aaa; font-size:1.1rem; margin-bottom:35px;">Nos ingénieurs développent votre agent personnalisé sous 48h.</p>
            <a href="https://wa.me/221771122598?text=Bonjour%20Forge%20Agent%20IA,%20je%20souhaite%20commander%20un%20agent%20IA%20sur%20mesure." 
               class="wa-btn" target="_blank">
               COMMANDER SUR WHATSAPP
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- 5. MOTEUR DE FORGE ---
elif st.session_state.view == "forge_custom":
    st.markdown(f"### SYSTÈME PRÊT : {st.session_state.selected_item['t']}")
    name = st.text_input("Désignation de l'Unité", value=st.session_state.selected_item['t'])
    instr = st.text_area("Protocoles Neuronaux", placeholder="Injectez ici vos instructions comportementales spécifiques...", height=150)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 EXÉCUTER LE SÉQUENÇAGE", use_container_width=True):
            st.session_state.temp_config = {"name": name, "instr": instr}
            st.session_state.view = "matrix"
            st.rerun()
    with col2:
        st.button("ANNULER", use_container_width=True, on_click=lambda: st.session_state.update({"view": "market"}))

# --- 6. SÉQUENÇAGE MATRIX ---
elif st.session_state.view == "matrix":
    st.markdown('<div class="matrix-box">', unsafe_allow_html=True)
    p = st.empty()
    for _ in range(16):
        lines = [f"ANALYSE_NOYAU_{random.randint(100,999)}...", "CONTOURNEMENT_DES_LIMITES_ACTIF", "CRYPTAGE_DE_L_UNITÉ_EN_COURS...", "CONNEXION_AU_RÉSEAU_GLOBAL"]
        p.markdown(f"<div>{random.choice(lines)}</div>" * 6, unsafe_allow_html=True)
        time.sleep(0.12)
    st.session_state.view = "ready"
    st.rerun()

# --- 7. UNITÉ FINALE ---
elif st.session_state.view == "ready":
    st.balloons()
    st.success("UNITÉ FORGÉE AVEC SUCCÈS")
    st.download_button("📥 TÉLÉCHARGER L'AGENT (JSON)", json.dumps(st.session_state.temp_config, indent=4), "agent_ia.json", use_container_width=True)
    st.button("RETOUR AU HUB", use_container_width=True, on_click=lambda: st.session_state.update({"view": "market"}))