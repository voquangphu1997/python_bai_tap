print("""
    Chao mung ban den voi game chon so 1, 2, 3
    Qui tac: ban vs may neu ai chon sao cho:
    Tong cuoi cung lon hon 21 thi nguoi lam cho tong lon hon se thua
""")

from random import randint

play_conti = "y"
while "y" in play_conti:
    current_number = 0
    while current_number <=21:
        turn = randint(1, 2)
        if turn == 1:
            player = input("Player: ")
            while (int(player) in range(1,4)) == False:
                player = input("Retype Player(only 1,2,3): ")
            current_number += int(player)
        else:
            computer = randint(1,3)
            print("computer: " + str(computer))
            current_number += computer
    print("current number: " + str(current_number))
    if turn ==1:
        print("Computer wins")
    else:
        print("Player wins")
    play_conti = input("Choi tiep ko: y (yes) or n(no)")
    while (("y"and"n") in play_conti) == False:
                play_conti = input("Only retype y(yes) or n(no) to continue: ")
print("good bye!")