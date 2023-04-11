import numpy as np
from celestial_bodies import Galaxy, Star, Planet
from physics.gravity import compute_net_force_on_body
from physics.integrators import update_positions, update_velocities
from physics.constants import G
from visualization.pygame_visualization import main as pygame_main
import matplotlib.pyplot as plt

# Define constants
time_step = 24 * 60 * 60  # Time step: 1 day

# Create celestial bodies
sun = Star("Sun", 1.989e30, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
earth = Planet("Earth", 5.972e24, np.array([147_095_000_000.0, 0.0, 0.0]), np.array([0.0, 30_290.0, 0.0]))

# Create the galaxy
milky_way = Galaxy("Milky Way")
milky_way.add_body(sun)
milky_way.add_body(earth)

# Define the simulation step function
def simulation_step():
    forces = [compute_net_force_on_body(body, milky_way.get_all_bodies(), G) for body in milky_way.get_all_bodies()]
    update_positions(milky_way.get_all_bodies(), time_step)
    update_velocities(milky_way.get_all_bodies(), forces, time_step)


# Run the Pygame visualization
pygame_main(simulation_step, milky_way)

# Define the plot_positions function
def plot_positions(galaxy):
    fig, ax = plt.subplots()

    for body in galaxy.get_all_bodies():
        x, y, z = body.position / 1e9
        if body.name == "Sun":
            color = "yellow"
        else:
            color = "green"
        ax.scatter(x, y, c=color)

    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.title("Solar System Positions")
    plt.grid()
    plt.axis("equal")
    plt.show()

# Run the simulation for a certain number of iterations
num_iterations = 100
for _ in range(num_iterations):
    simulation_step()

# Plot the final positions
plot_positions(milky_way)
