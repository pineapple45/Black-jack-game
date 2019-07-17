import random

suits=('Diamond','Club','Hearts','spades')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'King':10,'Queen':10,'Jack':10,
        'Ace':11}
total = 0

class Deck():
    def __init__(self):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append((suit,rank))

        bet_amt = None

        self.deck = deck
        self.bet_amt = bet_amt


    def shuffle(self):
        random.shuffle(self.deck)


    def accounts(self):
        global total
        if total == 0:
            total = int(input('Enter the total balance in your account: '))
        else:
            print(f"Your current account balance is {total}")


        self.bet_amt = int(input('Enter the betting amount: '))
        if self.bet_amt > total:
            print(f'Insufficient Balance !!!')
            exit(0)
        else:
            pass







class Hand(Deck):



    def __init__(self):
        Deck.__init__(self)
        Deck.shuffle(self)
        Deck.accounts(self)

        dealer_list = []
        player_list = []
        self.dealer_list = dealer_list
        self.player_list = player_list

        player_list_1 = []
        player_list_2 = []

        self.player_list_1 = player_list_1
        self.player_list_2 = player_list_2

        temp1_list = []
        temp2_list = []

        self.temp1_list = temp1_list
        self.temp2_list = temp2_list

        dealer_sum = 0
        player_sum = 0
        self.dealer_sum = dealer_sum
        self.player_sum = player_sum


        k = 0
        self.k = k
        j = 0
        self.j = j
        p = 0
        self.p = p

        player_sum_1 = 0
        player_sum_2 = 0

        self.player_sum_1 = player_sum_1
        self.player_sum_2 = player_sum_2



    def distribute(self):

        global total

        for i in range(0,2):
            self.dealer_list.append(self.deck[i])

        for j in range(2,4):
            self.player_list.append(self.deck[j])

        print("Dealers_Cards: ")
        print(self.dealer_list[0])
        self.dealer_sum = values[self.dealer_list[0][1]]
        print(self.dealer_sum)


        print("Players_Cards: ")

        self.player_sum = values[self.player_list[0][1]] + values[self.player_list[1][1]]
        print(self.player_list)
        print(self.player_sum)
        if (self.player_list[0][1] == 'Ace' and values[self.player_list[1][1]] == 10) or\
                (self.player_list[1][1] == 'Ace' and values[self.player_list[0][1]] == 10):
            print("BLACKJACK!!")
            total = total + self.bet_amt * 1.5
            print(f"total money is {total}")
            clear()
            cont()




    def hit(self):
                    global total

                    t = 0

                    if self.player_list_2 != []:
                        t = self.k

                    for i in range(len(self.dealer_list)+ 2 + t , 53):
                        ans = input('Do you want to hit(h)/stand(s)? ')

                        if ans.lower() == 'h':
                            self.player_list.append(self.deck[i])
                            self.player_sum += (values[self.deck[i][1]])
                            print("Players_Cards: ")
                            print(self.player_list)
                            print(self.player_sum)

                            if self.player_list_2 == []:
                                self.k += 1
                            else:
                                self.j += 1

                            if self.player_sum > 21:
                                print("It is the players Bust")
                                total = total-self.bet_amt
                                print(f"total money left is {total}")
                                if self.player_list[1] != self.deck[3]:
                                    return

                                else:
                                    clear()
                                    cont()

                        elif ans.lower() == 's':
                            break



    def stand(self):
        global total

        print("Dealers_Cards: ")
        print(self.dealer_list)

        self.dealer_sum = values[self.dealer_list[0][1]] + values[self.dealer_list[1][1]]
        print(self.dealer_sum)

        if (self.dealer_list[0][1] == 'Ace' and values[self.dealer_list[1][1]] == 10) or (self.dealer_list[1][1] == 'Ace' and values[self.dealer_list[0][1]] == 10):
            print("BLACKJACK!!")

        p = 0

        if self.player_list_2 == []:
            p  = self.k + self.j

        if self.dealer_sum<17:

            if self.player_list_2 == []:

                for i in range(len(self.player_list)-1+2 , 53):
                    self.dealer_list.append(self.deck[i])
                    self.dealer_sum += values[self.deck[i][1]]
                    if (self.dealer_sum<17):
                        print(self.dealer_list)
                        print(self.dealer_sum)
                        continue
                    elif(self.dealer_sum>=17):
                        print(self.dealer_list)
                        print(self.dealer_sum)
                        break
            else:
                for i in range(len(self.player_list_1)+len(self.player_list_2)+2 , 53):
                    self.dealer_list.append(self.deck[i])
                    self.dealer_sum += values[self.deck[i][1]]
                    if (self.dealer_sum<17):
                        print(self.dealer_list)
                        print(self.dealer_sum)
                        continue
                    elif(self.dealer_sum>=17):
                        print(self.dealer_list)
                        print(self.dealer_sum)
                        break




        if (self.dealer_sum >=17 and self.dealer_sum < 21) and self.dealer_sum<self.player_sum and self.player_sum != 21:
            print("The player wins!!")
            total = total + self.bet_amt
            print(f"total money left is {total}")


        elif (self.dealer_sum >=17 and self.dealer_sum < 21) and self.dealer_sum>self.player_sum and self.player_sum != 21:
            print("The dealer wins!!")
            total = total-self.bet_amt
            print(f"total money left is {total}")

        elif (self.dealer_sum == 21 and self.player_sum != 21):

            print("The dealer wins!!")
            total = total - self.bet_amt
            print(f"total money left is {total}")
        elif (self.dealer_sum > 21):
            print("It is the dealers BUST!!")
            total = total + self.bet_amt
            print(f"total money left is {total}")
        elif (self.dealer_sum == self.player_sum):
            print("PUSH")
            print("The game is a draw. No money deducted or won!!")
            print(f"total money left is {total}")
        elif (self.player_sum == 21):

            print("The player wins!!")
            total = total + self.bet_amt
            print(f"total money left is {total}")

        if self.player_list_2 != []:
            return
        else:
            clear()
            cont()





class SpecialCond(Hand):
        def __init__(self):
            Hand.__init__(self)
            Hand.distribute(self)

            a = 0
            b = 0



            self.a = a
            self.b = b


        def insurance(self):
            global total
            if self.dealer_list[0][1] == 'Ace':
                answer = input("Do you want to take insurance?(Y/N)")
                if answer.lower() == 'y':
                    print("Dealers_Cards: ")
                    print(self.dealer_list)

                    self.dealer_sum = values[self.dealer_list[0][1]] + values[self.dealer_list[1][1]]


                    if (self.dealer_list[0][1] == 'Ace' and values[self.dealer_list[1][1]] == 10):
                        total = total + 2*(self.bet_amt/2) - self.bet_amt
                        print(f"The total balance in account is {total}")
                        print("BLACKJACK!!")
                        print("You won the insurance bet!! ")
                        print("EVEN MONEY!!")
                        clear()
                        cont()
                    elif (self.dealer_list[0][1] == 'Ace' and values[self.dealer_list[1][1]] != 10):
                        total = total - (self.bet_amt/2)
                        print("Insurance bet lost")

                        if self.dealer_sum >=17 and self.dealer_sum <21:
                            if self.dealer_sum > self.player_sum:
                                print("The dealer wins!!")
                                total = total - self.bet_amt
                                print(f"The total balance in account is {total}")
                                clear()
                                cont()
                            elif self.dealer_sum < self.player_sum:
                                print("The player wins!!")
                                total = total + self.bet_amt
                                print(f"The total balance in account is {total}")
                                clear()
                                cont()


                        elif self.dealer_sum <17:
                            SpecialCond.stand(self)
                elif answer.lower() =='n':
                    return
            else:
                return


        def double_down(self):

            if (self.player_sum == 9 and (values[self.dealer_list[0][1]] > 1 and values[self.dealer_list[0][1]] < 7 ))\
                    or (self.player_list[0][1] == 'Ace'
                    and (values[self.player_list[1][1]] == 5 or values[self.player_list[1][1]] == 6  or values[self.player_list[1][1]] == 7))\
                    or ((self.player_sum == 10 or self.player_sum == 11) and (self.player_list[0][1] != 'Ace' or self.player_list[1][1] != 'Ace') ):
                answer = input("Do you want to double down (Y/N)? ")
                if answer.lower() == 'y':

                    self.player_list.append(self.deck[4])

                    print(self.player_list)
                    self.player_sum = self.player_sum + values[self.player_list[2][1]]
                    print(self.player_sum)
                    self.bet_amt = 2*self.bet_amt
                    if self.bet_amt >total:
                        print("Not enough sufficient funds for doubling the bet")
                        clear()
                        cont()

                    print("The bet amount is doubled")
                    SpecialCond.stand(self)


                elif answer.lower() == 'n':
                    return

        def split(self):
            if values[self.player_list[0][1]] == values[self.player_list[1][1]]:
                ans = input("Do you want to split(Y/N): ")
                if ans.lower() == 'y':
                    print('\n')
                    print("This is phase 1")
                    self.temp1_list = self.player_list
                    self.temp2_list = self.player_list

                    self.player_sum_1 = self.player_sum - values[self.temp1_list[1][1]]
                    self.player_sum_2 = self.player_sum - values[self.temp1_list[0][1]]

                    self.player_list_1.append(self.temp1_list[0])


                    self.player_sum = self.player_sum_1
                    self.player_list = self.player_list_1
                    SpecialCond.hit(self)
                    self.a = self.player_sum
                    print('\n')








                    print("This is phase 2")
                    self.player_sum = self.player_sum_2
                    self.player_list_2.append(self.temp2_list[1])
                    self.player_list = self.player_list_2
                    SpecialCond.hit(self)
                    self.b = self.player_sum
                    print('\n')
                    print("Result for phase 2")
                    print(f"The player sum of player_list_1 is: {self.b}")
                    if self.b > 21:
                        pass
                    else:
                        SpecialCond.stand(self)
                    self.player_sum = self.b
                    print("\n")
                    print("Result for phase 1")
                    print(f"The player sum of player_list_2 is: {self.a}")
                    if self.a > 21:
                        pass
                    else:
                        SpecialCond.stand(self)
                    clear()
                    cont()




def clear():
    print('\n'*5)



def cont():

    answer = input('Do you want to play again? (Y/N) ')

    if answer.lower() == 'y':
        special = SpecialCond()
        special.insurance()
        special.double_down()
        special.split()
        special.hit()
        special.stand()
    else:
        exit(0)



def start():
    answer = input('Do you want to play BLACKJACK? (Y/N) ')
    if answer.lower() == 'y':

        special = SpecialCond()
        special.insurance()
        special.double_down()
        special.split()
        special.hit()
        special.stand()

    else:
        exit(0)




def begin():
    print('\n')
    print(' '*40," WELCOME TO BLACKJACK")
    print(' '*40,"-----------------------")
    start()


begin()
