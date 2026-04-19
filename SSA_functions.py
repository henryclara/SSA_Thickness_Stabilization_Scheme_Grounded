from fenics import *
import matplotlib.pyplot as plt
from constants import *

def viscosity(ux,uy,thick):
    n = 3
    mu=0.5*thick*(A**(-1/n))*((ux.dx(0))**2+(uy.dx(1))**2\
       +ux.dx(0)*uy.dx(1)+0.25*(ux.dx(1)+uy.dx(0))**2\
       +1e-5**2 )**((1-n)/(2*n))
    return mu

def mark_bed_surface(msh, outflow_id=1, inflow_id=2, right_id=3, left_id=4):
    dim = msh.geometric_dimension()
    msh.init()
    boundaries = MeshFunction("size_t", msh, dim-1)
    boundaries.set_all(0)
    for facet in facets(msh):
        if facet.exterior() and facet.normal()[dim - 1] < -10 * DOLFIN_EPS:
            boundaries[facet] = inflow_id
        elif facet.exterior() and facet.normal()[dim - 1] > 10 * DOLFIN_EPS:
            boundaries[facet] = outflow_id
        elif facet.exterior() and facet.normal()[dim - 2] > 10 * DOLFIN_EPS:
            boundaries[facet] = right_id
        elif facet.exterior() and facet.normal()[dim - 2] < -10 * DOLFIN_EPS:
            boundaries[facet] = left_id
    return boundaries

def plot_field(field, label, cmap='plasma_r'):
    c=plot(field, cmap='plasma_r')
    cb = plt.colorbar(c)
    cb.set_label(label, size=20)
    cb.ax.tick_params(labelsize=15) 
    plt.xlabel(r'$x$ (m)', size=20)
    plt.ylabel(r'$y$ (m)', size=20)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.savefig("Results/" + label + "_dt_" + str(dt) + "_theta_" + str(theta) + "_T_" + str(T) + ".png", dpi=300)
