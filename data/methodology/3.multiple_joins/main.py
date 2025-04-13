import pandas as pd

def evaluate_candidate_multiple_joins(original, updated, candidate, join_left='id', join_right='client_id', new_column='city'):
    """
    Evaluates a candidate table using different join types and selects the join that best explains
    the new column.
    
    Parameters:
        original (DataFrame): The base table without the new column.
        updated (DataFrame): The table containing the new column.
        candidate (DataFrame): The candidate table that might explain the new column.
        join_left (str): The column name in original to join on.
        join_right (str): The column name in candidate to join on.
        new_column (str): The new column to verify.
        
    Returns:
        best_join_type (str): The join type that produces the best match.
        best_score (float): The matching score (from 0 to 1) for the best join type.
        best_merged (DataFrame): The merged DataFrame using the best join type.
    """
    join_types = ["inner", "left", "outer"]
    best_join_type = None
    best_score = -1
    best_merged = None
    
    # Iterate through the different join types
    for join_type in join_types:
        try:
            # Perform the join
            merged = original.merge(candidate, left_on=join_left, right_on=join_right, how=join_type)
            # Remove redundant join column if exists
            merged = merged.drop(columns=[join_right], errors='ignore')
            
            # To compare effectively, sort and reset index
            merged = merged.sort_values(by=join_left).reset_index(drop=True)
            updated_sorted = updated.sort_values(by=join_left).reset_index(drop=True)

            # Fill missing values in the new column to avoid comparison issues
            merged[new_column] = merged[new_column].fillna('')
            updated_sorted[new_column] = updated_sorted[new_column].fillna('')
            
            # Calculate matching score for the new column
            matching = (merged[new_column] == updated_sorted[new_column]).sum()
            total = len(updated_sorted)
            score = matching / total
            
            print(f"Join type '{join_type}': matching score = {score:.2f}")
            
            # Update best join if current score is better
            if score > best_score:
                best_score = score
                best_join_type = join_type
                best_merged = merged
        except Exception as e:
            print(f"Join type '{join_type}' failed with error: {e}")
    
    return best_join_type, best_score, best_merged

def main():
    # Load the main tables
    original = pd.read_csv("data/3.multiple_joins/original.csv")
    updated = pd.read_csv("data/3.multiple_joins/added_column.csv")
    
    # List of candidate table files
    candidate_files = [
        "data/3.multiple_joins/candidate_table_1.csv",
        "data/3.multiple_joins/candidate_table_2.csv",
        "data/3.multiple_joins/candidate_table_3.csv"
    ]
    
    best_candidate_overall = None
    overall_best_score = -1
    overall_best_details = {}
    
    # Iterate through candidate table files
    for file in candidate_files:
        candidate = pd.read_csv(file)
        join_type, score, merged = evaluate_candidate_multiple_joins(original, updated, candidate)
        print(f"\nBest join for candidate '{file}': '{join_type}' with score {score:.2f}")
        
        # Check if this candidate has the best matching overall
        if score > overall_best_score:
            overall_best_score = score
            best_candidate_overall = file
            overall_best_details = {
                "join_type": join_type,
                "merged": merged
            }
    
    print("\n✅ Overall best candidate table:", best_candidate_overall)
    print("✅ Best join type used:", overall_best_details.get("join_type"))
    print("✅ Merged result using best join:")
    print(overall_best_details.get("merged"))
    
if __name__ == "__main__":
    main()
