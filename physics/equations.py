import numpy as np
from .constants import G

def gravitational_force(body1, body2):
    distance = np.linalg.norm(body2.position - body1.position)
    force_magnitude = G * body1.mass * body2.mass / distance**2
    force_direction = (body2.position - body1.position) / distance
    return force_magnitude * force_direction
