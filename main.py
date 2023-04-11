import numpy as np
from celestial_bodies import Galaxy, Star, Planet
from physics.equations import gravitational_force
from physics.integrators import update_positions, update_velocities
from visualization.plot import plot_positions

# Initialize celestial bodies
milky_way = Galaxy("Milky Way")
sun = Star("Sun", 1.989e30, [0, 0, 0], [0, 0, 0])

# Define simplified initial positions and velocities for the planets
planets_data = [
    ("Mercury", 3.301e23, [57.9e9, 0, 0], [0, 47.87e3, 0]),
    ("Venus", 4.867e24, [108.2e9, 0, 0], [0, 35.02e3, 0]),
    ("Earth", 5.972e24, [147.1e9, 0, 0], [0, 29.78e3, 0]),
    ("Mars", 6.417e23, [206.6e9, 0, 0], [0, 24.077e3, 0]),
    ("Jupiter", 1.898e27, [740.5e9, 0, 0], [0, 13.07e3, 0]),
    ("Saturn", 5.683e26, [1.35e12, 0, 0], [0, 9.69e3, 0]),
    ("Uranus", 8.681e25, [2.74e12, 0, 0], [0, 6.81e3, 0]),
    ("Neptune", 1.024e26, [4.50e12, 0, 0], [0, 5.43e3, 0]),
]

for name, mass, position, velocity in planets_data:
    planet = Planet(name, mass, position, velocity)
    milky_way.add_body(planet)

# Simulation parameters
time_step = 3600 * 24 * 7  # 1 week in seconds
simulation_steps = 52 * 100  # 100 years

# Main simulation loop
for step in range(simulation_steps):
    forces = []

    for body1 in milky_way.get_all_bodies():
        net_force = np.array([0.0, 0.0, 0.0])

        for body2 in milky_way.get_all_bodies():
            if body1 != body2:
                net_force += gravitational_force(body1, body2)
        forces.append(net_force)

    # Update positions and velocities
    update_positions(milky_way.get_all_bodies(), time_step)
    update_velocities(milky_way.get_all_bodies(), forces, time_step)

    # Periodically visualize the simulation
    if step % 52 == 0:  # Every year
        plot_positions(milky_way.get_all_bodies())
