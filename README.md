# Topological Engine Monitor

Reproducibility code for the manuscript:

**Topological Engine Monitor: Persistent Homology-Based Fault Detection in Finite-Time Quantum Engines**

The repository simulates a finite-time single-qubit Otto engine, reconstructs
single-observable trajectories by time-delay embedding, computes persistent
homology, constructs persistence-image and persistence-silhouette features,
and compares the topological engine monitor (TEM) with a six-feature
spectral-statistical monitor (SSM).

## Repository structure

- `notebooks/01_global_timing_jitter.ipynb`  
  Global timing-jitter benchmark and the analyses used to generate the
  manuscript figures.
- `notebooks/02_adiabatic_ramp_distortion.ipynb`  
  Adiabatic-ramp exponent distortion.
- `notebooks/03_correlated_ou_sweep_noise.ipynb`  
  Correlated Ornstein–Uhlenbeck sweep noise.
- `notebooks/04_longitudinal_high_frequency_ripple.ipynb`  
  Longitudinal phase-coherent ripple.
- `notebooks/05_combined_multi_channel_degradation.ipynb`  
  Combined multi-channel control degradation.
- `figures/`  
  Publication figure exports supplied with the manuscript.
- `results/expected_auc.csv`  
  Cross-validated AUC values reported in the manuscript.

## Installation

### Using `venv`

```bash
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate         # Windows
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

### Using Conda

```bash
conda env create -f environment.yml
conda activate topological-engine-monitor
jupyter lab
```

## Reproducing the analysis

Each notebook is self-contained and can be executed independently from top
to bottom. Full runs use 1000 independent trajectories and therefore may
take substantial time. Random seeds are fixed in the notebooks.

The release uses the persistence-image widths reported in the revised
manuscript:

- `sigma_PI = 0.02` for global timing jitter and adiabatic-ramp distortion;
- `sigma_PI = 0.005` for OU sweep noise, longitudinal ripple, and the
  combined multi-channel benchmark.

Small numerical differences can occur across Python, BLAS, and package
versions, but the qualitative conclusions and performance hierarchy should
remain unchanged.

## Main reported AUC values

| Degradation model | SSM | TEM images | TEM silhouettes |
|---|---:|---:|---:|
| Global timing jitter | 0.8360 | 0.8782 | 0.7974 |
| Adiabatic ramp distortion | 0.7660 | 0.8537 | 0.8135 |
| Correlated sweep noise (OU) | 0.6932 | 0.9703 | 0.9490 |
| Longitudinal high-frequency ripple | 0.6759 | 0.9474 | 0.9071 |
| Combined multi-channel control degradation | 0.6817 | 0.9278 | 0.8463 |

## Data

All benchmark trajectories are generated synthetically by the notebooks.
No external or private dataset is required.

## License

A software license should be selected by the authors before public release.
A permissive license such as MIT or BSD-3-Clause is suitable if all authors
agree.
