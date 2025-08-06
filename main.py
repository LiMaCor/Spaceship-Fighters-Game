import pygame

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Fighters")

WHITE = (255, 255, 255)

FPS = 60

def draw():
    WINDOW.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()