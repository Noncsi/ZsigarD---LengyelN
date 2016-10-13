import sys
import time
running = True
counter_top = False
counter_middle = False
counter_bottom = False

#the board
top_row = ["7", "8", "9"]
middle_row = ["4", "5", "6"]
bottom_row = ["1", "2", "3"]

def grid(): #print board
    print(str(top_row) + "\n" + str(middle_row) + "\n" + str(bottom_row))              

def end_game(): # defines the end of the game--> restart = y, quit = n
    global top_row
    global middle_row
    global bottom_row
    global counter_top
    global counter_middle
    global counter_bottom
    counter_top = False
    counter_middle = False
    counter_bottom = False
    choice = input("New Game? (y/n): ")
    if choice == "y":        
        bottom_row[0] = "1"
        bottom_row[1] = "2"
        bottom_row[2] = "3"
        middle_row[0] = "4"
        middle_row[1] = "5"
        middle_row[2] = "6"
        top_row[0] = "7"
        top_row[1] = "8"
        top_row[2] = "9"
        game()
        
    elif choice == "n":
        sys.exit()

def counter_tr():               # defines in the top row if all of the field are occupied
    global top_row              # by at least 1 different character among them
    global counter_top
    global count1

    for i in range(3):
        count1 = 0
        if top_row[0] == "\U0001F435" or top_row[0] == "\U0001F34C":
            count1 = count1 + 1                       
        if top_row[1] == "\U0001F435" or top_row[1] == "\U0001F34C":
            count1 = count1 + 1                       
        if top_row[2] == "\U0001F435" or top_row[2] == "\U0001F34C":
            count1 = count1 + 1                       
        if count1 == 3:
            counter_top = True
        
                    
def counter_mr():              # defines in the top row if all of the field are occupied
    global middle_row          # by at least 1 different character among them
    global counter_middle
    global count2
    for i in range(3):
        count2 = 0
        if middle_row[0] == "\U0001F435" or middle_row[0] == "\U0001F34C":
            count2 = count2 + 1
        if middle_row[1] == "\U0001F435" or middle_row[1] == "\U0001F34C":
            count2 = count2 + 1
        if middle_row[2] == "\U0001F435" or middle_row[2] == "\U0001F34C":
            count2 = count2 + 1
        if count2 == 3:
            counter_middle = True
        break

            
def counter_br():           # defines in the top row if all of the field are occupied
    global bottom_row       # by at least 1 different character among them
    global counter_bottom
    global count3
    for i in range(3):
        count3 = 0
        if bottom_row[0] == "\U0001F435" or bottom_row[0] == "\U0001F34C":
            count3 = count3 + 1
        if bottom_row[1] == "\U0001F435" or bottom_row[1] == "\U0001F34C":
            count3 = count3 + 1
        if bottom_row[2] == "\U0001F435" or bottom_row[2] == "\U0001F34C":
            count3 = count3 + 1
        if count3 == 3:
            counter_bottom = True
        break
            

def win(): # defines what will happen if a player won: calls end_game() ---> restart\quit
    #player1 (monkey)
    #rows
    if  top_row[0] == "\U0001F435" and top_row[1] == "\U0001F435" and top_row[2] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()    

    if middle_row[0] == "\U0001F435" and middle_row[1] == "\U0001F435" and middle_row[2] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()

    if bottom_row[0] == "\U0001F435" and bottom_row[1] == "\U0001F435" and bottom_row[2] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()
    #corners
    if top_row[0] == "\U0001F435" and middle_row[1] == "\U0001F435" and bottom_row[2] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()

    if top_row[2] == "\U0001F435" and middle_row[1] == "\U0001F435" and bottom_row[0] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()
    #columns
    if top_row[0] == "\U0001F435" and middle_row[0] == "\U0001F435" and bottom_row[0] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()

    if top_row[1] == "\U0001F435" and middle_row[1] == "\U0001F435" and bottom_row[1] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()

    if top_row[2] == "\U0001F435" and middle_row[2] == "\U0001F435" and bottom_row[2] == "\U0001F435":
        print("\n" "Player 1 won!" "\n")
        end_game()

    #player2
    #rows
    if top_row[0] == "\U0001F34C" and top_row[1] == "\U0001F34C" and top_row[2] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()
    if middle_row[0]  == "\U0001F34C" and middle_row[1] == "\U0001F34C" and middle_row[2] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()
    if bottom_row[0] == "\U0001F34C" and bottom_row[1] == "\U0001F34C" and bottom_row[2] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()         
    #corners
    if top_row[0] == "\U0001F34C" and middle_row[1] == "\U0001F34C" and bottom_row[2] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()
    if top_row[2] == "\U0001F34C" and middle_row[1] == "\U0001F34C" and bottom_row[0] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()
    #columns
    if top_row[0] == "\U0001F34C" and middle_row[0] == "\U0001F34C" and bottom_row[0] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()
    if top_row[1] == "\U0001F34C" and middle_row[1] == "\U0001F34C" and bottom_row[1] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")   
        end_game()
    if top_row[2] == "\U0001F34C" and middle_row[2] == "\U0001F34C" and bottom_row[2] == "\U0001F34C":
        print("\n" "Player 2 won!" "\n")
        end_game()

#player1(monkey) fucntion 
def player1():
    print(" ")
    player_1 = input("\U0001F435 turn: ")
    print(" ")
    #top row of the board
    if player_1 == "7":
        if top_row[0] != "\U0001F435" and top_row[0] != "\U0001F34C":
            top_row[0] = "\U0001F435"
        else:
            player1()            
    elif player_1 == "8":
            if top_row[1] != "\U0001F435" and top_row[1] != "\U0001F34C":
                top_row[1] = "\U0001F435"
            else:
                player1()   
    elif player_1 == "9":
            if top_row[2] != "\U0001F435" and top_row[2] != "\U0001F34C":
                top_row[2] = "\U0001F435"
            else:
                player1()   
    # middle row of the board
    elif player_1 == "4":
            if middle_row[0] != "\U0001F435" and middle_row[0] != "\U0001F34C":
                middle_row[0] = "\U0001F435"
            else:
                player1()   
    elif player_1 == "5":
        if middle_row[1] != "\U0001F435" and middle_row[1] != "\U0001F34C":
            middle_row[1] = "\U0001F435"
        else:
            player1()   
    elif player_1 == "6":
        if middle_row[2] != "\U0001F435" and middle_row[2] != "\U0001F34C":
            middle_row[2] = "\U0001F435"
        else:
            player1()   
    #bottom row of the board
    elif player_1 == "1":
        if bottom_row[0] != "\U0001F435" and bottom_row[0] != "\U0001F34C":
            bottom_row[0] = "\U0001F435"
        else:
            player1() 
    elif player_1 == "2":
        if bottom_row[1] != "\U0001F435" and bottom_row[1] != "\U0001F34C":
            bottom_row[1] = "\U0001F435"
        else:
            player1() 
    elif player_1 == "3":
        if bottom_row[2] != "\U0001F435" and bottom_row[2] != "\U0001F34C":
            bottom_row[2] = "\U0001F435"
        else:
            player1() 
    else:
        print("Please use the numeric keyboard!",player_1)    
        player1()


#player2(banana) function
def player2():
    print(" ")
    player_2 = input("\U0001F34C turn: ")
    print(" ")
    #top row of the board
    if player_2 == "7":
        if top_row[0] != "\U0001F435" and top_row[0] != "\U0001F34C":
            top_row[0] = "\U0001F34C"
        else:
            player2() 
    elif player_2 == "8":
        if top_row[1] != "\U0001F435" and top_row[1] != "\U0001F34C":
            top_row[1] = "\U0001F34C"
        else:
            player2() 
    elif player_2 == "9":
        if top_row[2] != "\U0001F435" and top_row[2] != "\U0001F34C":
            top_row[2] = "\U0001F34C"
        else:
            player2() 
    #middle row of the board
    elif player_2 == "4":
        if middle_row[0] != "\U0001F435" and middle_row[0] != "\U0001F34C":
            middle_row[0] = "\U0001F34C"
        else:
            player2() 
    elif player_2 == "5":
        if middle_row[1] != "\U0001F435" and middle_row[1] != "\U0001F34C":
            middle_row[1] = "\U0001F34C"
        else:
            player2()
    elif player_2 == "6":
        if middle_row[2] != "\U0001F435" and middle_row[2] != "\U0001F34C":
            middle_row[2] = "\U0001F34C"
        else:
            player2()
    #bottom row of the board
    elif player_2 == "1":
        if bottom_row[0] != "\U0001F435" and bottom_row[0] != "\U0001F34C":
            bottom_row[0] = "\U0001F34C"
        else:
            player2()
    elif player_2 == "2":
        if bottom_row[1] != "\U0001F435" and bottom_row[1] != "\U0001F34C":
            bottom_row[1] = "\U0001F34C"
        else:
            player2()
    elif player_2 == "3":
        if bottom_row[2] != "\U0001F435" and bottom_row[2] != "\U0001F34C":
            bottom_row[2] = "\U0001F34C"
        else:
            player2() 
    else:
        print("Please usfgbdgdhtnete the numeric keyboard!")    
        player2()

def game():
    grid()
    while running:
        counter_tr()
        counter_mr()
        counter_br()
        player1()
        grid()       
        win()   
        counter_tr()
        counter_mr()
        counter_br()
        if counter_top == True and counter_middle == True and counter_bottom == True:
           print("It's  draw.")
           time.sleep(1)
           end_game() # if the game ends as a draw this calls the end_game()---> restart\quit
        player2()
        grid()  
        win()
game()     
