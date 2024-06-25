from window import Window,Line,Point
from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win=win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0,0)
        self._reset_cells_visited()

        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls(self,i,j):
        self._cells[i][j]._visited = True
        while True:
            unvisited = []

            if (i>0 and self._cells[i-1][j]._visited==False):
                unvisited.append((i-1,j))
            if (i<self._num_cols-1 and self._cells[i+1][j]._visited==False):
                unvisited.append((i+1,j))
            if (j>0 and self._cells[i][j-1]._visited==False):
                unvisited.append((i,j-1))
            if (j<self._num_rows-1 and self._cells[i][j+1]._visited==False):
                unvisited.append((i,j+1))

            if (unvisited==[]):
                self._draw_cell(i,j)
                return
            
            visit = unvisited[random.randint(0,len(unvisited)-1)]

            if (visit[0]==i-1):
                self._cells[i][j].has_left_wall=False
                self._cells[i-1][j].has_right_wall=False
            if (visit[0]==i+1):
                self._cells[i][j].has_right_wall=False
                self._cells[i+1][j].has_left_wall=False
            if (visit[1]==j+1):
                self._cells[i][j].has_bottom_wall=False
                self._cells[i][j+1].has_top_wall=False
            if (visit[1]==j-1):
                self._cells[i][j].has_top_wall=False
                self._cells[i][j-1].has_bottom_wall=False
            
            self._break_walls(visit[0],visit[1])
    
    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j._visited = False

    def _solve_dfs(self, i, j):
        self._animate()

        self._cells[i][j]._visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_dfs(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_dfs(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_dfs(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_dfs(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
    
    def solve(self):
        return self._solve_dfs(0,0)