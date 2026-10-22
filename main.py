import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import io

# Page configuration
st.set_page_config(
    page_title="Retail Studio · Store & Margin Operations",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# APPLE MINIMALIST DESIGN SYSTEM (ZERO EMOJIS, HIGH READABILITY)
# ---------------------------------------------------------
APPLE_CSS = """
<style>
html, body, [class*="css"], .stMarkdown {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    color: #1D1D1F;
    -webkit-font-smoothing: antialiased;
}

.stApp {
    background-color: #FBFBFD;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header[data-testid="stHeader"] {
    background-color: rgba(251, 251, 253, 0.8) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
}

.block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
    max-width: 1280px;
}

/* Header Banner */
.apple-header {
    margin-bottom: 24px;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}

.apple-kicker {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #86868B;
    margin-bottom: 4px;
}

.apple-headline {
    font-size: 30px;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: #1D1D1F;
    margin: 0;
    line-height: 1.2;
}

.apple-subhead {
    font-size: 14px;
    font-weight: 400;
    color: #86868B;
    margin-top: 5px;
    line-height: 1.4;
}

/* KPI Bento Cards */
.apple-card {
    background: #FFFFFF;
    border-radius: 14px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    padding: 20px 22px;
    transition: all 0.2s ease;
}

.apple-card:hover {
    border-color: rgba(0, 0, 0, 0.14);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
}

.kpi-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #86868B;
    margin-bottom: 6px;
}

.kpi-value {
    font-size: 28px;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: #1D1D1F;
    line-height: 1.1;
    margin-bottom: 6px;
}

.kpi-meta {
    display: inline-flex;
    align-items: center;
    font-size: 12px;
    font-weight: 500;
    color: #86868B;
}

.kpi-tag {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 980px;
    font-size: 11px;
    font-weight: 600;
    margin-right: 6px;
}

.tag-neutral { background: #F5F5F7; color: #515154; }
.tag-accent { background: rgba(0, 113, 227, 0.08); color: #0071E3; }
.tag-success { background: rgba(52, 199, 89, 0.12); color: #248A3D; }
.tag-warning { background: rgba(255, 149, 0, 0.12); color: #B25E00; }
.tag-purple { background: rgba(175, 82, 222, 0.12); color: #8932B5; }

/* Panels */
.apple-panel {
    background: #FFFFFF;
    border-radius: 14px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    padding: 22px 24px;
    margin-bottom: 22px;
}

.panel-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 16px;
}

.panel-title {
    font-size: 16px;
    font-weight: 600;
    color: #1D1D1F;
    margin: 0;
}

.panel-caption {
    font-size: 12px;
    color: #86868B;
    margin-top: 2px;
}

/* Step Help Callout for simple retail navigation */
.retail-guide-box {
    background: #FFFFFF;
    border: 1px solid rgba(0, 113, 227, 0.2);
    border-left: 4px solid #0071E3;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 13px;
    color: #1D1D1F;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Tabs */
div[data-baseweb="tab-list"] {
    background-color: #EBEBED;
    padding: 3px;
    border-radius: 10px;
    gap: 3px;
    border: none;
    margin-bottom: 22px;
    width: fit-content;
}

div[data-baseweb="tab"] {
    border-radius: 8px !important;
    padding: 8px 18px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #6E6E73 !important;
    background-color: transparent !important;
    border: none !important;
    transition: all 0.18s ease !important;
}

div[data-baseweb="tab"][aria-selected="true"] {
    background-color: #FFFFFF !important;
    color: #1D1D1F !important;
    font-weight: 600 !important;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #F5F5F7 !important;
    border-right: 1px solid rgba(0, 0, 0, 0.08) !important;
}

.sidebar-title {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #1D1D1F;
    margin-bottom: 12px;
}

.sidebar-divider {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.08);
    margin: 18px 0;
}

/* Buttons */
div.stButton > button {
    background-color: #0071E3 !important;
    color: #FFFFFF !important;
    border-radius: 980px !important;
    padding: 6px 18px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    border: none !important;
}

div.stButton > button:hover {
    background-color: #0077ED !important;
    box-shadow: 0 2px 8px rgba(0, 113, 227, 0.25) !important;
}

div.stDownloadButton > button {
    background-color: #F5F5F7 !important;
    color: #1D1D1F !important;
    border: 1px solid rgba(0, 0, 0, 0.12) !important;
    border-radius: 980px !important;
    padding: 6px 18px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

div.stDownloadButton > button:hover {
    background-color: #EBEBED !important;
}

/* Simple Print Card View */
.print-card {
    background: #FFFFFF;
    border: 1px solid #D2D2D7;
    border-radius: 12px;
    padding: 24px;
    margin-top: 10px;
}
</style>
"""
st.markdown(APPLE_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------
# DATA PIPELINE (SUPPORTS DEFAULT OR UPLOADED FILE)
# ---------------------------------------------------------
def process_data(df):
    # Normalize expected column names
    col_map = {}
    for col in df.columns:
        c_lower = str(col).strip().lower()
        if "product" in c_lower or "item" in c_lower or "name" in c_lower:
            col_map[col] = "Item"
        elif "supply" in c_lower or "cost" in c_lower or "buy" in c_lower:
            col_map[col] = "Cost_Price"
        elif "retail" in c_lower or "sale" in c_lower or "mrp" in c_lower or "sell" in c_lower:
            col_map[col] = "Sale_Price"
            
    df = df.rename(columns=col_map)
    if "Item" not in df.columns:
        df["Item"] = df.iloc[:, 0]
    if "Cost_Price" not in df.columns:
        df["Cost_Price"] = df.iloc[:, 1]
    if "Sale_Price" not in df.columns:
        df["Sale_Price"] = df.iloc[:, 2]

    # Clean numeric fields
    for col in ["Cost_Price", "Sale_Price"]:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace('₹', '', regex=True).str.replace(',', '', regex=True).str.strip().astype(float)
        else:
            df[col] = df[col].astype(float)

    # Simple categorization
    def categorize(name):
        n = str(name).lower()
        if any(w in n for w in ['water', 'drink', 'milk', 'buttermilk', 'juice', 'coffee']):
            return 'Beverages'
        elif any(w in n for w in ['paneer', 'butter']):
            return 'Dairy'
        elif any(w in n for w in ['atta', 'rice', 'moong', 'sugar']):
            return 'Staples'
        elif any(w in n for w in ['garbage', 'tissue', 'tabs', 'detergent']):
            return 'Household'
        elif any(w in n for w in ['chocolate', 'cookie', 'ice cream', 'dates', 'bites', 'walnut']):
            return 'Snacks & Sweets'
        return 'General'

    df['Category'] = df['Item'].apply(categorize)

    # Simplified display names for clarity
    def shorten_label(name):
        s = str(name).strip()
        words = s.split()
        return " ".join(words[:4]) if len(words) > 4 else s

    df['Display_Name'] = df['Item'].apply(shorten_label)

    # Sales units simulation (or use existing column if present)
    if "Monthly_Units" not in df.columns:
        np.random.seed(42)
        df['Monthly_Units'] = np.random.randint(28, 145, size=len(df))

    # Core economics
    df['Revenue'] = (df['Monthly_Units'] * df['Sale_Price']).round(2)
    df['Cost'] = (df['Monthly_Units'] * df['Cost_Price']).round(2)
    df['Profit'] = (df['Revenue'] - df['Cost']).round(2)
    df['Margin_%'] = (((df['Sale_Price'] - df['Cost_Price']) / df['Sale_Price']) * 100).round(1)

    # Product Quadrant Classification (BCG-style Store Matrix)
    margin_median = df['Margin_%'].median()
    volume_median = df['Monthly_Units'].median()

    def classify_quadrant(row):
        is_high_margin = row['Margin_%'] >= margin_median
        is_high_volume = row['Monthly_Units'] >= volume_median
        if is_high_margin and is_high_volume:
            return "Cash Generator"
        elif not is_high_margin and is_high_volume:
            return "Traffic Driver"
        elif is_high_margin and not is_high_volume:
            return "Specialty Premium"
        else:
            return "Underperformer"

    df['Quadrant'] = df.apply(classify_quadrant, axis=1)
    return df


def generate_sample_excel_template():
    sample_items = [
        {"Product Name": "Bisleri Mineral Water 20 LITRE", "SupplyPrice": 85.0, "RetailPrice": 120.0},
        {"Product Name": "Nandini Good Life Milk 500 ML", "SupplyPrice": 29.1, "RetailPrice": 32.0},
        {"Product Name": "Aashirvaad Superior MP Atta 5 KG", "SupplyPrice": 299.5, "RetailPrice": 358.0},
        {"Product Name": "Amul Pasteurised Butter 500 GM", "SupplyPrice": 285.2, "RetailPrice": 310.0},
        {"Product Name": "Surf Excel Matic Powder 1 KG", "SupplyPrice": 268.5, "RetailPrice": 290.0}
    ]
    template_df = pd.DataFrame(sample_items)
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine='openpyxl') as writer:
        template_df.to_excel(writer, index=False, sheet_name='StoreCatalog')
    return buf.getvalue()


# ---------------------------------------------------------
# SIDEBAR CONTROLS (DATA FILE + SIMPLE STORE CONTROLS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">Store Catalog File</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 12px; color: #6E6E73; margin-bottom: 8px;">Upload your own Excel or CSV price sheet to customize the entire dashboard for your store.</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload Store Sheet (.xlsx, .csv)",
        type=["xlsx", "xls", "csv"],
        help="Upload your product sheet with columns: Product Name, SupplyPrice, RetailPrice"
    )

    st.download_button(
        label="Download Blank Excel Template",
        data=generate_sample_excel_template(),
        file_name="store_catalog_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

    is_custom_upload = False
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                raw_input_df = pd.read_csv(uploaded_file)
            else:
                raw_input_df = pd.read_excel(uploaded_file)
            st.success(f"Custom store file loaded: {uploaded_file.name}")
            is_custom_upload = True
        except Exception as e:
            st.error(f"Error reading file: {e}")
            raw_input_df = pd.read_excel("sales_data.xlsx")
    else:
        raw_input_df = pd.read_excel("sales_data.xlsx")

    source_df = process_data(raw_input_df)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Store Department</div>', unsafe_allow_html=True)
    all_depts = ["All Departments"] + sorted(source_df["Category"].unique().tolist())
    selected_dept = st.selectbox(
        "Filter Department",
        options=all_depts,
        index=0,
        help="Choose a specific department or view all"
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Delivery & Orders</div>', unsafe_allow_html=True)
    lead_time_days = st.slider(
        "Supplier Delivery Time (Days)",
        min_value=2,
        max_value=21,
        value=7,
        help="How many days it takes for new stock to arrive"
    )

    safety_days = st.slider(
        "Extra Safety Buffer (Days)",
        min_value=0,
        max_value=14,
        value=2,
        help="Extra buffer days of stock in case supplier is late"
    )


# Apply department filter
if selected_dept != "All Departments":
    df = source_df[source_df["Category"] == selected_dept].copy()
else:
    df = source_df.copy()


# ---------------------------------------------------------
# CHART THEMING HELPER
# ---------------------------------------------------------
def apply_apple_chart_style(fig, height=340):
    fig.update_layout(
        font=dict(
            family='-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif',
            color='#1D1D1F',
            size=12
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=height,
        margin=dict(l=10, r=20, t=25, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11, color='#6E6E73'),
            bgcolor='rgba(255,255,255,0)'
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_size=12,
            font_family='-apple-system, sans-serif',
            font_color='#1D1D1F',
            bordercolor="rgba(0,0,0,0.1)"
        )
    )
    fig.update_xaxes(
        showline=False,
        showgrid=True,
        gridcolor='rgba(0, 0, 0, 0.04)',
        zeroline=False,
        tickfont=dict(size=11, color='#86868B')
    )
    fig.update_yaxes(
        showline=False,
        showgrid=True,
        gridcolor='rgba(0, 0, 0, 0.04)',
        zeroline=False,
        tickfont=dict(size=11, color='#86868B')
    )
    return fig


# ---------------------------------------------------------
# HEADER & STORE SNAPSHOT BANNER
# ---------------------------------------------------------
if is_custom_upload:
    st.markdown(f"""
<div class="apple-header">
    <div class="apple-kicker">Custom Store Catalog Active · {len(source_df)} SKUs Loaded</div>
    <div class="apple-headline">Store Operations & Margin Dashboard</div>
    <div class="apple-subhead">Customized live for <b>{uploaded_file.name}</b>. All margins, purchase orders, and pricing simulations are computed for your inventory.</div>
</div>
""", unsafe_allow_html=True)
else:
    st.markdown("""
<div class="apple-header">
    <div class="apple-kicker">Store Operations & Margin Center</div>
    <div class="apple-headline">Store Intelligence Dashboard</div>
    <div class="apple-subhead">Simple product margins, automated purchase orders, and pricing decision tools. (Upload your own Excel sheet in the sidebar to customize for your store).</div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 4 KEY STORE NUMBERS (SIMPLE & CLEAN)
# ---------------------------------------------------------
total_rev = df["Revenue"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()
blended_margin = (total_profit / total_rev * 100) if total_rev > 0 else 0

# Replenishment calculations
total_days_cycle = lead_time_days + safety_days
df["Daily_Sales"] = (df["Monthly_Units"] / 30.0).round(2)
df["Order_Units"] = (df["Daily_Sales"] * total_days_cycle).round(0).astype(int)
df["Order_Cost"] = (df["Order_Units"] * df["Cost_Price"]).round(2)

total_po_units = df["Order_Units"].sum()
total_po_cost = df["Order_Cost"].sum()

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="apple-card">
        <div class="kpi-title">Monthly Revenue</div>
        <div class="kpi-value">₹ {total_rev:,.0f}</div>
        <div class="kpi-meta"><span class="kpi-tag tag-accent">{len(df)} Products</span> Active catalog</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="apple-card">
        <div class="kpi-title">Estimated Profit</div>
        <div class="kpi-value">₹ {total_profit:,.0f}</div>
        <div class="kpi-meta"><span class="kpi-tag tag-success">₹ {(total_profit / total_rev * 100):.1f}% Yield</span> Net store gain</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="apple-card">
        <div class="kpi-title">Average Margin</div>
        <div class="kpi-value">{blended_margin:.1f}%</div>
        <div class="kpi-meta"><span class="kpi-tag tag-neutral">Gross Margin</span> Across items</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="apple-card">
        <div class="kpi-title">Next Reorder PO Total</div>
        <div class="kpi-value">₹ {total_po_cost:,.0f}</div>
        <div class="kpi-meta"><span class="kpi-tag tag-warning">{total_po_units} Units</span> Total replenishment</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# PRECOMPUTE STORE & DEPARTMENT SUMMARIES FOR ALL TABS
# ---------------------------------------------------------
dept_summary = df.groupby("Category").agg({
    "Revenue": "sum",
    "Profit": "sum",
    "Item": "count"
}).reset_index()
dept_summary["Margin_%"] = np.where(
    dept_summary["Revenue"] > 0,
    ((dept_summary["Profit"] / dept_summary["Revenue"]) * 100).round(1),
    0.0
)
dept_summary = dept_summary.sort_values(by="Revenue", ascending=True)

top_5 = df.sort_values(by="Margin_%", ascending=False).head(5) if len(df) > 0 else df


# ---------------------------------------------------------
# SIMPLIFIED, INTUITIVE NAVIGATION TABS
# ---------------------------------------------------------
tab_overview, tab_po, tab_simulator, tab_quadrant, tab_print = st.tabs([
    "Store Overview",
    "Purchase Order (PO)",
    "Discount & Promo Calculator",
    "Product Roles (Matrix)",
    "1-Page Store Snapshot"
])


# =========================================================
# TAB 1: STORE OVERVIEW (SIMPLE & CLEAR)
# =========================================================
with tab_overview:
    st.markdown("""
    <div class="retail-guide-box">
        <span><b>Guide for Retailer:</b> This section shows which departments generate the most cash and which products yield the best profit margins.</span>
    </div>
    """, unsafe_allow_html=True)

    o1, o2 = st.columns([1.5, 1])
    with o1:
        st.markdown("""
        <div class="apple-panel">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Revenue & Profit by Department</h3>
                    <div class="panel-caption">Compare how much money each department brings in versus profit</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        fig_dept = go.Figure()
        fig_dept.add_trace(go.Bar(
            y=dept_summary["Category"],
            x=dept_summary["Revenue"],
            name="Revenue",
            orientation="h",
            marker=dict(color="#0071E3", line=dict(width=0)),
            hovertemplate="<b>%{y}</b><br>Sales: ₹ %{x:,.2f}<extra></extra>"
        ))
        fig_dept.add_trace(go.Bar(
            y=dept_summary["Category"],
            x=dept_summary["Profit"],
            name="Profit",
            orientation="h",
            marker=dict(color="#34C759", line=dict(width=0)),
            hovertemplate="<b>%{y}</b><br>Profit: ₹ %{x:,.2f}<extra></extra>"
        ))
        fig_dept.update_layout(
            barmode="group",
            bargroupgap=0.15,
            bargap=0.3,
            xaxis=dict(tickformat="₹~s")
        )
        apply_apple_chart_style(fig_dept, height=310)
        st.plotly_chart(fig_dept, use_container_width=True, config={"displayModeBar": False})
        st.markdown("</div>", unsafe_allow_html=True)

    with o2:
        st.markdown("""
        <div class="apple-panel">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Top 5 Margin Leaders</h3>
                    <div class="panel-caption">Highest profit percentage items</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        top_5 = df.sort_values(by="Margin_%", ascending=False).head(5)
        for _, row in top_5.iterrows():
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(0,0,0,0.05);">
                <div>
                    <div style="font-size: 13px; font-weight: 600; color: #1D1D1F;">{row['Display_Name']}</div>
                    <div style="font-size: 11px; color: #86868B;">Retail: ₹ {row['Sale_Price']:.2f} · Cost: ₹ {row['Cost_Price']:.2f}</div>
                </div>
                <div>
                    <span class="kpi-tag tag-success">{row['Margin_%']:.1f}% Margin</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Simplified product table
    st.markdown("""
    <div class="apple-panel">
        <div class="panel-header">
            <div>
                <h3 class="panel-title">Catalog Quick View</h3>
                <div class="panel-caption">Complete product pricing and monthly volume</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        df[["Display_Name", "Category", "Cost_Price", "Sale_Price", "Margin_%", "Monthly_Units", "Revenue", "Profit"]].sort_values(by="Revenue", ascending=False),
        column_config={
            "Display_Name": st.column_config.TextColumn("Product Name", width="medium"),
            "Category": st.column_config.TextColumn("Department", width="small"),
            "Cost_Price": st.column_config.NumberColumn("Cost (₹)", format="₹ %.2f"),
            "Sale_Price": st.column_config.NumberColumn("Retail (₹)", format="₹ %.2f"),
            "Margin_%": st.column_config.ProgressColumn("Margin", format="%.1f%%", min_value=0, max_value=60),
            "Monthly_Units": st.column_config.NumberColumn("Monthly Sales", format="%d units"),
            "Revenue": st.column_config.NumberColumn("Sales (₹)", format="₹ %.2f"),
            "Profit": st.column_config.NumberColumn("Profit (₹)", format="₹ %.2f")
        },
        hide_index=True,
        use_container_width=True,
        height=320
    )
    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# TAB 2: PURCHASE ORDER (PO) GENERATOR
# =========================================================
with tab_po:
    st.markdown(f"""
    <div class="retail-guide-box">
        <span><b>Automated Supplier Purchase Order:</b> Calculates exactly how many units to reorder based on <b>{lead_time_days} days supplier delivery</b> + <b>{safety_days} days safety buffer</b>. Export the PO sheet directly to share with your distributor.</span>
    </div>
    """, unsafe_allow_html=True)

    po_summary1, po_summary2, po_summary3 = st.columns(3)
    with po_summary1:
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 16px 20px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #86868B;">Total Purchase Order Cost</div>
            <div style="font-size: 24px; font-weight: 600; color: #1D1D1F; margin-top: 3px;">₹ {total_po_cost:,.2f}</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 2px;">Total cash needed for this order</div>
        </div>
        """, unsafe_allow_html=True)
    with po_summary2:
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 16px 20px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #86868B;">Total Units to Reorder</div>
            <div style="font-size: 24px; font-weight: 600; color: #0071E3; margin-top: 3px;">{total_po_units} Units</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 2px;">Covers {total_days_cycle} days of inventory</div>
        </div>
        """, unsafe_allow_html=True)
    with po_summary3:
        high_order_skus = len(df[df["Order_Units"] >= 20])
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 16px 20px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #86868B;">Fast-Moving Items</div>
            <div style="font-size: 24px; font-weight: 600; color: #B25E00; margin-top: 3px;">{high_order_skus} Products</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 2px;">Need 20+ units immediately</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    po_table = df[[
        "Item", "Category", "Daily_Sales", "Order_Units", "Cost_Price", "Order_Cost"
    ]].sort_values(by="Order_Cost", ascending=False).reset_index(drop=True)

    st.dataframe(
        po_table,
        column_config={
            "Item": st.column_config.TextColumn("Product Name for Supplier", width="large"),
            "Category": st.column_config.TextColumn("Department", width="small"),
            "Daily_Sales": st.column_config.NumberColumn("Daily Sales", format="%.1f / day"),
            "Order_Units": st.column_config.NumberColumn("Quantity to Order", format="%d units"),
            "Cost_Price": st.column_config.NumberColumn("Supplier Price (₹)", format="₹ %.2f"),
            "Order_Cost": st.column_config.NumberColumn("Total Item Cost (₹)", format="₹ %.2f")
        },
        hide_index=True,
        use_container_width=True,
        height=380
    )

    # Export Buttons
    col_d1, col_d2 = st.columns([1, 4])
    with col_d1:
        po_csv = po_table.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download PO as CSV",
            data=po_csv,
            file_name="supplier_purchase_order.csv",
            mime="text/csv"
        )


# =========================================================
# TAB 3: DISCOUNT & PROMOTION SIMULATOR
# =========================================================
with tab_simulator:
    st.markdown("""
    <div class="retail-guide-box">
        <span><b>Promotion & Margin Simulator:</b> Test discounts (e.g. 5%, 10%, 15% off) or price markups before applying them in store. See immediately if your margin remains safe or turns red.</span>
    </div>
    """, unsafe_allow_html=True)

    sim_col_controls, sim_col_results = st.columns([1, 1.8])

    with sim_col_controls:
        st.markdown("""
        <div class="apple-panel">
            <h3 class="panel-title">Promotion Settings</h3>
            <div class="panel-caption">Choose promotional discount or price markup</div>
            <div style="height: 14px;"></div>
        """, unsafe_allow_html=True)

        promo_type = st.radio(
            "Promotion Strategy",
            ["Storewide Percentage Discount", "Price Markup / Price Increase", "Specific Department Discount"],
            index=0
        )

        target_cat = "All"
        if promo_type == "Specific Department Discount":
            target_cat = st.selectbox("Select Target Department", sorted(df["Category"].unique()))

        adjustment_pct = st.slider(
            "Percentage Change (%)",
            min_value=-25,
            max_value=25,
            value=-10 if "Discount" in promo_type else 5,
            step=1,
            help="Negative numbers indicate discounts; positive numbers indicate price increases"
        )

        expected_volume_boost = st.slider(
            "Estimated Sales Volume Impact (±%)",
            min_value=-20,
            max_value=50,
            value=15 if adjustment_pct < 0 else -5,
            step=5,
            help="Discounts usually increase customer volume; price hikes may slightly reduce volume"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Run simulation
    sim_df = df.copy()
    if target_cat == "All":
        mask = np.ones(len(sim_df), dtype=bool)
    else:
        mask = sim_df["Category"] == target_cat

    price_factor = 1.0 + (adjustment_pct / 100.0)
    volume_factor = 1.0 + (expected_volume_boost / 100.0)

    sim_df.loc[mask, "Sale_Price"] = (sim_df.loc[mask, "Sale_Price"] * price_factor).round(2)
    sim_df.loc[mask, "Monthly_Units"] = (sim_df.loc[mask, "Monthly_Units"] * volume_factor).round(0).astype(int)
    sim_df["Revenue"] = (sim_df["Monthly_Units"] * sim_df["Sale_Price"]).round(2)
    sim_df["Cost"] = (sim_df["Monthly_Units"] * sim_df["Cost_Price"]).round(2)
    sim_df["Profit"] = (sim_df["Revenue"] - sim_df["Cost"]).round(2)
    sim_df["Margin_%"] = (((sim_df["Sale_Price"] - sim_df["Cost_Price"]) / sim_df["Sale_Price"]) * 100).round(1)

    with sim_col_results:
        orig_profit = df["Profit"].sum()
        new_profit = sim_df["Profit"].sum()
        profit_delta = new_profit - orig_profit

        orig_margin = (df["Profit"].sum() / df["Revenue"].sum() * 100) if df["Revenue"].sum() > 0 else 0
        new_margin = (sim_df["Profit"].sum() / sim_df["Revenue"].sum() * 100) if sim_df["Revenue"].sum() > 0 else 0

        st.markdown("""
        <div class="apple-panel">
            <h3 class="panel-title">Projected Financial Impact</h3>
            <div class="panel-caption">Comparison against current baseline store numbers</div>
            <div style="height: 14px;"></div>
        """, unsafe_allow_html=True)

        res1, res2 = st.columns(2)
        with res1:
            profit_color = "#248A3D" if profit_delta >= 0 else "#D70015"
            st.markdown(f"""
            <div style="background: #F5F5F7; border-radius: 10px; padding: 14px 18px;">
                <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #86868B;">Net Profit Impact</div>
                <div style="font-size: 26px; font-weight: 600; color: {profit_color}; margin-top: 4px;">₹ {profit_delta:+,.2f}</div>
                <div style="font-size: 12px; color: #86868B; margin-top: 2px;">New Monthly Profit: ₹ {new_profit:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        with res2:
            st.markdown(f"""
            <div style="background: #F5F5F7; border-radius: 10px; padding: 14px 18px;">
                <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #86868B;">New Blended Margin</div>
                <div style="font-size: 26px; font-weight: 600; color: #1D1D1F; margin-top: 4px;">{new_margin:.1f}%</div>
                <div style="font-size: 12px; color: #86868B; margin-top: 2px;">Was {orig_margin:.1f}% ({new_margin - orig_margin:+.1f}%)</div>
            </div>
            """, unsafe_allow_html=True)

        # Danger check: any items sold below cost?
        below_cost = sim_df[sim_df["Sale_Price"] < sim_df["Cost_Price"]]
        if len(below_cost) > 0:
            st.markdown(f"""
            <div style="margin-top: 14px; background: rgba(255, 59, 48, 0.1); border-left: 3px solid #FF3B30; padding: 10px 14px; border-radius: 6px; font-size: 12px; color: #D70015;">
                <b>Warning:</b> {len(below_cost)} item(s) will be sold at a loss below supplier cost with this discount!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="margin-top: 14px; background: rgba(52, 199, 89, 0.1); border-left: 3px solid #34C759; padding: 10px 14px; border-radius: 6px; font-size: 12px; color: #248A3D;">
                All products maintain positive gross margins under this promotion.
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# TAB 4: PRODUCT ROLES (BCG-STYLE QUADRANT MATRIX)
# =========================================================
with tab_quadrant:
    st.markdown("""
    <div class="retail-guide-box">
        <span><b>Product Role Classification:</b> Tells the store owner exactly what role each product plays in the store so you know what to promote, what to keep, and what to renegotiate.</span>
    </div>
    """, unsafe_allow_html=True)

    quad_c1, quad_c2, quad_c3, quad_c4 = st.columns(4)
    with quad_c1:
        cg_count = len(df[df["Quadrant"] == "Cash Generator"])
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-top: 3px solid #34C759; border-radius: 12px; padding: 16px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #34C759;">Cash Generators</div>
            <div style="font-size: 22px; font-weight: 600; color: #1D1D1F; margin-top: 4px;">{cg_count} Items</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 4px;">High margin + high volume. Your store's profit engine. Keep always stocked.</div>
        </div>
        """, unsafe_allow_html=True)

    with quad_c2:
        td_count = len(df[df["Quadrant"] == "Traffic Driver"])
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-top: 3px solid #0071E3; border-radius: 12px; padding: 16px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #0071E3;">Traffic Drivers</div>
            <div style="font-size: 22px; font-weight: 600; color: #1D1D1F; margin-top: 4px;">{td_count} Items</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 4px;">Low margin + high volume (Milk, Atta). Bring footfall into store.</div>
        </div>
        """, unsafe_allow_html=True)

    with quad_c3:
        sp_count = len(df[df["Quadrant"] == "Specialty Premium"])
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-top: 3px solid #AF52DE; border-radius: 12px; padding: 16px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #AF52DE;">Specialty / Premium</div>
            <div style="font-size: 22px; font-weight: 600; color: #1D1D1F; margin-top: 4px;">{sp_count} Items</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 4px;">High margin + lower volume (Coffee, Walnuts). Give visible shelf placement.</div>
        </div>
        """, unsafe_allow_html=True)

    with quad_c4:
        up_count = len(df[df["Quadrant"] == "Underperformer"])
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08); border-top: 3px solid #FF9500; border-radius: 12px; padding: 16px;">
            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; color: #FF9500;">Underperformers</div>
            <div style="font-size: 22px; font-weight: 600; color: #1D1D1F; margin-top: 4px;">{up_count} Items</div>
            <div style="font-size: 11px; color: #86868B; margin-top: 4px;">Low margin + low volume. Renegotiate cost with supplier or consider delisting.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Simple filter by role
    selected_role = st.radio(
        "View Products by Role",
        ["All Roles", "Cash Generator", "Traffic Driver", "Specialty Premium", "Underperformer"],
        horizontal=True
    )

    role_filtered = df if selected_role == "All Roles" else df[df["Quadrant"] == selected_role]

    st.dataframe(
        role_filtered[[
            "Display_Name", "Category", "Quadrant", "Margin_%", "Monthly_Units", "Sale_Price", "Cost_Price", "Profit"
        ]].sort_values(by="Margin_%", ascending=False),
        column_config={
            "Display_Name": st.column_config.TextColumn("Product Name", width="medium"),
            "Category": st.column_config.TextColumn("Department", width="small"),
            "Quadrant": st.column_config.TextColumn("Role in Store", width="medium"),
            "Margin_%": st.column_config.ProgressColumn("Margin", format="%.1f%%", min_value=0, max_value=60),
            "Monthly_Units": st.column_config.NumberColumn("Monthly Volume", format="%d units"),
            "Sale_Price": st.column_config.NumberColumn("Retail", format="₹ %.2f"),
            "Cost_Price": st.column_config.NumberColumn("Cost", format="₹ %.2f"),
            "Profit": st.column_config.NumberColumn("Profit", format="₹ %.2f")
        },
        hide_index=True,
        use_container_width=True,
        height=360
    )


# =========================================================
# TAB 5: 1-PAGE STORE SNAPSHOT (PRINT / SHARE FRIENDLY)
# =========================================================
with tab_print:
    st.markdown("""
<div class="retail-guide-box">
    <span><b>1-Page Executive Summary:</b> A clean, compact summary ready to print or share with store partners, accountants, or suppliers.</span>
</div>
""", unsafe_allow_html=True)

    # Top 4 summary metrics rendered using clean apple-card containers
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown(f"""
<div class="apple-card">
    <div class="kpi-title">Total Monthly Sales</div>
    <div class="kpi-value">₹ {total_rev:,.0f}</div>
    <div class="kpi-meta"><span class="kpi-tag tag-accent">{len(df)} SKUs</span> Gross sales</div>
</div>
""", unsafe_allow_html=True)
    with p2:
        st.markdown(f"""
<div class="apple-card">
    <div class="kpi-title">Total Inventory Cost</div>
    <div class="kpi-value">₹ {total_cost:,.0f}</div>
    <div class="kpi-meta"><span class="kpi-tag tag-neutral">Stock Outlay</span> Goods cost</div>
</div>
""", unsafe_allow_html=True)
    with p3:
        st.markdown(f"""
<div class="apple-card">
    <div class="kpi-title">Net Store Profit</div>
    <div class="kpi-value" style="color: #248A3D;">₹ {total_profit:,.0f}</div>
    <div class="kpi-meta"><span class="kpi-tag tag-success">{(total_profit/total_rev*100 if total_rev else 0):.1f}%</span> Net yield</div>
</div>
""", unsafe_allow_html=True)
    with p4:
        st.markdown(f"""
<div class="apple-card">
    <div class="kpi-title">Blended Store Margin</div>
    <div class="kpi-value" style="color: #0071E3;">{blended_margin:.1f}%</div>
    <div class="kpi-meta"><span class="kpi-tag tag-neutral">Average Margin</span> Across catalog</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    col_t1, col_t2 = st.columns([1.3, 1])
    with col_t1:
        st.markdown("""
<div class="apple-panel">
    <h3 class="panel-title">Department Financial Breakdown</h3>
    <div class="panel-caption">Sales, profit, and margin contribution by department</div>
    <div style="height: 12px;"></div>
""", unsafe_allow_html=True)

        st.dataframe(
            dept_summary[["Category", "Revenue", "Profit", "Margin_%", "Item"]],
            column_config={
                "Category": st.column_config.TextColumn("Department", width="medium"),
                "Revenue": st.column_config.NumberColumn("Sales (₹)", format="₹ %d"),
                "Profit": st.column_config.NumberColumn("Profit (₹)", format="₹ %d"),
                "Margin_%": st.column_config.ProgressColumn("Margin", format="%.1f%%", min_value=0, max_value=60),
                "Item": st.column_config.NumberColumn("Catalog Items", format="%d SKUs")
            },
            hide_index=True,
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_t2:
        top_sku = top_5.iloc[0]['Display_Name']
        top_sku_margin = top_5.iloc[0]['Margin_%']
        st.markdown(f"""
<div class="apple-panel">
    <h3 class="panel-title">Action Summary for Retailer</h3>
    <div class="panel-caption">Key operational recommendations for your store</div>
    <div style="height: 14px;"></div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="background: #F5F5F7; border-radius: 10px; padding: 12px 16px;">
            <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #86868B;">Immediate Reorder Budget</div>
            <div style="font-size: 14px; font-weight: 600; margin-top: 2px; color: #1D1D1F;">Prepare ₹ {total_po_cost:,.0f} for the upcoming delivery cycle ({total_po_units} units).</div>
        </div>
        <div style="background: #F5F5F7; border-radius: 10px; padding: 12px 16px;">
            <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #86868B;">Top Profit Driver</div>
            <div style="font-size: 14px; font-weight: 600; margin-top: 2px; color: #1D1D1F;">{top_sku} leads store profitability with a {top_sku_margin:.1f}% gross margin.</div>
        </div>
        <div style="background: #F5F5F7; border-radius: 10px; padding: 12px 16px;">
            <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #86868B;">Inventory Health</div>
            <div style="font-size: 14px; font-weight: 600; margin-top: 2px; color: #1D1D1F;">{cg_count} Cash Generators active and {up_count} Underperformers identified for review.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
