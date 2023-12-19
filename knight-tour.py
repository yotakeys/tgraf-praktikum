
class KnightTour:
    n = 8
    iters = 0
    starting_point_x = 0
    starting_point_y = 0

    closed_tour = False
    end_point_x = 0
    end_point_y = 0

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def __init__(self, n, starting_point_x=0, starting_point_y=0, closed_tour=False, end_point_x=7, end_point_y=0):
        self.n = n
        self.starting_point_x = starting_point_x
        self.starting_point_y = starting_point_y
        self.end_point_x = end_point_x
        self.end_point_y = end_point_y
        self.closed_tour = closed_tour

    def is_available(self, x, y, board, pos):
        if (x >= 0 and y >= 0 and x < self.n and y < self.n and board[x][y] == -1):
            if (pos == (self.n**2 - 1) and self.closed_tour == True):
                if (x != self.end_point_x or y != self.end_point_y):
                    return False
            return True
        return False

    def print_solution(self, board):
        print("Iterations: ", self.iters)
        print("Solution: ")
        for i in range(self.n):
            for j in range(self.n):
                print(board[i][j], end=' ')
            print()

    def solve_knigh_tour(self):

        board = [[-1 for i in range(self.n)] for i in range(self.n)]
        board[self.starting_point_x][self.starting_point_y] = 0
        pos = 1

        if (not self.knight_tour_util(board, self.starting_point_x, self.starting_point_y, pos)):
            print("Solution does not exist")
        else:
            self.print_solution(board)
            print("Knight Tour Completed")

    def knight_tour_util(self, board, curr_x, curr_y, pos):
        self.iters += 1

        if (pos == self.n**2):
            return True

        for i in range(8):
            new_x = curr_x + self. move_x[i]
            new_y = curr_y + self.move_y[i]

            if (self.is_available(new_x, new_y, board, pos)):
                board[new_x][new_y] = pos
                if (self.knight_tour_util(board, new_x, new_y, pos+1)):
                    return True

                board[new_x][new_y] = -1
        return False


if __name__ == "__main__":
    KT = KnightTour(
        n=8,
        starting_point_x=0,
        starting_point_y=0,
        closed_tour=True,
        end_point_x=0,
        end_point_y=7
    )
    KT.solve_knigh_tour()
