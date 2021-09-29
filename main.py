import random
import pygame


class grid:
    def __init__(self, size=100, window_size=800) -> None:
        if 0 < size <= 200:
            self.size = size
        else:
            self.size = 100
        self.array = [[0] * size for _ in range(size)]
        self.window_size = window_size
        self.tile_size = window_size // size
        pygame.display.set_caption("Game of Life")
        self.window = pygame.display.set_mode((window_size, window_size))

    def generate_random(self, p=0.5) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.array[i][j] = 1 if random.uniform(0, 1) < p else 0

    def set_window_size(self, window_size):
        self.window_size = window_size

    def get_window_size(self):
        return self.window_size

    def set_window(self, window):
        self.window = window

    def get_window(self):
        return self.window

    def set_grid(self, array):
        self.array = array

    def get_grid(self) -> list:
        return self.array

    def set_tile(self, row, col, val) -> None:
        self.array[row][col] = val

    def get_tile(self, row, col) -> int:
        return self.array[row][col]

    def get_living_neighbours_count(self, row, col) -> int:
        left = col - 1 if col > 0 else self.size - 1
        right = col + 1 if col < self.size - 1 else 0
        top = row - 1 if row > 0 else self.size - 1
        bottom = row + 1 if row < self.size - 1 else 0
        total = 0
        total += self.array[row][left]
        total += self.array[row][right]
        total += self.array[top][col]
        total += self.array[bottom][col]
        total += self.array[top][left]
        total += self.array[top][right]
        total += self.array[bottom][left]
        total += self.array[bottom][right]
        return total

    def get_total_living(self) -> int:
        total = 0
        for row in self.array:
            total += sum(row)
        return total

    def print_grid(self) -> None:
        for row in self.array:
            print(row)

    def next_period(self) -> int:
        tmp = []
        total = 0
        for i in range(0, self.size):
            tmp.append([0] * self.size)
        for i in range(0, self.size):
            for j in range(0, self.size):
                tmp[i][j] = self.get_living_neighbours_count(i, j)
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.array[i][j] = 1 if tmp[i][j] == 3 or (self.array[i][j] == 1 and tmp[i][j] == 2) else 0
                total += self.array[i][j]
        return total

    def redraw(self):
        self.window.fill((255, 255, 255))
        for idy, row in enumerate(self.array):
            for idx, cell in enumerate(row):
                left = idx * self.tile_size
                top = idy * self.tile_size
                pygame.draw.rect(self.window,
                                 (0, 0, 0) if not cell else (0, 255, 0),
                                 pygame.Rect(left, top, self.tile_size,
                                 self.tile_size))
        pygame.display.update()

    def run(self, n=None) -> None:
        if not n:
            play = True
            while play:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break
                self.redraw()
                if self.next_period() == 0:
                    break

        else:
            for _ in range(0, n):
                self.redraw()
                if self.next_period() == 0:
                    break


def main() -> None:
    g = grid(200, 800)
    g.generate_random()
    g.run()


if __name__ == '__main__':
    main()
