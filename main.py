#   #   # Libraries
import pygame, asyncio
import matrix_operations as mat
from sys import exit
import math

#   #   # Initialise Pygame
pygame.init()
WINDOW_SIZE = (600,600)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
WINDOW = pygame.Surface((600,600))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("3d render")


square_coords = [0 for i in range(0,6)] # Alternatively len(cube_vectors)
coords_1 = [0 for i in range(0,6)]
coords_2 = [0 for i in range(0,6)] 
z_list = []


def rotate():
    global square_coords, coords_1, coords_2, x, y, z
    
    if x == 1:
        angle_x = 0.05
    elif x == 2:
        angle_x = -0.05
    else:
        angle_x = 0
    # Y
    if y == 1:
        angle_y = 0.05
    elif y == 2:    
        angle_y = -0.05
    else:
        angle_y = 0
    # Z
    if z == 1:
        angle_z = 0.05
    elif z == 2:
        angle_z = -0.05
    else:
        angle_z = 0
    
    if x:   
        transformation_x = [
            [1, 0, 0],
            [0, math.cos(angle_x), -math.sin(angle_x)],
            [0 ,math.sin(angle_x), math.cos(angle_x)]
        ]
    if y:
        transformation_y = [
            [math.cos(angle_y), 0, math.sin(angle_y)],
            [0, 1, 0],
            [-math.sin(angle_y), 0, math.cos(angle_y)]
         ]
    if z:
        transformation_z = [
            [math.cos(angle_z),-math.sin(angle_z), 0],
            [math.sin(angle_z),math.cos(angle_z), 0],
            [0, 0, 1]
        ]

    for i in range(len(cube_vectors)):
        for j in range(len(cube_vectors[i])):
            if x:
                cube_vectors[i][j] = mat.multiplication(transformation_x, cube_vectors[i][j]) # Multiply each 3d coord by transformation matrix
            if y:
                cube_vectors[i][j] = mat.multiplication(transformation_y, cube_vectors[i][j])
            if z:
                cube_vectors[i][j] = mat.multiplication(transformation_z, cube_vectors[i][j])
            
        square_coords[i] = [((300 + cube_vectors[i][j][0][0]),(300 + cube_vectors[i][j][1][0])) for j in range(len(cube_vectors[i]))] # Transforms coords: 3d -> 2d
        coords_1[i] = [square_coords[i][0], square_coords[i][1], square_coords[i][2]] # Assigns coords neccesary to draw white polygon
        coords_2[i] = [square_coords[i][3], square_coords[i][1], square_coords[i][2]] # Assigns coords neccesary to draw red polygon


cube_vectors = [[
    [ # Back Face
    [-25], # x = -25 is further left than x = 25
    [-25], # y = -25 is above y = 25
    [0] # z = 0 is behind z = -50
],
[
    [-25],
    [25],
    [0]
    ],
[
    [25],
    [-25],
    [0]
    ],
[
    [25],
    [25],
    [0]
    ],
],
[ # Front Face
    [
    [-25],
    [-25],
    [-50]
],
[
    [-25],
    [25],
    [-50]
    ],
[
    [25],
    [-25],
    [-50]
    ],
[
    [25],
    [25],
    [-50]
    ],

],
[ # Top Face
    [
    [-25],
    [-25],
    [0]
],
[
    [-25],
    [-25],
    [-50]
    ],
[
    [25],
    [-25],
    [0]
    ],
[
    [25],
    [-25],
    [-50]
    ],
    
],
[ # Bottom Face
    [
    [-25],
    [25],
    [0]
],
[
    [-25],
    [25],
    [-50]
    ],
[
    [25],
    [25],
    [0]
    ],
[
    [25],
    [25],
    [-50]
    ],
    
],

[ # Left Face
    [
    [-25],
    [-25],
    [0]
],
[
    [-25],
    [25],
    [0]
    ],
[
    [-25],
    [-25],
    [-50]
    ],
[
    [-25],
    [25],
    [-50]
    ],
],

[ # Right Face
    [
    [25],
    [-25],
    [0]
],
[
    [25],
    [-25],
    [0]
    ],
[
    [25],
    [-25],
    [-50]
    ],
[
    [25],
    [-25],
    [-50]
    ],
]


]
    
print(cube_vectors)

x,y,z = 0,0,0

async def main():
    global x,y,z
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN: 
                match event.key:
                    case pygame.K_w:
                        x = 1
                    case pygame.K_s:
                        x = 2
                    case pygame.K_d:
                        y = 1
                    case pygame.K_a:
                        y = 2
                    case pygame.K_q:
                        z = 2
                    case pygame.K_e:
                        z = 1
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_w:
                        x = 0      
                    case pygame.K_s:
                        x = 0
                    case pygame.K_d:
                        y = 0
                    case pygame.K_a:
                        y = 0
                    case pygame.K_q:
                        z = 0
                    case pygame.K_e:
                        z = 0


        

        
        WINDOW.fill((27,27,27))
        rotate()
        #print(square_coords)
        for i in range(len(square_coords)):
            #print(coords_1[i])
            #print(square_coords[i])
            #print(coords_2[i])
            pygame.draw.polygon(WINDOW, (255,255,255), coords_1[i])
            pygame.draw.polygon(WINDOW, (255,0,0), coords_2[i])


        surface = pygame.transform.scale(WINDOW, WINDOW_SIZE)
        SCREEN.blit(surface, (0,0))
        
        pygame.display.update()
        CLOCK.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
