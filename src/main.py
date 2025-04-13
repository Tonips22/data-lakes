import pandas as pd

# Load the CSV files
original = pd.read_csv("data/1.basic_example/original.csv")
updated = pd.read_csv("data/1.basic_example/added_column.csv")
candidate = pd.read_csv("data/1.basic_example/candidate_table.csv")

print("\n📄 Original table:")
print(original)

print("\n🆕 Updated table with new column:")
print(updated)

print("\n🔍 Candidate table (potential source of the new column):")
print(candidate)

# Attempt to join original with candidate table
merged = original.merge(candidate, left_on="id", right_on="id_client", how="inner")

# Drop redundant column
merged = merged.drop(columns=["id_client"])

print("\n✅ Result after join:")
print(merged)

# Check if the join successfully explains the new column
matches = merged.equals(updated)
print("\n🎯 Does the join correctly explain the new column?:", "Yes" if matches else "No")
