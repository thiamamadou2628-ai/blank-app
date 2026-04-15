import streamlit as st
import json
import random
import time

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="FORGE IA | SENEGAL EDITION", layout="wide")

# --- 2. SYSTÈME D'UI : ICÔNES TOMBANTES & CSS CYBER ---
def inject_ui():
    # Liste d'icônes tech pour l'effet Matrix
    icons = ["🤖", "⚙️", "💻", "🧠", "⚛️", "🛡️", "⚡", "🌐", "💾", "🔑"]
    html_icons = ""
    for i in range(15):
        left = random.randint(0, 95)
        duration = random.randint(10, 25)
        delay = random.randint(0, 10)
        size = random.randint(15, 30)
        html_icons += f'<div class="bg-icon" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}px;">{random.choice(icons)}</div>'
    
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
        
        .stApp {{ background-color: #050507; color: #f0f0f0; font-family: 'Rajdhani', sans-serif; overflow: hidden; }}
        
        /* Animation Arrière-plan */
        @keyframes fall {{ 
            0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 0; }} 
            15% {{ opacity: 0.25; }} 
            85% {{ opacity: 0.25; }} 
            100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }} 
        }}
        .bg-icon {{ position: fixed; top: -10%; z-index: 0; pointer-events: none; animation: fall linear infinite; }}
        
        /* Titre Néon Gold */
        .neon-title {{ 
            font-family: 'Orbitron'; 
            background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
            text-align: center; font-size: 3rem; margin-bottom: 20px; 
            position: relative; z-index: 1; 
        }}

        /* Cartes Cyber-Glass Compactes */
        .service-card {{ 
            background: rgba(255, 255, 255, 0.03); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 4px; padding: 18px; height: 320px; 
            display: flex; flex-direction: column; justify-content: space-between; 
            backdrop-filter: blur(10px); position: relative; z-index: 1; transition: 0.3s; 
        }}
        .service-card:hover {{ border-color: #ffd700; box-shadow: 0 0 20px rgba(255, 215, 0, 0.2); transform: translateY(-5px); }}
        
        .card-accent {{ position: absolute; top: 0; left: 0; width: 3px; height: 100%; }}
        .accent-free {{ background: #00f2fe; box-shadow: 0 0 10px #00f2fe; }}
        .accent-pay {{ background: #ffd700; box-shadow: 0 0 10px #ffd700; }}
        
        .domain-tag {{ font-family: 'Orbitron'; font-size: 0.6rem; color: #00f2fe; letter-spacing: 1px; }}
        .card-title {{ font-family: 'Orbitron'; font-size: 1.1rem; color: #ffffff; margin: 5px 0; }}
        .price-value {{ font-family: 'Orbitron'; font-size: 1rem; font-weight: bold; text-align: right; }}
        
        /* Boite de paiement */
        .payment-box {{ background: rgba(15, 15, 25, 0.95); border: 1px solid #ffd700; padding: 25px; border-radius: 8px; text-align: center; }}
        </style>
        {html_icons}
        """, unsafe_allow_html=True)

inject_ui()

# --- 3. CATALOGUE DES 19 MODÈLES ---
CATALOGUE = [
    {"dom": "CODE", "t": "Assistant Python", "price": "GRATUIT", "d": "Optimisation et debug de scripts Python.", "instr": "Expert Python senior..."},
    {"dom": "EDITION", "t": "Correcteur Ortho", "price": "GRATUIT", "d": "Correction de mémoires et textes académiques.", "instr": "Correcteur académique..."},
    {"dom": "ART", "t": "Générateur Prompt", "price": "GRATUIT", "d": "Prompts Midjourney et Flux ultra-précis.", "instr": "Prompt Engineer..."},
    {"dom": "GAME", "t": "Maître de Jeu", "price": "GRATUIT", "d": "Narration de JDR interactive.", "instr": "Game Master..."},
    {"dom": "LEGAL", "t": "Expert Contrats", "price": "5000 FCFA", "d": "Analyse juridique et clauses de contrats.", "instr": "Avocat spécialisé..."},
    {"dom": "SEO", "t": "Auditeur Google", "price": "15000 FCFA", "d": "Stratégie de mots-clés et ranking.", "instr": "Expert SEO..."},
    {"dom": "CYBER", "t": "Pentester IA", "price": "25000 FCFA", "d": "Audit de vulnérabilités et sécurité.", "instr": "Hacker éthique..."},
    {"dom": "PRO", "t": "Ghostwriter LinkedIn", "price": "7500 FCFA", "d": "Contenu viral pour influenceurs pro.", "instr": "Expert LinkedIn..."},
    {"dom": "RH", "t": "Scanneur de CV", "price": "10000 FCFA", "d": "Matching profils et postes vacants.", "instr": "Recruteur senior..."},
    {"dom": "BIZ", "t": "Business Planner", "price": "50000 FCFA", "d": "Business plans complets pour banques.", "instr": "Consultant strat..."},
    {"dom": "IMMO", "t": "Expert Immo SN", "price": "12000 FCFA", "d": "Calcul rentabilité et cash-flow immobilier.", "instr": "Expert Immo..."},
    {"dom": "ADS", "t": "Média Buyer", "price": "15000 FCFA", "d": "Ads Facebook, TikTok et Google.", "instr": "Média Buyer..."},
    {"dom": "SANTÉ", "t": "Assistant Médical", "price": "10000 FCFA", "d": "Analyse simplifiée de rapports médicaux.", "instr": "Assistant santé..."},
    {"dom": "TECH", "t": "Architecte Cloud", "price": "30000 FCFA", "d": "Infrastructures AWS / Azure.", "instr": "Cloud Architect..."},
    {"dom": "STUDY", "t": "Tuteur Académique", "price": "5000 FCFA", "d": "Support aux étudiants et thèses.", "instr": "Professeur IA..."},
    {"dom": "VIDEO", "t": "Scriptwriter YT", "price": "8000 FCFA", "d": "Scripts vidéo à haute rétention.", "instr": "Scénariste..."},
    {"dom": "ECOM", "t": "Fiches Produits", "price": "7000 FCFA", "d": "Copywriting pour Shopify/Amazon.", "instr": "Copywriter..."},
    {"dom": "VIP", "t": "Concierge Luxe", "price": "15000 FCFA", "d": "Voyages et services exclusifs.", "instr": "Concierge..."},
    {"dom": "INVEST", "t": "Analyste Pitch", "price": "20000 FCFA", "d": "Analyse de decks pour investisseurs.", "instr": "Analyste VC..."}
]

# --- 4. GESTION DE LA NAVIGATION ---
if "view" not in st.session_state: st.session_state.view = "market"

# --- 5. LOGIQUE DES VUES ---

# MARCHÉ
if st.session_state.view == "market":
    st.markdown('<h1 class="neon-title">FORGE IA | CENTRAL CORE</h1>', unsafe_allow_html=True)
    col_s, _ = st.columns([1, 1])
    with col_s:
        search = st.text_input("🔍 RECHERCHE (DOMAINE OU AGENT)...")
    
    filtered = [i for i in CATALOGUE if search.lower() in i['t'].lower() or search.lower() in i['dom'].lower()]
    st.divider()

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                is_free = item["price"] == "GRATUIT"
                with cols[j]:
                    st.markdown(f"""
                    <div class="service-card">
                        <div class="card-accent {'accent-free' if is_free else 'accent-pay'}"></div>
                        <div>
                            <div class="domain-tag">{item['dom']}</div>
                            <div class="card-title">{item['t']}</div>
                            <div style="font-size:0.85rem; color:#bbb; border-top:1px solid rgba(255,255,255,0.05); padding-top:10px;">{item['d']}</div>
                        </div>
                        <div class="price-value" style="color:{'#00f2fe' if is_free else '#ffd700'};">{item['price']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"CONFIGURER {item['t']}", key=f"btn_{i+j}"):
                        st.session_state.selected_item = item
                        st.session_state.view = "forge_custom"
                        st.rerun()

# FORGE PERSONNALISÉE
elif st.session_state.view == "forge_custom":
    item = st.session_state.selected_item
    st.markdown(f'<h1 class="neon-title">PERSONNALISATION</h1>', unsafe_allow_html=True)
    st.markdown(f"### ⚙️ {item['t']} ({item['price']})")
    
    n_name = st.text_input("Nom de l'agent", value=item["t"])
    n_instr = st.text_area("Directives (Cerveau de l'IA)", value=item["instr"], height=250)
    st.session_state.temp_config = {"name": n_name, "instr": n_instr}
    
    c1, c2 = st.columns([1, 4])
    with c1:
        if st.button("🚀 GÉNÉRER"):
            st.session_state.view = "download_ready" if item["price"] == "GRATUIT" else "payment_gate"
            st.rerun()
    with c2:
        if st.button("← Retour"): st.session_state.view = "market"; st.rerun()

# PAIEMENT (SENEGAL OPTIMIZED)
elif st.session_state.view == "payment_gate":
    item = st.session_state.selected_item
    config = st.session_state.temp_config
    st.markdown('<h1 class="neon-title">PAIEMENT SÉCURISÉ</h1>', unsafe_allow_html=True)
    
    cols = st.columns([1, 1.5, 1])
    with cols[1]:
        st.markdown(f"""
            <div class="payment-box">
                <h3>Finalisation : {config['name']}</h3>
                <p>Montant : <b style="color:#ffd700; font-size:1.4rem;">{item['price']}</b></p>
                <hr style="border-color:rgba(255,255,255,0.1);">
                <p>Payez via <b>Wave</b> ou <b>Orange Money</b> pour débloquer votre IA.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # NOTE : Ici tu mettras ton lien CinetPay ou ton lien de paiement local
        pay_url = "https://votre-lien-de-paiement.com" 
        
        st.markdown(f"""
            <div style="text-align:center; margin-top:20px;">
                <a href="{pay_url}" target="_blank" 
                   style="background: #2ecc71; color: white; padding: 15px 35px; text-decoration: none; font-weight: bold; border-radius: 5px; display: inline-block;">
                    🟢 PAYER PAR WAVE / ORANGE MONEY
                </a>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("J'AI PAYÉ ✅"):
            with st.spinner("Vérification..."):
                time.sleep(2)
                st.session_state.view = "download_ready"
                st.rerun()
        if st.button("Annuler"): st.session_state.view = "market"; st.rerun()

# TÉLÉCHARGEMENT
elif st.session_state.view == "download_ready":
    config = st.session_state.temp_config
    st.markdown('<h1 class="neon-title">IA FORGÉE</h1>', unsafe_allow_html=True)
    st.success(f"L'agent '{config['name']}' est prêt pour l'exportation.")
    
    final_json = json.dumps(config, indent=4)
    st.download_button("📥 TÉLÉCHARGER LE FICHIER JSON", final_json, f"{config['name']}.json")
    
    if st.button("← Retour au Marché"): st.session_state.view = "market"; st.rerun()