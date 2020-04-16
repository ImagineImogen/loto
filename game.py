import random
import player

class Game:
    def index_2d(self, mylist, val):
        """
        Finds the index of a specific value in a 2D-list (sublist).
        
        Input:
        - mylist: two-dimensional list (list with sublists)
        - val: value to find the index
        Output:
        - postn: index of the value in the list
        """
        for i in range(len(mylist)):
            for j in range(len(mylist[i])):
                if mylist[i][j] == val:
                    postn = [i, j]
        return postn[0], postn[1]

    def check_keg(self, keg, table, list):
        """
        Checks if the keg is in the card of the player.
        If the keg corresponds, the number is put in brackets.
        
        Input:
        - table: card of the player
        - list: list containing numbers from the card
        Output: updated card and list
        """
        if "_" + str(keg) + "_" in table:
            table = table.replace("_" + str(keg) + "_", "[" + str(keg) + "]")
            l,m = self.index_2d(list, str(keg))
            list[l][m] = "[" + str(keg) + "]"
        return table, list

    def winner(self, list, win=0):
        """
        Input:
        - list: list containing numbers from the card
        Output:
        - win: boolean-type variable (1 = won, 0 = has not won)
        """
        if all(elem.startswith("[") or elem.startswith("_") for elem in list):
            win = 1
        return win


class Play(Game):
    def __init__(self, kegs, player_1, player_2, player_1_list, player_2_list):
        self.__kegs = kegs
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_list = player_1_list
        self.player_2_list = player_2_list
    
    def is_winner(self, player):
        """
        Displays who is the winner of the game.
        
        Input:
        - player: player's number (player 1, player 2, etc.)
        """
        print("\nPlayer " + str(player) + " won!\n")

    def finished(self, list, player, win=0):
        """
        Verifies if the player won.
        
        Input:
        - list: list containing numbers from the player's card
        - player: player's number (player 1, player 2, etc.)
        Output:
        - win: returns 1 if the player has won.
        """
        for x in range(len(list)):
            if Game.winner(self, list[x]):
                win = 1
                self.is_winner(player)
        return win


    def withdraw(self):
        """
        Creates the bag of n kegs.
        
        Input:
        - self.__kegs: maximum number of kegs to be withdrawn
        Output:
        - bag: bag of n unique kegs
        """
        self._bag = random.sample(range(1, self.__kegs), self.__kegs-1)
        return self._bag
        

    def play(self, win=0):
        """
        Main function of the LOTO game.
        Withdraws a keg and fill out the player's card if corresponds.
        
        Input:
        - kegs: maximum number of kegs to be withdrawn
        - player_1: player 1 card game
        - player_2: player 2 card game
        - player_1_list: list containing player 1 card numbers
        - player_2_list: list containing player 2 card numbers
        Output:
        - player_1: updated player 1 card game
        - player_2: updated player 2 card game
        """
        self.bag = self.withdraw()
        
        while not win:
            keg = self.bag[0]
            print("Step #" + str(100-len(self.bag)) + "\tKeg withdrawn:", keg)
            
            self.player_1, self.player_1_list = Game.check_keg(self, keg, self.player_1, self.player_1_list)
            self.player_2, self.player_2_list = Game.check_keg(self, keg, self.player_2, self.player_2_list)

            print("\nPlayer 1")
            print(self.player_1)
            print("\n")
            print("Player 2")
            print(self.player_2)
            print("\n")
            
            win = self.finished(self.player_1_list, 1) or self.finished(self.player_2_list, 2)
            
            self.bag.remove(keg)
            
            if len(self.bag) == 0:
                print("\nEnd of the game! The bag is empty.\n")
                break

        return self.player_1, self.player_2
    
