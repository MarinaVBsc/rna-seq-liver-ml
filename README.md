## RNA-Seq Liver ML — Machine Learning for Liver Gene Expression

A Machine Learning project using bulk RNA-seq to distinguish healthy human liver samples from hepatocellular carcinoma (TCGA-LIHC).

# Objective

Build a complete ML pipeline to classify healthy vs tumor liver tissue using bulk RNA-Seq data from:

- Human Liver RNA-Seq (Kaggle) — 903 healthy samples

- TCGA-LIHC — hepatocellular carcinoma + adjacent normals

This project integrates:

- Bioinformatics

- Machine Learning

- Data visualization

- Biological interpretation

# Project Structure
``` bash
rna-seq-liver-ml/
├── data/                        # raw datasets (not uploaded)
├── notebooks/                   # step-by-step workflow
├── src/                         # reusable code (preprocessing, models, plots)
├── results/                     # figures, metrics, outputs
├── models/                      # trained models
├── README.md
└── requirements.txt
```


# Workflow
1. Download data

Kaggle dataset (healthy liver)

TCGA-LIHC dataset (tumor + normal)

2. Preprocessing

Gene filtering

Normalization (log2)

Standardization

Batch correction (optional)

3. EDA

Gene expression distributions

Correlation analysis

Differential expression overview

4. Dimensionality Reduction

PCA

UMAP

5. Machine Learning

Models tested:

Logistic Regression (baseline)

Random Forest

XGBoost

Neural Network (MLP)

Metrics:

ROC-AUC

Precision / Recall

Confusion matrix

# Interpretation

Feature importance

Top genes driving classification

Biological interpretation (GO/KEGG optional)

## Getting Started

Install dependencies:

pip install -r requirements.txt

Run the notebooks in order:

01_download_data.ipynb
02_preprocessing.ipynb
03_EDA.ipynb
04_dimensionality_reduction.ipynb
05_ml_models.ipynb
06_interpretation.ipynb
