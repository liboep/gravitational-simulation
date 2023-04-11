def update_positions(celestial_bodies, dt):
    for body in celestial_bodies:
        body.position += body.velocity * dt

def update_velocities(celestial_bodies, forces, dt):
    for i, body in enumerate(celestial_bodies):
        body.velocity += forces[i] * dt / body.mass