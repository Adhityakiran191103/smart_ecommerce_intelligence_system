# Smart E-commerce Intelligence System

An end-to-end retail analytics project built progressively while learning Python, Pandas, data analysis, customer analytics, machine learning concepts, and business storytelling.

The goal is to transform raw e-commerce transaction data into meaningful business insights that support better decision-making.

---

## Project Goal

Build a complete E-commerce Intelligence System capable of:

- Data cleaning and validation
- Exploratory sales analysis
- Product performance analysis
- Customer behaviour analysis
- RFM (Recency, Frequency, Monetary) analysis
- Customer segmentation
- Sales and revenue trends
- Data visualization and dashboards
- Business insights and recommendations

**Learning approach:** This repository contains the project structure and roadmap through Day 27. Each module is implemented progressively as the corresponding concepts are learned.

---

## Current Progress

**Current milestone: Day 18 / 27**

- [x] Days 1–17: Learning activities and foundational implementation.
- [ ] Day 17: Integrate and validate RFM scoring and segmentation.
- [x] Day 18: Customer Intelligence concepts and knowledge assessment.
- [ ] Day 18: Complete practical customer analysis implementation.
- [ ] Days 19–27: Continue analytics, visualization, dashboard development, and final documentation.

### Day 18 – Customer Intelligence & Behaviour Analysis

**Status:** In Progress

**Topics Covered:**
- Customer Behaviour Analysis
- Purchase Frequency Analysis
- Total Customer Spending
- Average Order Value (AOV)
- High-Value Customer Identification
- Customer Retention Strategies

**Tools & Technologies:**
- Python
- Pandas
- groupby()
- sum()
- count()
- mean()

**Practical Learning Objectives:**
- Analyse customer-level transactions.
- Calculate total spending per customer.
- Identify repeat and one-time customers.
- Calculate average order value.
- Identify high-value customers.
- Generate actionable customer insights.

**Knowledge Assessment:**
- Completed a 5-question Customer Intelligence quiz.
- Score: 4/5 (80%).

**Business Application:**

Understand customer purchasing behaviour to improve customer retention, loyalty programmes, and targeted marketing strategies.

---

## Dataset

This project uses the **Online Retail** transaction dataset.

Expected local dataset location:

`data/raw/Online Retail.xlsx`

Typical dataset columns:

| Column | Description |
|---|---|
| InvoiceNo | Transaction invoice number |
| StockCode | Product identification code |
| Description | Product description |
| Quantity | Number of items purchased |
| InvoiceDate | Transaction date |
| UnitPrice | Price per item |
| CustomerID | Customer identification |
| Country | Customer's country |

The scripts will validate actual column names rather than silently assuming the dataset structure.

**Important:** Keep the original dataset locally. Do not upload it to GitHub unless its redistribution licence permits it.

---

## Repository Structure

```text
smart-ecommerce-intelligence-system/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .env.example
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   └── README.md
│
├── src/
│   └── ecommerce_intelligence/
│       ├── __init__.py
│       ├── config.py
│       ├── data_loader.py
│       ├── data_cleaning.py
│       ├── sales_analysis.py
│       ├── product_analysis.py
│       ├── customer_analysis.py
│       ├── rfm_analysis.py
│       ├── segmentation.py
│       └── visualizations.py
│
├── scripts/
│   ├── run_pipeline.py
│   └── README.md
│
├── reports/
│   ├── figures/
│   └── README.md
│
├── tests/
│   ├── README.md
│   └── test_smoke.py
│
└── docs/
    ├── PROJECT_ROADMAP.md
    └── DATA_DICTIONARY.md
```

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Development | VS Code, Jupyter Notebook |
| Version Control | Git, GitHub |
| Data Processing | Excel, CSV |
| Dashboard | Streamlit, Power BI |
| Analytics | EDA, RFM, Customer Segmentation |

Technologies will be introduced progressively throughout the project.

---

## Project Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Add the dataset

Place your dataset inside:

```text
data/raw/Online Retail.xlsx
```

The original dataset is intentionally excluded from Git using `.gitignore`.

### 4. Run tests

```bash
python -m pytest
```

### 5. Run the project pipeline

```bash
python scripts/run_pipeline.py
```

The pipeline entry point will be completed as the relevant project modules are developed.

---

## GitHub Workflow

Use the following commands from the project root whenever you complete a learning milestone.

Check modified files:

```bash
git status
```

Review changes:

```bash
git diff
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Day 18: Customer Intelligence and Behaviour Analysis"
```

Push changes:

```bash
git push origin main
```

Never commit passwords, API keys, private information, or the raw dataset.

---

## Project Roadmap

The project follows a structured 27-day learning and implementation plan.

| Phase | Days | Focus |
|---|---|---|
| Phase 1 | 1–7 | Python Fundamentals |
| Phase 2 | 8–14 | Pandas and Data Cleaning |
| Phase 3 | 15–17 | Retail Analytics and RFM Fundamentals |
| Phase 4 | 18–20 | Customer, Sales and Product Intelligence |
| Phase 5 | 21–23 | Advanced Analysis and Visualization |
| Phase 6 | 24–25 | Business Insights and Dashboard Development |
| Phase 7 | 26–27 | Testing, Documentation and Final Project |

For the detailed daily learning plan, see:

[`docs/PROJECT_ROADMAP.md`](docs/PROJECT_ROADMAP.md)

---

## Learning Objectives

By the end of this project, the objective is to demonstrate the ability to:

- Work with real-world retail datasets.
- Clean and preprocess transactional data.
- Perform exploratory data analysis.
- Analyse customer purchasing behaviour.
- Build RFM-based customer segments.
- Identify sales and product performance patterns.
- Create meaningful visualizations and dashboards.
- Translate analytical findings into business recommendations.
- Maintain a structured, documented GitHub project.

---

## Final Deliverable

A complete Smart E-commerce Intelligence System demonstrating practical data analysis skills, customer intelligence, business insights, and data visualization using a real-world retail dataset.

**Project Duration:** 27 Days

**Learning Commitment:** Progressive daily implementation

**Project Status:** In Progress 🚀

---

*Building practical data science skills through consistent learning, implementation, experimentation, and documentation.*
