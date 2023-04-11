import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_positions(bodies):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for body in bodies:
        x, y, z = body.position
        ax.scatter(x, y, z, label=body.name)
        ax.text(x, y, z, body.name)

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.legend()

    plt.show()
