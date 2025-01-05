import pygame
import random
import sys

# Inisialisasi pygame
pygame.init()

# Konstanta layar
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid oncoming cars")

# Warna
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Kecepatan game
FPS = 60
clock = pygame.time.Clock()

# Memuat gambar
PLAYER_IMAGE = pygame.image.load("image/player.png")
ENEMY_IMAGES = {
    'red': pygame.image.load("image/red_car.png"),
    'blue': pygame.image.load("image/blue_car.png"),
    'yellow': pygame.image.load("image/yellow_car.png"),
}

# Ubah ukuran gambar
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (40, 60))
ENEMY_IMAGES = {color: pygame.transform.scale(img, (40, 60)) for color, img in ENEMY_IMAGES.items()}


class Car:
    def __init__(self, x, y, image, speed):
        self._x = x
        self._y = y
        self._image = image
        self._speed = speed

    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))

    def move(self):
        self._y += self._speed

    def is_out_of_bounds(self):
        return self._y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._image.get_width(), self._image.get_height())

class PlayerCar(Car):
    def move(self, keys):
        if keys[pygame.K_LEFT] and self._x > 50:
            self._x -= self._speed
        if keys[pygame.K_RIGHT] and self._x < WIDTH - 50 - self._image.get_width():
            self._x += self._speed
        if keys[pygame.K_UP] and self._y > 0:
            self._y -= self._speed
        if keys[pygame.K_DOWN] and self._y < HEIGHT - self._image.get_height():
            self._y += self._speed

def draw_road():
    pygame.draw.rect(SCREEN, GRAY, (50, 0, WIDTH - 100, HEIGHT))
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(SCREEN, WHITE, (WIDTH // 2 - 5, i, 10, 20))

def spawn_enemy(enemies):
    """Fungsi untuk membuat musuh baru jika belum mencapai batas maksimum."""
    if len(enemies) < MAX_ENEMIES:
        while True:
            enemy_x = random.randint(50, WIDTH - 100 - 40)
            enemy_speed = random.randint(3, 6)
            enemy_image = random.choice(ENEMY_IMAGES)
            enemy = Car(enemy_x, -60, enemy_image, enemy_speed)
            if not any(enemy.get_rect().colliderect(e.get_rect()) for e in enemies):
                enemies.append(enemy)
                break

def game_over_screen(score):
    font = pygame.font.SysFont(None, 30)
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

    SCREEN.fill(BLACK)
    SCREEN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
    SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 30))
    SCREEN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 90))
    pygame.display.flip()

   #Update skor ketika musuh keluar dari layar.
    def update_score(self):
        """Perbarui skor ketika musuh keluar dari layar."""
        out_of_bounds = [enemy for enemy in self.enemies if enemy.is_out_of_bounds()]
        self.score += len(out_of_bounds)
        self.enemies = [enemy for enemy in self.enemies if not enemy.is_out_of_bounds()]

    #Fungsi utama game. Berisi loop permainan.
    def run(self):
        """Fungsi utama game."""
        running = True
        while running:
            SCREEN.fill(YELLOW)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.draw_road()
            self.player.draw(SCREEN)

            if random.randint(1, 20) == 1:
                self.spawn_enemy()

            for enemy in self.enemies:
                enemy.move()
                enemy.draw(SCREEN)

            if self.check_collision():
                self.game_over()
                return

            self.update_score()

            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            SCREEN.blit(score_text, (10, 10))
            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
