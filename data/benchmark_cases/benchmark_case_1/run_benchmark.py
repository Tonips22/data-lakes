import os
import pandas as pd
from main import evaluate_candidate_multiple_joins

def run_benchmark_case(case_folder):
    print(f"\n🚀 Running benchmark in: {case_folder}")
    
    # Load original and updated datasets
    original = pd.read_csv(os.path.join(case_folder, "original.csv"))
    updated = pd.read_csv(os.path.join(case_folder, "updated.csv"))

    # Detect candidate files automatically
    candidate_files = [f for f in os.listdir(case_folder) if f.startswith("candidate")]
    
    best_score = -1
    best_result = {}
    
    for filename in candidate_files:
        path = os.path.join(case_folder, filename)
        candidate = pd.read_csv(path)
        join_type, score, merged = evaluate_candidate_multiple_joins(original, updated, candidate)
        print(f"📄 {filename} → Join: {join_type}, Score: {score:.2f}")
        
        if score > best_score:
            best_score = score
            best_result = {
                "file": filename,
                "score": score,
                "join_type": join_type,
                "merged": merged
            }

    print(f"\n🏁 Best match: {best_result['file']}")
    print(f"🔗 Join type: {best_result['join_type']} with score {best_result['score']:.2f}")
    print(best_result["merged"])

# Run for case 1
if __name__ == "__main__":
    run_benchmark_case("data/benchmark_cases/benchmark_case_1")
