import random
from os import system, name

class Check:
    def check_card(self, list):
        """
        Checks if the card has 5 numbers per row.
        
        Input:
        - list: list containing numbers from the player's card
        Output: updated card and list with 5 numbers per row
        """
        for i in range(len(list)):
            count = list[i].count('__')
            if count < 4:
                for j in range(4-count):
                    a = random.randrange(len(list[i])-3)
                    if list[i][a].isdigit():
                        list[i][a] = "__"
                    else:
                        try:
                            list[i][a+1] = "__"
                        except:
                            list[i][a+2] = "__"
                        finally:
                            try:
                                list[i][a+3] = "__"
                            except:
                                list[i][a-1] = "__"
                        pass
            elif count > 4:
                for j in range(count-4):
                    a = random.randrange(len(list[i])-3)
                    if list[i][a].isdigit():
                        try:
                            list[i][a+1] = str(random.randrange(1,99))
                        except:
                            list[i][a+2] = str(random.randrange(1,99))
                        finally:
                            try:
                                list[i][a+3] = str(random.randrange(1,99))
                            except:
                                list[i][a-1] = str(random.randrange(1,99))
                            pass
                    else:
                        list[i][a] = str(random.randrange(1,99))
        return list


class Player(Check):
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
    
    def card_making(self):
        """
        Creates a card game with a size rows x columns. 
        
        Input:
        - columns: number of columns for the card game
        - rows: number of rows for the card game
        Output:
        - row: card game
        - row_list: card game numbers listed in a list object
        """
        new_card = [[random.randrange(1,100) for x in range(self.rows)] for y in range(self.columns)]
        l = [[0 for x in range(self.rows)] for y in range(self.columns)]

        for i in range(self.columns):
            for j in range(self.rows):
                new_card[i][j] = self.blank(new_card[i][j])
                l[i][j] = str(new_card[i][j])

        l = [l[0] + l[1] + l[2],
             l[3] + l[4] + l[5],
             l[6] + l[7] + l[8]]

        self.row_list = Check.check_card(self, l)
        self.row = self.card(self.row_list)

        return self.row, self.row_list
    
    def card(self, list):
        """
        Creates the card game for the player. 
        
        Input:
        - list: considered list containing player's card numbers
        Output: card
        """
        card = ""
        for i in range(len(list)):
            for j in range(len(list[i])):
                card = self.display(j, len(list[i]), list[i][j], card)
        return card

    def blank(self, item):
        """
        Randomly puts or not no number in the card, expressed as '__'. 
        
        Input:
        - item: item of the player's card
        Output: updated item
        """
        boolean = random.randint(0, 1)
        if boolean == 1:
            item = '__'
        return item

    def card(self, list):
        """
        Creates the card game for the player. 
        
        Input:
        - list: considered list containing player's card numbers
        Output: card
        """
        self.card = ""
        for i in range(len(list)):
            for j in range(len(list[i])):
                self.card = self.display(j, list[i][j], self.card)
        return self.card

    def display(self, a, item, row):
        """
        Modifies the string message to be displayed to make
        it homogeneous, in order to have a 3x9 card. 
        
        Input:
        - a: index number in the card's row
        - columns: columns of the card
        - item: specific item in the card of the player (seen as matrix POV)
        - row: card of the player
        Output: updated row
        """
        if a <= 8 and item != '__':
            if int(item) > self.columns:
                row += "|___" + str(item) + "__|"
            else:
                row += "|___" + str(item) + "___|"
        elif a <= 8 and item == '__':
            row += "|___" + str(item) + "__|"
        else:
            row += "\n"
        return row
