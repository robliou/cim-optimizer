# cim-optimizer

[![tests](https://github.com/mcmahon-lab/cim-optimizer/actions/workflows/tests.yml/badge.svg)](https://github.com/mcmahon-lab/cim-optimizer/actions/workflows/tests.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains a reference implementation of a simulator of the Coherent Ising Machine (CIM). For more information, please see the [documentation](https://cim-optimizer.readthedocs.io/en/latest/). 

The CIM was [developed](https://doi.org/10.1038/s42254-022-00440-8) as a photonic machine for heuristically solving Ising-optimization problems. Simulations of the CIM can be thought of as an unconventional, dynamical-systems-based, heuristic algorithm for solving Ising problems, which can compete with more conventional Ising-solving algorithms (such as simulated annealing, parallel tempering, and branch-and-bound).

There are two main intended audiences for this repository:
1. People who would like to use a state-of-the-art implementation of the CIM algorithm to heuristically solve Ising problems (for example, to benchmark the CIM approach against other heuristic approaches).
2. People who would like to study the workings of the CIM approach through simulation, and/or would like to have a quantitative model of CIM performance to make predictions about how future CIM hardware implementations will perform.

Most of the code in this repository resides within a Python file `solve_Ising.py`. This repository is written in Python, and all input and result data for users is formatted in NumPy, while the source code uses PyTorch libraries for GPU acceleration. Several demonstration notebooks are provided in the [notebooks](https://github.com/mcmahon-lab/cim-optimizer/tree/main/notebooks) directory, and showcase how to configure and run the solver function.

The goal of the CIM (and its simulation and variants) is to heuristically optimize the following $N$-variable objective function (the classical $N$-spin Ising Hamiltonian):

$$ H = -\sum_{1\leq i < j \leq N} J_{ij}\sigma_i \sigma_j - \sum_{1 \leq i \leq N} h_i \sigma_i$$

where $J$ is an $N \times N$ coupling matrix and $h$ is an $N$-dimensional vector representing the Zeeman external field. Each Ising spin is represented as $\sigma_i \in$ { $-1, 1$ }.

This repository uses solver algorithms adapted from:
- Discrete-Time Measurement-Feedback Coherent Ising Machine
> P.L. McMahon*, A. Marandi*, Y. Haribara, R. Hamerly, C. Langrock, S. Tamate, T. Inagaki, H. Takesue, S. Utsunomiya, K. Aihara, R.L. Byer, M.M. Fejer, H. Mabuchi, Y. Yamamoto. A fully programmable 100-spin coherent Ising machine with all-to-all connections. _Science_ **354**, No. 6312, 614 - 617 (2016). https://doi.org/10.1126/science.aah5178
- Amplitude-Heterogeneity-Correction variant of the CIM algorithm
> T. Leleu, Y. Yamamoto, P.L. McMahon, and K. Aihara, Destabilization of local minima in analog spin systems by correction of amplitude heterogeneity. _Physical Review Letters_ **122**, 040607 (2019). https://doi.org/10.1103/PhysRevLett.122.040607
- Chaotic-Amplitude-Control variant of the CIM algorithm
> T. Leleu, F. Khoyratee, T. Levi, R. Hamerly, T. Kohno, K. Aihara. Scaling advantage of chaotic amplitude control for high-performance combinatorial optimization. Commun Phys **4**, 266 (2021). https://doi.org/10.1038/s42005-021-00768-0

All of the algorithms implemented are for _classical_ models of the CIM. See https://doi.org/10.1364/QIM.2017.QW3B.2 and https://doi.org/10.1117/12.2613817 for examples of discussions of quantum models of the CIM, which are not implemented in this repository.

Please see the references within the cited papers for a fuller picture of the history and development of the Coherent-Ising-Machine approach to heuristically solving Ising problems, which was begun at Stanford University in the group of Yoshihisa Yamamoto circa 2010.

# Getting Started (The Short Version)

## Installation

```
pip install cim-optimizer
```

## Usage

```
from cim_optimizer.solve_Ising import *
import numpy as np
N = 20 # number of spins
J = np.random.randint(-100,100,size=(N,N)) # spin-spin-coupling matrix of a random Ising instance
J = J + J.T # ensure the matrix J is symmetric
np.fill_diagonal(J, 0) # ensure diagonal elements of the coupling matrix J are zero
h = np.random.randint(-100,100,size=(N)) # external-field vector of a random Ising instance
solution = Ising(J, h).solve()
print(solution)
```

# Getting Started (The Longer Version)
- For background on CIMs, metadata, and GPU acceleration check out [Example 1](https://github.com/mcmahon-lab/cim-optimizer/blob/main/notebooks/Example%201%20-%20CIM%20Introduction.ipynb).
- Hyperparameters and hyperparameter tuning (with BOHB) is showcased in [Example 2](https://github.com/mcmahon-lab/cim-optimizer/blob/main/notebooks/Example%202%20-%20Hyperparameter%20Setup.ipynb).
- An example solving the Maritime Inventory Routing Problem, which with the Ising mapping used, includes non-zero external-field terms [Example 3](https://github.com/mcmahon-lab/cim-optimizer/blob/main/notebooks/Example%203%20-%20MIRP%20with%20CIM.ipynb).

# Requirements
- Requires Python Version >= 3.7
- Requires PyTorch Version 1.12.1 to be compiled with CUDA 11.6 (for GPU acceleration). See Pytorch's [installation page](https://pytorch.org/) for more information.
- Requires [BOHB-HPO Version 0.5.2](https://pypi.org/project/BOHB-HPO/) 
- For an exhaustive list of requirements, see the [**requirements.txt**](https://github.com/mcmahon-lab/cim-optimizer/blob/main/requirements.txt) file.

# Contributors

Francis Chen, Brian Isakov, Tyler King, Timothée Leleu, Tatsuhiro Onodera, Peter McMahon

# Funding acknowledgements

The development of this open-source implementation of CIM algorithm variants was partially supported by an NSF Expeditions award (CCF-1918549).

# How to cite

If you use this code in your research, please consider citing it. You can retrieve an APA or BibTeX citation by clicking 'Cite this repository' on the sidebar in GitHub, or you can view the raw citation data in [CITATION.cff](https://github.com/mcmahon-lab/cim-optimizer/blob/main/CITATION.cff).

# License

The code in this repository is released under the following license:

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

A copy of this license is given in this repository as [license.txt](https://github.com/mcmahon-lab/cim-optimizer/blob/main/license.txt).
