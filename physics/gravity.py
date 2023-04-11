import numpy as np
from .constants import G

def compute_net_force_on_body(body, other_bodies, gravitational_constant):
    net_force = np.array([0.0, 0.0, 0.0])

    for other_body in other_bodies:
        if body == other_body:
            continue

        distance_vector = other_body.position - body.position
        distance_magnitude = np.linalg.norm(distance_vector)
        force_magnitude = gravitational_constant * body.mass * other_body.mass / distance_magnitude**2
        force_direction = distance_vector / distance_magnitude
        force = force_magnitude * force_direction
        net_force += force

    return net_force
