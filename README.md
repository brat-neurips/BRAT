# BRAT: Boulevard Regularized Additive Regression Trees

This repository contains the code, experiments, and documentation for the paper [Statistical Inference for Gradient Boosting Regression](https://openreview.net/attachment?id=gLU0UV85Kv&name=pdf) submitted to the 2025 NeurIPS conference. All experiments are GPU optional. Simulations are done on python 3.9.6.

## Initialization

```bash
pip install -r requirements.txt
pip install -e .
```

## Reproduce Results

You can find all the algorithms in `./src/BRAT/algorithms.py` defined. `./src/BRAT/variance_estimation.py` provides the methods of computing the reweighting vector $r_n$ and gives the built-in variance estimation. 

To reproduce the results presented in the paper, you can find 4 notebooks in `./experiments/`:

1. `1d_intervals.ipynb`: Visualizations of built-in interval estimations given by BRATD.

2. `optuna_mse.ipynb`: Fetch and clean the data from [UCI Machine Learning Repository](https://archive.ics.uci.edu/). Tune the models using *Optuna* and visualize the optimized models' mse trajectories with error bars.

3. `coverage_rates.ipynb`: Evaluate the performance of our built-in intervals in terms of coverage. You can reproduce the rainclouds plot of coverage rates in this notebook. 

4. `variable_importance.ipynb`: An example and a trajectory study of the type I and type II error made by the model as sample size increases is provided in this notebook.

## Repo Layout

```bash
src/BRAT/
experiments/    # Reproduce paper experiments here!
requirements.txt
setup.py
README.md
```