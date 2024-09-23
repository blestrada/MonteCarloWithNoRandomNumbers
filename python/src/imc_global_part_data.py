"""Global particle data."""

# Particle Parameters
Nx = -1
Nmu = -1
Nt = -1
Nxi = -1

n_max = -1

# Global list of particle properties
particle_prop = []
scattered_particles = []

# Census grid
census_grid = []

# Some parameters
# mode : random numbers or no random numbers (rn or nrn)
# scattering: using analog scattering or implicit scattering - used only in NRN mode (analog or implicit)
mode = None
scattering = None