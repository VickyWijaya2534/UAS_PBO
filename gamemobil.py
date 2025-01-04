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

