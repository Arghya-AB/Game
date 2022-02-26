import time
import os

while True:
    try:
        import random

        def playgames():
            print("\n")
            print("\t\tWELCOME TO ARENA")
            print()
            print()
            print("\t\tPLEASE SELECT ONE OF THE GAME MODES:")
            print(
                "\t\tRULES WILL BE PROVIDED ON ENTERING A GAME MODE.(IN CASE OF LOCAL MULTIPLAYER YOU WILL START THE GAME)"
            )
            print("\t\t1. 3X3 TIC TAC TOE SINGLEPLAYER")
            print("\t\t2. 3X3 TIC TAC TOE LOCAL MULTIPLAYER")
            print("\t\t3. 4X4 TIC TAC TOE SINGLEPLAYER <$howdown orig!n@ls>")
            print("\t\t4. 4X4 TIC TAC TOE LOCAL MULTIPLAYER <$howdown orig!n@ls>")
            print("\t\t5. STICK GAME <$howdown orig!n@ls>")
            print("\t\t6. CATCH THE THEIF GAME MULTIPLAYER.<$howdown orig!n@ls>\n\n")
            x = 1
            while x == 1:
                user3 = input("\t\tEnter Option: ")
                if (
                    user3 == "1"
                    or user3 == "2"
                    or user3 == "3"
                    or user3 == "4"
                    or user3 == "5"
                    or user3 == "6"
                ):
                    x = 0
                else:
                    print("\t\tInvalid input.")
            if user3 == "1":
                print("\n\n\n")
                import os, time, random

                # If there are 3 X or 3 O in any win condition then this function
                # terminates the program and returns who has won else returns false
                def gamefinish():  # Checks if game is finished or not
                    x = [
                        [R[1], R[2], R[3]],
                        [R[4], R[5], R[6]],
                        [R[7], R[8], R[9]],
                        [R[2], R[5], R[8]],
                        [R[1], R[4], R[7]],
                        [R[1], R[5], R[9]],
                        [R[3], R[6], R[9]],
                        [R[3], R[5], R[7]],
                    ]
                    lc = [C_Token] * 3
                    lu = [U_Token] * 3
                    if lc in x:
                        return "Computer"
                    elif lu in x:
                        return "User"
                    else:
                        return False

                # If player has allowed computer to win then this function wins the game
                def win():
                    x = [
                        [R[1], R[2], R[3]],
                        [R[4], R[5], R[6]],
                        [R[7], R[8], R[9]],
                        [R[2], R[5], R[8]],
                        [R[1], R[4], R[7]],
                        [R[1], R[5], R[9]],
                        [R[3], R[6], R[9]],
                        [R[3], R[5], R[7]],
                    ]
                    n = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [2, 5, 8],
                        [1, 4, 7],
                        [1, 5, 9],
                        [3, 6, 9],
                        [3, 5, 7],
                    ]
                    lc = ([C_Token] * 2) + [" "]
                    if lc in x:
                        R[n[x.index(lc)][2]] = C_Token
                    else:
                        lc = [C_Token, " ", C_Token]
                        if lc in x:
                            R[n[x.index(lc)][1]] = C_Token
                        else:
                            lc = [" ", C_Token, C_Token]
                            if lc in x:
                                R[n[x.index(lc)][0]] = C_Token

                # If player has allowed the computer to win then this program returns true else false
                def checkwin():
                    x = [
                        [R[1], R[2], R[3]],
                        [R[4], R[5], R[6]],
                        [R[7], R[8], R[9]],
                        [R[2], R[5], R[8]],
                        [R[1], R[4], R[7]],
                        [R[1], R[5], R[9]],
                        [R[3], R[6], R[9]],
                        [R[3], R[5], R[7]],
                    ]
                    n = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [2, 5, 8],
                        [1, 4, 7],
                        [1, 5, 9],
                        [3, 6, 9],
                        [3, 5, 7],
                    ]
                    flag = 0
                    lc = ([C_Token] * 2) + [" "]
                    if lc in x:
                        flag = 1
                    else:
                        lc = [C_Token, " ", C_Token]
                        if lc in x:
                            flag = 1
                        else:
                            lc = [" ", C_Token, C_Token]
                            if lc in x:
                                flag = 1
                    return flag == 1

                # This function identifies if blocking user is required or not
                def checkblock():
                    x = [
                        [R[1], R[2], R[3]],
                        [R[4], R[5], R[6]],
                        [R[7], R[8], R[9]],
                        [R[2], R[5], R[8]],
                        [R[1], R[4], R[7]],
                        [R[1], R[5], R[9]],
                        [R[3], R[6], R[9]],
                        [R[3], R[5], R[7]],
                    ]
                    n = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [2, 5, 8],
                        [1, 4, 7],
                        [1, 5, 9],
                        [3, 6, 9],
                        [3, 5, 7],
                    ]
                    flag = 0
                    lu = ([U_Token] * 2) + [" "]
                    if lu in x:
                        flag = 1
                    else:
                        lu = [U_Token, " ", U_Token]
                        if lu in x:
                            flag = 1
                        else:
                            lu = [" ", U_Token, U_Token]
                            if lu in x:
                                flag = 1
                    return flag == 1

                # This blocks user from winning
                def block():
                    x = [
                        [R[1], R[2], R[3]],
                        [R[4], R[5], R[6]],
                        [R[7], R[8], R[9]],
                        [R[2], R[5], R[8]],
                        [R[1], R[4], R[7]],
                        [R[1], R[5], R[9]],
                        [R[3], R[6], R[9]],
                        [R[3], R[5], R[7]],
                    ]
                    n = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [2, 5, 8],
                        [1, 4, 7],
                        [1, 5, 9],
                        [3, 6, 9],
                        [3, 5, 7],
                    ]
                    lu = ([U_Token] * 2) + [" "]
                    if lu in x:
                        R[n[x.index(lu)][2]] = C_Token
                    else:
                        lu = [U_Token, " ", U_Token]
                        if lu in x:
                            R[n[x.index(lu)][1]] = C_Token
                        else:
                            lu = [" ", U_Token, U_Token]
                            if lu in x:
                                R[n[x.index(lu)][0]] = C_Token

                # This shows the original board
                def showboard():
                    print("\t\t     |     |")
                    print("\t\t ", 1, " | ", 2, " | ", 3)
                    print("\t\t_____|_____|_____")
                    print("\t\t     |     |")
                    print("\t\t ", 4, " | ", 5, " | ", 6)
                    print("\t\t_____|_____|_____")
                    print("\t\t     |     |")
                    print("\t\t ", 7, " | ", 8, " | ", 9)
                    print("\t\t     |     |\n")

                # From here your own program starts
                R = {
                    1: " ",
                    2: " ",
                    3: " ",
                    4: " ",
                    5: " ",
                    6: " ",
                    7: " ",
                    8: " ",
                    9: " ",
                }

                def Invalid_Input():
                    board_update()
                    print("\t\tInvalid Input!\n____________________")
                    print("\t\tHere is the board.........  Please input accordingly")
                    time.sleep(0.2)
                    showboard()
                    time.sleep(3)

                def board_set():
                    for i in range(1, 10):
                        R[i] = " "

                def board_reset():
                    for i in range(1, 10):
                        R[i] = i

                def board_update():
                    print("\t\t     |     |")
                    print("\t\t ", R[1], " | ", R[2], " | ", R[3])
                    print("\t\t_____|_____|_____")
                    print("\t\t     |     |")
                    print("\t\t ", R[4], " | ", R[5], " | ", R[6])
                    print("\t\t_____|_____|_____")
                    print("\t\t     |     |")
                    print("\t\t ", R[7], " | ", R[8], " | ", R[9])
                    print("\t\t     |     |\n")

                # Token Select
                showboard()
                while True:
                    U_Token = input("\t\tDo you want X or O?\n\t\t--->")
                    if U_Token.upper() == "X":
                        C_Token = "O"
                    elif U_Token.upper() == "O":
                        C_Token = "X"
                    else:
                        Invalid_Input()
                        continue
                    U_Token = U_Token.upper()
                    break
                board_set()
                board_update()
                # Whose Turn? + Start the game
                start = 0
                if random.randint(0, 1) != 0:
                    R[random.randint(1, 9)] = C_Token
                    board_update()
                    start = 1
                move = 0
                while " " in list(R.values()):
                    move += 1
                    while True:
                        board_update()
                        try:
                            User = int(
                                input("\t\tYour Turn!\n\t\tEnter your position(1-9):")
                            )
                            if (User < 1 or User > 9) or R[User] != " ":
                                Invalid_Input()
                                continue
                            break
                        except:
                            Invalid_Input()
                            continue
                    R[User] = U_Token
                    board_update()
                    if (
                        gamefinish() == "User"
                    ):  # if game has finished then this terminates program
                        print("\t\t", gamefinish(), "won the game.\nOh no.......")
                        name_scores[nowuser][0] += 7
                        name_scores[nowuser][1] += 1
                        time.sleep(3)
                        break
                    else:
                        if checkwin():  # if allowed to win then win
                            win()
                            board_update()
                            if gamefinish() == "Computer":
                                print(
                                    "\t\t",
                                    gamefinish(),
                                    "won the game.\nYou will never defeat AI",
                                )
                                name_scores[nowuser][0] -= 5
                                name_scores[nowuser][2] += 1
                                time.sleep(3)
                                break
                        elif checkblock():  # elif player winning then block
                            block()
                            board_update()
                            print("\t\tHa!!! I blocked you.")
                            time.sleep(1)
                        else:  # else use a definite strategy and ccount is corner count of user
                            ccount = 0
                            if R[1] == U_Token:
                                ccount += 1
                            if R[3] == U_Token:
                                ccount += 1
                            if R[9] == U_Token:
                                ccount += 1
                            if R[7] == U_Token:
                                ccount += 1
                            if R[5] == " ":
                                R[5] = C_Token
                                board_update()
                            elif (
                                R[1] == " " or R[2] == " " or R[3] == " " or R[4] == " "
                            ) and not (
                                start != 1 and (ccount > 1 and move == 2)
                            ):  # This determines if user has used corner corner tactic or not
                                corner = [1, 3, 7, 9]
                                while True:
                                    r = random.randint(0, 3)
                                    if R[corner[r]] == " ":
                                        R[corner[r]] = C_Token
                                        break
                                board_update()
                            else:
                                edge = [2, 4, 6, 8]
                                while True:
                                    r = random.randint(0, 3)
                                    if R[edge[r]] == " ":
                                        R[edge[r]] = C_Token
                                        break
                                board_update()
                    if " " not in list(R.values()):
                        print("\t\tIt is a tie.")
                        name_scores[nowuser][0] += 0
                        name_scores[nowuser][3] += 1
                        break

                else:
                    print("\t\tIt is a tie")
                    name_scores[nowuser][0] += 0
                    name_scores[nowuser][3] += 1
            # THIS SERVER HAS FOLLOWING VALID OPTIONS
            # Existing user,newuser,exit,profile,play game, see events, see offers, see active boosts, see leaderboard, logout, 3X3 single player in playgame
            # shrink functions by clicking the arrow on right side of line number 250,272,277,307,369,431,484,511,522,526
            if user3 == "2":
                print("\n\n\n")
                print(
                    "\t\tPlease give input as directed or else the program might crash."
                )
                print(
                    "\t\tWELCOME TO CLASSIC TIC TAC TOE. YOU ARE UP AGAINST YOUR CHOSEN OPPONENT."
                )
                print("\t\tSCORE 3 TOKENS IN ANY STRAIGHT LINE OR DIAGONAL TO WIN.")
                print(
                    "\t\t1 MOVE PER PLAYER. THELOGGED IN USER SHOULD BEGIN!!! \n\n\t\tLET THE GAME BEGIN."
                )
                print("\n")

                def play2():
                    def graphic(lister1):
                        r1 = ["   ", "   ", "   "]
                        r2 = ["   ", "   ", "   "]
                        r3 = ["   ", "   ", "   "]
                        maxr = [r1, r2, r3]
                        for p in range(1, 4):
                            for q in range(1, 4):
                                if (p, q) in lister1:
                                    if lister1.index((p, q)) % 2 == 0:
                                        maxr[q - 1][p - 1] = " X "
                                    else:
                                        maxr[q - 1][p - 1] = " O "
                        print("\t\t    1          2         3     ")
                        print("\t\t          |         |         ")
                        print(
                            "\t\t1   ",
                            r1[0],
                            "   |   ",
                            r1[1],
                            "   |   ",
                            r1[2],
                            "   ",
                            sep="",
                        )
                        print("\t\t _________|_________|_________")
                        print("\t\t          |         |         ")
                        print(
                            "\t\t2   ",
                            r2[0],
                            "   |   ",
                            r2[1],
                            "   |   ",
                            r2[2],
                            "   ",
                            sep="",
                        )
                        print("\t\t__________|_________|_________")
                        print("\t\t          |         |         ")
                        print(
                            "\t\t3   ",
                            r3[0],
                            "   |   ",
                            r3[1],
                            "   |   ",
                            r3[2],
                            "   ",
                            sep="",
                        )
                        print("\t\t          |         |          ")

                    def check(input1):
                        if (
                            len(input1) == 2
                            and (input1[0] in range(1, 4))
                            and (input1[1] in range(1, 4))
                        ):
                            return True
                        else:
                            return False

                    def endgame(lister2):
                        w1 = ["   ", "   ", "   "]
                        w2 = ["   ", "   ", "   "]
                        w3 = ["   ", "   ", "   "]
                        maxw = [w1, w2, w3]
                        for p in range(1, 4):
                            for q in range(1, 4):
                                if (p, q) in lister2:
                                    if lister2.index((p, q)) % 2 == 0:
                                        maxw[q - 1][p - 1] = " X "
                                    else:
                                        maxw[q - 1][p - 1] = " O "
                        if (w1[0] == w1[1]) and (w1[1] == w1[2]) and (w1[0] != "   "):
                            return True
                        elif (w2[0] == w2[1]) and (w2[1] == w2[2]) and (w2[0] != "   "):
                            return True
                        elif (w3[0] == w3[1]) and (w3[1] == w3[2]) and (w3[0] != "   "):
                            return True
                        elif (w1[0] == w2[0]) and (w2[0] == w3[0]) and (w1[0] != "   "):
                            return True
                        elif (w1[1] == w2[1]) and (w2[1] == w3[1]) and (w1[1] != "   "):
                            return True
                        elif (w1[2] == w2[2]) and (w2[2] == w3[2]) and (w1[2] != "   "):
                            return True
                        elif (w1[0] == w2[1]) and (w2[1] == w3[2]) and (w1[0] != "   "):
                            return True
                        elif (w1[2] == w2[1]) and (w2[1] == w3[0]) and (w1[2] != "   "):
                            return True
                        else:
                            return False

                    lis = []
                    graphic(lis)
                    print("\t\tThis game follows a graphical coordinate")
                    print("\t\tsystem with coordinates as (x,y). The X axis")
                    print("\t\tis written above board and the Y axis on left side.")
                    print("\t\tExample-(1,1) will result in left corner of board.")
                    for a in range(1, 10):
                        if a % 2 == 1:
                            x = 1
                            while x == 1:
                                b = eval(input("\t\tEnter X: "))
                                if check(b):
                                    x = 0
                                else:
                                    x = 1
                                    print("\t\tInvalid input.")
                            lis.append(b)
                            graphic(lis)
                            if endgame(lis):
                                print("\t\tX won the game.")
                                name_scores[nowuser][0] += 7
                                name_scores[nowuser][1] += 1
                                break
                        else:
                            x = 1
                            while x == 1:
                                b = eval(input("\t\tEnter O: "))
                                if check(b):
                                    x = 0
                                else:
                                    x = 1
                                    print("\t\tInvalid input.")
                            lis.append(b)
                            graphic(lis)
                            if endgame(lis):
                                print("\t\tO won the game.")
                                name_scores[nowuser][0] -= 5
                                name_scores[nowuser][2] += 1
                                break
                    else:
                        print("\t\tTie")
                        name_scores[nowuser][0] += 0
                        name_scores[nowuser][3] += 1

                play2()
                a = nowuser
                input("\t\tPress Enter to go back to menu: ")
            if user3 == "3":
                print("\n\n\n")
                print(
                    "\t\tPlease give input as directed or else the program might crash."
                )
                print(
                    "\t\tWELCOME TO EPIC VERSION OF TIC TAC TOE. YOU ARE UP AGAINST THE COMPUTER."
                )
                print("\t\tSCORE 4 TOKENS IN ANY STRAIGHT LINE OR DIAGONAL TO WIN.")
                print(
                    "\t\t2 MOVE PER PLAYER. ATTACK AS WELL AS DEFEND. THINGS WILL GET INTRESTING NOW. \n\nLET THE GAME BEGIN."
                )
                print("\n")
                import random

                def play3():
                    def graphic(lister1):
                        r1 = ["   ", "   ", "   ", "   "]
                        r2 = ["   ", "   ", "   ", "   "]
                        r3 = ["   ", "   ", "   ", "   "]
                        r4 = ["   ", "   ", "   ", "   "]
                        maxr = [r1, r2, r3, r4]
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister1:
                                    if (
                                        lister1.index((p, q)) % 4 == 0
                                        or lister1.index((p, q)) % 4 == 1
                                    ):
                                        maxr[q - 1][p - 1] = " X "
                                    else:
                                        maxr[q - 1][p - 1] = " O "
                        print("\t\t    1          2         3         4")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t1   ",
                            r1[0],
                            "   |   ",
                            r1[1],
                            "   |   ",
                            r1[2],
                            "   |   ",
                            r1[3],
                            sep="",
                        )
                        print("\t\t _________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t2   ",
                            r2[0],
                            "   |   ",
                            r2[1],
                            "   |   ",
                            r2[2],
                            "   |   ",
                            r2[3],
                            sep="",
                        )
                        print("\t\t__________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t3   ",
                            r3[0],
                            "   |   ",
                            r3[1],
                            "   |   ",
                            r3[2],
                            "   |   ",
                            r3[3],
                            sep="",
                        )
                        print("\t\t _________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t4   ",
                            r4[0],
                            "   |   ",
                            r4[1],
                            "   |   ",
                            r4[2],
                            "   |   ",
                            r4[3],
                            sep="",
                        )
                        print("\t\t          |         |         |         ")

                    def check(input1, lister6):
                        if (
                            len(input1) == 2
                            and (input1[0] in range(1, 5))
                            and (input1[1] in range(1, 5))
                            and str(input1[0]).isdigit()
                            and str(input1[1]).isdigit()
                            and input1 not in lister6
                        ):
                            return True
                        else:
                            return False

                    def endgame(lister2):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        dic = {
                            1: (1, 1),
                            2: (2, 1),
                            3: (3, 1),
                            4: (4, 1),
                            5: (1, 2),
                            6: (2, 2),
                            7: (3, 2),
                            8: (4, 2),
                            9: (1, 3),
                            10: (2, 3),
                            11: (3, 3),
                            12: (4, 3),
                            13: (1, 4),
                            14: (2, 4),
                            15: (3, 4),
                            16: (4, 4),
                        }
                        xl = []
                        ol = []
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister2:
                                    if (
                                        lister2.index((p, q)) % 4 == 0
                                        or lister2.index((p, q)) % 4 == 1
                                    ):
                                        xl.append(dicter[(p, q)])
                                    else:
                                        ol.append(dicter[(p, q)])
                        win = [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16],
                            [1, 5, 9, 13],
                            [2, 6, 10, 14],
                            [3, 7, 11, 15],
                            [4, 8, 12, 16],
                            [1, 6, 11, 16],
                            [4, 7, 10, 13],
                        ]
                        for a in win:
                            d = list(a)
                            count = 0
                            for b in ol:
                                if b in a:
                                    d.remove(b)
                                    count += 1
                            if count > 3 and d == []:
                                return "O"
                        else:
                            for a in win:
                                d = list(a)
                                count = 0
                                for b in xl:
                                    if b in a:
                                        d.remove(b)
                                        count += 1
                                if count > 3 and d == []:
                                    return "X"
                            else:
                                return False

                    def comwin1(lister3):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        xl = []
                        dic = {
                            1: (1, 1),
                            2: (2, 1),
                            3: (3, 1),
                            4: (4, 1),
                            5: (1, 2),
                            6: (2, 2),
                            7: (3, 2),
                            8: (4, 2),
                            9: (1, 3),
                            10: (2, 3),
                            11: (3, 3),
                            12: (4, 3),
                            13: (1, 4),
                            14: (2, 4),
                            15: (3, 4),
                            16: (4, 4),
                        }
                        ol = []
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister3:
                                    if (
                                        lister3.index((p, q)) % 4 == 0
                                        or lister3.index((p, q)) % 4 == 1
                                    ):
                                        xl.append(dicter[(p, q)])
                                    else:
                                        ol.append(dicter[(p, q)])
                        win = [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16],
                            [1, 5, 9, 13],
                            [2, 6, 10, 14],
                            [3, 7, 11, 15],
                            [4, 8, 12, 16],
                            [1, 6, 11, 16],
                            [4, 7, 10, 13],
                        ]
                        for a in win:
                            d = list(a)
                            count = 0
                            for b in ol:
                                if b in a:
                                    d.remove(b)
                                    count += 1
                            if count > 1:
                                for c in xl:
                                    if c in a:
                                        break
                                else:
                                    if len(lister3) % 2 != 0 and count < 3:
                                        return False
                                        break
                                    elif dic[d[0]] not in lister3:
                                        return dic[d[0]]
                                        break
                                    else:
                                        return dic[d[1]]
                                        break
                        else:
                            return False

                    def comwin2(lister3):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        xl = []
                        dic = {
                            1: (1, 1),
                            2: (2, 1),
                            3: (3, 1),
                            4: (4, 1),
                            5: (1, 2),
                            6: (2, 2),
                            7: (3, 2),
                            8: (4, 2),
                            9: (1, 3),
                            10: (2, 3),
                            11: (3, 3),
                            12: (4, 3),
                            13: (1, 4),
                            14: (2, 4),
                            15: (3, 4),
                            16: (4, 4),
                        }
                        ol = []
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister3:
                                    if (
                                        lister3.index((p, q)) % 4 == 0
                                        or lister3.index((p, q)) % 4 == 1
                                    ):
                                        xl.append(dicter[(p, q)])
                                    else:
                                        ol.append(dicter[(p, q)])
                        win = [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16],
                            [1, 5, 9, 13],
                            [2, 6, 10, 14],
                            [3, 7, 11, 15],
                            [4, 8, 12, 16],
                            [1, 6, 11, 16],
                            [4, 7, 10, 13],
                        ]
                        for a in win:
                            d = list(a)
                            count = 0
                            for b in ol:
                                if b in a:
                                    d.remove(b)
                                    count += 1
                            if count > 1:
                                for c in xl:
                                    if c in a:
                                        break
                                else:
                                    if dic[d[0]] not in lister3:
                                        return dic[d[0]]
                                        break
                                    else:
                                        return dic[d[1]]
                                        break
                        else:
                            return False

                    def comblock1(lister3):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        xl = []
                        dic = {
                            1: (1, 1),
                            2: (2, 1),
                            3: (3, 1),
                            4: (4, 1),
                            5: (1, 2),
                            6: (2, 2),
                            7: (3, 2),
                            8: (4, 2),
                            9: (1, 3),
                            10: (2, 3),
                            11: (3, 3),
                            12: (4, 3),
                            13: (1, 4),
                            14: (2, 4),
                            15: (3, 4),
                            16: (4, 4),
                        }
                        ol = []
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister3:
                                    if (
                                        lister3.index((p, q)) % 4 == 0
                                        or lister3.index((p, q)) % 4 == 1
                                    ):
                                        ol.append(dicter[(p, q)])
                                    else:
                                        xl.append(dicter[(p, q)])
                        win = [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16],
                            [1, 5, 9, 13],
                            [2, 6, 10, 14],
                            [3, 7, 11, 15],
                            [4, 8, 12, 16],
                            [1, 6, 11, 16],
                            [4, 7, 10, 13],
                        ]
                        for a in win:
                            d = list(a)
                            count = 0
                            for b in ol:
                                if b in a:
                                    d.remove(b)
                                    count += 1
                            if count > 1:
                                for c in xl:
                                    if c in a:
                                        break
                                else:
                                    if dic[d[0]] not in lister3:
                                        return dic[d[0]]
                                        break
                                    else:
                                        return dic[d[1]]
                                        break
                        else:
                            return False

                    def comblock2(lister3):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        xl = []
                        dic = {
                            1: (1, 1),
                            2: (2, 1),
                            3: (3, 1),
                            4: (4, 1),
                            5: (1, 2),
                            6: (2, 2),
                            7: (3, 2),
                            8: (4, 2),
                            9: (1, 3),
                            10: (2, 3),
                            11: (3, 3),
                            12: (4, 3),
                            13: (1, 4),
                            14: (2, 4),
                            15: (3, 4),
                            16: (4, 4),
                        }
                        ol = []
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister3:
                                    if (
                                        lister3.index((p, q)) % 4 == 0
                                        or lister3.index((p, q)) % 4 == 1
                                    ):
                                        ol.append(dicter[(p, q)])
                                    else:
                                        xl.append(dicter[(p, q)])
                        win = [
                            [1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16],
                            [1, 5, 9, 13],
                            [2, 6, 10, 14],
                            [3, 7, 11, 15],
                            [4, 8, 12, 16],
                            [1, 6, 11, 16],
                            [4, 7, 10, 13],
                        ]
                        for a in win:
                            d = list(a)
                            count = 0
                            for b in ol:
                                if b in a:
                                    d.remove(b)
                                    count += 1
                            if count > 1:
                                for c in xl:
                                    if c in a:
                                        break
                                else:
                                    if dic[d[0]] not in lister3:
                                        return dic[d[0]]
                                        break
                                    else:
                                        return dic[d[1]]
                                        break
                        else:
                            return False

                    def AI1(lister4):
                        if len(lister4) != 2 and len(lister4) != 3:
                            if comwin1(lister4):
                                return comwin1(lister4)
                            elif comblock1(lister4):
                                return comblock1(lister4)
                            else:
                                dicter = {
                                    (1, 1): 1,
                                    (2, 1): 2,
                                    (3, 1): 3,
                                    (4, 1): 4,
                                    (1, 2): 5,
                                    (2, 2): 6,
                                    (3, 2): 7,
                                    (4, 2): 8,
                                    (1, 3): 9,
                                    (2, 3): 10,
                                    (3, 3): 11,
                                    (4, 3): 12,
                                    (1, 4): 13,
                                    (2, 4): 14,
                                    (3, 4): 15,
                                    (4, 4): 16,
                                }
                                dic = {
                                    1: (1, 1),
                                    2: (2, 1),
                                    3: (3, 1),
                                    4: (4, 1),
                                    5: (1, 2),
                                    6: (2, 2),
                                    7: (3, 2),
                                    8: (4, 2),
                                    9: (1, 3),
                                    10: (2, 3),
                                    11: (3, 3),
                                    12: (4, 3),
                                    13: (1, 4),
                                    14: (2, 4),
                                    15: (3, 4),
                                    16: (4, 4),
                                }
                                if (
                                    (dic[7] not in lister4)
                                    or (dic[6] not in lister4)
                                    or (dic[10] not in lister4)
                                    or (dic[11] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [6, 7, 10, 11]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                elif (
                                    (dic[1] not in lister4)
                                    or (dic[4] not in lister4)
                                    or (dic[13] not in lister4)
                                    or (dic[16] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [1, 4, 13, 16]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                else:
                                    while True:
                                        r1 = random.randint(1, 4)
                                        r2 = random.randint(1, 4)
                                        if (r1, r2) not in lister4:
                                            return (r1, r2)
                                            break
                        else:
                            dicter = {
                                (1, 1): 1,
                                (2, 1): 2,
                                (3, 1): 3,
                                (4, 1): 4,
                                (1, 2): 5,
                                (2, 2): 6,
                                (3, 2): 7,
                                (4, 2): 8,
                                (1, 3): 9,
                                (2, 3): 10,
                                (3, 3): 11,
                                (4, 3): 12,
                                (1, 4): 13,
                                (2, 4): 14,
                                (3, 4): 15,
                                (4, 4): 16,
                            }
                            xl = []
                            dic = {
                                1: (1, 1),
                                2: (2, 1),
                                3: (3, 1),
                                4: (4, 1),
                                5: (1, 2),
                                6: (2, 2),
                                7: (3, 2),
                                8: (4, 2),
                                9: (1, 3),
                                10: (2, 3),
                                11: (3, 3),
                                12: (4, 3),
                                13: (1, 4),
                                14: (2, 4),
                                15: (3, 4),
                                16: (4, 4),
                            }
                            ol = []
                            for p in range(1, 5):
                                for q in range(1, 5):
                                    if (p, q) in lister4:
                                        if (
                                            lister4.index((p, q)) % 4 == 0
                                            or lister4.index((p, q)) % 4 == 1
                                        ):
                                            xl.append(dicter[(p, q)])
                                        else:
                                            ol.append(dicter[(p, q)])
                            xl.sort()
                            ol.sort()
                            clo = (
                                ([1, 16], [11, 13]),
                                ([4, 13], [10, 16]),
                                ([1, 13], [5, 16]),
                                ([13, 16], [4, 14]),
                                ([4, 16], [8, 13]),
                                ([1, 4], [3, 13]),
                                ([5, 12], [7, 11]),
                                ([8, 9], [6, 10]),
                                ([6, 11], [10, 16]),
                                ([7, 10], [11, 13]),
                                ([7, 11], [10, 15]),
                                ([6, 10], [11, 14]),
                                ([1, 10], [7, 11]),
                                ([11, 13], [6, 7]),
                                ([7, 16], [6, 10]),
                                ([4, 6], [10, 11]),
                                ([6, 13], [10, 11]),
                                ([10, 16], [7, 11]),
                                ([4, 11], [6, 7]),
                                ([1, 7], [6, 10]),
                                ([2, 15], [10, 11]),
                                ([3, 14], [10, 11]),
                                ([2, 14], [10, 11]),
                                ([3, 15], [10, 11]),
                                ([5, 12], [7, 11]),
                                ([8, 9], [7, 11]),
                                ([5, 8], [7, 11]),
                                ([9, 12], [7, 11]),
                            )
                            for i in clo:
                                if xl == i[0]:
                                    if dic[i[1][0]] not in lister4:
                                        return dic[i[1][0]]
                                    else:
                                        return dic[i[1][1]]
                            else:
                                if comblock1(lister4):
                                    return comblock1(lister4)
                                elif (
                                    (dic[7] not in lister4)
                                    or (dic[6] not in lister4)
                                    or (dic[10] not in lister4)
                                    or (dic[11] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [6, 7, 10, 11]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                elif (
                                    (dic[1] not in lister4)
                                    or (dic[4] not in lister4)
                                    or (dic[13] not in lister4)
                                    or (dic[16] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [1, 4, 13, 16]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                else:
                                    while True:
                                        r1 = random.randint(1, 4)
                                        r2 = random.randint(1, 4)
                                        if (r1, r2) not in lister4:
                                            return (r1, r2)
                                            break

                    def AI2(lister4):
                        if comwin2(lister4):
                            return comwin2(lister4)
                        elif len(lister4) == 2 or len(lister4) == 3:
                            dicter = {
                                (1, 1): 1,
                                (2, 1): 2,
                                (3, 1): 3,
                                (4, 1): 4,
                                (1, 2): 5,
                                (2, 2): 6,
                                (3, 2): 7,
                                (4, 2): 8,
                                (1, 3): 9,
                                (2, 3): 10,
                                (3, 3): 11,
                                (4, 3): 12,
                                (1, 4): 13,
                                (2, 4): 14,
                                (3, 4): 15,
                                (4, 4): 16,
                            }
                            xl = []
                            dic = {
                                1: (1, 1),
                                2: (2, 1),
                                3: (3, 1),
                                4: (4, 1),
                                5: (1, 2),
                                6: (2, 2),
                                7: (3, 2),
                                8: (4, 2),
                                9: (1, 3),
                                10: (2, 3),
                                11: (3, 3),
                                12: (4, 3),
                                13: (1, 4),
                                14: (2, 4),
                                15: (3, 4),
                                16: (4, 4),
                            }
                            ol = []
                            for p in range(1, 5):
                                for q in range(1, 5):
                                    if (p, q) in lister4:
                                        if (
                                            lister4.index((p, q)) % 4 == 0
                                            or lister4.index((p, q)) % 4 == 1
                                        ):
                                            xl.append(dicter[(p, q)])
                                        else:
                                            ol.append(dicter[(p, q)])
                            xl.sort()
                            ol.sort()
                            clo = (
                                ([1, 16], [11, 13]),
                                ([4, 13], [10, 16]),
                                ([1, 13], [5, 16]),
                                ([13, 16], [4, 14]),
                                ([4, 16], [8, 13]),
                                ([1, 4], [3, 13]),
                                ([5, 12], [7, 11]),
                                ([8, 9], [6, 10]),
                                ([6, 11], [10, 16]),
                                ([7, 10], [11, 13]),
                                ([7, 11], [10, 15]),
                                ([6, 10], [11, 14]),
                                ([1, 10], [7, 11]),
                                ([11, 13], [6, 7]),
                                ([7, 16], [6, 10]),
                                ([4, 6], [10, 11]),
                                ([6, 13], [10, 11]),
                                ([10, 16], [7, 11]),
                                ([4, 11], [6, 7]),
                                ([1, 7], [6, 10]),
                            )
                            for i in clo:
                                if xl == i[0]:
                                    if dic[i[1][0]] not in lister4:
                                        return dic[i[1][0]]
                                    else:
                                        return dic[i[1][1]]
                            else:
                                if comblock2(lister4):
                                    return comblock2(lister4)
                                elif (
                                    (dic[7] not in lister4)
                                    or (dic[6] not in lister4)
                                    or (dic[10] not in lister4)
                                    or (dic[11] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [6, 7, 10, 11]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                elif (
                                    (dic[1] not in lister4)
                                    or (dic[4] not in lister4)
                                    or (dic[13] not in lister4)
                                    or (dic[16] not in lister4)
                                ):
                                    while True:
                                        r = random.randint(0, 3)
                                        jk = [1, 4, 13, 16]
                                        if dic[jk[r]] not in lister4:
                                            return dic[jk[r]]
                                            break
                                else:
                                    while True:
                                        r1 = random.randint(1, 4)
                                        r2 = random.randint(1, 4)
                                        if (r1, r2) not in lister4:
                                            return (r1, r2)
                                            break
                        elif comblock2(lister4):
                            return comblock2(lister4)
                        else:
                            dicter = {
                                (1, 1): 1,
                                (2, 1): 2,
                                (3, 1): 3,
                                (4, 1): 4,
                                (1, 2): 5,
                                (2, 2): 6,
                                (3, 2): 7,
                                (4, 2): 8,
                                (1, 3): 9,
                                (2, 3): 10,
                                (3, 3): 11,
                                (4, 3): 12,
                                (1, 4): 13,
                                (2, 4): 14,
                                (3, 4): 15,
                                (4, 4): 16,
                            }
                            dic = {
                                1: (1, 1),
                                2: (2, 1),
                                3: (3, 1),
                                4: (4, 1),
                                5: (1, 2),
                                6: (2, 2),
                                7: (3, 2),
                                8: (4, 2),
                                9: (1, 3),
                                10: (2, 3),
                                11: (3, 3),
                                12: (4, 3),
                                13: (1, 4),
                                14: (2, 4),
                                15: (3, 4),
                                16: (4, 4),
                            }
                            if (
                                (dic[7] not in lister4)
                                or (dic[6] not in lister4)
                                or (dic[10] not in lister4)
                                or (dic[11] not in lister4)
                            ):
                                while True:
                                    r = random.randint(0, 3)
                                    jk = [6, 7, 10, 11]
                                    if dic[jk[r]] not in lister4:
                                        return dic[jk[r]]
                                        break
                            elif (
                                (dic[1] not in lister4)
                                or (dic[4] not in lister4)
                                or (dic[13] not in lister4)
                                or (dic[16] not in lister4)
                            ):
                                while True:
                                    r = random.randint(0, 3)
                                    jk = [1, 4, 13, 16]
                                    if dic[jk[r]] not in lister4:
                                        return dic[jk[r]]
                                        break
                            else:
                                while True:
                                    r1 = random.randint(1, 4)
                                    r2 = random.randint(1, 4)
                                    if (r1, r2) not in lister4:
                                        return (r1, r2)
                                        break

                    def easyAE(lister4):
                        if comwin1(lister4):
                            return comwin1(lister4)
                        elif comblock1(lister4):
                            return comblock1(lister4)
                        else:
                            dic = {
                                1: (1, 1),
                                2: (2, 1),
                                3: (3, 1),
                                4: (4, 1),
                                5: (1, 2),
                                6: (2, 2),
                                7: (3, 2),
                                8: (4, 2),
                                9: (1, 3),
                                10: (2, 3),
                                11: (3, 3),
                                12: (4, 3),
                                13: (1, 4),
                                14: (2, 4),
                                15: (3, 4),
                                16: (4, 4),
                            }
                            while True:
                                r = random.randint(1, 16)
                                if dic[r] not in lister4:
                                    return dic[r]
                                    break

                    lis = []
                    graphic(lis)
                    print("\t\tThis game follows a graphical coordinate")
                    print("\t\tsystem with coordinates as (x,y). The X axis")
                    print("\t\tis written above board and the Y axis on left side.")
                    print("\t\tExample-(1,1) will result in left corner of board.")
                    x = 1
                    while x == 1:
                        hj = input("\t\tSelect game difficulty --- EASY or HARD: ")
                        if hj.lower() == "easy" or hj.lower() == "hard":
                            x = 0
                        else:
                            x = 1
                            print("\t\tInvalid")
                    if hj.lower() == "hard":
                        for l in range(1, 9):
                            if l % 2 == 1:
                                x1 = eval(input("\t\tEnter 1st move coordinate: "))
                                x2 = eval(input("\t\tEnter 2nd move coordinate: "))
                                lis.append(x1)
                                lis.append(x2)
                                graphic(lis)
                                if endgame(lis):
                                    print("\t\t", endgame(lis), "won the game.")
                                    break
                            else:
                                a = input("\t\tHmm... Press enter.")
                                lis.append(AI1(lis))
                                lis.append(AI1(lis))
                                graphic(lis)
                                if endgame(lis):
                                    print("\t\t", endgame(lis), "won the game.")
                                    break

                        else:
                            print("\t\tTie")
                            name_scores[nowuser][0] += 0
                            name_scores[nowuser][3] += 1
                        if endgame(lis) == "X":
                            name_scores[nowuser][0] += 7
                            name_scores[nowuser][1] += 1
                        elif endgame(lis) == "O":
                            name_scores[nowuser][0] -= 5
                            name_scores[nowuser][2] += 1
                    else:
                        for l in range(1, 9):
                            if l % 2 == 1:
                                x1 = eval(input("\t\tEnter 1st move coordinate: "))
                                x2 = eval(input("\t\tEnter 2nd move coordinate: "))
                                lis.append(x1)
                                lis.append(x2)
                                graphic(lis)
                                if endgame(lis):
                                    print("\t\t", endgame(lis), "won the game.")
                                    input("\t\tPress enter")
                                    break
                            else:
                                a = input("\t\tHmm... Press enter.")
                                lis.append(easyAE(lis))
                                lis.append(easyAE(lis))
                                graphic(lis)
                                if endgame(lis):
                                    print("\t\t", endgame(lis), "won the game.")
                                    input("\t\tPress enter")
                                    break

                        else:
                            print("\t\tTie")
                            input("\t\tPress enter")
                            name_scores[nowuser][0] += 0
                            name_scores[nowuser][3] += 1
                        if endgame(lis) == "X":
                            name_scores[nowuser][0] += 7
                            name_scores[nowuser][1] += 1
                        elif endgame(lis) == "O":
                            name_scores[nowuser][0] -= 5
                            name_scores[nowuser][2] += 1

                play3()
                a = nowuser
                input("\t\tPRESS ENTER TO GO BACK TO MENU")
            if user3 == "4":
                print("\n\n\n")
                print(
                    "\t\tPlease give input as directed or else the program might crash."
                )
                print(
                    "\t\tWELCOME TO EPIC VERSION OF TIC TAC TOE. YOU ARE UP AGAINST YOUR LOCAL OPPONENT."
                )
                print("\t\tSCORE 4 TOKENS IN ANY STRAIGHT LINE OR DIAGONAL TO WIN.")
                print(
                    "\t\t2 MOVE PER PLAYER. ATTACK AS WELL AS DEFEND. THINGS WILL GET INTRESTING NOW.\n\t\tTHE LOGGED IN PLAYER WILL START. \n\nLET THE GAME BEGIN."
                )
                print("\n")

                def play4():
                    def graphic(lister1):
                        r1 = ["   ", "   ", "   ", "   "]
                        r2 = ["   ", "   ", "   ", "   "]
                        r3 = ["   ", "   ", "   ", "   "]
                        r4 = ["   ", "   ", "   ", "   "]
                        maxr = [r1, r2, r3, r4]
                        for p in range(1, 5):
                            for q in range(1, 5):
                                if (p, q) in lister1:
                                    if (
                                        lister1.index((p, q)) % 4 == 0
                                        or lister1.index((p, q)) % 4 == 1
                                    ):
                                        maxr[q - 1][p - 1] = " X "
                                    else:
                                        maxr[q - 1][p - 1] = " O "
                        print("\t\t    1          2         3         4")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t1   ",
                            r1[0],
                            "   |   ",
                            r1[1],
                            "   |   ",
                            r1[2],
                            "   |   ",
                            r1[3],
                            sep="",
                        )
                        print("\t\t _________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t2   ",
                            r2[0],
                            "   |   ",
                            r2[1],
                            "   |   ",
                            r2[2],
                            "   |   ",
                            r2[3],
                            sep="",
                        )
                        print("\t\t__________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t3   ",
                            r3[0],
                            "   |   ",
                            r3[1],
                            "   |   ",
                            r3[2],
                            "   |   ",
                            r3[3],
                            sep="",
                        )
                        print("\t\t _________|_________|_________|_________")
                        print("\t\t          |         |         |         ")
                        print(
                            "\t\t4   ",
                            r4[0],
                            "   |   ",
                            r4[1],
                            "   |   ",
                            r4[2],
                            "   |   ",
                            r4[3],
                            sep="",
                        )
                        print("\t\t          |         |         |         ")

                    def check(input1, lister6):
                        if (
                            len(input1) == 2
                            and (input1[0] in range(1, 5))
                            and (input1[1] in range(1, 5))
                            and str(input1[0]).isdigit()
                            and str(input1[1]).isdigit()
                            and input1 not in lister6
                        ):
                            return True
                        else:
                            return False

                    def endgame(lister2):
                        dicter = {
                            (1, 1): 1,
                            (2, 1): 2,
                            (3, 1): 3,
                            (4, 1): 4,
                            (1, 2): 5,
                            (2, 2): 6,
                            (3, 2): 7,
                            (4, 2): 8,
                            (1, 3): 9,
                            (2, 3): 10,
                            (3, 3): 11,
                            (4, 3): 12,
                            (1, 4): 13,
                            (2, 4): 14,
                            (3, 4): 15,
                            (4, 4): 16,
                        }
                        newlisX = []
                        newlisO = []
                        for i in lister2:
                            if lister2.index(i) % 4 == 0 or lister2.index(i) % 4 == 1:
                                newlisX.append(dicter[i])
                            else:
                                newlisO.append(dicter[i])
                        for k in range(1, 5):
                            count = 0
                            for m in range(0, 4):
                                if k + m * 4 in newlisX:
                                    count += 1
                            if count == 4:
                                return "X"
                                break
                        else:
                            for k in range(1, 5):
                                count = 0
                                for m in range(0, 4):
                                    if k + m * 4 in newlisO:
                                        count += 1
                                if count == 4:
                                    return "O"
                                    break
                            else:
                                macX = list(newlisX)
                                macO = list(newlisO)
                                macX.sort()
                                macO.sort()
                                for a in range(1, 17, 4):
                                    if range(a, a + 5) in macX:
                                        return "X"
                                        break
                                    elif [a, a + 1, a + 2, a + 3, a + 4] in macO:
                                        return "O"
                                        break
                                else:
                                    if range(1, 21, 5) in macX:
                                        return "X"
                                    elif range(4, 16, 3) in macX:
                                        return "X"
                                    elif range(1, 21, 5) in macO:
                                        return "O"
                                    elif range(4, 16, 3) in macO:
                                        return "O"
                                    else:
                                        return False

                    lis = []
                    graphic(lis)
                    for l in range(1, 9):
                        if l % 2 == 1:
                            x1 = eval(input("\t\tEnter x1: "))
                            x2 = eval(input("\t\tEnter x2: "))
                            lis.append(x1)
                            lis.append(x2)
                            graphic(lis)
                            if endgame(lis):
                                print("\t\t", endgame(lis), "won the game.")
                                name_scores[nowuser][0] += 7
                                name_scores[nowuser][1] += 1
                                break
                        else:
                            O1 = eval(input("Enter O1: "))
                            O2 = eval(input("Enter O2: "))
                            lis.append(O1)
                            lis.append(O2)
                            graphic(lis)
                            if endgame(lis):
                                print("\t\t", endgame(lis), "won the game.")
                                name_scores[nowuser][0] -= 5
                                name_scores[nowuser][2] += 1
                                break
                    else:
                        print("\t\tTie")
                        name_scores[nowuser][0] += 0
                        name_scores[nowuser][3] += 1

                play4()
                a = nowuser
                input("\t\tPRESS ENTER TO GO BACK TO MENU")
            if user3 == "5":
                print("\n\n\n")
                import random

                def graphic(t, n):
                    if n <= 20:
                        print("||   " * n)
                        print("||   " * n)
                        print("||   " * n)
                        print("||   " * n)
                    elif n <= 40:
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * (n - 20))
                        print("||   " * (n - 20))
                        print("||   " * (n - 20))
                        print("||   " * (n - 20))
                    elif n <= 60:
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * (n - 40))
                        print("||   " * (n - 40))
                        print("||   " * (n - 40))
                        print("||   " * (n - 40))
                    elif n <= 80:
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * (n - 60))
                        print("||   " * (n - 60))
                        print("||   " * (n - 60))
                        print("||   " * (n - 60))
                    else:
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("||   " * 20)
                        print("\n\n")
                        print("||   " * (n - 80))
                        print("||   " * (n - 80))
                        print("||   " * (n - 80))
                        print("||   " * (n - 80))
                    print("\n\n\t\tNUMBER OF STICKS REMAINING:", n)
                    print("\t\tNUMBER OF STICKS REMOVED:", (t - n), "\n\n")

                print("\t\tWELCOME TO THE STICK GAME. YOU ARE UP AGAINST COMPUTER.")
                print("\t\tBEWARE!! THE COMPUTER IS A PRO AT THIS GAME.")
                print(
                    "\t\tTHE PLAYER AND THE COMPUTER WILL BOTH REMOVE SOME STICKS \n\t\tWITH A MUTUALLY DECIDED UPPER LIMIT IN THEIR TURN"
                )
                print(
                    "\t\tYOU WIN IF COMPUTER REMOVES LAST STICK AND LOSE IF YOU REMOVE THE LAST STICK.\n\n"
                )
                print("\t\tLET THE GAME BEGIN\n\n")
                x = 1
                while x == 1:
                    total = input("\t\tEnter how many total sticks at start: ")
                    if total.isdigit() and int(total) in range(1, 100):
                        total = int(total)
                        x = 0
                    else:
                        if not total.isdigit():
                            print("\t\tPlease enter a number.")
                        else:
                            print("\t\tThe number should be less than 100")
                x = 1
                while x == 1:
                    max_sticks = input(
                        "\t\tEnter how many max sticks allowed to remove per turn: "
                    )
                    if max_sticks.isdigit() and int(max_sticks) in range(2, 20):
                        max_sticks = int(max_sticks)
                        x = 0
                    else:
                        if not max_sticks.isdigit():
                            print("\t\tPlease enter a number.")
                        else:
                            print("\t\tThe number should be less than 20")
                lis = []
                for i in range(total - 1, -1, -(max_sticks + 1)):
                    lis.append(i)
                lis = lis[::-1]
                r = random.randint(0, 1)
                if r == 1:
                    print("\t\tYou will start first.")
                else:
                    print("\t\tI will start first.")
                now = total
                graphic(total, now)
                ctr = 1
                while now != 0:
                    if ctr % 2 == r:
                        x = 1
                        while x == 1:
                            remove = input(
                                "\t\tEnter how many sticks you want to remove: "
                            )
                            if (
                                remove.isdigit()
                                and int(remove) in range(1, max_sticks + 1)
                                and int(remove) <= now
                            ):
                                remove = int(remove)
                                x = 0
                            else:
                                if not remove.isdigit():
                                    print("\t\tPlease enter a number.")
                                else:
                                    print(
                                        "\t\tThe number should be less than",
                                        max_sticks + 1,
                                    )
                        now -= remove
                        if now == 0:
                            print("\t\tCOMPUTER WON....")
                            print("\t\tI TOLD YOU... YOU WILL NEVER DEFEAT AI.")
                            name_scores[nowuser][0] -= 5
                            name_scores[nowuser][2] += 1
                            break
                        graphic(total, now)
                        ctr += 1
                    else:
                        removed = total - now
                        # print(removed)
                        if (
                            (ctr == 1 and lis[0] == 0)
                            or (random.randint(1, 1000) > 950)
                            or (removed in lis)
                        ):
                            if now > max_sticks:
                                remove = random.randint(1, max_sticks)
                            else:
                                remove = random.randint(1, now)
                        else:
                            removed1 = lis[((removed - lis[0]) // (max_sticks + 1)) + 1]
                            remove = removed1 - removed
                        print("\t\tComputer removed", remove, "sticks")
                        now -= remove
                        if now == 0:
                            print("\t\tCOMPUTER LOST....")
                            print("\t\tWOW!!!! You played excellently.")
                            name_scores[nowuser][0] += 10
                            name_scores[nowuser][1] += 1
                            break
                        graphic(total, now)
                        ctr += 1
            if user3 == "6":
                print("\t\tTHIS IS A GAME IN WHICH YOU PLAY AGAINST")
                print("\t\tYOUR LOCAL OPPONENT. YOU MAY PLAY AS THIEF")
                print("\t\tOR AS POLICE. THE POLICE CATCHES THE THIEF")
                print("\t\tUSE W A S D TO MOVE. THE BLOCKS ARE PLACES")
                print("\t\tWHERE THE THIEF CANNOT MOVE BUT THE POLICE CAN")
                print("\t\tTHEY SPAWN RANDOMLY IN THE MAP")

                import random

                def graphic(lister1, block):
                    r1 = ["   ", "   ", "   ", "   "]
                    r2 = ["   ", "   ", "   ", "   "]
                    r3 = ["   ", "   ", "   ", "   "]
                    r4 = ["   ", "   ", "   ", "   "]
                    maxr = [r1, r2, r3, r4]
                    for p in range(1, 5):
                        for q in range(1, 5):
                            if (p, q) in block:
                                maxr[q - 1][p - 1] = "BLK"
                    for p in range(1, 5):
                        for q in range(1, 5):
                            if (p, q) in lister1:
                                if lister1.index((p, q)) % 2 == 1:
                                    maxr[q - 1][p - 1] = " " + "#" + " "
                                else:
                                    maxr[q - 1][p - 1] = " " + chr(8106) + " "
                    print("\n\n")
                    print("\t\t     1          2           3           4")
                    print("\t\t   ___________________________________________ ")
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |          |          |          |          |")
                    print(
                        "\t\t1 |    ",
                        r1[0],
                        "   |   ",
                        r1[1],
                        "    |   ",
                        r1[2],
                        "    |   ",
                        r1[3],
                        "    |",
                        sep="",
                    )
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |__________|__________|__________|__________|")
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |          |          |          |          |")
                    print(
                        "\t\t2 |    ",
                        r2[0],
                        "   |   ",
                        r2[1],
                        "    |   ",
                        r2[2],
                        "    |   ",
                        r2[3],
                        "    |",
                        sep="",
                    )
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |__________|__________|__________|__________|")
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |          |          |          |          |")
                    print(
                        "\t\t3 |    ",
                        r3[0],
                        "   |   ",
                        r3[1],
                        "    |   ",
                        r3[2],
                        "    |   ",
                        r3[3],
                        "    |",
                        sep="",
                    )
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |__________|__________|__________|__________|")
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |          |          |          |          |")
                    print(
                        "\t\t4 |    ",
                        r4[0],
                        "   |   ",
                        r4[1],
                        "    |   ",
                        r4[2],
                        "    |   ",
                        r4[3],
                        "    |",
                        sep="",
                    )
                    print("\t\t  |          |          |          |          |")
                    print("\t\t  |__________|__________|__________|__________|")
                    print("\n\n")

                def changer(lister2, nowco):
                    nowco = list(nowco)
                    newco = [-1, -1]
                    for i in lister2:
                        if i == "w":
                            newco[1] = nowco[1] - 1
                        if i == "a":
                            newco[0] = nowco[0] - 1
                        if i == "s":
                            newco[1] = nowco[1] + 1
                        if i == "d":
                            newco[0] = nowco[0] + 1
                        newco = nowco
                    return tuple(nowco)

                xco = (1, 1)
                oco = (4, 4)
                bloclis = [(0, 0), (0, 0), (0, 0)]
                li1 = []
                graphic([(1, 1), (4, 4)], [])
                print("\n\n\t\tLET THE GAME BEGIN\n\n")
                for l in range(1, 10):
                    while True:
                        blockco1_1 = random.randint(1, 4)
                        blockco1_2 = random.randint(1, 4)
                        r = random.randint(1, 2)
                        if (
                            blockco1_1 != xco[0]
                            and blockco1_1 != oco[1]
                            and blockco1_2 != xco[1]
                            and blockco1_2 != oco[1]
                            and (not (r == 2 and (blockco1_1 == blockco1_2)))
                        ):
                            break
                    block1 = (blockco1_1, blockco1_1)
                    while True:
                        blockco2_1 = random.randint(1, 4)
                        blockco2_2 = random.randint(1, 4)
                        r = random.randint(1, 2)
                        if (
                            blockco2_1 != xco[0]
                            and blockco2_1 != oco[1]
                            and blockco2_2 != xco[1]
                            and blockco2_2 != oco[1]
                            and ((blockco2_1, blockco2_2) != (blockco1_1, blockco1_2))
                            and (not (r == 2 and (blockco2_1 == blockco2_2)))
                        ):
                            break
                    block2 = (blockco2_1, blockco2_1)
                    blocklis = [block1, block2]
                    graphic([xco, oco], blocklis)
                    for i in range(1, 3):
                        if i == 1:
                            pqr = "w"
                        else:
                            x = 1
                            while x == 1:
                                if l % 4 != 0:
                                    pqr = input(
                                        "\t\tEnter command to change Thief coordinates: "
                                    )
                                    if (
                                        (
                                            (pqr == "w" and xco[1] != 1)
                                            or (pqr == "a" and xco[0] != 1)
                                            or (pqr == "s" and xco[1] != 4)
                                            or (pqr == "d" and xco[0] != 4)
                                        )
                                        and changer([pqr, pqr], xco) != block1
                                        and changer([pqr, pqr], xco) != block2
                                    ):
                                        x = 0
                                    else:
                                        print("\t\tInvalid input")
                                        x = 1
                                else:
                                    print(
                                        "\t\tTHIEF'S ABILITY HAS ACTIVATED. ENTER ANY COORDINATE FOR THEIF TO TELEPORT--- EXAMPLE (1,1):  ",
                                        end="",
                                    )
                                    pqr = input("")
                                    if (
                                        pqr[0] == "("
                                        and pqr[1].isdigit()
                                        and (int(pqr[1]) in range(1, 5))
                                        and (pqr[2] == ",")
                                        and pqr[3].isdigit()
                                        and int(pqr[3]) in range(1, 5)
                                        and pqr[4] == ")"
                                    ):
                                        pqr == eval(pqr)
                                        xco = pqr
                        if i % 4 != 0:
                            li1.append(pqr)
                    xco = changer(li1, xco)
                    graphic([xco, oco], blocklis)
                    if xco == oco:
                        print("\t\tThief has been caught")
                        graphic([xco, oco], blocklis)
                        break

                    li1 = []

                    for i in range(1, 3):
                        if i == 1:
                            pqr = "w"
                        else:
                            x = 1
                            while x == 1:
                                pqr = input(
                                    "\t\tEnter command to change Police coordinates: "
                                )
                                if (
                                    (pqr == "w" and oco[1] != 1)
                                    or (pqr == "a" and oco[0] != 1)
                                    or (pqr == "s" and oco[1] != 4)
                                    or (pqr == "d" and oco[0] != 4)
                                ):
                                    x = 0
                                else:
                                    print("\t\tInvalid input")
                                    x = 1
                        li1.append(pqr)
                    oco = changer(li1, oco)
                    if xco == oco:
                        print("\t\tThief has been caught")
                        graphic([xco, oco], blocklis)
                        break
                    li1 = []
                else:
                    print("\t\tThief has won.")

            a = nowuser

        print(
            """        ##############################################################################
        #									     #
        #  ######   #    #   ######   #  #  #   ###      ######   #  #  #   #     #  #
        #  #        #    #   #    #   #  #  #   #  ##    #    #   #  #  #   # #   #  #
        #  ######   ######   #    #   #  #  #   #    #   #    #   #  #  #   #  #  #  #
        #       #   #    #   #    #   #  #  #   #  ##    #    #   #  #  #   #   # #  #
        #  ######   #    #   ######    ## ##    ###      ######    ## ##    #     #  #
        #									     #
        #	        ######    ####     ## ##    ######   ######		     #
        #	        #        #    #   #  #  #   #        #			     #
        #	        #  ###   ######   #  #  #   ####     ######		     #
        #	        #    #   #    #   #  #  #   #             #		     #
        #	        ######   #    #   #  #  #   ######   ######		     #
        #									     #
        ##############################################################################\n"""
        )
        print(
            """
                                               ,...................
                                             ,..................========
                                            ....~=##############=======+
                                           ...##################=======.
                                          ..=######+...,    +##=======,..
                                          ..=###### ., .....  +=====+,....
                                             ###########~,..  ======
                                          .....##############~=====+.....
                                          ..........###########====......
                                            ............#######,==......
                                          =###.,........+#####+ .......
                                          ####################~......,
                                          #################+======,
                                             ++++++++++++ =======+
                                             
             """
        )
        existplayers_and_pass = {
            "Sam": "pokemon",
            "TheLastLegend": "death",
            "Doom": "master123",
            "Winner": "wins55",
        }
        name_scores = {
            "Sam": [65, 10, 5, 6, ["Scorer", "Winno"]],
            "TheLastLegend": [80, 15, 7, 13, ["AI", "Quick"]],
            "Doom": [20, 5, 3, 9, []],
            "Winner": [40, 10, 6, 8, []],
        }  # This list contains total score,winning games,losing games,tied games,boosts active...... score=7*win -5*loss+0*tie
        events = [["Victor Event", "AI"], ["Draw Penalty", "Quick"]]  # event,prize
        offers = [["Scorer", "10$"], ["Winno", "5$"]]
        developers = {
            "Robin": "123456",
            "Arghya": "Rocket",
            "Himay": "ultimocaribou",
            "Neal": "Shah",
        }
        # PLS DESIGN CAPTCHA CODE PROFILE VIEW AND GAME.
        print()
        print()
        print("\t\t$$$$$$$$$$  WELCOME TO SHOWDOWN GAMES  $$$$$$$$$$")
        while True:
            print()
            print()
            print("\t\tPLEASE SELECT AN OPTION FROM THE GIVEN MENU.")
            print("\t\t1. EXISTING USER LOGIN")
            print("\t\t2. NEW USER SIGNUP")
            print("\t\t3. DEVELOPER LOGIN")
            print("\t\t4. LOGIN INCOGNITO AS GUEST (Your scores will not be saved)")
            print("\t\t5. EXIT")
            x = 1
            while x == 1:
                user = input("\t\tEnter Option: ")
                if (
                    user == "1"
                    or user == "2"
                    or user == "3"
                    or user == "4"
                    or user == "5"
                ):
                    x = 0
                else:
                    print("\t\tInvalid input.")
            if user == "2":
                print("\n\n\n")
                print(
                    "\t\tWELCOME TO USER SIGNUP. PLEASE ENTER YOUR NAME AND PASSWORD."
                )
                x = 1
                while x == 1:
                    a = input("\t\tEnter name or press enter key to go back: ")
                    if a == "":
                        break
                    elif a in existplayers_and_pass and a in name_scores:
                        print("\t\tThis name already exists. Please enter name again.")
                    elif len(a) >= 14:
                        print("\t\tName is too long.")
                    else:
                        x = 0
                if a == "":
                    continue
                b = input("\t\tEnter password or press enter key to go back: ")
                if b == "":
                    continue
                existplayers_and_pass[a] = b
                name_scores[a] = [0, 0, 0, 0, []]
                print(
                    "\t\tCongratulations!! You have added a game account to our server."
                )
                print("\t\tENTER ANY OF THE GIVEN OPTIONS.")
                print("\t\t1. MENU")
                print("\t\t2. EXIT")
                x = 1
                while x == 1:
                    user1 = input("\t\tEnter Option: ")
                    if user1 == "1" or user1 == "2":
                        x = 0
                    else:
                        print("\t\tInvalid input.")
                if user1 == "1":
                    continue
                if user1 == "2":
                    print("\t\tTHANKS FOR USING OUR GAME. BYE!!!")
                    break
            if user == "5":
                break
            if user == "1":
                print("\n\n\n")
                print("\t\tWELCOME TO EXISTING USER LOGIN\n\n")
                if user == "1":
                    print("\n\n\n")
                    a = input("\t\tEnter Username: ")
                    if a not in existplayers_and_pass and a not in name_scores:
                        print("\t\tInvalid name.")
                        continue
                    else:
                        b = input("\t\tEnter password: ")
                        if b != existplayers_and_pass[a]:
                            print("\t\tWrong password.")
                            continue
                        else:
                            nowuser = a
                    print("\t\tWELCOME", nowuser.upper())
                    while True:
                        print("\n\n\n")
                        print("\t\tPLEASE SELECT AN OPTION FROM THE GIVEN MENU: ")
                        print("\t\t1. MY PROFILE")
                        print("\t\t2. PLAY GAME")
                        print("\t\t3. SEE EVENTS")
                        print("\t\t4. SEE OFFERS")
                        print("\t\t5. SEE ACTIVE BOOSTS")
                        print("\t\t6. SEE LEADERBOARD")
                        print("\t\t7. EDIT PROFILE")
                        print("\t\t8. LOGOUT")
                        x = 1
                        while x == 1:
                            user2 = input("\t\tEnter Option: ")
                            if (
                                user2 == "1"
                                or user2 == "2"
                                or user2 == "3"
                                or user2 == "4"
                                or user2 == "5"
                                or user2 == "6"
                                or user2 == "7"
                                or user2 == "8"
                            ):
                                x = 0
                            else:
                                print("\t\tInvalid input.")
                        if user2 == "1":
                            print("\n\n\n")
                            print("\t\tPLAYER NAME: ", a)
                            print("\t\tCURRENT PASSWORD: ", existplayers_and_pass[a])
                            print("\t\tGAMES WON: ", name_scores[a][1])
                            print("\t\tGAMES LOST: ", name_scores[a][2])
                            print("\t\tGAMES TIED: ", name_scores[a][3])
                            print("\t\tTOTAL SCORE: ", name_scores[a][0])
                            if name_scores[a][2] != 0:
                                print(
                                    "\t\tWIN LOSS RATIO: ",
                                    str(name_scores[a][1] / name_scores[a][2])[:4],
                                )
                            else:
                                print("\t\tWIN LOSS RATIO: NA")
                            print()
                            print()
                            input("\t\tPress enter key to go back to player menu.")
                            print()
                            print()
                            continue
                        elif user2 == "3":
                            print("\n\n\n")
                            print("\t\tHERE ARE THE EVENTS THAT ARE ACTIVE NOW.")
                            print("\t\tPLAY HARD TO WIN AMAZING BOOSTS.")
                            for i in events:
                                print("\t\tEVENT: ", i[0], "   PRIZE: ", i[1])
                            print()
                            print()
                            input("\t\tPress enter key to go back to menu.")
                            print()
                            print()
                            continue
                        elif user2 == "4":
                            print("\n\n\n")
                            print(
                                "\t\tHERE ARE THE OFFERS WHICH ARE AVAILABLE IN THE SHOP."
                            )
                            q = 1
                            ml = []
                            for i in range(len(offers)):
                                if offers[i][0] not in name_scores[a][4]:
                                    print(
                                        "\t\t" + (str(q) + "." + " BOOST:"),
                                        offers[i][0],
                                        "   PRICE:",
                                        offers[i][1],
                                    )
                                    ml.append(offers[i][0])
                                    q += 1
                            if ml == []:
                                print("\t\t<There are no offers now.>")
                            print("\t\tPLEASE SELECT FROM THE OPTIONS:")
                            i = 0
                            for i in range(1, len(ml) + 1):
                                print("\t\t" + str(i) + ". " + "BUY OFFER " + str(i))
                            print("\t\t" + str(i + 1) + ".", "BACK TO PLAYER MENU")
                            x = 1
                            while x == 1:
                                user3 = input("\t\tEnter Option: ")
                                if user3.isdigit() and int(user3) in range(
                                    1, len(ml) + 2
                                ):
                                    x = 0
                                else:
                                    print("\t\tInvalid input.")
                            if int(user3) == len(ml) + 1:
                                print()
                                print()
                                continue
                            else:
                                print("\t\tYOU HAVE BOUGHT AN OFFER!!!")
                                name_scores[a][4].append(ml[int(user3) - 1])
                                input("\t\tPRESS ENTER TO GO TO PLAYER MENU")
                                print()
                                print()
                                continue
                        elif user2 == "5":
                            print("\n\n\n")
                            print("\t\tHERE ARE YOUR ACTIVE BOOSTS:")
                            for i in name_scores[a][4]:
                                print("\t\t", i.upper())
                            if name_scores[a][4] == []:
                                print("\t\t<You have no active boosts.>")
                            input("\t\tPress enter to return to player menu.")
                            print()
                            print()
                            continue
                        elif user2 == "6":
                            print("\n\n\n")
                            print(
                                "\t\tHERE IS THE GAME LEADERBOARD. THE TOP PLAYER AT THE END OF THE MONTH \n\t\tWILL WIN AN EXCITING PRIZE.\n\n"
                            )
                            nu = list(name_scores.items())
                            templist = []
                            for i, j in nu:
                                templist.append([j[0], i])
                            templist.sort()
                            templist = templist[::-1]
                            print(
                                "\t\t"
                                + " " * 5
                                + "Name:"
                                + " " * 5
                                + " " * 2
                                + "Score:"
                                + " " * 2
                            )
                            ctr = 0
                            for i in templist:
                                ctr += 1
                                print(
                                    "\t\t"
                                    + " " * ((15 - len(i[1])) // 2)
                                    + str(i[1])
                                    + " "
                                    * (
                                        ((15 - len(i[1])) // 2)
                                        + int(len(i[1]) % 2 == 0)
                                    ),
                                    end="",
                                )
                                print(
                                    " "
                                    * (
                                        ((8 - len(str(i[0]))) // 2)
                                        + int(len(str(i[0])) % 2 != 0)
                                    )
                                    + str(i[0])
                                    + " " * ((8 - len(str(i[0]))) // 2),
                                    end="",
                                )
                                if i[1] == a:
                                    print("         YOUR POSITION", end="")
                                    mr = ctr
                                print()
                            print()
                            print("\t\tYOUR RANK: ", mr)
                            input("\t\tPRESS ENTER KEY TO GO BACK TO MENU")
                            continue
                        elif user2 == "8":
                            print("\n\n\n")
                            if (
                                input("\t\tAre you sure you want to go back (y/n): ")
                                == "y"
                            ):
                                break
                            else:
                                continue
                        elif user2 == "2":
                            print("\n\n\n")
                            playgames()
                        elif user2 == "7":
                            print("\n\n\n")
                            print("\t\tWHAT DO YOU WANT TO CHANGE:")
                            print("\t\t1.USERNAME")
                            print("\t\t2.PASSWORD")
                            while True:
                                ino = input("\t\tENTER OPTION OR ENTER TO EXIT: ")
                                if ino == "1" or ino == "2" or ino == "":
                                    break
                                else:
                                    print("Invalid option.")
                            if ino == "":
                                continue
                            if ino == "1":
                                while True:
                                    ino2 = input("\t\tPlease enter new name: ")
                                    if ino2 in existplayers_and_pass:
                                        print("\t\tName already exists")
                                    else:
                                        pass1 = existplayers_and_pass[nowuser]
                                        sco2 = name_scores[nowuser]
                                        del name_scores[nowuser]
                                        del existplayers_and_pass[nowuser]
                                        name_scores[ino2] = sco2
                                        existplayers_and_pass[ino2] = pass1
                                        nowuser = ino2
                                        a = ino2
                                        print(
                                            "\t\tYou have successfully changed your name."
                                        )
                                        input("\t\tPress enter to go back: ")
                                        break
                            elif ino == "2":
                                ino2 = input("\t\tPlease enter new password: ")
                                existplayers_and_pass[nowuser] = ino2
                                print(
                                    "\t\tYou have successfully changed your password."
                                )
                            continue

            if user == "4":
                print("\n\n\n")
                while True:
                    print("\n\n\t\tYOU HAVE LOGGED IN INCOGNITO AS GUEST.")
                    print("\t\tYOUR SCORES WILL NOT BE SAVED NOW.")
                    print("\t\tLOG IN AS AN USER TO GET MANY MORE FEATURES")
                    print("\t\tPLEASE SELECT ONE OF THE FOLLOWING OPTIONS")
                    print("\t\t1.PLAY GAMES")
                    print("\t\t2.LOGOUT\n\n")
                    name_scores["g1"] = [0, 0, 0, 0, []]
                    nowuser = "g1"
                    a = "g1"
                    x = 1
                    while x == 1:
                        user4 = input("\t\tEnter Option: ")
                        if user4 == "1" or user4 == "2":
                            x = 0
                        else:
                            print("\t\tInvalid input.")
                    if user4 == "1":
                        print("\n\n\n")
                        playgames()
                    else:
                        del name_scores["g1"]
                        break
            if user == "3":
                print("\n\n")
                print("\t\tWELCOME TO DEVELOPER LOGIN\n\n")
                p = input("\t\tEnter Username: ")
                if p not in developers:
                    print("\t\tInvalid name.")
                    continue
                else:
                    q = input("\t\tEnter password: ")
                    if q != developers[p]:
                        print("\t\tWrong password.")
                        continue
                    else:
                        nowdev = p
                print("\n\t\tWELCOME DEVELOPER", nowdev.upper())
                while True:
                    print("\n\n\n")
                    print("\t\tPLEASE SELECT AN OPTION FROM THE GIVEN MENU.")
                    print("\t\t1. VIEW ALL PROFILES")
                    print("\t\t2. START EVENT")
                    print("\t\t3. END EVENT")
                    print("\t\t4. LEADERBOARD")
                    print("\t\t5. ADD OFFER")
                    print("\t\t6. REMOVE OFFER")
                    print("\t\t7. SEE EVENTS")
                    print("\t\t8. SEE OFFERS")
                    print("\t\t9. EXIT")
                    x = 1
                    while x == 1:
                        user5 = input("\t\tEnter Option: ")
                        if (
                            user5 == "1"
                            or user5 == "2"
                            or user5 == "3"
                            or user5 == "4"
                            or user5 == "5"
                            or user5 == "6"
                            or user5 == "7"
                            or user5 == "8"
                            or user5 == "9"
                        ):
                            x = 0
                        else:
                            print("\t\tInvalid input.")
                    if user5 == "1":
                        print("\n\n\n")
                        print("\t\tPLEASE SELECT AN OPTION FROM THE GIVEN MENU.")
                        print("\t\t1. VIEW ALL PROFILES")
                        print("\t\t2. VIEW A SINGLE PROFILE")
                        print("\t\t3. BACK")
                        x = 1
                        while x == 1:
                            user6 = input("\t\tEnter Option: ")
                            if user6 == "1" or user6 == "2" or user6 == "3":
                                x = 0
                            else:
                                print("\t\tInvalid input.")
                        if user6 == "1":
                            print("\n\n\n")
                            for a in existplayers_and_pass:
                                print("\t\tPLAYER NAME: ", a)
                                print(
                                    "\t\tCURRENT PASSWORD: ", existplayers_and_pass[a]
                                )
                                print("\t\tGAMES WON: ", name_scores[a][1])
                                print("\t\tGAMES LOST: ", name_scores[a][2])
                                print("\t\tGAMES TIED: ", name_scores[a][3])
                                print("\t\tTOTAL SCORE: ", name_scores[a][0])
                                if name_scores[a][2] != 0:
                                    print(
                                        "\t\tWIN LOSS RATIO: ",
                                        str(name_scores[a][1] / name_scores[a][2])[:4],
                                    )
                                else:
                                    print("\t\tWIN LOSS RATIO: NA")
                                print()
                                print()
                                if (
                                    input(
                                        "\t\tPress enter key to go to next player or q to exit."
                                    )
                                    == "q"
                                ):
                                    break
                                print()
                                print()
                            continue
                        elif user6 == "2":
                            print("\n\n\n")
                            po = 1
                            while po == 1:
                                pq = input("\t\tEnter playername: ")
                                if pq not in existplayers_and_pass:
                                    print("\t\tInvalid username ")
                                    print("\t\tHere are the list of players.")
                                    for i in existplayers_and_pass:
                                        print(i)
                                    po = 1
                                else:
                                    print("\t\tPLAYER NAME: ", pq)
                                    print(
                                        "\t\tCURRENT PASSWORD: ",
                                        existplayers_and_pass[pq],
                                    )
                                    print("\t\tGAMES WON: ", name_scores[pq][1])
                                    print("\t\tGAMES LOST: ", name_scores[pq][2])
                                    print("\t\tGAMES TIED: ", name_scores[pq][3])
                                    print("\t\tTOTAL SCORE: ", name_scores[pq][0])
                                    if name_scores[pq][2] != 0:
                                        print(
                                            "\t\tWIN LOSS RATIO: ",
                                            str(
                                                name_scores[pq][1] / name_scores[pq][2]
                                            )[:4],
                                        )
                                    else:
                                        print("\t\tWIN LOSS RATIO: NA")
                                    print()
                                    print()
                                    input("\t\tPress enter key to go back")
                                    print()
                                    print()
                                    break
                                continue
                        elif user6 == "3":
                            continue
                    elif user5 == "2":
                        print("\n\n\n")
                        while True:
                            print(
                                "\t\tPLEASE ENTER NAME OF EVENT YOU WANT TO START OR ENTER TO EXIT."
                            )
                            eve = input("\t\t")
                            if eve == "":
                                break
                            elif eve == input("\t\tPLEASE CONFIRM NAME AGAIN:\n\t\t"):
                                print("\t\tPLEASE ENTER PRIZE OF EVENT:")
                                pri = input("\t\t")
                                if pri == input(
                                    "\t\tPLEASE CONFIRM PRIZE AGAIN:\n\t\t"
                                ):
                                    events.append([eve, pri])
                                    print("\t\tYou have added event.")
                                    break
                                else:
                                    print("\t\tPrize not confirmed")
                            else:
                                print("\t\tName not confirmed")
                    elif user5 == "3":
                        print("\n\n\n")
                        while True:
                            print(
                                "\t\tPLEASE ENTER NAME OF EVENT YOU WANT TO END OR ENTER TO EXIT."
                            )
                            eve = input("")
                            if eve == "":
                                break
                            elif eve == input("\t\tPLEASE CONFIRM NAME AGAIN:\n"):
                                for i in events:
                                    if i[0] == eve:
                                        del events[events.index(i)]
                                        fl = 1
                                    else:
                                        fl = 0
                                if fl == 1:
                                    print("\t\tYou have deleted event", eve)
                                    break
                                else:
                                    print("\t\tNo such event.")
                                    print("\t\tHere are the events.")
                                    for i in events:
                                        print("\t\t", i[0])

                            else:
                                print("\t\tName not confirmed")
                    elif user5 == "4":
                        print("\n\n\n")
                        print(
                            "\t\tHERE IS THE GAME LEADERBOARD. THE TOP PLAYER AT THE END OF THE MONTH \nWILL WIN AN EXCITING PRIZE.\n\n"
                        )
                        nu = list(name_scores.items())
                        templist = []
                        for i, j in nu:
                            templist.append([j[0], i])
                        templist.sort()
                        templist = templist[::-1]
                        print(
                            "\t\t"
                            + " " * 5
                            + "Name:"
                            + " " * 5
                            + " " * 2
                            + "Score:"
                            + " " * 2
                        )
                        ctr = 0
                        for i in templist:
                            ctr += 1
                            print(
                                "\t\t",
                                " " * ((15 - len(i[1])) // 2)
                                + str(i[1])
                                + " "
                                * (((15 - len(i[1])) // 2) + int(len(i[1]) % 2 == 0)),
                                end="",
                            )
                            print(
                                " "
                                * (
                                    ((8 - len(str(i[0]))) // 2)
                                    + int(len(str(i[0])) % 2 != 0)
                                )
                                + str(i[0])
                                + " " * ((8 - len(str(i[0]))) // 2),
                                end="",
                            )
                            print()
                        print("\n\n")
                    elif user5 == "9":
                        break
                    elif user5 == "5":
                        print("\n\n\n")
                        while True:
                            print(
                                "\t\tPLEASE ENTER NAME OF OFFER YOU WANT TO ADD OR ENTER TO EXIT."
                            )
                            eve = input("\t\t")
                            if eve == "":
                                break
                            elif eve == input("\t\tPLEASE CONFIRM OFFER AGAIN:\n\t\t"):
                                print("\t\tPLEASE ENTER PRICE OF OFFER:\n\t\t")
                                pri = input("\t\t") + "$"
                                if pri == (
                                    input("\t\tPLEASE CONFIRM PRICE OF OFFER:\n\t\t")
                                    + "$"
                                ):
                                    offers.append([eve, pri])
                                    print("\t\tYou have added an offer.")
                                    break
                                else:
                                    print("\t\tPrice not confirmed")
                            elif eve == "":
                                break
                            else:
                                print("\t\tOffer not confirmed")
                    elif user5 == "6":
                        print("\n\n\n")
                        while True:
                            print(
                                "\t\tPLEASE ENTER NAME OF OFFER YOU WANT TO REMOVE OR ENTER TO EXIT."
                            )
                            eve = input("\t\t")
                            if eve == "":
                                break
                            elif eve == input("\t\tPLEASE CONFIRM NAME AGAIN:\n"):
                                for i in offers:
                                    if i[0] == eve:
                                        del offers[offers.index(i)]
                                        fl = 1
                                    else:
                                        fl = 0
                                if fl == 1:
                                    print("\t\tYou have deleted offer", eve)
                                    break
                                else:
                                    print("\t\tNo such offer.")
                                    print("\t\tHere are names of offers:")
                                    for i in offers:
                                        print("\t\t", i[0])
                            elif eve == "":
                                break

                            else:
                                print("\t\tName not confirmed")
                    elif user5 == "8":
                        print("\n\n\n")
                        print("\t\tHERE ARE THE OFFERS AVAILABLE:\n")
                        for i in offers:
                            print("\t\tName:", i[0], "\t\tPrice:", i[1])
                        print()
                        input("\t\tPress enter to go back.")
                    elif user5 == "7":
                        print("\n\n\n")
                        print("\t\tHERE ARE THE CURRENT EVENTS: ")
                        for i in events:
                            print("\t\tName:", i[0], "\t\tPrize:", i[1])
                        print()
                        input("\t\tPress enter to go back.")
        os.system("taskkill /f /im wmplayer.exe")
        os.system("taskkill /im vlc.exe")
        break

    except:
        print("\t\tThe program crashed........")
        print("\t\tExecuting again............")
        continue
