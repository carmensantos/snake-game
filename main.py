# Import necessary libraries for the game.
import pygame
import random

# Initialize Pygame and set up the game window.
pygame.init()
square_width = 750 # Width of the game window.
pixel_width = 50 # Size of the pixels (snake and target blocks).
screen = pygame.display.set_mode([square_width] * 2) # Create the game window.
clock = pygame.time.Clock() # Clock to control the refresh rate.
running = True # Control variable for the main game loop.


# Function to generate random starting positions within the game area.
def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


# Function to reset the game when the snake dies or is restarted.
def reset():
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()


# Function to check if the snake has gone out of bounds.
def is_out_of_bounds():
    return snake_pixel.bottom > square_width or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width


# Initialize the snake and target with their positions and sizes.
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0) # Initial direction of the snake (stationary).
snake_length = 1 # Initial length of the snake.

target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

# Main game loop.
while running:
    # Process events (e.g., closing the window).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black") # Clear the screen.

    # Check and handle if the snake goes out of bounds.
    if is_out_of_bounds():
        # Reset the snake and target upon colliding with the edge.
        snake_length = 1
        target.center = generate_starting_position()
        snake_pixel.center = generate_starting_position()
        snake = [snake_pixel.copy()]

    # Check if the snake has reached the target.
    if snake_pixel.center == target.center:
        target.center = generate_starting_position() # Move the target.
        snake_length += 1 # Increase the length of the snake.
        snake.append(snake_pixel.copy())

     # Handle keyboard input to control the direction of the snake.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = (0, - pixel_width)
    if keys[pygame.K_s]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = (- pixel_width, 0)
    if keys[pygame.K_d]:
        snake_direction = (pixel_width, 0)

    # Draw the snake and target on the screen.
    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    # Move the snake in the indicated direction.
    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy()) # Add a new segment to the end of the snake.
    snake = snake[-snake_length:] # Maintain the length of the snake.

    pygame.display.flip() # Update the screen.

    clock.tick(10) # Control the refresh rate at 10 FPS.

pygame.quit() # Close Pygame when the main loop ends.
