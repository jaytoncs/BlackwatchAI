import sys
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from collectors.cisa import get_cisa_kev

st.set_page_config(
    page_title="Blackwatch AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #070B14 0%, #0B1220 50%, #111827 100%);
    color: #E5E7EB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(135deg, rgba(37,99,235,0.22), rgba(15,23,42,0.95));
    border: 1px solid rgba(96,165,250,0.35);
    padding: 2rem;
    border-radius: 24px;
    margin-bottom: 1.5rem;
    box-shadow: 0 0 40px rgba(37,99,235,0.15);
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0;
}

.hero p {
    color: #9CA3AF;
    font-size: 1.1rem;
}

.metric-card {
    background: rgba(17,24,39,0.92);
    border: 1px solid rgba(75,85,99,0.55);
    padding: 1.4rem;
    border-radius: 18px;
    box-shadow: 0 0 24px rgba(0,0,0,0.25);
}

.metric-label {
    color: #9CA3AF;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #F9FAFB;
}

.status-live {
    color: #22C55E;
    font-weight: 700;
}

.status-elevated {
    color: #F97316;
    font-weight: 700;
}

.brief-card {
    background: rgba(15,23,42,0.96);
    border-left: 5px solid #3B82F6;
    padding: 1.5rem;
    border-radius: 18px;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

.threat-card {
    background: rgba(17,24,39,0.96);
    border: 1px solid rgba(75,85,99,0.5);
    padding: 1.3rem;
    border-radius: 18px;
    margin-bottom: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    background: rgba(239,68,68,0.18);
    color: #FCA5A5;
    border: 1px solid rgba(239,68,68,0.35);
}

.small-muted {
    color: #9CA3AF;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

kev_items = get_cisa_kev(limit=15)
current_time = datetime.now().strftime("%B %d, %Y • %I:%M %p")

st.markdown(f"""
<div class="hero">
    <h1>🛡️ Blackwatch AI</h1>
    <p>Mission Control for cyber threat intelligence and decision support.</p>
    <p class="small-muted">Last updated: {current_time}</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Threat Level</div>
        <div class="metric-value status-elevated">Elevated</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Active Exploits</div>
        <div class="metric-value">{len(kev_items)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">CISA KEV Feed</div>
        <div class="metric-value status-live">Live</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Platform Version</div>
        <div class="metric-value">v0.2.0</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="brief-card">
    <h3>Executive Brief</h3>
    <p>
    Blackwatch AI identified <strong>{len(kev_items)}</strong> known exploited vulnerabilities from CISA's live KEV catalog.
    These vulnerabilities have confirmed real-world exploitation and should be prioritized over routine vulnerability review.
    The next phase of Blackwatch AI will introduce intelligent prioritization, AI-generated executive briefings,
    and industry-specific risk analysis.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Mission Control: Active Exploited Vulnerabilities")

for item in kev_items:
    st.markdown(f"""
    <div class="threat-card">
        <span class="badge">KNOWN EXPLOITED</span>
        <h3>{item['id']} — {item['name']}</h3>
        <p><strong>Vendor/Product:</strong> {item['vendor']} {item['product']}</p>
        <p><strong>Date Added:</strong> {item['date_added']} &nbsp; | &nbsp; <strong>Due Date:</strong> {item['due_date']}</p>
        <p><strong>Required Action:</strong> {item['action']}</p>
        <p class="small-muted">Source: {item['source']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="brief-card">
    <h3>Coming Next</h3>
    <p>
    Blackwatch Priority Engine • AI Executive Briefings • Industry Risk Profiles • Threat Forecasting
    </p>
</div>
""", unsafe_allow_html=True)
