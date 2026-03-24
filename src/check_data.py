import pandas as pd

datasets = ['heart.csv', 'credit_card.csv', 'insurance.csv']

for dataset in datasets:
    df = pd.read_csv(f'datasets/{dataset}')
    print(f"\n{dataset}:")
    print(f"  Rows: {len(df)}")
    print(f"  Columns: {len(df.columns)}")
    print(f"  Missing values: {df.isnull().sum().sum()}")

# German credit (special case)
german = pd.read_csv('datasets/german_credit.csv', sep='\s+', header=None)
print("\ngerman_credit.csv:")
print("  Rows:", len(german))
print("  Columns:", len(german.columns))
print("  Missing values:", german.isnull().sum().sum())
