from window import Window
from maze import Maze
import sys


if __name__=="__main__":
    num_rows = 75
    num_cols = 100
    margin = 10
    screen_x = 960
    screen_y = 540
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win,10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()
