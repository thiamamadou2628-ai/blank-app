import streamlit as st
import json
import random
import time
import streamlit.components.v1 as components

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="FORGE IA | SENEGAL FREE", layout="wide")

# --- 2. SYSTÈME D'UI : ICÔNES TOMBANTES & CSS CYBER ---
def inject_ui():
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
        
        .stApp {{ background-color: #050507; color: #f0f0f0; font-family: 'Rajdhani', sans-serif; }}
        
        @keyframes fall {{ 
            0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 0; }} 
            15% {{ opacity: 0.25; }} 
            85% {{ opacity: 0.25; }} 
            100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }} 
        }}
        .bg-icon {{ position: fixed; top: -10%; z-index: 0; pointer-events: none; animation: fall linear infinite; }}
        
        .neon-title {{ 
            font-family: 'Orbitron'; 
            background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
            text-align: center; font-size: 3rem; margin-bottom: 10px; 
        }}

        .service-card {{ 
            background: rgba(255, 255, 255, 0.03); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 4px; padding: 18px; height: 280px; 
            display: flex; flex-direction: column; justify-content: space-between; 
            backdrop-filter: blur(10px); transition: 0.3s; 
        }}
        .service-card:hover {{ border-color: #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.2); transform: translateY(-5px); }}
        
        .domain-tag {{ font-family: 'Orbitron'; font-size: 0.6rem; color: #00f2fe; letter-spacing: 1px; }}
        .card-title {{ font-family: 'Orbitron'; font-size: 1.1rem; color: #ffffff; margin: 5px 0; }}
        .free-badge {{ font-family: 'Orbitron'; font-size: 0.8rem; color: #2ecc71; font-weight: bold; }}

        /* Zone Publicité */
        .ad-zone {{ 
            background: rgba(255,255,255,0.05); 
            border: 1px dashed rgba(255,255,255,0.2); 
            text-align: center; padding: 10px; margin: 10px 0;
            color: #666; font-size: 0.8rem;
        }}
        </style>
        {html_icons}
        """, unsafe_allow_html=True)

inject_ui()

# --- 3. CATALOGUE 100% GRATUIT ---
CATALOGUE = [
    {"dom": "CODE", "t": "Assistant Python", "price": "ACCÈS LIBRE", "d": "Optimisation et debug de scripts Python.", "instr": "Expert Python senior..."},
    {"dom": "EDITION", "t": "Correcteur Ortho", "price": "ACCÈS LIBRE", "d": "Correction de mémoires et textes académiques.", "instr": "Correcteur académique..."},
    {"dom": "ART", "t": "Générateur Prompt", "price": "ACCÈS LIBRE", "d": "Prompts Midjourney et Flux ultra-précis.", "instr": "Prompt Engineer..."},
    {"dom": "IMMO", "t": "Expert Immo SN", "price": "ACCÈS LIBRE", "d": "Calcul rentabilité immobilier Sénégal.", "instr": "Expert Immo..."},
    {"dom": "SEO", "t": "Auditeur Google", "price": "ACCÈS LIBRE", "d": "Stratégie de mots-clés et ranking.", "instr": "Expert SEO..."},
    {"dom": "PRO", "t": "Ghostwriter LinkedIn", "price": "ACCÈS LIBRE", "d": "Contenu viral pour influenceurs pro.", "instr": "Expert LinkedIn..."},
    {"dom": "RH", "t": "Scanneur de CV", "price": "ACCÈS LIBRE", "d": "Matching profils et postes vacants.", "instr": "Recruteur senior..."},
    {"dom": "BIZ", "t": "Business Planner", "price": "ACCÈS LIBRE", "d": "Business plans complets.", "instr": "Consultant strat..."},
    {"dom": "ADS", "t": "Média Buyer", "price": "ACCÈS LIBRE", "d": "Ads Facebook, TikTok et Google.", "instr": "Média Buyer..."},
    {"dom": "SANTÉ", "t": "Assistant Médical", "price": "ACCÈS LIBRE", "d": "Analyse simplifiée de rapports.", "instr": "Assistant santé..."},
    {"dom": "STUDY", "t": "Tuteur Académique", "price": "ACCÈS LIBRE", "d": "Support aux étudiants sénégalais.", "instr": "Professeur IA..."},
    {"dom": "VIDEO", "t": "Scriptwriter YT", "price": "ACCÈS LIBRE", "d": "Scripts vidéo haute rétention.", "instr": "Scénariste..."},
    {"dom": "ECOM", "t": "Fiches Produits", "price": "ACCÈS LIBRE", "d": "Copywriting pour boutiques en ligne.", "instr": "Copywriter..."}
]

# --- 4. LOGIQUE DES VUES ---
if "view" not in st.session_state: st.session_state.view = "market"

# PUB HAUT
st.markdown('<div class="ad-zone">ESPACE PUBLICITAIRE DISPONIBLE</div>', unsafe_allow_html=True)

if st.session_state.view == "market":
    st.markdown('<h1 class="neon-title">FORGE IA FREE</h1>', unsafe_allow_html=True)
    st.write("<center style='color:#888'>Accès illimité aux cerveaux artificiels les plus puissants.</center>", unsafe_allow_html=True)
    
    search = st.text_input("🔍 RECHERCHE UN EXPERT...")
    filtered = [i for i in CATALOGUE if search.lower() in i['t'].lower() or search.lower() in i['dom'].lower()]
    
    st.divider()

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="service-card">
                        <div>
                            <div class="domain-tag">{item['dom']}</div>
                            <div class="card-title">{item['t']}</div>
                            <div style="font-size:0.85rem; color:#bbb; padding-top:10px;">{item['d']}</div>
                        </div>
                        <div class="free-badge">{item['price']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"FORGER {item['t']}", key=f"btn_{i+j}"):
                        st.session_state.selected_item = item
                        st.session_state.view = "forge_custom"
                        st.rerun()

elif st.session_state.view == "forge_custom":
    item = st.session_state.selected_item
    st.markdown(f'<h1 class="neon-title">CONFIGURATION</h1>', unsafe_allow_html=True)
    
    n_name = st.text_input("Nom de ton IA", value=item["t"])
    n_instr = st.text_area("Cerveau de l'agent (Instructions)", value=item["instr"], height=200)
    st.session_state.temp_config = {"name": n_name, "instr": n_instr}
    
    if st.button("🚀 GÉNÉRER MAINTENANT (GRATUIT)"):
        with st.spinner("Forgeage en cours..."):
            time.sleep(1.5)
            st.session_state.view = "download_ready"
            st.rerun()
    
    if st.button("← Retour"): st.session_state.view = "market"; st.rerun()

elif st.session_state.view == "download_ready":
    config = st.session_state.temp_config
    st.markdown('<h1 class="neon-title">UNITÉ PRÊTE</h1>', unsafe_allow_html=True)
    st.success(f"L'agent '{config['name']}' a été forgé avec succès.")
    
    final_json = json.dumps(config, indent=4)
    st.download_button("📥 RÉCUPÉRER MON AGENT IA", final_json, f"{config['name']}.json")
    
    st.info("💡 Importez ce fichier dans votre interface ChatGPT ou Claude pour activer l'expert.")
    
    if st.button("← Créer une autre IA"): st.session_state.view = "market"; st.rerun()

# PUB BAS
st.divider()
st.markdown('<div class="ad-zone">ZONE DE PUBLICITÉ INFÉRIEURE</div>', unsafe_allow_html=True)