import pandas as pd

def evaluate_candidate(original, updated, candidate, join_left='id', join_right='client_id', new_column='city'):
    """
    Evaluates a candidate table by joining it with the original table and
    comparing the result with the updated table that includes the new column.

    Parameters:
        original (DataFrame): The base table without the new column.
        updated (DataFrame): The table containing the new column.
        candidate (DataFrame): The candidate table that might explain the new column.
        join_left (str): The column name in original to join on.
        join_right (str): The column name in candidate to join on.
        new_column (str): The new column to verify.

    Returns:
        score (float): The ratio of rows where the new column data matches.
    """
    # Perform the join with candidate table
    merged = original.merge(candidate, left_on=join_left, right_on=join_right, how="inner")
    # Drop the redundant join column
    merged = merged.drop(columns=[join_right])
    
    # Compare the merged result with the updated table for the new column.
    # One simple approach: count how many rows match the new column exactly.
    # Ensure both dataframes are aligned by 'id'
    merged = merged.sort_values(by=join_left).reset_index(drop=True)
    updated_sorted = updated.sort_values(by=join_left).reset_index(drop=True)
    
    # Calculate the number of matching rows in the new column
    matching = (merged[new_column] == updated_sorted[new_column]).sum()
    total = len(updated_sorted)
    
    # Return a matching score (0 to 1)
    score = matching / total
    return score, merged

def main():
    # Load the main tables
    original = pd.read_csv("data/2.compare_example/original.csv")
    updated = pd.read_csv("data/2.compare_example/added_column.csv")
    
    # List of candidate table filenames
    candidate_files = [
        "data/2.compare_example/candidate_table_1.csv",
        "data/2.compare_example/candidate_table_2.csv",
        "data/2.compare_example/candidate_table_3.csv"
    ]
    
    best_score = -1
    best_candidate = None
    best_merged = None
    
    # Iterate over candidate files and evaluate each
    for file in candidate_files:
        candidate = pd.read_csv(file)
        score, merged = evaluate_candidate(original, updated, candidate)
        print(f"\nEvaluation for {file}:")
        print(f"Matching score: {score:.2f}")
        if score > best_score:
            best_score = score
            best_candidate = file
            best_merged = merged
    
    print("\n✅ Best candidate table:", best_candidate)
    print("✅ Best merged result:")
    print(best_merged)
    
if __name__ == "__main__":
    main()
