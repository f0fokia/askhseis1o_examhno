import random

player1_wins = 0
player2_wins = 0
draws = 0
for times in range(1, 101):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])

    random.shuffle(xartia)
    player1 = []
    sum1 = 0
    while sum1 < 16:
        sum1 = 0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]
    if sum1 > 21:
        player2_wins = player2_wins + 1
    else:
        player2 = []
        sum2 = 0
        while sum2 < 16:
            sum2 = 0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2 + 10
                else:
                    sum2 = sum2 + card[0]
        if sum2 > 21:
            player1_wins = player1_wins + 1
        else:
            if sum1 > sum2:
                player1_wins = player1_wins + 1
            elif sum2 > sum1:
                player2_wins = player2_wins + 1
            else:
                draws = draws + 1

print("Player 1 wins:", player1_wins)
print("Player 2 wins:", player2_wins)
print("Draws:", draws)

print("if the player 1 started only with the cards 10 or J,Q,K and player 2 with any number exept 10")

import random

player1_wins = 0
player2_wins = 0
draws = 0
for times in range(1, 101):
    xartia = []
    xartia_p1 = []
    xartia_p2 = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    xarti_p1 = [i for i in range(10, 11)] + figures
    xarti_p2 = [i for i in range(1, 10)]
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    for i in xarti_p1:
        for j in color:
            xartia_p1.append([i, j])
    for i in xarti_p2:
        for j in color:
            xartia_p2.append([i, j])
    random.shuffle(xartia)
    random.shuffle(xartia_p1)
    random.shuffle(xartia_p2)
    player1 = []
    sum1 = 0
    my_boolean_p1 = True
    while sum1 < 16:
        sum1 = 0
        if my_boolean_p1:
            player1.append(xartia_p1.pop())
            for card in player1:
                if card[0] in figures:
                    sum1 = sum1 + 10
                else:
                    sum1 = sum1 + card[0]
            xartia.remove(card)
            my_boolean_p1 = False
        else:
            player1.append(xartia.pop())
            for card in player1:
                if card[0] in figures:
                    sum1 = sum1 + 10
                else:
                    sum1 = sum1 + card[0]
    if sum1 > 21:
        player2_wins = player2_wins + 1
    else:
        player2 = []
        sum2 = 0
        my_boolean_p2 = True
        while sum2 < 16:
            sum2 = 0
            if my_boolean_p2:
                player2.append(xartia_p2.pop())
                for card in player2:
                    if card[0] in figures:
                        sum2 = sum2 + 10
                    else:
                        sum2 = sum2 + card[0]
                        # xartia.remove(card)
                my_boolean_p1 = False
            else:
                player2.append(xartia.pop())
                for card in player2:
                    if card[0] in figures:
                        sum2 = sum2 + 10
                    else:
                        sum2 = sum2 + card[0]
        if sum2 > 21:
            player1_wins = player1_wins + 1
        else:
            if sum1 > sum2:
                player1_wins = player1_wins + 1
            elif sum2 > sum1:
                player2_wins = player2_wins + 1
            else:
                draws = draws + 1

print("Player 1 wins:", player1_wins)
print("Player 2 wins:", player2_wins)
print("Draws:", draws)