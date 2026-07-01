import sys
from pathlib import Path

# Allow Python to find our project folders
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from collectors.cisa import get_cisa_kev

# ----------------------------
# Page Setup
# ----------------------------

st.set_page_config(
    page_title="Blackwatch AI",
    page_icon="🛡️",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("🛡️ Blackwatch AI")
st.subheader("Autonomous Threat Intelligence Platform")

st.divider()

# ----------------------------
# Get Live Data
# ----------------------------

kev_items = get_cisa_kev(limit=10)

# ----------------------------
# Metrics
# ----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Threat Level", "ELEVATED")

with col2:
    st.metric("Known Exploited Vulnerabilities", len(kev_items))

with col3:
    st.metric("Feed Status", "LIVE")

st.divider()

# ----------------------------
# Executive Brief
# ----------------------------

st.header("Executive Brief")

st.info(
    f"Blackwatch AI detected {len(kev_items)} actively exploited vulnerabilities "
    "from CISA's Known Exploited Vulnerabilities Catalog."
)

# ----------------------------
# Mission Control
# ----------------------------

st.header("Mission Control")

for item in kev_items:

    with st.container(border=True):

        st.subheader(item["id"])

        st.write(f"**Vendor:** {item['vendor']}")
        st.write(f"**Product:** {item['product']}")
        st.write(f"**Vulnerability:** {item['name']}")
        st.write(f"**Date Added:** {item['date_added']}")
        st.write(f"**Due Date:** {item['due_date']}")
