# Magnetite Slab

[![DOI](https://img.shields.io/badge/DOI-10.1021/acs.jpclett.3c01290-blue)](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290)  

This repository contains scripts and data related to the slab section of [**Oxidation-State Dynamics and Emerging Patterns in Magnetite**](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290)  

[<img src="TOC2.png" alt="Table of Contents Figure" width="35%">](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290) 

## Overview  
This repository provides computational workflows and analysis scripts used in the study of magnetite slabs. The scripts focus on exploring the oxidation state dynamics, annealing schemes, surface terminations, and vacancy evolution. The main objectives include:

- Comparison of different annealing schemes (linear vs. exponential temperature decay).
- Analysis of surface terminations and their properties.
- Evaluation of vacancy evolution in magnetite slabs.
- Modeling of slabs with fixed bulk properties to test theoretical predictions.
- Identification of trimeron fingerprints and oxidation state constraints.

## Repository Structure  
```
bulk_magnetite/
│
├── 220510_001_DBT_annealing_scheme_comparison/        # Comparison of different annealing schemes
│
├── 220815_001_111_DBT_001_SCV_comparison/            # Modeling different surface terminations
│   ├── 1_OO1_DBT/                                     # Oxidation state dynamics for 001-DBT
│   ├── 2_111_tet1/                                   # Oxidation state dynamics for 111-tet1
│   ├── 3_001_SCV/                                    # Oxidation state dynamics for 001-SCV
│   ├── 4_analysis/                                   # Data analysis scripts
│   ├── 5_benchmark_slurm/                            # Computational efficiency checks using SLURM
│
├── 220906_001_DBT_linear_exp_comparison/             # Annealing scheme comparison
│   ├── 1_linear/                                     # Linear temperature decay
│   ├── 2_exp/                                        # Exponential temperature decay
│   ├── 3_oct_constrained/                            # Constrained oxidation state swaps to Fe_oct
│   ├── 4_trimeron_analysis/                          # Trimeron fingerprint analysis
│   ├── 6_results/                                    # Results and visualizations
│
├── 221008_111_tet1_figure/                           # Visualization and figure generation
│
├── 230328_vacancy/                                   # Vacancy evolution in magnetite slabs
│   ├── 1_gen/                                        # Vacancy generation scripts
│   ├── 2_eq/                                         # Equilibration scripts
│   ├── 3_analysis/                                   # Analysis of vacancy effects
│
├── 231214_surface_with_bulk/                         # Slabs with fixed bulk properties
│   ├── 1_surface21L_bulk22L/                         # Slabs with 21-layer surface and 22-layer bulk
│   ├── 2_surface13L-21L-29L_bulk24L/                 # Multiple surface/bulk configurations
│   ├── gen_slab/                                     # 001-DBT slab generation scripts
└── README.md                                         # Repository documentation
```
