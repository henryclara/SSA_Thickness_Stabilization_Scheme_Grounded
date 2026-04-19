# The Thickness Stabilisation Scheme for Grounded Ice

This repository contains a Shallow Shelf Approximation (SSA) model implemented with the FEniCS finite element software. We introduce the Thickness Stabilization Scheme (TSS), which treats the driving force implicitly and significantly increases the largest stable time-step size, whilst retaining high accuracy in SSA simulations. This repository contains:

- A Jupyter Notebook, which outlines the derivation of the Thickness Stabilization Scheme
- A mesh generated using Gmsh

**Licensing details**

- Gmsh and FEniCS are open-source softwares.

**References**

T. Westling Dolling, A.C.J. Henry and J. Ahlkrona. A numerical stabilization scheme for the shallow shelf approximation.

C. Geuzaine and J.-F. Remacle. Gmsh: a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities. International Journal for Numerical Methods in Engineering 79(11), pp. 1309-1331, 2009. https://gmsh.info/

A. Logg, K.-A. Mardal, G. N. Wells et al. Automated Solution of Differential Equations by the Finite Element Method, Springer(2012). https://link.springer.com/book/10.1007/978-3-642-23099-8
