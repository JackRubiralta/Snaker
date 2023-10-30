from time import sleep
import os
import random
import copy

WIDTH = 30
HEIGHT = 30

UP = -30
DOWN = 30
LEFT = -1
RIGHT = 1


grid = [i * WIDTH + j for i in range(HEIGHT) for j in range(WIDTH)]

class snake:
    head = 1
    body = [2]
    tail = 3
    food = 73
    direction = UP

    def move():
        snake.tail = snake.body[-1]
        snake.body = [snake.head] + snake.body[:-1]
        snake.head = snake.head + snake.direction
        
    def changeDirection(direction):
        snake.direction = direction
        
    def generateNewFood():
        while True:
            new_food_position = random.randint(0, len(grid) - 1)
            if new_food_position not in (snake.head, *snake.body, snake.tail):
                snake.food = new_food_position
                break

    def grow():
        snake.body.append(snake.tail)
        snake.tail = snake.body[-1]
        


    



# reversed
snakes_hamiltonian_cycle = [DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, UP]

'''
   RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN, UP,
    DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, UP,
'''

    
def printSnake():
    result_str = ''
    for y in range(HEIGHT):
        
        for x in range(WIDTH):
            
            if ((x + y * WIDTH) in (snake.body + [snake.tail])) and (snakes_hamiltonian_cycle[x + y * WIDTH] == UP):
                result_str = result_str + '   \u001b[34m|\u001b[0m'
            else:
                if ((x + (y - 1) * WIDTH) in (snake.body + [snake.tail])) and ((y > 0) and (snakes_hamiltonian_cycle[x + (y - 1) * WIDTH] == DOWN)):
                    result_str = result_str + '   \u001b[34m|\u001b[0m'
                else:
                    result_str = result_str + '    '
        result_str = result_str + ' \n'
       
        for x in range(WIDTH):
            
            color = ''
            if (x + y * WIDTH) == snake.head:
                color = '\u001b[32m' # green
            elif (x + y * WIDTH) == snake.tail:
                color = '\u001b[34m' # blue
            elif (x + y * WIDTH) in snake.body:
                color = '\u001b[34m' # blue
            elif (x + y * WIDTH) == snake.food:
                color = '\u001b[31m'# red
             
            if ((x + y * WIDTH) in (snake.body + [snake.tail])) and (snakes_hamiltonian_cycle[x + y * WIDTH] == LEFT):
                if color == '\u001b[32m' or color == '\u001b[31m':
                    result_str = result_str + ' — ' + color + 'O'
                else:
                    result_str = result_str + color + ' — ' + 'O'
            else:
                if (((x - 1) + y * WIDTH) in (snake.body + [snake.tail])) and ((x > 0) and (snakes_hamiltonian_cycle[(x - 1) + y * WIDTH] == RIGHT)):
                    
                    result_str = result_str + ' \u001b[34m— ' + color + 'O'
                  
                else:
                    result_str = result_str + color + '   ' + 'O'
            
            result_str = result_str + '\u001b[0m' # reset color
        result_str = result_str + ' \n'

    print(result_str)

def printHamiltonianCycle(cycle):
    result_str = ''
    for y in range(HEIGHT):
        
        for x in range(WIDTH):
            if (cycle[x + y * WIDTH] == UP) or ((y > 0) and (cycle[x + (y - 1) * WIDTH] == DOWN)):
                if ((x + y * WIDTH) in (snake.body + [snake.tail])) and (snakes_hamiltonian_cycle[x + y * WIDTH] == UP):
                    result_str = result_str + '   \u001b[34m|\u001b[0m'
                else:
                    if ((x + (y - 1) * WIDTH) in (snake.body + [snake.tail])) and ((y > 0) and (snakes_hamiltonian_cycle[x + (y - 1) * WIDTH] == DOWN)):
                        result_str = result_str + '   \u001b[34m|\u001b[0m'
                    else:
                        result_str = result_str + '   |'
            else:
                result_str = result_str + '    '
        result_str = result_str + ' \n'
       
       
        for x in range(WIDTH):
            # LEFT IN FRONT HAS 
            # RIGHT BEHIND
            temp = False
            color = ''
            if (x + y * WIDTH) == snake.head:
                color = '\u001b[32m' # green
            elif (x + y * WIDTH) == snake.tail:
                temp = True
                color = '\u001b[34m' # blue
            elif (x + y * WIDTH) in snake.body:
                color = '\u001b[34m' # blue
            elif (x + y * WIDTH) == snake.food:
                color = '\u001b[31m'# red
             
            if (cycle[x + y * WIDTH] == LEFT):
                if color == '\u001b[32m': # head
                    result_str = result_str + ' — ' + '\u001b[34m' + color + 'O'
                elif color == '\u001b[31m': # food
                    result_str = result_str + ' — ' + color + 'O'
                else:
                    result_str = result_str + color + ' — ' + 'O'

            elif ((x > 0) and (cycle[(x - 1) + y * WIDTH] == RIGHT)):
                
                if color == '\u001b[32m':
                    result_str = result_str + ' \u001b[34m— ' + color + 'O'
                elif color == '\u001b[31m':
                    result_str = result_str + ' — ' + color + 'O'
                elif temp:
                    result_str = result_str + ' — ' + color + 'O'
                else:
                    result_str = result_str + color + ' — ' + 'O'
            else:
                result_str = result_str + color + '   O'
            
            result_str = result_str + '\u001b[0m' # reset color
        result_str = result_str + ' \n'

    print(result_str)


def generatePathToFood(hamiltonian_cycle):
    
    path_to_food = [snake.head] #
    current_tile = snake.head
    
    while (True):

        next_tile = hamiltonian_cycle[current_tile] + current_tile

        current_tile = next_tile
        if (current_tile == snake.food):
            break
        
        path_to_food.append(next_tile) 

    return path_to_food

def generateLoop(hamiltonian_cycle, start):
    loop = []
    current_tile = start
    while (True):
        next_tile = hamiltonian_cycle[current_tile] + current_tile

        current_tile = next_tile
        loop.append(next_tile) 
        if (current_tile == start):
            break
        
        

    return loop


def generateFromFoodToTail(hamiltonian_cycle):
    path_from_food_to_tail = []
    current_tile = snake.food

    

    while (True):

        next_tile = hamiltonian_cycle[current_tile] + current_tile
      

        current_tile = next_tile
        if (current_tile == snake.tail):
            break
        
        path_from_food_to_tail.append(next_tile) 

    return path_from_food_to_tail


 


def improveSnakesHamiltonianCycle():
    global snakes_hamiltonian_cycle
    
    if snake.head + snakes_hamiltonian_cycle[snake.head] == snake.food:
        return # maybe dont need this

    path_to_food = generatePathToFood(snakes_hamiltonian_cycle) 
    #print(path_to_food)
    #print(f"{snake.food=}")

    candidates = []
    # THIS MIGHT NEED SOME MORE TESTING IN ORDR TO MAKE SURE THAT IT FIND ALL -> POSSIBLE <- canidates as  path_from_food_to_tail cant restrict it

    for tile in path_to_food:
        match snakes_hamiltonian_cycle[tile]:
            case -30: # UP
                edge_tile = tile + RIGHT + UP  
                if edge_tile in grid and snakes_hamiltonian_cycle[edge_tile] == DOWN and edge_tile in path_to_food and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                    candidates.append((tile, edge_tile))

            case 30: # DOWN
                edge_tile = tile + RIGHT + DOWN 
                if edge_tile in grid and snakes_hamiltonian_cycle[edge_tile] == UP and edge_tile in path_to_food and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                    candidates.append((tile, edge_tile))                
            
            case 1: # RIGHT
                edge_tile = tile + DOWN + RIGHT # changing this from down to up works
                if edge_tile in grid and snakes_hamiltonian_cycle[edge_tile] == LEFT and edge_tile in path_to_food and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                    candidates.append((tile, edge_tile))        

            case -1: # LEFT
                edge_tile = tile + DOWN + LEFT # changing this from down to up works
                if edge_tile in grid and snakes_hamiltonian_cycle[edge_tile] == RIGHT and edge_tile in path_to_food and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                    candidates.append((tile, edge_tile))


  
    #print(f"{len(candidates)=}")
    
    if len(candidates) == 0:
        return

    # Split it into 2 cycles
    shortcutted_hamiltonian_cycles = []
    for candidate in candidates:
        new_hamiltonian_cycle = copy.deepcopy(snakes_hamiltonian_cycle)
        
        
        tile, edge_tile = candidate
        tile_direction, edge_tile_direction = new_hamiltonian_cycle[tile], new_hamiltonian_cycle[edge_tile]
        
        orientation = tile_direction
        if orientation in [UP, DOWN]:
            edge_tile_x = edge_tile % WIDTH
            tile_x = tile % WIDTH 
            if tile_x < edge_tile_x: 
                tile_direction, edge_tile_direction = RIGHT, LEFT
            else:
                tile_direction, edge_tile_direction = LEFT, RIGHT
        else:
            edge_tile_y = edge_tile // WIDTH 
            tile_y = tile // WIDTH 
            if tile_y < edge_tile_y: # tile[1] < edge_tile[1]
                tile_direction, edge_tile_direction = DOWN, UP
            else:
                tile_direction, edge_tile_direction = UP, DOWN
        new_hamiltonian_cycle[tile] = tile_direction
        new_hamiltonian_cycle[edge_tile] = edge_tile_direction

        #printHamiltonianCycle(new_hamiltonian_cycle)

        # NEXT PART
        path_from_food_to_tail = generateFromFoodToTail(new_hamiltonian_cycle)
        

        new_loop = generateLoop(new_hamiltonian_cycle, candidate[0]) 
        if snake.food in new_loop or snake.head in new_loop or snake.tail in new_loop or any(x in snake.body for x in new_loop):
            new_loop = generateLoop(new_hamiltonian_cycle, candidate[1]) 


        #print(f'{new_loop=}')
        #printHamiltonianCycle(new_hamiltonian_cycle)
        mending_candidates = []
        # THIS MIGHT NEED SOME MORE TESTING IN ORDR TO MAKE SURE THAT IT FIND ALL -> POSSIBLE <- canidates as  path_from_food_to_tail cant restrict it
        for tile in path_from_food_to_tail:
            match new_hamiltonian_cycle[tile]:
                case -30: # UP
                    edge_tile = tile + LEFT + UP
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == DOWN and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))

                    edge_tile = tile + RIGHT + UP
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == DOWN and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))
                               
                case 30: # DOWN
                    edge_tile = tile + LEFT + DOWN
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == UP and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))

                    edge_tile = tile + RIGHT + DOWN
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == UP and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))
               
                case 1: # RIGHT
                    edge_tile = tile + UP + RIGHT
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == LEFT and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))

                    edge_tile = tile + DOWN + RIGHT
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == LEFT and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))

                case -1: # LEFT
                    edge_tile = tile + UP + LEFT 
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == RIGHT and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))

                    edge_tile = tile + DOWN + LEFT
                    if edge_tile in grid and new_hamiltonian_cycle[edge_tile] == RIGHT and edge_tile in new_loop and (abs(edge_tile // WIDTH - tile // WIDTH) == 1):
                        mending_candidates.append((tile, edge_tile))


        # Make it one whole cycle again            
        if len(mending_candidates) == 0:
            continue
        #print(f"{mending_candidates=}")
        
        for mending_candidate in mending_candidates:
            shortcutted_hamiltonian_cycle = copy.deepcopy(new_hamiltonian_cycle)

            tile, edge_tile = mending_candidate
            tile_direction, edge_tile_direction = shortcutted_hamiltonian_cycle[tile], shortcutted_hamiltonian_cycle[edge_tile]
            
            orientation = tile_direction
            if orientation in [UP, DOWN]:
                edge_tile_x = edge_tile % WIDTH
                tile_x = tile % WIDTH 
                
                if tile_x < edge_tile_x:
                    tile_direction, edge_tile_direction = RIGHT, LEFT
                else:
                    tile_direction, edge_tile_direction = LEFT, RIGHT
            else:

                edge_tile_y = edge_tile // WIDTH 
                tile_y = tile // WIDTH 
                if tile_y < edge_tile_y:
                    tile_direction, edge_tile_direction = DOWN, UP
                else:
                    tile_direction, edge_tile_direction = UP, DOWN
            shortcutted_hamiltonian_cycle[tile] = tile_direction
            shortcutted_hamiltonian_cycle[edge_tile] = edge_tile_direction

            shortcutted_hamiltonian_cycles.append(shortcutted_hamiltonian_cycle)
            #printHamiltonianCycle(shortcutted_hamiltonian_cycle)


    # find the shortest one

    shortest_path_length = len(generatePathToFood(snakes_hamiltonian_cycle))
    #print(f"printHamiltonianCycle")
    for shortcutted_hamiltonian_cycle in shortcutted_hamiltonian_cycles:
        if len(generatePathToFood(shortcutted_hamiltonian_cycle)) < shortest_path_length:
            snakes_hamiltonian_cycle = shortcutted_hamiltonian_cycle 

    #print('')
    #print('------------------------------')


#improveSnakesHamiltonianCycle()


def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    snake.generateNewFood()
    printSnake()

    steps = 0
    while len(snake.body) != (HEIGHT * WIDTH - 2):
        

        #sleep(0.05)
        
        snake.changeDirection(snakes_hamiltonian_cycle[snake.head])
        snake.move()
        steps = steps + 1


        if (snake.head) == snake.food:
            snake.generateNewFood()
            snake.grow()
        
        last_snakes_hamiltonian_cycle = []
        while (last_snakes_hamiltonian_cycle != snakes_hamiltonian_cycle):
            last_snakes_hamiltonian_cycle = snakes_hamiltonian_cycle
            improveSnakesHamiltonianCycle()   
                      
        
       
        os.system('cls' if os.name == 'nt' else 'clear')

        #printSnake()
        printHamiltonianCycle(snakes_hamiltonian_cycle)
        #distance_to_food = len(generatePathToFood(snakes_hamiltonian_cycle))
        print(f"Total Steps: {steps}")
    
    print(f"Total Steps: {steps}")







main()

# FASTEST 58454
# NEW FASTEST 56637
        
# thanks to https://stackoverflow.com/questions/7371227/algorithm-to-find-a-random-hamiltonian-path-in-a-grid
        
