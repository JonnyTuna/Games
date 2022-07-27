import random
import pygame
import os

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("2048")

FPS = 60
VEL = 120
WIDTH, HEIGHT = 480, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))
BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Buttons', 'menu.png')), (50, 50))
PLAY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Buttons', 'play.png')), (200, 150))
ICON2048 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Buttons', '2048_icon.png')), (200, 200))

MAIN_FONT = pygame.font.SysFont('comicsans', 30)
MAIN_FONT_BIGGER = pygame.font.SysFont('comicsans', 80)
MAIN_FONT_MEDIUM = pygame.font.SysFont('comicsans', 60)

T2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '2.png')), (120, 120))
T4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '4.png')), (120, 120))
T8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '8.png')), (120, 120))
T16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '16.png')), (120, 120))
T32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '32.png')), (120, 120))
T64 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '64.png')), (120, 120))
T128 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '128.png')), (120, 120))
T256 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '256.png')), (120, 120))
T512 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '512.png')), (120, 120))
T1024 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '1024.png')), (120, 120))
T2048 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '2048.png')), (120, 120))
T4096 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '4096.png')), (120, 120))
T8192 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '8192.png')), (120, 120))
T16384 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '16384.png')), (120, 120))
T32768 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiles', '32768.png')), (120, 120))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)

class Tile(object):
    def __init__(self, value, position, image):
        self.value = value
        self.position = position
        self.image = image

available_squares = []
tiles_on_board = []
global tile_moved
tile_moved = 0

def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BUTTON, (10, 490))
    pygame.display.update()

def start_game():
    draw_position_x = 0
    draw_position_y = 0
    for i in range(4):
        for i in range(4):
            pygame.draw.rect(WIN, GREY, pygame.Rect(draw_position_x, draw_position_y, 120, 120))
            available_squares.append(pygame.Rect(draw_position_x, draw_position_y, 120, 120))
            draw_position_x += 120
        draw_position_x = 0
        draw_position_y += 120
    for i in range(2):
        next_spawn_square = available_squares[random.randint(1, len(available_squares) - 1)]
        tile = Tile(2, pygame.Rect(next_spawn_square), T2)
        tiles_on_board.append(tile)
        available_squares.remove(next_spawn_square)
        WIN.blit(T2, next_spawn_square)

def spawn_new_tile():
    possible_squares = []
    x = 0
    y = 0
    for i in range(4):
        for i in range(4):
            possible_squares.append(pygame.Rect(x, y, 120, 120))
            x += 120
        x = 0
        y += 120
    for potential_square in tiles_on_board:
        try:
            possible_squares.remove(pygame.Rect(potential_square.position.x, potential_square.position.y, 120, 120))
        except:
            None
    random_number = random.randint(1, 10)
    print(random_number)
    if random_number < 10:
        next_spawn_square = possible_squares[random.randint(0, len(possible_squares) - 1)]
        tile = Tile(2, pygame.Rect(next_spawn_square), T2)
        tiles_on_board.append(tile)
        WIN.blit(T2, next_spawn_square)
    if random_number == 10:
        next_spawn_square = possible_squares[random.randint(0, len(possible_squares) - 1)]
        tile = Tile(4, pygame.Rect(next_spawn_square), T4)
        tiles_on_board.append(tile)
        WIN.blit(T4, next_spawn_square)

def check_for_loss():
    possible_to_move = False
    game_over = False
    if len(tiles_on_board) == 16:
        for tile in tiles_on_board:
            for other_tile in tiles_on_board:
                if tile.value == other_tile.value:
                    if tile.position.y == other_tile.position.y:
                        if tile.position.x + 120 == other_tile.position.x or tile.position.x - 120 == other_tile.position.x:
                            possible_to_move = True
                            game_over = False
                    if tile.position.x == other_tile.position.x:
                        if tile.position.y + 120 == other_tile.position.y or tile.position.y - 120 == other_tile.position.y:
                            possible_to_move = True
                            game_over = False
        if not possible_to_move:
            end_game()
            game_over = True
    return game_over

def end_game():
    draw_text = MAIN_FONT_MEDIUM.render("GAME OVER", 1, RED)
    WIN.blit(draw_text, (50, 180))
    draw_text = MAIN_FONT.render("click anywhere to exit", 1, WHITE)
    WIN.blit(draw_text, (90, 300))
    pygame.display.update()

def wait_for_KEYUP():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False

def wait_for_KEYDOWN():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False

def wait_for_MOUSEUP():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                waiting = False

def wait_for_MOUSEDOWN():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def redraw_board():
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, GREY, pygame.Rect(0, 0, 480, 480))
    WIN.blit(BUTTON, (10, 490))
    WIN.blit(MAIN_FONT.render('Score:', 1, WHITE), (290, 510))
    WIN.blit(MAIN_FONT.render('Highscore: ', 1, WHITE), (231, 475))
    pygame.display.update()
    for tile in tiles_on_board:
        WIN.blit(tile.image, pygame.Rect(tile.position.x, tile.position.y, 120, 120))
        pygame.display.update()

def draw_menu():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BUTTON, (10, 490))
    WIN.blit(MAIN_FONT_BIGGER.render('MENU', 1, WHITE), (110, -15))
    WIN.blit(ICON2048, (140, 100))
    WIN.blit(PLAY_BUTTON, (140, 330))
    pygame.display.update()

def check_highest_tile():
    highest_tile = 2
    for tile in tiles_on_board:
        if tile.value > highest_tile:
            highest_tile = tile.value
    return highest_tile

def display_win():
    draw_text = MAIN_FONT_BIGGER.render("YOU WIN!", 1, GREEN)
    WIN.blit(draw_text, (50, 180))
    pygame.display.update()

def update_score():
    #Score
    score = 0
    for tile in tiles_on_board:
        score += tile.value
    score_text = str(score)
    draw_text = MAIN_FONT.render(score_text, 1, WHITE)
    WIN.blit(draw_text, (390, 510))
    pygame.display.update()
    return score

def update_highscore(score):
    file = open('Highscore.txt', 'r')
    f = file.readlines()
    lines = []
    for line in f:
        if line[-1] == "\n":
            lines.append(line[:-1])
        else:
            lines.append(line)
    highscore = int(lines[0])
    if int(lines[0]) <= score:
        highscore = score
        file = open('Highscore.txt', 'w')
        file.write(str(highscore))
        file.close()
    WIN.blit(MAIN_FONT.render(str(highscore), 1, WHITE), (390, 475))
    pygame.display.update()
    return highscore

def combine_value(tile):
    combined_value = tile.value*2
    if combined_value == 4:
        image = T4
    if combined_value == 8:
        image = T8
    if combined_value == 16:
        image = T16
    if combined_value == 32:
        image = T32
    if combined_value == 64:
        image = T64
    if combined_value == 128:
        image = T128
    if combined_value == 256:
        image = T256
    if combined_value == 512:
        image = T512
    if combined_value == 1024:
        image = T1024
    if combined_value == 2048:
        image = T2048
    if combined_value == 4096:
        image = T4096
    if combined_value == 8192:
        image = T8192
    if combined_value == 16384:
        image = T16384
    if combined_value == 32768:
        image = T32768
    return image

def handle_movement(keys_pressed):
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        wait_for_KEYUP()
        ordered_tiles = []
        search_x = 360
        search_y = 0
        for i in range(4):
            for i in range(4):
                for tile in tiles_on_board:
                    if tile.position.x == search_x and tile.position.y == search_y:
                        ordered_tiles.append(tile)
                search_y += 120
            search_y = 0
            search_x -= 120
        # Move tiles
        for i in range(4):
            tiles_to_collide = []
            position_to_move = 360
            for i in range(4):
                if tile.position.x == position_to_move:
                    for tile in ordered_tiles:
                        clear_to_move = True
                        for square in tiles_on_board:
                            if tile.position.x == 360:
                                clear_to_move = False
                            elif tile.position.x + 120 == square.position.x and tile.position.y == square.position.y:
                                clear_to_move = False
                                if tile.value == square.value and tile.position.x + 120 == square.position.x:
                                    tiles_to_collide.append(tile)

                        if clear_to_move:
                            try:
                                tiles_on_board.remove(tile)
                            except:
                                None
                            tile.position.x += 120
                            tiles_on_board.append(tile)
                            WIN.blit(tile.image, (tile.position.x, tile.position.y))

                    for tile in tiles_to_collide:
                        for each_tile in tiles_to_collide:
                            if each_tile.position.x == tile.position.x and each_tile.position.y == tile.position.y:
                                tiles_to_collide.remove(each_tile)
                        try:
                            tiles_on_board.remove(tile)
                        except:
                            None
                        for square in tiles_on_board:
                            if tile.position.y == square.position.y and tile.position.x + 120 == square.position.x:
                                tiles_on_board.remove(square)
                        tile.image = combine_value(tile)
                        tile.value = tile.value * 2
                        tile.position = pygame.Rect(tile.position.x, tile.position.y, 120, 120)
                        tile.position.x += 120
                        tiles_on_board.append(tile)
                        WIN.blit(tile.image, (tile.position.x, tile.position.y))
                position_to_move -= 120

    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        wait_for_KEYUP()
        ordered_tiles = []
        search_x = 0
        search_y = 0
        for i in range(4):
            for i in range(4):
                for tile in tiles_on_board:
                    if tile.position.x == search_x and tile.position.y == search_y:
                        ordered_tiles.append(tile)
                search_y += 120
            search_y = 0
            search_x += 120
        # Move tiles
        for i in range(4):
            tiles_to_collide = []
            position_to_move = 0
            for i in range(4):
                if tile.position.x == position_to_move:
                    for tile in ordered_tiles:
                        clear_to_move = True
                        for square in tiles_on_board:
                            if tile.position.x == 0:
                                clear_to_move = False
                            elif tile.position.x - 120 == square.position.x and tile.position.y == square.position.y:
                                clear_to_move = False
                                if tile.value == square.value and tile.position.x - 120 == square.position.x:
                                    tiles_to_collide.append(tile)

                        if clear_to_move:
                            try:
                                tiles_on_board.remove(tile)
                            except:
                                None
                            tile.position.x -= 120
                            tiles_on_board.append(tile)
                            WIN.blit(tile.image, (tile.position.x, tile.position.y))

                    for tile in tiles_to_collide:
                        for each_tile in tiles_to_collide:
                            if each_tile.position.x == tile.position.x and each_tile.position.y == tile.position.y:
                                tiles_to_collide.remove(each_tile)
                        try:
                            tiles_on_board.remove(tile)
                        except:
                            None
                        for square in tiles_on_board:
                            if tile.position.y == square.position.y and tile.position.x - 120 == square.position.x:
                                tiles_on_board.remove(square)
                        tile.image = combine_value(tile)
                        tile.value = tile.value * 2
                        tile.position = pygame.Rect(tile.position.x, tile.position.y, 120, 120)
                        tile.position.x -= 120
                        tiles_on_board.append(tile)
                        WIN.blit(tile.image, (tile.position.x, tile.position.y))
                position_to_move += 120

    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        wait_for_KEYUP()
        ordered_tiles = []
        search_x = 0
        search_y = 0
        for i in range(4):
            for i in range(4):
                for tile in tiles_on_board:
                    if tile.position.x == search_x and tile.position.y == search_y:
                        ordered_tiles.append(tile)
                search_x += 120
            search_x = 0
            search_y += 120
        # Move tiles
        for i in range(4):
            tiles_to_collide = []
            position_to_move = 0
            for i in range(4):
                if tile.position.y == position_to_move:
                    for tile in ordered_tiles:
                        clear_to_move = True
                        for square in tiles_on_board:
                            if tile.position.y == 0:
                                clear_to_move = False
                            elif tile.position.y - 120 == square.position.y and tile.position.x == square.position.x:
                                clear_to_move = False
                                if tile.value == square.value and tile.position.y - 120 == square.position.y:
                                    tiles_to_collide.append(tile)

                        if clear_to_move:
                            try:
                                tiles_on_board.remove(tile)
                            except:
                                None
                            tile.position.y -= 120
                            tiles_on_board.append(tile)
                            WIN.blit(tile.image, (tile.position.x, tile.position.y))

                    for tile in tiles_to_collide:
                        for each_tile in tiles_to_collide:
                            if each_tile.position.x == tile.position.x and each_tile.position.y == tile.position.y:
                                tiles_to_collide.remove(each_tile)
                        try:
                            tiles_on_board.remove(tile)
                        except:
                            None
                        for square in tiles_on_board:
                            if tile.position.x == square.position.x and tile.position.y - 120 == square.position.y:
                                tiles_on_board.remove(square)
                        tile.image = combine_value(tile)
                        tile.value = tile.value * 2
                        tile.position = pygame.Rect(tile.position.x, tile.position.y, 120, 120)
                        tile.position.y -= 120
                        tiles_on_board.append(tile)
                        WIN.blit(tile.image, (tile.position.x, tile.position.y))
                position_to_move += 120

    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
        wait_for_KEYUP()
        ordered_tiles = []
        search_x = 0
        search_y = 360
        for i in range(4):
            for i in range(4):
                for tile in tiles_on_board:
                    if tile.position.x == search_x and tile.position.y == search_y:
                        ordered_tiles.append(tile)
                search_x += 120
            search_x = 0
            search_y -= 120
        # Move tiles
        for i in range(4):
            tiles_to_collide = []
            position_to_move = 360
            for i in range(4):
                if tile.position.y == position_to_move:
                    for tile in ordered_tiles:
                        clear_to_move = True
                        for square in tiles_on_board:
                            if tile.position.y == 360:
                                clear_to_move = False
                            elif tile.position.y + 120 == square.position.y and tile.position.x == square.position.x:
                                clear_to_move = False
                                if tile.value == square.value and tile.position.y + 120 == square.position.y:
                                    tiles_to_collide.append(tile)

                        if clear_to_move:
                            try:
                                tiles_on_board.remove(tile)
                            except:
                                None
                            tile.position.y += 120
                            tiles_on_board.append(tile)
                            WIN.blit(tile.image, (tile.position.x, tile.position.y))

                    for tile in tiles_to_collide:
                        for each_tile in tiles_to_collide:
                            if each_tile.position.x == tile.position.x and each_tile.position.y == tile.position.y:
                                tiles_to_collide.remove(each_tile)
                        try:
                            tiles_on_board.remove(tile)
                        except:
                            None
                        for square in tiles_on_board:
                            if tile.position.x == square.position.x and tile.position.y + 120 == square.position.y:
                                tiles_on_board.remove(square)
                        tile.image = combine_value(tile)
                        tile.value = tile.value * 2
                        tile.position = pygame.Rect(tile.position.x, tile.position.y, 120, 120)
                        tile.position.y += 120
                        tiles_on_board.append(tile)
                        WIN.blit(tile.image, (tile.position.x, tile.position.y))
                position_to_move -= 120

    if keys_pressed[pygame.K_SPACE]:
        wait_for_KEYUP()
        for tile in tiles_on_board:
            print("Tile of value: "+str(tile.value)+" at x = "+str(tile.position.x)+", y = "+str(tile.position.y))

# MAIN
draw_window()
start_game()
pygame.display.update()
clock = pygame.time.Clock()
redraw_board()
run = True
menu_open = True
has_won = False
mouse_moved = False
game_over = False
while run:
    clock.tick(FPS)
    mouse = pygame.mouse.get_pos()
    highest_tile = check_highest_tile()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if not menu_open:
            if not game_over:
                check_for_loss()
                game_over = check_for_loss()
                tiles_before = []
                tiles_after = []
                for tile in tiles_on_board:
                    tiles_before.append(tile.position.x)
                    tiles_before.append(tile.position.y)
                keys_pressed = pygame.key.get_pressed()
                handle_movement(keys_pressed)
                if event.type == pygame.KEYDOWN:
                    for tile in tiles_on_board:
                        tiles_after.append(tile.position.x)
                        tiles_after.append(tile.position.y)
                    if tiles_before != tiles_after:
                        spawn_new_tile()
                        redraw_board()
                        score = update_score()
                        update_highscore(score)
                        highscore = update_highscore(score)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] >= 10 and mouse[0] <= 60 and mouse[1] >=490 and mouse[1] <=540:
                        menu_open = True
            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_open = True
                    game_over = False


    if menu_open:
        draw_menu()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_moved = True
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_moved:
            if mouse[0] >= 10 and mouse[0] <= 60 and mouse[1] >=490 and mouse[1] <=540:
                redraw_board()
                menu_open = False
                mouse_moved = False
            if mouse[0] >= 140 and mouse[0] <= 340 and mouse[1] >= 330 and mouse[1] <= 480:
                tiles_on_board = []
                draw_window()
                start_game()
                pygame.display.update()
                clock = pygame.time.Clock()
                redraw_board()
                has_won = False
                mouse_moved = False
                menu_open = False
                game_over = False

    if not has_won and highest_tile == 2048:
        display_win()
        has_won = True

