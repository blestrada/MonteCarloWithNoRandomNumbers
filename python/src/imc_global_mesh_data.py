"""Global mesh data."""

ncells = -1
xsize = -1.0
dx = -1.0

# Cell arrays

cellpos = -1.0
temp = -1.0
temp0 = -1.0
radtemp = -1.0
radtemp0 = -1.0
nrgdep = -1.0
nrgscattered = -1.0
sigma_a = []
sigma_s = []
sigma_t = []

# Nodal arrays

nodepos = -1.0

# Boundary conditions (reflecting or vacuum)
left_bc = None
right_bc = None
