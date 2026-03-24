import streamlit as st
import pandas as pd
import time
import urllib.parse
from datetime import datetime

# 1. CONFIGURACIÓN ESTÉTICA "NEBULA CHU JOY EDITION"
st.set_page_config(page_title="VITAL NEBULA PRO", layout="centered", page_icon="🧬")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    
    .stApp { 
        background: radial-gradient(circle at 50% 50%, #0d1117 0%, #000000 100%); 
        color: #FFFFFF; font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        font-family: 'Orbitron', sans-serif; text-align: center; letter-spacing: 12px;
        background: linear-gradient(180deg, #00FFCC 0%, #FFFFFF 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-top: 20px; filter: drop-shadow(0 0 15px rgba(0,255,204,0.3));
    }

    /* Botones de Acción Estilo Pro */
    .stButton > button {
        border-radius: 12px; height: 3.5em; font-family: 'Orbitron';
        background: linear-gradient(90deg, #00FFCC, #008870); color: white;
        border: none; transition: 0.4s; width: 100%;
    }
    .stButton > button:hover { box-shadow: 0 0 20px #00FFCC; transform: scale(1.02); }

    /* Glassmorphism para Triage */
    div[data-testid="stCheckbox"], div[data-testid="stToggleButton"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 255, 204, 0.1) !important;
        border-radius: 15px !important; padding: 15px !important; margin-bottom: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1 class='main-title'>NEBULA VITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FFCC; letter-spacing:4px; font-size:0.7rem;'>SISTEMA MÉDICO DE ASISTENCIA INTEGRAL</p>", unsafe_allow_html=True)

# --- 2. PANEL DE CONTACTO DIRECTO (CORREGIDO) ---
MI_NUMERO = st.secrets["TELEFONO"]

st.markdown("### 🚨 ACCIÓN INMEDIATA")
c_tel, c_wa = st.columns(2)
with c_tel:
    st.link_button("📞 LLAMAR AHORA", f"tel:+{MI_NUMERO}", use_container_width=True, type="primary")
with c_wa:
    msg_base = urllib.parse.quote("Hola Dr., solicito asistencia inmediata de la plataforma VITAL.")
    st.link_button("💬 WHATSAPP", f"https://wa.me{MI_NUMERO}/?text={msg_base}", use_container_width=True)

with st.expander("📍 SEDE FÍSICA Y HORARIOS"):
    st.write("**Centro Médico Integral Fisioimperium**")
    st.write("Av. Infancia 410, Consultorio 2, Cusco.")
    st.caption("Atención presencial previa cita. Emergencias digitales 24/7.")

st.divider()

# --- 3. SISTEMA DE TRIAGE ---
st.markdown("### 🧪 EVALUACIÓN DE SÍNTOMAS")
col1, col2 = st.columns(2)
with col1:
    f1 = st.checkbox("💓 RITMO CARDIACO")
    f2 = st.checkbox("🫁 RESPIRACIÓN")
    f3 = st.checkbox("🌀 EQUILIBRIO / MAREO")
with col2:
    m1 = st.checkbox("😰 ANSIEDAD / PÁNICO")
    m2 = st.checkbox("🧠 NEBLINA MENTAL")
    m3 = st.toggle("🌿 CANNABIS RESCUE")

# --- 4. PROTOCOLO DE ESTABILIZACIÓN ---
if any([f1, f2, f3, m1, m2, m3]):
    if m3: color, modo = "#A2FF00", [("INHALA", 5, "expand"), ("EXHALA", 5, "contract")]
    elif f3: color, modo = "#FFB800", [("INHALA", 6, "expand"), ("EXHALA", 6, "contract")]
    else: color, modo = "#00FFCC", [("INHALA", 4, "expand"), ("RETÉN", 4, "hold"), ("EXHALA", 4, "contract")]

    ph_txt = st.empty()
    ph_viz = st.empty()
    
    if st.button("▶ INICIAR SESIÓN PRO", use_container_width=True):
        for _ in range(2):
            for fase, seg, anim in modo:
                ph_txt.markdown(f"<h2 style='text-align:center; color:{color}; font-family:Orbitron;'>{fase}</h2>", unsafe_allow_html=True)
                steps = 30
                for i in range(steps + 1):
                    t = i / steps
                    ease = t * t * (3 - 2 * t)
                    r = 60 + (ease * 40) if anim == "expand" else 100 - (ease * 40) if anim == "contract" else 100
                    viz = f'<div style="display:flex;justify-content:center;"><svg width="220" height="220"><circle cx="110" cy="110" r="{r}" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-width="3""")/>></svg></div>'
                    ph_viz.markdown(viz, unsafe_allow_html=True)
                    time.sleep(seg / steps)
        
        st.success("Sesión completada.")
        alivio = st.select_slider("¿Nivel de mejoría?", options=range(1, 11), value=5)

        # --- 5. GESTIÓN DINÁMICA DE CONSULTAS ---
        st.divider()
        sintomas_txt = ", ".join([s for s, b in zip(["Corazón", "Respiración", "Mareo", "Ansiedad", "Foco"], [f1, f2, f3, m1, m2]) if b])

        if m3: # MODO EMERGENCIA
            st.error("🚨 ATENCIÓN PRIORITARIA")
            txt_e = f"EMERGENCIA CANNABIS: Alivio {alivio}/10. Síntomas: {sintomas_txt}."
            url_e = f"https://wa.me{MI_NUMERO}/?text={urllib.parse.quote(txt_e)}"
            st.link_button("🔥 CONTACTAR DOCTOR AHORA", url_e, use_container_width=True, type="primary")
        else: # MODO AGENDA
            st.markdown("<h3 style='text-align:center;'>RESERVAR CITA DE SEGUIMIENTO</h3>", unsafe_allow_html=True)
            ca, cb = st.columns(2)
            f_cita = ca.date_input("Fecha", min_value=datetime.now())
            h_cita = cb.selectbox("Hora", ["10:00 AM", "04:00 PM", "07:00 PM"])
            
            msg_c = f"Deseo programar consulta para el {f_cita} a las {h_cita}. Síntomas: {sintomas_txt}."
            st.link_button("📩 SOLICITAR DISPONIBILIDAD", f"https://wa.me{MI_NUMERO}/?text={urllib.parse.quote(msg_c)}", use_container_width=True)

with st.sidebar:
    st.markdown("### NEBULA VITAL PRO")
    st.caption("Cusco, Perú - v3.0")
    st.info("Utilice esta herramienta bajo supervisión o como apoyo a su tratamiento médico.")

