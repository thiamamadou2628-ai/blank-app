import streamlit as st
import json
import random
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="FORGE IA | ULTIMATE BUSINESS", layout="wide")

# --- 2. SYSTÈME D'UI & ANIMATIONS ---
def inject_ui_ultimate():
    # Icônes tombantes en arrière-plan
    icons = ["🤖", "⚙️", "💻", "🧠", "⚛️", "🛡️", "⚡", "🌐", "💾", "🔑"]
    html_icons = "".join([f'<div class="bg-icon" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(10, 25)}s; animation-delay:{random.randint(0, 10)}s; font-size:{random.randint(15, 30)}px;">{random.choice(icons)}</div>' for _ in range(15)])
    
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&family=Fira+Code:wght@400;500&display=swap');
        
        .stApp {{ background-color: #050507; color: #f0f0f0; font-family: 'Rajdhani', sans-serif; }}
        
        /* Arrière-plan */
        @keyframes fall {{ 0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 0; }} 15% {{ opacity: 0.25; }} 100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }} }}
        .bg-icon {{ position: fixed; top: -10%; z-index: 0; pointer-events: none; animation: fall linear infinite; }}

        /* Logo Animé */
        .logo-container {{ display: flex; flex-direction: column; align-items: center; margin-bottom: 20px; z-index: 10; }}
        .forge-sphere {{ 
            width: 80px; height: 80px; border-radius: 50%;
            background: radial-gradient(circle, #ffd700 20%, #b8860b 60%, transparent 70%);
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.6);
            animation: pulseSphere 3s infinite ease-in-out; position: relative;
        }}
        @keyframes pulseSphere {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.1); box-shadow: 0 0 45px rgba(255, 215, 0, 0.9); }} }}
        .neon-title {{ font-family: 'Orbitron'; background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; }}

        /* 1. TICKER ACTIVITÉ (Bandeau défilant) */
        .ticker-wrapper {{ 
            width: 100%; overflow: hidden; background: rgba(255, 215, 0, 0.1); 
            border-top: 1px solid rgba(255, 215, 0, 0.2); border-bottom: 1px solid rgba(255, 215, 0, 0.2);
            padding: 5px 0; margin-bottom: 30px;
        }}
        .ticker-text {{ 
            display: inline-block; white-space: nowrap; animation: ticker 40s linear infinite;
            font-family: 'Orbitron'; font-size: 0.7rem; color: #ffd700;
        }}
        @keyframes ticker {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}

        /* 3. EFFET MATRIX */
        .matrix-container {{
            background: #000; color: #00ff41; font-family: 'Fira Code', monospace;
            padding: 20px; border: 1px solid #00ff41; height: 300px; overflow: hidden; position: relative;
        }}
        .matrix-line {{ animation: matrixMove 2s linear infinite; opacity: 0.8; font-size: 0.8rem; }}
        @keyframes matrixMove {{ from {{ transform: translateY(-100%); }} to {{ transform: translateY(100%); }} }}

        /* Cartes & Boutons */
        .service-card {{ 
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 4px; padding: 18px; height: 260px; transition: 0.3s;
            display: flex; flex-direction: column; justify-content: space-between;
        }}
        .service-card:hover {{ border-color: #ffd700; background: rgba(255, 215, 0, 0.05); }}
        .premium-card {{ border: 1px solid #ffd700 !important; }}
        .custom-card {{ border: 1px dashed #00f2fe !important; background: rgba(0, 242, 254, 0.05) !important; }}
        </style>
        {html_icons}
        <div class="logo-container">
            <div class="forge-sphere"></div>
            <h1 class="neon-title">FORGE IA</h1>
        </div>
        <div class="ticker-wrapper">
            <div class="ticker-text">
                ⚡ Saliou (Dakar) a forgé un Assistant Python -- 💰 Vente Premium : Expert Immo SN (Thiès) -- ⚡ 241 Agents créés aujourd'hui -- 🌐 Nouveau : Mode Sur-Mesure pour Entreprises -- 💰 Modou a rejoint le programme Business -- 🚀 IA forgeage en cours...
            </div>
        </div>
    """, unsafe_allow_html=True)

inject_ui_ultimate()

# --- 3. CATALOGUE (Hybride + Sur-Mesure) ---
CATALOGUE = [
    {"id": "amb", "type": "FREE", "dom": "MKTG", "t": "Ambassadeur Digital", "p": "GRATUIT", "d": "Promotion virale naturelle."},
    {"id": "py", "type": "FREE", "dom": "CODE", "t": "Assistant Python", "p": "GRATUIT", "d": "Debug & Optimisation."},
    {"id": "law", "type": "PREMIUM", "dom": "DROIT", "t": "Expert Juridique SN", "p": "15 $", "d": "Droit des affaires Sénégalais.", "link": "https://gumroad.com/l/ton-lien-juridique"},
    {"id": "biz", "type": "PREMIUM", "dom": "BIZ", "t": "Business Planner Pro", "p": "25 $", "d": "Plans financiers investisseurs.", "link": "https://gumroad.com/l/ton-lien-biz"}
]

if "view" not in st.session_state: st.session_state.view = "market"

# --- 4. VUE MARCHÉ ---
if st.session_state.view == "market":
    cols = st.columns(2)
    for idx, item in enumerate(CATALOGUE):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="service-card {'premium-card' if item['type'] == 'PREMIUM' else ''}">
                <div>
                    <div style="font-family:'Orbitron'; font-size:0.6rem; color:#00f2fe;">{item['dom']}</div>
                    <div style="font-family:'Orbitron'; font-size:1.1rem; color:white; margin:5px 0;">{item['t']}</div>
                    <div style="color:#bbb; font-size:0.85rem;">{item['d']}</div>
                </div>
                <div style="color:{'#ffd700' if item['type'] == 'PREMIUM' else '#2ecc71'}; font-weight:bold;">{item['p']}</div>
            </div>
            """, unsafe_allow_html=True)
            if item['type'] == 'PREMIUM':
                st.link_button("🛒 ACHETER SUR GUMROAD", item['link'], use_container_width=True)
            else:
                if st.button(f"⚒️ FORGER L'AGENT", key=f"f_{idx}", use_container_width=True):
                    st.session_state.selected_item = item
                    st.session_state.view = "forge_custom"
                    st.rerun()

    # 2. SECTION SUR-MESURE (Attractivité Business)
    st.divider()
    st.markdown("""
        <div class="service-card custom-card">
            <h3 style="color:#00f2fe; margin-top:0; font-family:'Orbitron';">🤖 SERVICE SUR-MESURE</h3>
            <p style="font-size:0.9rem;">Besoin d'une IA spécifique pour votre entreprise au Sénégal ? Nous développons votre agent personnalisé sous 48h.</p>
            <div style="color:#00f2fe; font-weight:bold;">DEVIS GRATUIT</div>
        </div>
    """, unsafe_allow_html=True)
    st.button("📩 CONTACTER NOTRE EXPERT (WHATSAPP)", use_container_width=True)

# --- 5. VUE CONFIGURATION ---
elif st.session_state.view == "forge_custom":
    st.subheader(f"Configuration : {st.session_state.selected_item['t']}")
    n_name = st.text_input("Nom de l'unité", value=st.session_state.selected_item['t'])
    n_instr = st.text_area("Instructions cérébrales", height=150)
    
    if st.button("🚀 LANCER LA FORGE"):
        st.session_state.temp_config = {"name": n_name, "instr": n_instr}
        st.session_state.view = "generating" # Direction l'effet Matrix
        st.rerun()
    st.button("Annuler", on_click=lambda: st.session_state.update({"view": "market"}))

# --- 6. VUE MATRIX (L'Effet Visuel) ---
elif st.session_state.view == "generating":
    st.markdown('<div class="matrix-container">', unsafe_allow_html=True)
    placeholder = st.empty()
    for _ in range(20):
        code_lines = [f"0x{random.randint(100,999)} FORGING_CORE_... SUCCESS", "DOWLOADING_KNOWLEDGE_PACK...", "ENCRYPTING_PERSONA_JSON...", "SYNCING_WITH_SENEGAL_SERVER..."]
        placeholder.markdown(f'<div class="matrix-line">{random.choice(code_lines)}</div>' * 10, unsafe_allow_html=True)
        time.sleep(0.1)
    st.session_state.view = "download_ready"
    st.rerun()

# --- 7. VUE TÉLÉCHARGEMENT ---
elif st.session_state.view == "download_ready":
    st.success("FORGEAGE TERMINÉ AVEC SUCCÈS")
    st.download_button("📥 RÉCUPÉRER MON AGENT IA", json.dumps(st.session_state.temp_config, indent=4), "agent.json")
    st.button("Retour au Marché", on_click=lambda: st.session_state.update({"view": "market"}))