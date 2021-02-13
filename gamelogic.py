import re
import copy
import random


class TicTacToe():
    random.seed()

    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.player_piece = ""
        self.computer_piece = ""
        self.pieces = []
        self.won = False

    def init_variables(self):
        self.columns, self.rows = self.init_dimensions()
        self.player_piece, self.computer_piece = self.request_playpiece()
        self.pieces = self.init_pieces(self.columns, self.rows)

    def init_dimensions(self):
        while True:
            size = input("Please enter the size for your Tic Tac Toe board? e.g. 3 for 3x3 board\n")
            if size.isdigit() and int(size) > 1 and int(size) < 11:
                break
            else:
                print("Please enter an integer between 2 and 10")

        return int(size), int(size)

    def init_pieces(self, columns, rows):
        columns = ["-" for i in range(0, columns)]
        pieces = [copy.copy(columns) for i in range(0, rows)]

        return pieces

    def request_playpiece(self):
        while True:
            playpiece = input("Please enter the character you want to play with, X or O?")
            if playpiece.upper() == 'X':
                return playpiece.upper(), 'O'
            elif playpiece.upper() == 'O':
                return playpiece.upper(), 'X'
            else:
                print('You did not enter the correct character, please try again...')

    def show_board(self):
        print("\n")
        for i in range(0, len(self.pieces)):
            if i > 0:
                print("-" * (((len(self.pieces[0]) - 1) * 4) + 1))
            for j in range(0, len(self.pieces[0])):
                if j > 0:
                    print(" | ", end='')
                print(self.pieces[j][i], end='')
            print("")
        print("\n")

    def player_turn(self):
        pattern = r'^\d{1,2},\d{1,2}$'
        while True:
            coordinates = input("Please enter the coordinates for the field you want to fill? Please use comma seperated row, column, like 1,2.\n")
            coord_match = re.match(pattern, coordinates)
            if coord_match:
                selected_row = int(coordinates.split(',')[0])
                selected_column = int(coordinates.split(',')[1])
            else:
                selected_row = None
                selected_column = None

            if (coord_match and (selected_row > 0) and (selected_row <= len(self.pieces[0])) and
                    (selected_column > 0) and (selected_column <= len(self.pieces)) and
                    (self.pieces[(selected_column - 1)][(selected_row - 1)] == '-')):
                break
            else:
                print("Please enter coordinates that are still empty and exist")
        self.pieces[(selected_column - 1)][(selected_row - 1)] = self.player_piece

    def computer_turn(self):
        open_positions_coords = []
        for i in range(0, len(self.pieces)):
            for j in range(0, len(self.pieces[0])):
                if self.pieces[i][j] == '-':
                    open_positions_coords.append(f'{i + 1},{j + 1}')

        computer_choice = random.randint(0, (len(open_positions_coords) - 1))

        selected_row = int(open_positions_coords[computer_choice].split(',')[0])
        selected_column = int(open_positions_coords[computer_choice].split(',')[1])

        self.pieces[(selected_column - 1)][(selected_row - 1)] = self.computer_piece

        print("The computer has made a move...")

        return

    def game_end(self):
        winner = self.check_if_winner()
        if (sum(sl.count('-') for sl in self.pieces) == 0):
            print("There are no more possibilities, the game has ended")
            return True
        elif winner != "":
            print(f"The winner is player {winner}")
            return True
        else:
            return False

    def check_if_winner(self):
        player_won = ''

        # Check all columns for vertical matches
        for i in range(0, (self.columns)):
            check = ''
            for j in range(0, (self.rows)):
                if j == 0:
                    check = self.pieces[j][i]
                elif self.pieces[j][i] == check and check != '-':
                    if j == (self.rows - 1):
                        self.won = True
                        player_won = check
                    continue
                else:
                    break

        # Check all rows for horizontal matches
        for i in range(0, (self.rows)):
            check = ''
            for j in range(0, (self.columns)):
                if j == 0:
                    check = self.pieces[i][j]
                elif self.pieces[i][j] == check and check != '-':
                    if j == (self.columns - 1):
                        self.won = True
                        player_won = check
                    continue
                else:
                    break

        # Check all diagonals for matches
        for i in range(0, (self.rows)):
            if i == 0:
                column = self.columns - 1
                check = self.pieces[i][column]
            elif self.pieces[i][column] == check and check != '-':
                if i == (self.rows - 1):
                    self.won = True
                    player_won = check
                column -= 1
                continue
            else:
                break

            column -= 1

        for i in range(0, (self.columns)):
            if i == 0:
                row = 0
                check = self.pieces[row][i]
            elif self.pieces[row][i] == check and check != '-':
                if i == (self.columns - 1):
                    self.won = True
                    player_won = check
                row += 1
                continue
            else:
                break

            row += 1

        if self.won is True:
            return player_won
        else:
            return ''

    def restart_game(self):
        while True:
            restart = input('Do you want to play another game? (Y/N)')
            if restart.upper() == 'Y':
                return True
            elif restart.upper() == 'N':
                return False
            else:
                print('You did not enter the correct character, please try again...')

    def start_game(self):
        print("\n")
        print(f"You will play with {self.player_piece}, the computer plays with {self.computer_piece}")

        self.show_board()
        while True:
            self.player_turn()
            self.show_board()

            if self.game_end():
                break

            self.computer_turn()
            self.show_board()

            if self.game_end():
                break
