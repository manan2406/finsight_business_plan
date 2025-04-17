"""
FinSight - Smart Financial Analysis Platform Prototype

This is a Streamlit-based UI/UX prototype for FinSight, designed for founders, CFOs, 
investors, and consultants. The prototype focuses on document upload, financial ratio 
analysis display, and a clean, intuitive interface.

To run this prototype:
1. Install dependencies: pip install streamlit pandas numpy matplotlib pillow
2. Run the app: streamlit run app.py

Note: This is a visual prototype only. No actual file processing or analysis is performed.
All data shown is mock data for demonstration purposes.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="FinSight - Financial Analysis Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    :root {
        --primary: #1a3a5f;
        --secondary: #f0f2f6;
        --accent: #4CAF50;
        --warning: #f44336;
        --text: #333333;
    }
    .main-header {
        color: var(--primary);
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .sub-header {
        color: var(--primary);
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .ratio-card {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }
    .ratio-healthy {
        background-color: rgba(76, 175, 80, 0.1);
        border-left: 4px solid #4CAF50;
    }
    .ratio-warning {
        background-color: rgba(255, 152, 0, 0.1);
        border-left: 4px solid #FF9800;
    }
    .ratio-danger {
        background-color: rgba(244, 67, 54, 0.1);
        border-left: 4px solid #f44336;
    }
    .ratio-value {
        font-size: 1.5rem;
        font-weight: 700;
    }
    .ratio-title {
        font-weight: 600;
        color: var(--primary);
    }
    .ratio-description {
        font-size: 0.9rem;
        color: #666;
    }
    .upload-btn {
        background-color: var(--primary);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 5px;
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
    }
    .feature-box {
        background-color: var(--secondary);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .logo-placeholder {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary);
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        font-size: 0.8rem;
        color: #666;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Create a placeholder logo
def create_logo():
    fig, ax = plt.subplots(figsize=(2, 0.8))
    ax.text(0.5, 0.5, 'FinSight', fontsize=20, ha='center', va='center', color='#1a3a5f', fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    buf.seek(0)
    plt.close(fig)  # Close figure to free memory
    return Image.open(buf)

# Sidebar navigation
with st.sidebar:
    st.image(create_logo(), width=150)
    st.markdown("---")
    # Navigation
    page = st.radio("Navigation", ["Home", "Analysis", "Help"], key="nav")
    st.session_state.page = page  # Sync radio selection with session state
    st.markdown("---")
    st.markdown("### About FinSight")
    st.markdown("FinSight helps you analyze financial statements, extract key ratios, and visualize insights quickly and accurately.")
    st.markdown("---")
    st.markdown("© 2025 FinSight")  # Updated year to match current date

# Mock data for financial ratios
def get_mock_ratios():
    return {
        "Liquidity Ratios": {
            "Current Ratio": {"value": 1.8, "status": "healthy", "description": "Measures the company's ability to pay short-term obligations."},
            "Quick Ratio": {"value": 1.2, "status": "healthy", "description": "A more stringent measure of liquidity, excluding inventory."},
            "Cash Ratio": {"value": 0.5, "status": "warning", "description": "Measures a company's ability to cover short-term liabilities with cash."}
        },
        "Profitability Ratios": {
            "Gross Margin": {"value": 35.0, "status": "healthy", "description": "Percentage of revenue retained after direct costs."},
            "Net Profit Margin": {"value": 8.5, "status": "healthy", "description": "Percentage of revenue that is net income."},
            "Return on Equity (ROE)": {"value": 15.2, "status": "healthy", "description": "Measures profitability relative to shareholders' equity."}
        }
    }

# Mock bar chart
def create_mock_bar_chart():
    fig, ax = plt.subplots(figsize=(8, 4))
    categories = ['Current Ratio', 'Quick Ratio', 'Cash Ratio']
    values = [1.8, 1.2, 0.5]
    colors = ['#4CAF50', '#4CAF50', '#FF9800']
    ax.bar(categories, values, color=colors)
    ax.set_ylabel('Ratio Value')
    ax.set_title('Key Financial Ratios')
    ax.axhline(y=1.0, color='#f44336', linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    return fig

# Home Page
def home_page():
    st.markdown('<h1 class="main-header">Simplify Financial Analysis with FinSight</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h2>Welcome to FinSight</h2>
        <p>FinSight helps founders, CFOs, investors, and consultants analyze financial statements, 
        extract key ratios, and visualize insights quickly and accurately.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">How It Works</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📄</div>
            <h3>Upload Files</h3>
            <p>Upload balance sheets and income statements in PDF, Excel, or CSV format.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <h3>Get Ratios</h3>
            <p>FinSight automatically calculates key financial ratios and metrics.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📈</div>
            <h3>Visualize Insights</h3>
            <p>View insights through intuitive charts and customizable reports.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Upload Your Financial Documents</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload balance sheets or income statements", 
                                    type=["pdf", "xlsx", "csv"],
                                    help="Supported formats: PDF, Excel, CSV")
    
    if uploaded_file is not None:
        st.success(f"File Uploaded: {uploaded_file.name}")
        with st.spinner("Analyzing your financial document..."):
            time.sleep(2)
        st.info("Analysis complete! Navigate to the Analysis page to view results.")
        if st.button("View Analysis"):
            st.session_state.page = "Analysis"
            st.rerun()  # Updated from st.experimental_rerun()
    else:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background-color: #f8f9fa; border-radius: 10px; border: 1px dashed #ccc;">
            <p>Drag and drop your files here or click to browse</p>
            <p style="font-size: 0.8rem; color: #666;">Supported formats: PDF, Excel, CSV</p>
        </div>
        """, unsafe_allow_html=True)

# Analysis Page
def analysis_page():
    st.markdown('<h1 class="main-header">Financial Analysis</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Select Context Mode</h2>', unsafe_allow_html=True)
    context_mode = st.selectbox(
        "Choose a context mode for your analysis:",
        ["Investor", "Board", "Audit"],
        help="Different modes emphasize different aspects of the analysis"
    )
    
    context_descriptions = {
        "Investor": "Investor Mode: Emphasizes growth metrics and visualizations suitable for pitches.",
        "Board": "Board Mode: Focuses on comprehensive performance indicators for board meetings.",
        "Audit": "Audit Mode: Highlights compliance metrics and financial health indicators."
    }
    st.info(context_descriptions[context_mode])
    
    st.markdown('<h2 class="sub-header">Key Financial Ratios</h2>', unsafe_allow_html=True)
    ratios = get_mock_ratios()
    
    for category, category_ratios in ratios.items():
        st.markdown(f"<h3>{category}</h3>", unsafe_allow_html=True)
        cols = st.columns(min(len(category_ratios), 3))  # Limit to 3 columns for layout
        for i, (ratio_name, ratio_data) in enumerate(category_ratios.items()):
            with cols[i % len(cols)]:
                status_class = f"ratio-{ratio_data['status']}"
                st.markdown(f"""
                <div class="ratio-card {status_class}">
                    <div class="ratio-title">{ratio_name}</div>
                    <div class="ratio-value">{ratio_data['value']}</div>
                    <div class="ratio-description">{ratio_data['description']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Visualizations</h2>', unsafe_allow_html=True)
    st.pyplot(create_mock_bar_chart())
    
    st.markdown('<h2 class="sub-header">AI-Generated Insights</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Financial Health Summary</h3>
        <p>Your company shows strong liquidity with a Current Ratio of 1.8. The Gross Margin of 35% is above average.</p>
        <p>Monitor the Cash Ratio (0.5), which indicates limited cash reserves.</p>
    </div>
    """, unsafe_allow_html=True)

# Help Page
def help_page():
    st.markdown('<h1 class="main-header">Help & Support</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Frequently Asked Questions</h2>', unsafe_allow_html=True)
    with st.expander("How do I upload files?"):
        st.markdown("""
        1. Navigate to the Home page.
        2. Click the "Upload Your Financial Documents" section.
        3. Drag and drop or browse for files (PDF, Excel, CSV).
        """)
    with st.expander("What financial ratios are calculated?"):
        st.markdown("""
        - **Liquidity**: Current Ratio, Quick Ratio, Cash Ratio
        - **Profitability**: Gross Margin, Net Profit Margin, ROE
        """)
    
    st.markdown('<h2 class="sub-header">Contact Us</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Need help?</h3>
        <p>Email: support@finsight.com</p>
        <p>Phone: (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)

# Main app logic
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Analysis":
    analysis_page()
elif st.session_state.page == "Help":
    help_page()

# Footer
st.markdown("""
<div class="footer">
    FinSight Prototype - Version 0.1 - © 2025 FinSight
</div>
""", unsafe_allow_html=True)