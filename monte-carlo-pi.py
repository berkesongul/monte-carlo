import pygame
import random
import math
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
WIDTH, HEIGHT = 600, 600
INFO_HEIGHT = 100
RADIUS = WIDTH // 2
CENTER = (WIDTH // 2, HEIGHT // 2)
TOTAL_DROPS_TARGET = 1000000000 # Total number of marbles to drop
DROPS_PER_FRAME = 20000     # Simulation speed

def run_simulation():
    pygame.init()
    screen = pygame.display.set_caption("Monte Carlo Pi Simulation")
    screen = pygame.display.set_mode((WIDTH, HEIGHT + INFO_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 20)

    # Data Storage
    hits = 0
    total = 0
    history = [] # Stores pi estimates for the graph

    # Paint the background once
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), CENTER, RADIUS, 2)

    running = True
    while running and total < TOTAL_DROPS_TARGET:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drop multiple marbles at once (for speed)
        for _ in range(DROPS_PER_FRAME):
            if total >= TOTAL_DROPS_TARGET: break
            
            # Random coordinate (within the square)
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

            # Distance to center (Euclidean distance)
            distance = math.sqrt((x - CENTER[0])**2 + (y - CENTER[1])**2)
            
            total += 1
            if distance <= RADIUS:
                hits += 1
                color = (255, 60, 60) # Red (Inside)
            else:
                color = (60, 60, 255) # Blue (Outside)

            # Draw the point
            pygame.draw.circle(screen, color, (x, y), 2)
            
            # Pi Estimate and History
            current_pi = 4 * (hits / total)
            history.append(current_pi)

        # Update Info Panel
        pygame.draw.rect(screen, (240, 240, 240), (0, HEIGHT, WIDTH, INFO_HEIGHT))
        stat_text = font.render(f"Top: {total} | Hits: {hits} | Pi: {current_pi:.5f}", True, (30, 30, 30))
        error = abs(math.pi - current_pi)
        error_text = font.render(f"Error Margin: {error:.6f}", True, (100, 0, 0))
        
        screen.blit(stat_text, (20, HEIGHT + 20))
        screen.blit(error_text, (20, HEIGHT + 55))

        pygame.display.flip()
        # clock.tick(60) # Uncomment to cap the frame rate

    pygame.quit()
    return history

# --- ANALYSIS AND GRAPH ---
if __name__ == "__main__":
    print("Starting simulation...")
    pi_values = run_simulation()
    
    print("Drawing graph...")
    plt.figure(figsize=(10, 6))
    plt.plot(pi_values, label="Pi Estimate", color='blue', linewidth=1)
    plt.axhline(y=math.pi, color='red', linestyle='--', label=f"Actual Pi ({math.pi:.5f})")
    plt.title(f"Pi Convergence via Monte Carlo Method ({len(pi_values)} Samples)")
    plt.xlabel("Number of Marbles Dropped")
    plt.ylabel("Estimated Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()