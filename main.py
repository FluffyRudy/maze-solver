import pygame
from random import randint
import sys
from maze import maze, solution

class Colors:
    WHITE = pygame.Color(255, 255, 255, 255)
    BLACK = pygame.Color(0, 0, 0, 255)
    RED = pygame.Color(255, 0, 0)
    LIME = pygame.Color(5, 255, 120)
    BACKGROUND = BLACK
    FOREGROUND = WHITE

    @staticmethod
    def random_color():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

class Settings(Colors):
    SCREEN_WIDTH = 990
    SCREEN_HEIGHT = 990
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    GRID_SIZE = 33
    MAX_ROWS = int(SCREEN_HEIGHT / GRID_SIZE)
    MAX_COLS = int(SCREEN_WIDTH / GRID_SIZE)
    FPS = 60
    INIT_POS = (0, 0)

class BFSVisualizer(Settings):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(Settings.SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        #ui
        self.grid = [[Settings.FOREGROUND for i in range(Settings.MAX_ROWS)] for j in range(Settings.MAX_COLS)]
        self.generate_maze()
        self.grid_iterator = self.BFS()

    def draw_grids(self):
        for row in range(Settings.MAX_ROWS):
            for col in range(Settings.MAX_COLS):
                pygame.draw.rect(
                    self.screen, 
                    self.grid[row][col], 
                    (col * Settings.GRID_SIZE, row * Settings.GRID_SIZE, Settings.GRID_SIZE, Settings.GRID_SIZE),
                    3, 10
                )
    
    def generate_maze(self):
        for row in range(Settings.MAX_ROWS):
            for col in range(Settings.MAX_COLS):
                if maze[row][col] == 1:
                    self.grid[row][col] = self.FOREGROUND
                else:
                    self.grid[row][col] = self.RED

    def BFS(self):
        queue = [Settings.INIT_POS]

        while len(queue) > 0:
            curr_x, curr_y = queue.pop(0)
            if self.grid[curr_x][curr_y] != Settings.FOREGROUND:
                continue
            self.grid[curr_x][curr_y] = Settings.LIME
            if curr_x - 1 >= 0:
                queue.append((curr_x - 1, curr_y))
            if curr_x + 1 < Settings.MAX_COLS:
                queue.append((curr_x + 1, curr_y))
            if curr_y - 1 >= 0:
                queue.append((curr_x, curr_y - 1))
            if curr_y + 1 < Settings.MAX_ROWS:
                queue.append((curr_x, curr_y + 1))
            yield self.grid.copy()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def update(self):
        self.draw_grids()
        try:
            self.grid = next(self.grid_iterator)
        except:
            self.grid_iterator = None
            for path in solution:
                pygame.draw.rect(
                    self.screen,
                    "blue",
                    (path[1] * Settings.GRID_SIZE, path[0] * Settings.GRID_SIZE, Settings.GRID_SIZE, Settings.GRID_SIZE),
                    0, 10
                )
            pygame.draw.rect(self.screen, Settings.RED, (0, 0, Settings.GRID_SIZE, Settings.GRID_SIZE))
            pygame.draw.rect(self.screen, Settings.RED, (29 * Settings.GRID_SIZE, 29 * Settings.GRID_SIZE, Settings.GRID_SIZE, Settings.GRID_SIZE))

    def run(self):
        while True:
            self.clock.tick(Settings.FPS)
            self.handle_events()
            self.update()
            pygame.display.update()


if __name__ == "__main__":
    visualizer = BFSVisualizer()
    visualizer.run()