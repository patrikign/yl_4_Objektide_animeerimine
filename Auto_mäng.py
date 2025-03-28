import pygame
import random

# Initsialiseeri Pygame
pygame.init()

# Mängu akna suurus
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autode mäng")

# Pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")
sinine_auto = pygame.transform.rotate(sinine_auto, 180)

# Auto suurused
car_width, car_height = punane_auto.get_size()


def wait_for_start():
    font = pygame.font.Font(None, 36)
    while True:
        screen.fill((0, 0, 0))
        start_text = font.render("Vajuta ENTER, et alustada", True, (255, 255, 255))
        screen.blit(start_text, (WIDTH // 2 - 140, HEIGHT // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return


def run_game():
    red_x = WIDTH // 2 - car_width // 2
    red_y = HEIGHT - car_height - 20  # Aseta punane auto alla

    blue_cars = []
    for _ in range(3):
        blue_x = random.randint(170, WIDTH - 170 - car_width)
        blue_y = random.randint(-300, -50)  # Sinised autod alustavad ülevalt
        blue_cars.append([blue_x, blue_y])

    score = 0
    speed = 5
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(taust, (0, 0))
        screen.blit(punane_auto, (red_x, red_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and red_x > 170:
            red_x -= speed
        if keys[pygame.K_RIGHT] and red_x < WIDTH - 170 - car_width:
            red_x += speed

        # Siniste autode liikumine ja kokkupõrke tuvastamine
        for car in blue_cars:
            car[1] += 5  # Liiguvad alt üles
            if car[1] > HEIGHT:
                car[1] = random.randint(-300, -50)
                car[0] = random.randint(170, WIDTH - 170 - car_width)
                score += 1
            screen.blit(sinine_auto, (car[0], car[1]))

            # Kontrolli kokkupõrget
            if red_x < car[0] + car_width and red_x + car_width > car[0] and red_y < car[
                1] + car_height and red_y + car_height > car[1]:
                running = False

        # Kuva skoor
        font = pygame.font.Font(None, 36)
        score_text = font.render("Skoor: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Sündmuste kontroll
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.flip()
        clock.tick(30)

    # Mängu lõpp
    while True:
        screen.fill((0, 0, 0))
        game_over_text = font.render("Mäng lõppes! Skoor: " + str(score), True, (255, 255, 255))
        restart_text = font.render("Vajuta ENTER, et uuesti mängida", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        screen.blit(restart_text, (WIDTH // 2 - 140, HEIGHT // 2 + 20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                run_game()
                return


wait_for_start()
run_game()
