# Smart E-commerce Intelligence System

An end-to-end retail analytics project built progressively while learning Python, Pandas, data analysis, customer analytics, and business storytelling.

## Project goal

Turn transactional e-commerce data into useful business insights, including:
- data cleaning and validation
- exploratory sales and product analysis
- customer-level analysis
- RFM (Recency, Frequency, Monetary) scoring
- customer segmentation
- visual dashboards and business recommendations

> **Learning approach:** The repository contains the complete project structure and roadmap through Day 27. Implement each module as you learn it. Do not copy future solutions before completing the relevant learning day.

## Current progress

- [x] Learning work through Day 17 is in progress/completed progressively.
- [ ] Integrate and validate the Day 17 RFM scoring and segmentation script.
- [ ] Complete Days 18–27 using the roadmap below.

Update this section as you progress.

## Dataset

This project is designed around the **Online Retail** transaction dataset.

Expected source file (keep it locally; do not commit it unless you have confirmed its redistribution licence):
`data/raw/Online Retail.xlsx`

Typical columns include:
`InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.

The scripts should validate the actual column names in your copy rather than silently assuming them.

## Repository structure

```text
smart-ecommerce-intelligence-system/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .env.example
├── data/
│   ├── raw/                 # Original dataset (not committed)
│   ├── processed/           # Cleaned/intermediate data (not committed)
│   └── README.md
├── notebooks/
│   └── README.md
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
├── scripts/
│   ├── run_pipeline.py
│   └── README.md
├── reports/
│   ├── figures/
│   └── README.md
├── tests/
│   ├── README.md
│   └── test_smoke.py
└── docs/
    ├── PROJECT_ROADMAP.md
    └── DATA_DICTIONARY.md
```

## Setup

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

Place your local dataset at:

```text
data/raw/Online Retail.xlsx
```

The original dataset is intentionally excluded from Git by `.gitignore`.

### 4. Run tests

```bash
python -m pytest
```

### 5. Run the pipeline

The pipeline entry point will be completed as the relevant topics are learned:

```bash
python scripts/run_pipeline.py
```

## GitHub workflow

Run these commands from the project root after reviewing the files:

```bash
git init
git add .
git status
git commit -m "Initial project structure and roadmap"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/smart-ecommerce-intelligence-system.git
git push -u origin main
```

Replace the remote URL with your own GitHub repository URL. If the repository already exists locally, do not run `git init` again; inspect `git status` first.

Before every commit:

```bash
git status
git diff
```

Never commit passwords, API keys, private data, or the raw dataset unless you have confirmed it is appropriate to publish.

## Project roadmap

See [`docs/PROJECT_ROADMAP.md`](docs/PROJECT_ROADMAP.md) for the Day 1–27 learning and implementation plan.
