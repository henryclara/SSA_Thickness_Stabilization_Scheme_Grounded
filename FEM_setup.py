from fenics import *
from constants import *
from SSA_functions import *
import numpy as np

# Read in the mesh

p0 = Point(0.0, 0.0)
p1 = Point(100000.0, 100000.0)

nx = 100
ny = 100

mesh = RectangleMesh(p0, p1, nx, ny)
h = CellDiameter(mesh)

# Define the function spaces

V = FunctionSpace(mesh, 'P', 1)
VV = VectorFunctionSpace(mesh,"CG",1)

uvec=Function(VV)
(ux,uy)=split(uvec)

uvect=TrialFunction(VV)
(u1,u2)=split(uvect)

vvect=TestFunction(VV)
(v1,v2)=split(vvect)

phi = TestFunction(V)
thick_new = TrialFunction(V)

# Interpolate fields 

a_s_ = Expression("1.0", degree=2)
a_b_ = Expression("0.0", degree=2)
a_s = interpolate(a_s_, V)
a_b = interpolate(a_b_, V)

n = FacetNormal(mesh)

slope = 1.0e-2
zb0 = 0.0        # bed elevation at y = 0
H0 = 300.0       # initial ice thickness

zb_expr = Expression("zb0 - slope*x[1]", degree=1, zb0=zb0, slope=slope)
zs_expr = Expression("zb0 + H0 - slope*x[1]", degree=1, zb0=zb0, H0=H0, slope=slope)

zb = interpolate(zb_expr, V)
zs = interpolate(zs_expr, V)

# Basal friction details

xc = 50000.0
sigma_x = 25000.0

yc = 25000.0
Ly = 15000.0

beta_bg2_val = 1e-2
beta_stream2_val = 5e-4

beta2_expr = Expression(
    "beta_bg2 - (beta_bg2 - beta_stream2) "
    "* exp(-pow(x[0] - xc, 2) / (2.0 * sigma_x * sigma_x)) "
    "* 0.5 * (1.0 + tanh((x[1] - yc) / Ly))",
    degree=2,
    beta_bg2=beta_bg2_val,
    beta_stream2=beta_stream2_val,
    xc=xc,
    sigma_x=sigma_x,
    yc=yc,
    Ly=Ly
)

beta2 = interpolate(beta2_expr, V)

thick = Function(V)
thick.vector()[:] = zs.vector() - zb.vector()

thick_bc = interpolate(thick, V)

# Boundary conditions

boundaries = mark_bed_surface(mesh)
ds = Measure("ds", domain=mesh, subdomain_data=boundaries)
n = FacetNormal(mesh)

# Define boundary conditions (BCs)

# Dirichlet BCs for the velocity field
bc1 = DirichletBC(VV.sub(0), 0.0, boundaries,2)
bc2 = DirichletBC(VV.sub(1), 0.0, boundaries,2)
bc3 = DirichletBC(VV.sub(0), 0.0, boundaries,3)
bc4 = DirichletBC(VV.sub(0), 0.0, boundaries,4)

# Dirichlet BCs for the thickness field

#H_bc1 = DirichletBC(V, thick_bc, boundaries, 1)
#H_bc2 = DirichletBC(V, thick_bc, boundaries, 2)
#H_bc3 = DirichletBC(V, thick_bc, boundaries, 3)
#H_bc4 = DirichletBC(V, thick_bc, boundaries, 4)
