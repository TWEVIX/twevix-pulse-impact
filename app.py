import base64
import pandas as pd
import streamlit as st

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="TWEVIX PULSE™ | Audited Solutions & Impact Telemetry",
    page_icon="favicon.png",
    layout="wide",
)
with open("logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()



st.markdown(
    """
    <style>
    .stApp { background-color: #020617; color: #f8fafc; }
    .hero-banner {
        background: linear-gradient(135deg, rgba(16,185,129,0.16) 0%, #0f172a 70%);
        border: 1px solid rgba(52,211,153,0.4);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
    }
    .impact-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-left: 4px solid #10b981;
        border-radius: 14px;
        padding: 22px 24px;
        margin-bottom: 14px;
    }
    .metric-pill {
        display: inline-block;
        background: rgba(16,185,129,0.15);
        color: #6ee7b7;
        border: 1px solid rgba(52,211,153,0.35);
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    .sector-tag {
        display: inline-block;
        background: #1e293b;
        color: #94a3b8;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .stButton > button, .stLinkButton > a {
        background: #10b981 !important;
        color: #020617 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

DEFAULT_CASES = [
    {
        "credential_id": "TVX-8F4A2C91E0B7",
        "client_sector": "Food & Hospitality SME",
        "deployment_title": "Perishable Waste & RFM Retention Engine for Kigali Artisan Bakery",
        "problem_solved": "High daily unsold afternoon pastry waste and unmonitored drop-off among repeat weekend buyers.",
        "impact_metric": "+14% Monthly Net Margin • -22% Perishable Waste",
        "verified_outcome": "Audited 90 days of POS & stock CSVs; isolated 22% afternoon perishable waste and engineered an RFM loyalty bundle recovering 14% monthly margin.",
        "stack": "Python | RFM Segmentation | Margin Diagnostics",
        "name": "Jean-Paul Mugisha",
        "cycle_number": "Cycle 01 (3 Months)",
        "issue_date": "2026-08-15",
    },
    {
        "credential_id": "TVX-4B9E10D7C3A2",
        "client_sector": "Agri-Supply Chain & NGO",
        "deployment_title": "East African Agricultural Supply-Chain Price Volatility Forecaster",
        "problem_solved": "Unpredictable staple commodity price swings disrupting regional procurement budgets.",
        "impact_metric": "12,000+ Market Records Modeled • -18% Forecast Error",
        "verified_outcome": "Co-built time-series forecasting pipelines across 12,000+ regional market records with international peer reviewers.",
        "stack": "Holt-Winters Forecasting | Pandas | Time-Series Modeling",
        "name": "Jean-Paul Mugisha",
        "cycle_number": "Cycle 02 (3 Months)",
        "issue_date": "2026-11-15",
    },
    {
        "credential_id": "TVX-3D91B7E4A205",
        "client_sector": "Healthcare & Cold-Chain Operations",
        "deployment_title": "Cold-Chain Drift Audit & 14-Day Roster Modeling for Outpatient Clinic",
        "problem_solved": "Manual refrigeration temperature logs missing early compressor drift and reactive weekend overtime.",
        "impact_metric": "2 Early Compressor Failures Prevented • -19% Overtime Cost",
        "verified_outcome": "Processed 2,160 hourly refrigeration logs via IsolationForest anomaly detection; flagged 2 early compressor drift events and balanced weekend shift coverage.",
        "stack": "IsolationForest Anomaly Detection | Shift Optimization | Python",
        "name": "Aline Uwase",
        "cycle_number": "Cycle 01 (3 Months)",
        "issue_date": "2026-11-15",
    },
]

@st.cache_data(ttl=300)
def load_cases():
    url = st.secrets.get("PULSE_SHEET_CSV_URL", "")
    if url:
        try:
            return pd.read_csv(url).fillna("").to_dict(orient="records")
        except Exception:
            pass
    return DEFAULT_CASES

cases = load_cases()
st.markdown(
    f"""
    <div style="display:flex;align-items:center;gap:16px;padding:8px 0 20px 0;">
        <img src="data:image/png;base64,{logo_b64}" style="width:62px;height:62px;border-radius:50%;border:2px solid #fbbf24;object-fit:cover;" />
        <div>
            <div style="font-size:26px;font-weight:900;letter-spacing:-0.02em;line-height:1.1;color:#f8fafc;">
                TWEVIX <span style="color:#fbbf24;">PULSE™</span>
            </div>
            <div style="font-size:12px;font-weight:700;letter-spacing:0.16em;color:#94a3b8;text-transform:uppercase;margin-top:4px;">
                 • AUDITED OUTCOME TELEMETRY
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-banner">
        <div style="color:#34d399;font-size:0.78rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;">
            TWEVIX PULSE™ • AUDITED OUTCOME TELEMETRY
        </div>
        <h1 style="margin:0 0 8px 0;font-size:2rem;">Audited Solutions &amp; Impact Showcase</h1>
        <p style="color:#94a3b8;margin:0;max-width:760px;">
            Inspect verified real-world deployments executed by supervised TWEVIX PULSE™ data science pods—complete with before-and-after operational ROI metrics.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
c1.metric("Audited Deployments", f"{len(cases)} Verified Cases")
c2.metric("Average Margin / Cost Gain", "14% – 22% Improvement")
c3.metric("Verification Standard", "SHA-256 Cryptographic")

st.divider()

sectors = ["All Sectors"] + sorted(list({r.get("client_sector", "General") for r in cases if r.get("client_sector")}))
chosen_sector = st.pills("Filter Deployments by Industry Sector:", sectors, default="All Sectors")
if not chosen_sector:
    chosen_sector = "All Sectors"

for idx, row in enumerate(cases):
    if chosen_sector != "All Sectors" and row.get("client_sector") != chosen_sector:
        continue

    st.markdown(
        f"""
        <div class="impact-card">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px;">
                <span class="sector-tag">{row.get('client_sector', 'Enterprise')} • Audit ID: {row.get('credential_id', '')}</span>
                <span class="metric-pill">✓ {row.get('impact_metric', 'Verified ROI')}</span>
            </div>
            <h3 style="margin:4px 0 8px 0;color:#f8fafc;">{row.get('deployment_title', '')}</h3>
            <p style="color:#94a3b8;margin:0;font-size:0.95rem;">
                <strong>Challenge:</strong> {row.get('problem_solved', '')}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander(f"Inspect Audited Methodology & Deploy Similar Solution →", expanded=(idx == 0)):
        left, right = st.columns([2.2, 1])
        with left:
            st.markdown(f"**Verified Outcome:** {row.get('verified_outcome', '')}")
            tools = [t.strip() for t in str(row.get("stack", "")).split("|") if t.strip()]
            if tools:
                st.markdown("**Technical Stack:** " + " • ".join([f"`{t}`" for t in tools]))
            st.caption(f"Delivery Lead: **{row.get('name', '')}** ({row.get('cycle_number', '')}) • Verified {row.get('issue_date', '')}")
        with right:
            st.link_button(
                "Request Similar Deployment →",
                f"mailto:info.pulse@://gmail.com{str(row.get('deployment_title', '')).replace(' ', '%20')}",
                use_container_width=True,
            )

st.divider()
st.link_button("← Back to TWEVIX PULSE™ Home", "https://twevix.com")
