import pygame
import sys
from celestial_bodies import Galaxy

# Initialization
pygame.init()
width, height = 1200, 800  # Define the window dimensions
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System Simulation")

def project_3d_to_2d(pos, camera_distance):
    x, y, z = pos
    scale = camera_distance / (z + camera_distance)
    x2d = int(width / 2 + x * scale)
    y2d = int(height / 2 + y * scale)
    return x2d, y2d

def draw_bodies(galaxy, camera_distance):
    screen.fill((0, 0, 0))  # Clear the screen (black background)

    for body in galaxy.get_all_bodies():
        # Project 3D position to 2D screen coordinates
        x, y, z = body.position / 1e9
        x2d, y2d = project_3d_to_2d((x, y, z), camera_distance)

        # Choose color based on body type
        if body.name == "Sun":
            color = (255, 255, 0)
        else:
            color = (0, 255, 0)

        # Draw the body
        pygame.draw.circle(screen, color, (x2d, y2d), 5)

    pygame.display.flip()  # Update the display

def main(simulation_function, galaxy):
    clock = pygame.time.Clock()
    camera_distance = 50

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Run the simulation step
        simulation_function()

        # Draw the celestial bodies
        draw_bodies(galaxy, camera_distance)

        # Limit the frame rate
        clock.tick(60)
