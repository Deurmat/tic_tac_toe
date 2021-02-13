from gamelogic import TicTacToe


def main():
    header = r"""
     ______   __     ______        ______   ______     ______        ______   ______     ______    
    /\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\   
    \/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\   
       \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ 
        \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/ 
    """
    print(header)
    print('Welcome to Tic Tac Toe')

    while True:
        game = TicTacToe()
        game.init_variables()
        game.start_game()

        if game.restart_game():
            print("\n")
            continue
        else:
            print("Thanks for playing Tic Tic Toe, Bye!")
            break


if __name__ == '__main__':
    main()
