# 🛒 Sales Performance Analytics

_Develop a centralized sales analytics solution to evaluate revenue performance, customer behaviour, and operational performance, supporting data-driven commercial and operational decision-making.._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation<a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-question--key-finding">Research Question & Key Finding</a>
- <a href="#dashboard">Dashboard</a>
- <a href="how-to-run-this-project">How to Run This Project</a>
- <a href="final-recommendations">Final Recommendations</a>
- <a href="author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluate revenue key drivers to drive strategic insights for the upcomming business year, A compliete data pipeline was built using padnas(ETL) due less amount of the transactionla dataset.Python for the EDA & Power Bi for the visualization.

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

The Tata Data Visualization job simulation requires analyzing retail transaction data to answer strategic business questions for the CEO and CMO. The objective is to identify the key drivers of revenue to support data-driven decisions for the upcoming business year.

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- The singel source of file(CSVs) located in `/data/` floder.
- clean, analytical table created for the EDA & visualization for the Power Bi.
  
---
<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>


- Python(Pandas, Matplotlib, Seaborn)
- Power Bi(Interactive Dashboard)
- Github

---
<h2><a class="anchor" id="project-structure"></a>Project Structue</h2>

```
sales_performance_analysis/
├── config/
│   ├── __init__.py
│   ├── paths.py
│   └── settings.py
│
├── dashboard/
│   └── sales_performance(tcs).pbix
│
├── data/
│   ├── analytics/
│   ├── clean/
│   ├── raw/
│   └── semantic_model/
│
├── image/
│
├── logs/
│   └── pipeline.log
│
├── notebooks/
│   ├── 01_data_quality_assesment_&_preparation.ipynb
│   ├── 02_Analytics_Sales_Development.ipynb
│   ├── 03_sale_performance_analysis.ipynb
│   └── 04_Semantic_Model_Preparation.ipynb
│
├── Outcomes/
│   ├── Retail Sales Performance Analytics report.pptx
│   └── Retail_Sales_Analytics_slide.desk.pdf
│
├── src/
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── build_analytics_sales.py
│   │
│   ├── clean/
│   │   ├── __init__.py
│   │   └── build_clean_sales.py
│   │
│   ├── semantic_model/
│   │   ├── __init__.py
│   │   ├── build_dim_customer.py
│   │   ├── build_dim_date.py
│   │   └── build_semantic_model.py
│   │
│   └── main.py
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── logger.py
│   └── validation.py
│
├── README.md
└── requirements.txt
```

---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaining & Preparation</h2>

A comprehensive assessment was performed on the raw dataset before any transformations were applied. The assessment included:

- Dataset structure validation
- Schema verification
- Data type validation
  - Invoice Date Stored as Text, Convert to datetime.
  - Invoice Date Stored as Text, Convert to datetime.
- Missing Values
  - Missing Product Descriptions	1,454 records have missing descriptions. Remove from the analytical dataset.
  - Missing CustomerID	135,080 transactions have missing CustomerIDs. Retain for revenue analysis; exclude from customer-level analysis.
- Duplicate Records
  - Duplicate Records	5,268 duplicate records. Remove duplicate records.
- Negative & zeero Values
  - Negative Quantity	474 non-cancellation records were identified as internal inventory and administrative adjustments with zero unit price and no revenue impact.	Remove operational adjustment records; retain legitimate customer returns.
  - Negative Unit Price	Only 2 records contained negative unit prices. Manual inspection confirmed they were bad debt accounting adjustments, not retail sales.	Remove from the analytical dataset.
  - Zero Unit Price	582 zero-price transactions were identified. Only operational records (e.g., check, found, adjustment, Manual, amazon) were excluded, while genuine product transactions were retained.	Remove operational records; retain legitimate zero-price customer transactions.
- Created analytics table & Features Engineering with grian: One row represents one product sold within a single invoice (Invoice Line Grain).
- Business rule investigation
  
---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis(EDA)</h2>

- Negative Values

  - Negative Quantity: Represents product returns and cancellation transactions. Internal inventory adjustments were identified and removed during data cleaning.
  - Revenue: Revenue reversal caused by a return/cancellation
  

- Outliers
  - Distribution plots and boxplots confirm substantial extreme values across Quantity, UnitPrice, and Revenue. These values significantly influence mean-based statistics, making median and quartile measures more representative of typical transaction behavior.

- Correlation
  - Revenue is strongly volume-driven — Total Revenue correlates strongly with Total Quantity (0.93).
  - Repeat purchasing matters — Total Revenue has a strong relationship with Total Orders (0.80).
  - Unit price has minimal impact — Average Unit Price shows almost no relationship with Total Revenue (0.03).
  

---
<h2><a class="anchor" id="research-question--key-finding"></a>Research Question & Key Finding</h2>

  -  **Revenue Growth:** November 2011 generated £1.46M, representing the peak monthly revenue during the analysis period.
.
  - **Market Concentration:** The United Kingdom contributed approximately 84% of total revenue (£8.19M), making it the dominant market.
  - **Customer Segmentation:** Registered Customers generated £8.28M (84.9%) of total revenue, significantly outperforming Guest Customers.
  - **Customer Engagement:** Approximately 65% of identifiable customers were repeat customers, highlighting strong repeat purchasing behavior.
  - **Product Performance:** The top 10 products contributed approximately 9.9% of total revenue, indicating that revenue is distributed across a broad product portfolio.
  - **Cancellation Impact:** Cancellations resulted in approximately £894K in cancelled revenue, with a 16.08% cancellation order rate.
  
---
<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

- Power BI Dashboard includes:
  - **Executive Overview** — Revenue trends, market performance, top products, and cancellation impact
  - **Customer & Marketing Insights** — Customer segmentation, engagement, repeat purchasing, product reach, and country engagement
  - **Interactive Drill-Through Analysis** — Detailed country and product-level performance analysis

### Executive Overview

![Executive Overview Dashboard](image/executive_overview.png)

### Customer & Marketing Insights

![Customer & Marketing Dashboard](image/customer_and_marketing.png)

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

---

1. Clone the repository

```bash
git clone https://github.com/yourusername/sale_performance_analysis.git
cd sale_performance_analysis

2. Create and activate a virtual environment

python -m venv .venv

Windows:

.venv\Scripts\activate

3. Install the required dependencies

pip install -r requirements.txt

4. Run the complete data pipeline

The project uses a local file-based pipeline. No database is required.

Run:

python -m src.main
```

5. Open and run notebooks:
   - `notebooks/01_data_quality_assessment_&_preparation.ipynb`
   - `notebooks/02_Analytics_Sales_Development.ipynb`
   - `notebooks/03_sale_performance_analysis.ipynb`
   - `notebooks/04_Semantic_Model_Preparation.ipynb`
  
6. Open Power BI Dashboard:
   - `dashboard/sales_performance(tcs).pbix`

---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Diversify revenue by selectively expanding in established high-performing European markets.
- Prepare inventory, fulfilment, and operations ahead of peak seasonal demand periods.
- Strengthen customer retention through personalized marketing and repeat-purchase initiatives.
- Increase guest customer registration to support long-term engagement and customer value.
- Optimize product and inventory planning using both revenue and sales-volume performance.
- Investigate and reduce order cancellations to minimize revenue leakage.
- Increase customer value through cross-selling and targeted product recommendations.

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Kartik Bhaskar**  
Data Analyst  
📧 Email: kartikbhaskarx.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kartikbhaskar/)  
