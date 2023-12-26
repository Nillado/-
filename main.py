import pygame

BACKGROUND = (0, 0, 0)

pygame.init()

window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


my_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 3, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1,1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1,1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1,1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1] ]


class Area():

    def __init__(self, x=0, y=0, width = 5, height = 5, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = BACKGROUND
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def outline(self, window, outline_color, outline_width):
        pygame.draw.rect(window, outline_color, self.rect, outline_width)
    def fill(self, window):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):

    def __init__(self, filename, x=0, y=0, width=5, height=5):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self, window):
        self.fill(window)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def change(self, new_image):
        self.image = pygame.image.load(new_image)


class Label(Area):

    def set_text(self, text=" ", fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, window, shift_x=0, shift_y=0):
        self.fill(window)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


board_game = []

y = 0
for i in range(12):
    board_game.append([])
    x = 5
    for j in range(20):
        if my_array[i][j] == 1:
            block = Label(x, y, 40, 40, (0, 255, 0))
            block.set_text('')
            board_game[i].append(block)
        x += 41
    y += 41

def start_game():

    pacman = Picture("images/pacman_1.png", 250, 300, 58, 58)

    prizrak_1 = Picture("images/prizrak1.png", 650, 340, 58, 58)
    prizrak_2 = Picture("images/prizrak2.png", 450, 330, 58, 58)
    prizrak_3 = Picture("images/prizrak3.png", 250, 380, 58, 58)

    pr1_move = "right"
    pr2_move = "up"
    pr3_move = "right"

    flipped = pygame.transform.flip(pacman.image, True, False)

    coin_1 = Picture("images/coin.png", 330, 340, 58, 58)
    coin_2 = Picture("images/coin.png", 150, 340, 58, 58)
    coin_3 = Picture("images/coin.png", 200, 300, 58, 58)
    coin_4 = Picture("images/coin.png", 500, 120, 58, 58)
    coin_5 = Picture("images/coin.png", 450, 280, 58, 58)
    coin_6 = Picture("images/coin.png", 330, 600, 58, 58)
    coin_7 = Picture("images/coin.png", 100, 530, 58, 58)

    coins = [coin_1, coin_2, coin_3, coin_4, coin_5, coin_6, coin_7]

    side_pacman = 'right'

    lose = False

    win = False

    wall = False

    move_l, move_r, move_u, move_d = False, False, False, False

    while True:

        window.fill(BACKGROUND)

        for i in range(len(board_game)):
            for j in range(len(board_game[i])):
                board_game[i][j].draw(window)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN and lose == False:

                if event.key == pygame.K_d:
                    move_r = True
                    side_pacman = 'right'

                if event.key == pygame.K_a:
                    move_l = True
                    side_pacman = 'left'

                if event.key == pygame.K_w:
                    move_u = True

                if event.key == pygame.K_s:
                    move_d = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    move_r = False

                if event.key == pygame.K_a:
                    move_l = False

                if event.key == pygame.K_w:
                    move_u = False

                if event.key == pygame.K_s:
                    move_d = False

        if move_r == True:
            pacman.rect.x += 5

        if side_pacman == 'left':
            pacman.image = flipped

        if side_pacman == 'right':
            pacman.image = pygame.image.load("images/pacman_1.png")

        if move_l == True:
            pacman.rect.x -= 5

        if move_u == True:
            pacman.rect.y -= 5

        if move_d == True:
            pacman.rect.y += 5

        for i in range(len(board_game)):
            for j in range(len(board_game[i])):
                if move_r == True and board_game[i][j].colliderect(pacman):
                    pacman.rect.x -= 5
                if move_l == True and board_game[i][j].colliderect(pacman):
                    pacman.rect.x += 5
                if move_d == True and board_game[i][j].colliderect(pacman):
                    pacman.rect.y -= 5
                if move_u == True and board_game[i][j].colliderect(pacman):
                    pacman.rect.y += 5
        
        pacman.draw(window)

        prizrak_1.draw(window)

        if pr1_move == 'left':
            if prizrak_1.rect.x > 610:
                prizrak_1.rect.x -= 3
            else:
                pr1_move = 'right'

        if pr1_move == 'right':
            if prizrak_1.rect.x < 850:
                prizrak_1.rect.x += 3
            else:
                pr1_move = 'left'

        if prizrak_1.colliderect(pacman):
            lose = True

        prizrak_2.draw(window)
        if pr2_move == 'up':
            if prizrak_2.rect.y > 100:
                prizrak_2.rect.y -= 3
            else:
                pr2_move = 'down'

        if pr2_move == 'down':
            if prizrak_2.rect.y < 650:
                prizrak_2.rect.y += 3
            else:
                pr2_move = 'up'

        if prizrak_2.colliderect(pacman):
            lose = True

        prizrak_3.draw(window)

        if pr3_move == 'left':
            if prizrak_3.rect.x > 120:
                prizrak_3.rect.x -= 3
            else:
                pr3_move = 'right'

        if pr3_move == 'right':
            if prizrak_3.rect.x < 350:
                prizrak_3.rect.x += 3
            else:
                pr3_move = 'left'

        if prizrak_3.colliderect(pacman):
            lose = True

        if lose == True:
            lose_t = Label(200, 200, 0, 0)
            lose_t.set_text("YOU LOSE!", 55, (255, 0, 0))
            lose_t.draw(window)

        for coin in coins:
            coin.draw(window)
            if coin.colliderect(pacman.rect):
                coin.fill(window)
                coins.remove(coin)

        if len(coins) == 0:
            lose_t = Label(200, 200, 0, 0)
            lose_t.set_text("YOU WIN!", 55, (0, 255, 0))
            lose_t.draw(window)

        pygame.display.update()
        clock.tick(60)

start_game()