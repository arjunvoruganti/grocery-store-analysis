import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(page_title="Retail Inventory & Margin Dashboard", layout="wide")

st.title("📊 Retail Analytics & Pricing Optimization Dashboard")
st.write("Product margin analysis and inventory planning based on your store catalog.")

# 1. Load and Map Data from Excel
@st.cache_data
def load_data():
    df = pd.read_excel("sales_data.xlsx")
    
    # Map exact column names from your Excel sheet
    df = df.rename(columns={
        "Product Name": "Item",
        "SupplyPrice": "Cost_Price",
        "RetailPrice": "Sale_Price"
    })
    
    # Clean price columns (remove currency symbols like ₹ or commas if stored as text)
    for col in ["Cost_Price", "Sale_Price"]:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace('₹', '', regex=True).str.replace(',', '', regex=True).str.strip().astype(float)
    
    # Auto-assign categories based on item names for filtering
    def assign_category(name):
        name_lower = str(name).lower()
        if any(w in name_lower for w in ['water', 'drink', 'milk', 'buttermilk', 'juice', 'coffee']):
            return 'Beverages'
        elif any(w in name_lower for w in ['paneer', 'butter']):
            return 'Dairy'
        elif any(w in name_lower for w in ['atta', 'rice', 'moong', 'sugar']):
            return 'Grains & Staples'
        elif any(w in name_lower for w in ['garbage', 'tissue', 'tabs', 'detergent']):
            return 'Household & Cleaning'
        elif any(w in name_lower for w in ['chocolate', 'cookie', 'ice cream', 'dates', 'bites', 'walnut']):
            return 'Snacks & Sweets'
        else:
            return 'General'

    df['Category'] = df['Item'].apply(assign_category)
    
    # Simulate estimated monthly units sold for catalog analytics
    np.random.seed(42)
    df['Estimated_Monthly_Qty'] = np.random.randint(25, 150, size=len(df))
    
    # Calculate financial metrics
    df['Revenue'] = df['Estimated_Monthly_Qty'] * df['Sale_Price']
    df['Cost'] = df['Estimated_Monthly_Qty'] * df['Cost_Price']
    df['Profit'] = df['Revenue'] - df['Cost']
    df['Margin_%'] = ((df['Sale_Price'] - df['Cost_Price']) / df['Sale_Price']) * 100
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading sales_data.xlsx: {e}")
    st.stop()

# 2. Sidebar Settings & Filters
st.sidebar.header("Dashboard Filters")
selected_category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

lead_time = st.sidebar.number_input("Supplier Lead Time (Days):", min_value=1, value=7)

# Filter Dataframe
filtered_df = df[df["Category"].isin(selected_category)] if selected_category else df

# 3. Top KPI Summary Cards
total_revenue = filtered_df["Revenue"].sum()
total_profit = filtered_df["Profit"].sum()
overall_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Estimated Monthly Revenue", f"₹ {total_revenue:,.2f}")
col2.metric("Estimated Monthly Profit", f"₹ {total_profit:,.2f}")
col3.metric("Avg Profit Margin", f"{overall_margin:.1f}%")

st.markdown("---")

# 4. Data Visualizations
st.subheader("📈 Product & Profitability Visualizations")
tab1, tab2 = st.tabs(["Top Products by Margin (%)", "Supply Price vs. Retail Price"])

with tab1:
    margin_sorted = filtered_df.sort_values(by="Margin_%", ascending=False)
    fig_bar = px.bar(margin_sorted.head(15), x="Margin_%", y="Item", orientation="h", 
                     title="Top 15 Products by Profit Margin (%)", color="Margin_%")
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    fig_scatter = px.scatter(filtered_df, x="Cost_Price", y="Sale_Price", text="Item", color="Category",
                             title="Supply Price vs. Retail Price across Categories")
    st.plotly_chart(fig_scatter, use_container_width=True)

# 5. Inventory Reorder & Stock Planning
st.markdown("---")
st.subheader("📦 Inventory Reorder Point Planner")
st.write(f"Calculated recommended safety stock thresholds based on a **{lead_time}-day lead time**:")

reorder_df = filtered_df[['Item', 'Category', 'Estimated_Monthly_Qty', 'Sale_Price', 'Cost_Price', 'Margin_%']].copy()
reorder_df["Daily_Sales_Rate"] = (reorder_df["Estimated_Monthly_Qty"] / 30).round(2)
reorder_df["Reorder_Point_Units"] = (reorder_df["Daily_Sales_Rate"] * lead_time).round(1)

st.dataframe(reorder_df[["Item", "Category", "Estimated_Monthly_Qty", "Daily_Sales_Rate", "Reorder_Point_Units", "Margin_%"]], use_container_width=True)
