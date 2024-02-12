import pygame
from random import randint
import sys
from maze import maze, solution, start_position, end_position

class Colors:
    WHITE = pygame.Color(255, 255, 255, 255)
    BLACK = pygame.Color(0, 0, 0, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    FADED_RED = pygame.Color(255, 100, 100)
    GREY = pygame.Color(140, 135, 132)
    BACKGROUND = WHITE
    FOREGROUND = BLACK

    @staticmethod
    def random_color():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

class Settings(Colors):
    SCREEN_WIDTH = 990
    SCREEN_HEIGHT = 990
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    GRID_SIZE = int(SCREEN_WIDTH / len(maze))
    MAX_ROWS = int(SCREEN_HEIGHT / GRID_SIZE)
    MAX_COLS = int(SCREEN_WIDTH / GRID_SIZE)
    FPS = 60
    INIT_POS = start_position

class BFSVisualizer(Settings):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(Settings.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
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
                    0, 1
                )
    
    def generate_maze(self):
        for row in range(Settings.MAX_ROWS):
            for col in range(Settings.MAX_COLS):
                if maze[row][col] == 1:
                    self.grid[row][col] = self.FOREGROUND
                else:
                    self.grid[row][col] = self.FADED_RED

    def BFS(self):
        queue = [Settings.INIT_POS]

        while len(queue) > 0:
            curr_x, curr_y = queue.pop(0)
            if self.grid[curr_x][curr_y] != Settings.FOREGROUND:
                continue
            self.grid[curr_x][curr_y] = Settings.GREY
            if curr_x == end_position[0] and curr_y == end_position[1]:
                self.grid_iterator = None
                return
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
            if solution == None:
                return
            for i in range(len(solution) - 1):
                pygame.draw.line(
                    self.screen,
                    "blue",
                    (
                        solution[i][1] * Settings.GRID_SIZE + Settings.GRID_SIZE // 2, 
                        solution[i][0] * Settings.GRID_SIZE+ Settings.GRID_SIZE // 2
                    ),
                    (
                        solution[i+1][1] * Settings.GRID_SIZE + Settings.GRID_SIZE // 2, 
                        solution[i+1][0] * Settings.GRID_SIZE + Settings.GRID_SIZE // 2),
                    10
                )
        start_rect = (start_position[1] * Settings.GRID_SIZE, start_position[0] * Settings.GRID_SIZE, Settings.GRID_SIZE, Settings.GRID_SIZE)
        end_rect = (end_position[1] * Settings.GRID_SIZE, end_position[0] * Settings.GRID_SIZE, Settings.GRID_SIZE, Settings.GRID_SIZE)
        pygame.draw.rect(self.screen, Settings.GREEN, start_rect, 0, 50)
        pygame.draw.rect(self.screen, Settings.GREEN, end_rect, 0, 50)

    def run(self):
        while True:
            self.clock.tick(Settings.FPS)
            self.handle_events()
            self.update()
            pygame.display.update()


if __name__ == "__main__":
    visualizer = BFSVisualizer()
    visualizer.run()