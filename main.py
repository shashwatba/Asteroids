import pygame
import sys as sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shooters = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)   
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shooters, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  
    asteroidField = AsteroidField()  
     

    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            a = asteroid.checkForCollisions(player)
            if a:
                print("Game Over!")
                sys.exit()
            for shots in shooters:
                if shots.checkForCollisions(asteroid):
                    shots.kill()
                    asteroid.split()
        for characters in drawable:
            characters.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000   
        




if __name__ == "__main__":
    main()