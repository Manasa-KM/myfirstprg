import random

print("-----------WELCOME TO GAMEZONE-----------")
print("_____________Select your game____________")
print("           1.GUESSING NUMBER")
print("           2.TIC TAC TOE")
print("           3.Exit")
print("_________________________________________")
aa=1
while aa==1:
    choice = int(input("Enter your choice:\n"))
    if choice==1:
        print("___________________________________________")
        print("____Welcome to the NUMBER GUESSING game____")
        print("_______________Let's start_________________")
        name = input("Enter your name:   ")
        ch = int(input("Hello! " + name + " , would  you like to play guessing number game:\nPress 1 for yes\n      0 for no\n"))
        atempts = 0
        highscore = 0
        finalhighscore = 0
        if ch==0:
            print("Thats okay!")
        if ch!=0 and ch!=1:
            print("Invallid option")
        while ch == 1:
            expno = random.randint(1,20)
            for i in range(1, 11):
                guess = int(input("Enter your guess number between 1 to 20:   "))
                if guess > expno:
                    print("Your guess is greater than the number.")
                elif guess < expno:
                    print("Your guess is smaller than the number.")
                else:
                    print("Congrats! your guess is correct and you took ", i, " attempts.")
                    if i > atempts:
                        atempts = i
                        if atempts == 1:
                            highscore = 10
                        else:
                            highscore = 10 - atempts
                    break
            if i == 10:
                print("You have reached the maximum attempts, Better luck next time.")
            ch = int(input("Do you want to play again(1/0):   "))
            if finalhighscore < highscore:
                finalhighscore = highscore

        print("Your high score is:   ", finalhighscore, "/10")
        print("Thats cool")

        print("_________________________________")
    elif choice==2:
        print("---------------------------------")
        print("_____Welcome to TIC TAC TOE_____")
        print("Lets start...")
        ch=1
        while 1:
            board = [i for i in range(0, 9)]
            you, comp = '', ''
            moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
            winpat = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
            tab = range(1, 10)
            def print_board():
                x = 1
                for i in board:
                    end = ' | '
                    if x % 3 == 0:
                        end = ' \n'
                        if i != 1: end += '---------\n';
                    char = ' '
                    if i in ('X', 'O'): char = i;
                    x += 1
                    print(char, end=end)
            def select_char():
                chars = ('X', 'O')
                if random.randint(0, 1) == 0:
                    return chars[::-1]
                return chars
            def can_move(brd, you, move):
                if move in tab and brd[move - 1] == move - 1:
                    return True
                return False
            def can_win(brd, you, move):
                places = []
                x = 0
                for i in brd:
                    if i == you: places.append(x);
                    x += 1
                win = True
                for tup in winpat:
                    win = True
                    for ix in tup:
                        if brd[ix] != you:
                            win = False
                            break
                    if win == True:
                        break
                return win
            def make_move(brd, you, move, undo=False):
                if can_move(brd, you, move):
                    brd[move - 1] = you
                    win = can_win(brd, you, move)
                    if undo:
                        brd[move - 1] = move - 1
                    return (True, win)
                return (False, False)
            def computer_move():
                move = -1
                for i in range(1, 10):
                    if make_move(board, comp, i, True)[1]:
                        move = i
                        break
                if move == -1:
                    for i in range(1, 10):
                        if make_move(board, you, i, True)[1]:
                            move = i
                            break
                if move == -1:
                    for tup in moves:
                        for mv in tup:
                            if move == -1 and can_move(board, comp, mv):
                                move = mv
                                break
                return make_move(board, comp, move)


            def space_exist():
                return board.count('X') + board.count('O') != 9


            you, comp= select_char()
            print('You are %s and computer is %s' % (you, comp))
            result = '<<<< Draw >>>>>'
            while space_exist():
                print_board()
                print(' Make your move in the range [1-9] : ', end='')
                move = int(input())
                moved, won = make_move(board, you, move)
                if not moved:
                    print(' !!!! Invalid move ! please try again !')
                    continue
                    #
                if won:
                    result = '$$$$$$ Congratulations!  You won the game! $$$$$$'
                    break
                elif computer_move()[1]:
                    result = '!!!! You lost the game, better luck next time !!!!! '
                    break;
            print_board()
            print(result)
            ch=int(input("Do you want to play again(1/0)"))
            if ch==0:
                break
        print("Thanks for playing")
        print("_______________________________________________________")
    elif choice==3:
        aa=0
    else:
        print("Invalid option, please enter the correct option.")
print("_________________________________________________________")


