## 02_preprocessing
# Preprocessing steps for GSE77314 dataset

import pandas as pd
import numpy as np
import os

data_path = "data/raw/gse77314/GSE77314_differential_genes.xlsx"
df = pd.read_excel(data_path)
df.head()

df = df.drop_duplicates()

for col in df.select_dtypes(include=['datetime64[ns]']).columns:
    df[col] = df[col].astype(str)

df.info()

processed_path = "data/processed"
os.makedirs(processed_path, exist_ok=True)

out_file = os.path.join(processed_path, "preprocessed_genes.csv")
df.to_csv(out_file, index=False)
out_file
