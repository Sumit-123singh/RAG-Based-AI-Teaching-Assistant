import joblib

df = joblib.load("embedding.joblib")
print(" Loaded DataFrame:")
print(df.head())
