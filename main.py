import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 

	# Create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	# Create Player
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return

		screen.fill("black")

		# hook player update 
		#player.update(dt)

		# render player
		#player.draw(screen)

		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if player.is_colliding(asteroid):
				sys.exit("Game Over!")
			for bullet in shots:
				if asteroid.is_colliding(bullet):
					bullet.kill()
					asteroid.split()

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit FPS to 60 frames per second 
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()