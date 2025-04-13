# External Version Explanation / Rome Assignment 2025

This project extends the work of [Shraga and Miller, 2023] by proposing a system to explain **external attribute additions** in dataset versions within a Data Lake.  
The system searches across candidate tables and applies different join strategies to find the best explanation for a newly added column.

---

## Project Structure

- `data/`: Contains the datasets used in the project.
    - `data/methodology/`: Contains every step of the methodology. (datasets and main scripts)
    - `data/benchmark_cases/`: Contains the benchmark cases used in the project.
- `src/`:: Contains the source code of the project.
    - `main.py`: Main script of the methodology cases.
    - `run_benchmark.py`: Main script of the benchmark cases.
- `requirements.txt`: Dependencias del proyecto.

## How to run the project

1. Clone the repository
    ```bash
    git clone https://github.com/Tonips22/data-lakes.git
    cd data-lakes
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run a benchmark case:

    modify the `run_benchmark.py` script to select the benchmark case you want to run.
    ```python
    run_benchmark_case("data/benchmark_cases/benchmark_case_1")  # Or case_2, case_3, etc.
    ```

    Then run the script:
    ```bash
    python src/run_benchmark.py
    ```

## Benchmark Cases Included

| Case | Description           | Expected Behavior         |
|------|-----------------------|---------------------------|
| 1    | Perfect match         | Score = 1.0               |
| 2    | Partial match         | Score between 0.0 and 1.0 |
| 3    | Incorrect candidates  | Score = 0.0               |
| 4    | No joinable keys      | Score = 0.0               |


## Author

#### 🦸‍♀️ Antonio Garcia Torres

- [LinkedIn](https://www.linkedin.com/in/antonio-garc%C3%ADa-torres-a635992b6/)
- [tonigt.dev](https://tonigt.dev/)


