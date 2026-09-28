import pandas as pd

df = pd.read_parquet("/Users/kavivignesh/ML/test-00000-of-00001.parquet")
df.to_csv("airline_passenger_satisfaction_test.csv", index=False)

df1 = pd.read_parquet("/Users/kavivignesh/ML/train-00000-of-00001.parquet")
df1.to_csv("airline_passenger_satisfaction_train.csv", index=False)
print(df.shape)
print("CSV created successfully")