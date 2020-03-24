import pygame

class Ball:
	def __init__(self, x, y, radius, screen):
		self.x = x
		self.y = y
		self.radius = radius
		self.screen = screen

	def draw(self):
		pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.radius)

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()
ball1 = Ball(100, 100, 20, screen)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	screen.fill((0, 0, 0))

	ball1.draw()

	pygame.display.flip()
	clock.tick(60)
