# * * * The N Queens Problem * * *

class Square():
    def __init__(self, occupied=False):
        self.__occupied = occupied

    @property
    def occupied(self):
        return self.__occupied
    @occupied.setter
    def occupied(self, value):
        self.__occupied = value

    def __str__(self):
        if self.occupied == True:
            return "Q|"
        else:
            return " |"

# Board[row][col]
class Board():
    def __init__(self,n):
        self.n = n
        self.queensFound = 0
        self.board = [[Square(False) for col in range(n)] for row in range(n)]

    def solve(self, row=0):
        for col in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col].occupied = True
                if row+1 == self.n:
                    self.printBoard()
                else:
                    self.solve(row+1)
                self.board[row][col].occupied = False

    def isSafe(self, row, col):
        # diagonal checking directions(M for middle)
        #       1     2     3
        # |row-, col-| |row-, col+|1
        # |          |M|          |2
        # |row+, col-| |row+, col+|3
        def checkDiagonal(self, row, col , Rrow, Ccol):
            r = row + Rrow
            c = col + Ccol
            if Rrow == -1 and Ccol == -1:
                while r >= 0 and c >=0:
                    if self.board[r][c].occupied == True:
                        return False
                    c-=1
                    r-=1
            if Rrow == -1 and Ccol == 1:
                while r >= 0 and c < self.n:
                    if self.board[r][c].occupied == True:
                        return False
                    c+=1
                    r-=1 
            if Rrow == 1 and Ccol == 1:
                while r < self.n and c < self.n:
                    if self.board[r][c].occupied == True:
                        return False
                    c+=1
                    r+=1
            if Rrow == 1 and Ccol == -1:
                while r < self.n and c >= 0:
                    if self.board[r][c].occupied == True:
                        return False
                    c-=1
                    r+=1
            return True


        # checks if Column number 'col' is clear of queens
        for r in range(self.n):
            if self.board[r][col].occupied == True:
                return False
        # checks if Row number 'row' is clear of queens
        for c in range(self.n):
            if self.board[row][c].occupied == True:
                return False
        
        if (checkDiagonal(self, row, col , -1, -1) and checkDiagonal(self, row, col , -1, +1) and 
            checkDiagonal(self, row, col , +1, +1) and checkDiagonal(self, row, col , +1, -1)):
            return True
        return False


    def printBoard(self):
        self.queensFound = self.queensFound + 1
        print('+-' + '--'*self.n + '+')
        print("Solution number:",self.queensFound)

        print(" ",end="")
        for i in range(self.n):
            print(i+1,end=" ")
        print()

        for i in range(self.n):
            print ('|', end="")
            for j in range(self.n):
                print(self.board[i][j], end="")
            print(i+1)
        print('+-' + '--'*self.n + '+\n')

def main():
    # recomended not to choose N larger than 9
    print("* * * The N Queens Problem * * *")
    numOfQueens = int(input("Please enter the num of queens(N): "))
    b = Board(numOfQueens)
    b.solve()
    print("{} Solutions Found!\n".format(b.queensFound))
    input("Press enter to exit\n")

main()