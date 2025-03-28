# Concurrency Simulation

This Python project demonstrates **concurrency and data streaming techniques** using:

- `multiprocessing`: Parallel execution using multiple processes.
- `threading`: Lightweight concurrent execution using threads.
- `generators`: Lazy evaluation of data streams.
- `pipelines`: Composable data processing flows.

The simulation uses **random jiu-jitsu attack names** to illustrate real-time, concurrent data generation and processing.

---

## 🚀 How to Run

> Requires **Python +3.6+**. No external libraries needed.

### 1. Clone the repo
```bash
git clone https://github.com/your-username/jiujitsu-concurrency-simulation.git
cd jiujitsu-concurrency-simulation
```

### 2. Run scripts
```bash
python3 multiprocessing_demo.py
python3 threading_demo.py
python3 generator_stream.py
python3 generator_pipeline.py
```

---

## 🧠 Concepts Demonstrated

| Concept         | Script                   | Description                                         |
|----------------|--------------------------|-----------------------------------------------------|
| Processes       | `multiprocessing_demo.py` | Demonstrates parallel execution with lock sharing. |
| Threads         | `threading_demo.py`       | Runs multiple threads with synchronized access.     |
| Lazy Generators | `generator_stream.py`     | Simulates delayed streaming of attacks.             |
| Pipelines       | `generator_pipeline.py`   | Composes generators into a processing chain.        |

---

