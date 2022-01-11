"""
Marwan Mashaly
Dec 3, 2020
Assignment 8.2 Bingo
"""
#-----------------------------imports------------------------------------
import random               # import the random module
import turtle               # allows to use the turtle library
import time                 # allows to use the time module
#-----------------------------Turtle Setup-----------------------
wn = turtle.Screen()                   # Create a graphics window
wn.bgcolor("light grey")               # set the background color
tia = turtle.Turtle()                  # tia
tia.color("red")                       # make red
tia.speed(0)                           # set tess speed to 0
style = ("Arial", 40)
#--------------------------Functions-----------------------------------
#strGame = input("Would you like to play(yes/no): ")     # input
strGame = "yes"                     # set game to yes
strBingo = True                     # bingo = true
lstRow1 = ["_", "_", "_", "_", "_"] # define row1 list
lstRow2 = ["_", "_", "_", "_", "_"] # define row2 list
lstRow3 = ["_", "_", "_", "_", "_"] # define row3 list
lstRow4 = ["_", "_", "_", "_", "_"] # define row4 list
lstRow5 = ["_", "_", "_", "_", "_"] # define row5 list
lstClmn1 = ["_", "_", "_", "_", "_"]    # define column1 list
lstClmn2 = ["_", "_", "_", "_", "_"]    # define column2 list
lstClmn3 = ["_", "_", "_", "_", "_"]    # define column3 list
lstClmn4 = ["_", "_", "_", "_", "_"]    # define column4 list
lstClmn5 = ["_", "_", "_", "_", "_"]    # define column5 list
lstDgnal1 = ["_", "_", "_", "_", "_"]  # define diagonal list
lstDgnal2 = ["_", "_", "_", "_", "_"]  # define diagonal list
intCalledNum = 0                    # set value to callednum
lstCardNums = []                    # define list
intSquare = 0                       # set value to variable
def drawBoard():                        # function to draw board
    for i in range(3):                  # range for how many time to draw
        for intSquares in range(5):         # range for 3 squares
            for intSides in range(4):       # range for 4 sides
                tia.fd(100)                 # forward 100 units
                tia.rt(90)                  # right 90 degrees
            tia.fd(100)                     # forward
        tia.rt(90)                          # right 90 degrees
        tia.fd(100)                         # forward 100 units
        tia.rt(90)                          # right 90 degrees
        for intSquares in range(5):         # range for 3 squares
            for intSides in range(4):       # range for 4 sides
                tia.fd(100)                 # forward 100 units
                tia.lt(90)                  # right 90 degrees
            tia.fd(100)                     # forward 100 units\
        tia.lt(90)                          # right 90 degrees
        tia.fd(100)                         # forward 100 units
        tia.lt(90)                          # right 90 degrees
    tia.pu()                        # pen up
    tia.goto(30, -50)               # 30, -50
    tia.write("B\t    I\t    N\t   G\t   O", font=style)  # write on screen
    
    generateRndms()                         # cal function

def generateRndms():         # function to generate RNDM nums
    lstBoardNums = []        # define list
    intFd = 0                # set value
    intFd2 = 0               # set value
    intMinNum = 1            # set intial value
    intMaxNum = 15           # set max value
    lstFstClmn = random.sample(range(intMinNum, intMaxNum), 5)                       # get random num
    lstBoardNums.append(lstFstClmn) # add to list
    tia.rt(90)              # turn right
    for i in range(5):      # range for each colum
        tia.pu()            # pen up
        tia.goto(25, -75)   # 25, -75
        intFd += 100        # increase by 100
        tia.fd(intFd)       # forward by intFd
        tia.write(lstFstClmn[i], font=style)    # write on screen
    intMinNum = intMinNum + 15          # increase Min value
    intMaxNum = intMaxNum + 15          # increase Max value
    lstScndClmn = random.sample(range(intMinNum, intMaxNum), 5)                     # get random num
    lstBoardNums.append(lstScndClmn)    # append to list
    intFd = 0               # set intfd to 0
    for i in range(5):      # range to column
        tia.pu()            # pen up
        tia.goto(125, -75)  # 125, -75
        intFd += 100        # increase by 100
        tia.fd(intFd)       # forward by intFd
        tia.write(lstScndClmn[i], font=style)   # write on screen
    intMinNum = intMinNum + 15         # increase Min value
    intMaxNum = intMaxNum + 15         # increase Max value
    lstThdClmn = random.sample(range(intMinNum, intMaxNum), 5)                      # get ndm num
    lstBoardNums.append(lstThdClmn)     # append to list
    intFd = 0               # set intFd to 0
    for i in range(5):      # range for column
        tia.pu()            # pen up
        tia.goto(225, -75)  # 225, -75
        intFd += 100        # increase by 100
        tia.fd(intFd)       # forward by intFd
        tia.write(lstThdClmn[i], font=style)    # write on screen
    intMinNum = intMinNum + 15          # increase Min value
    intMaxNum = intMaxNum + 15          # increase Max value
    lstFrthClm = random.sample(range(intMinNum, intMaxNum), 5)                      # get Rndm num
    lstBoardNums.append(lstFrthClm)     # append to list
    intFd = 0               # set to 0
    for i in range(5):      # range for column
        tia.pu()            # pen up
        tia.goto(325, -75)  # 325, -75
        intFd += 100        # increase by 100
        tia.fd(intFd)       # forward by 100
        tia.write(lstFrthClm[i], font=style)    # write on Screen
    intMinNum = intMinNum + 15        # increase Min value
    intMaxNum = intMaxNum + 15        # increase Max value
    lstFfthClmn = random.sample(range(intMinNum, intMaxNum), 5)                      # get Rndm num
    lstBoardNums.append(lstFfthClmn)    # append ro list
    intFd = 0                # set to 0
    for i in range(5):      # range for column
        tia.pu()            # pen up
        tia.goto(425, -75)  # 425, -75
        intFd += 100        # increase by 100
        tia.fd(intFd)       # forward by intFd
        tia.write(lstFfthClmn[i], font=style)   # write on screen

def chooseSquare(x, y):    # function to know where user clicked
    global lstClmn1         # define global
    global lstClmn2         # define global
    global lstClmn3         # define global
    global lstClmn4         # define global
    global lstClmn5         # define global
    global lstRow1          # define global
    global lstRow2          # define global
    global lstRow3          # define global
    global lstRow4          # define global
    global lstRow5          # define global
    intRow1 = range(-200, -100) # define range
    intRow2 = range(-300, -201) # define global
    intRow3 = range(-400, -301) # define global
    intRow4 = range(-500, -401) # define global
    intRow5 = range(-600, -501) # define global
    intClmn1 = range(0, 100)    # define global
    intClmn2 = range(100, 200)  # define global
    intClmn3 = range(200, 300)  # define global
    intClmn4 = range(300, 400)  # define global
    intClmn5 = range(400, 500)  # define global
    print(x, y)     # print

    if int(x) in intClmn1:  # condition if x in range
        if int(y) in intRow1:     # condition if y in range
            intSquare = 0   # set value
            lstClmn1[0] = "o"   # set value to position
            lstRow1[0] = "o"    # set value to position
            lstDgnal1[0] = "o"  # set value to position
            print lstClmn1      # print
            print lstRow1       # print
        elif int(y) in intRow2: # condition if y in range
            intSquare = 5       # set value
            lstClmn1[1] = "o"   # set value to position
            lstRow2[0] = "o"    # set value to position
            print lstClmn1      # print
            print lstRow2       # print
            
        elif int(y) in intRow3: # condition if y in range
            intSquare = 10      # set value
            lstClmn1[2] = "o"   # set value to position
            lstRow3[0] = "o"    # set value to position
            print lstClmn1      # print
            print lstRow2       # print
        elif int(y) in intRow4: # condition if y in range
            intSquare = 15      # set value
            lstClmn1[3] = "o"   # set value to position
            lstRow4[0] = "o"    # set value to position
            print lstClmn1      # print
            print lstRow4       # print
        elif int(y) in intRow5: # condition if y in range
            intSquare = 20      # set value 
            lstClmn1[4] = "o"   # set value to position
            lstRow5[0] = "o"    # set value to position
            print lstClmn1      # print
            print lstRow5       # print
    
    elif int(x) in intClmn2:    # condition if x in range
        if int(y) in intRow1:   # condition if y in range
            intSquare = 1       # set value
            lstClmn2[0] = "o"   # set value to position
            lstRow1[1] = "o"    # set value to position
            print lstClmn2      # print
            print lstRow1       # print
        elif int(y) in intRow2: # condition if y in range
            intSquare = 6       # set value
            lstClmn2[1] = "o"   # set value to position
            lstRow2[1] = "o"    # set value to position
            lstDgnal1[1] = "o"  # set value to position
            print lstClmn2      # print
            print lstRow2       # print
        
        elif int(y) in intRow3: # condition if y in range
            intSquare = 11      # set value
            lstClmn2[1] = "o"   # set value to position
            lstRow3[1] = "o"    # set value to position
            print lstClmn2      # print
            print lstRow3       # print
        
        elif int(y) in intRow4: # condition if y in range
            intSquare = 16      # set value
            lstClmn2[1] = "o"   # set value to position
            lstRow4[2] = "o"    # set value to position
            print lstClmn2      # print
            print lstRow4       # print
        elif int(y) in intRow5: # condition if y in range 
            intSquare = 21      # set value
            lstClmn2[1] = "o"   # set value to position
            lstRow5[4] = "o"    # set value to position
            print lstClmn2      # print
            print lstRow5       # print

    elif int(x) in intClmn3:    # condition if x in range
        if int(y) in intRow1:   # condition if y in range
            intSquare = 2       # set value
            lstRow1[2] = "o"    # set value to position
            lstClmn3[0] = "o"   # set value to position
            print lstClmn3      # print
            print lstRow1       # print
        
        elif int(y) in intRow2: # condition if y in range
            intSquare = 7       # set value
            lstRow2[2] = "o"    # set value to position
            lstClmn3[1] = "o"   # set value to position
            print lstClmn3      # print
            print lstRow2       # print
        
        elif int(y) in intRow3: # condition if y in range
            intSquare = 12      # set value
            lstRow3[2] = "o"    # set value to position
            lstClmn3[2] = "o"   # set value to position
            lstDgnal1[2] = "o"  # set value to position
            print lstClmn3      # print
            print lstRow3       # print
        elif int(y) in intRow4: # condition if y in range
            intSquare = 17      # set value
            lstRow4[2] = "o"    # set value to position
            lstClmn3[3] = "o"   # set value to position
            print lstClmn3      # print
            print lstRow4       # print
        elif int(y) in intRow5: # condition if y in range
            intSquare = 22      # set value
            lstRow5[2] = "o"    # set value to position
            lstClmn3[4] = "o"   # set value to position
            print lstClmn3      # print
            print lstRow5       # print
    elif int(x) in intClmn4:    # condition if x in range
        if int(y) in intRow1:   # condition if y in range
            intSquare = 3       # set value
            lstRow1[3] = "o"    # set value to position
            lstClmn4[0] = "o"   # set value to position
            print lstClmn4      # print
            print lstRow1       # print
        elif int(y) in intRow2: # condition if y in range
            intSquare = 8       # set value
            lstRow2[3] = "o"    # set value to position
            lstClmn4[1] = "o"   # set value to position
            print lstClmn4      # print
            print lstRow2       # print
        elif int(y) in intRow3: # condition if y in range
            intSquare = 13      # set value
            lstRow3[3] = "o"    # set value to position
            lstClmn4[2] = "o"   # set value to position
            print lstClmn4      # print
            print lstRow3       # print
        elif int(y) in intRow4: # condition if y in range
            intSquare = 18      # set value
            lstRow4[3] = "o"    # set value to position
            lstClmn4[3] = "o"   # set value to position
            lstDgnal1[3] = "o"  # set value to position
            print lstClmn4      # print
            print lstRow4       # print
        elif int(y) in intRow5: # condition if y in range
            intSquare = 23      # set value
            lstRow5[3] = "o"    # set value to position
            lstClmn4[4] = "o"   # set value to position
            print lstClmn4      # print
            print lstRow5       # print
    elif int(x) in intClmn5:    # condition if x in range
        if int(y) in intRow1:   # condition if y in range
            intSquare = 4       # set value
            lstRow1[4] = "o"    # set value to position 
            lstClmn5[0] = "o"   # set value to position
            lstDgnal2[4] = "o"  # set value to position
            print lstClmn5      # print
            print lstRow1       # print
        elif int(y) in intRow2: # condition if y in range
            intSquare = 9       # set value
            lstRow2[4] = "o"    # set value to position
            lstClmn5[1] = "o"   # set value to position
            print lstClmn5      # print
            print lstRow2       # print
        elif int(y) in intRow3: # condition if y in range
            intSquare = 14      # set value
            lstRow3[4] = "o"    # set value to position
            lstClmn5[2] = "o"   # set value to position
            print lstClmn5      # print
            print lstRow3       # print
        elif int(y) in intRow4: # condition if y in range
            intSquare = 19      # set value
            lstRow4[4] = "o"    # set value to position
            lstClmn5[3] = "o"   # set value to position
            print lstClmn5      # print
            print lstRow4       # print
        elif int(y) in intRow5: # condition if y in range
            intSquare = 24      # set value
            lstRow5[4] = "o"    # set value to position
            lstClmn5[4] = "o"   # set value to position
            lstDgnal1[4] = "o"  # set value to position
            print lstClmn5      # print
            print lstRow5       # print
    drawCircle(intSquare)       # call Function

def drawCircle(intSquare):      # function to draw circle 
    if intSquare == 0:          # if square 0
            tia.pu()            # pen up
            tia.goto(10, -150)  # 10, -150
            tia.pd()            # pen down
            tia.circle(40)      # circle 
    if intSquare == 5:          # if square 5
            tia.pu()            # pen up 
            tia.goto(10, -250)  # 10, -250
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 10:         # if square 10
            tia.pu()            # pen up
            tia.goto(10, -350)  # 10, -350
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 15:         # if square 15
            tia.pu()            # pen up
            tia.goto(10, -450)  # 10, -450
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 20:         # if square 20
            tia.pu()            # pen up
            tia.goto(10, -550)  # 10, -550
            tia.pd()            # pen down
            tia.circle(40)      # draw circle

    if intSquare == 1:          # if square 1
            tia.pu()            # pen up
            tia.goto(110, -150) # 110, -150
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 6:          # if square 6
            tia.pu()            # pen up
            tia.goto(110, -250) # 110, -250
            tia.pd()            # pen down
            tia.circle(40)      # draw circle 
    if intSquare == 11:         # if square 11
            tia.pu()            # pen up
            tia.goto(110, -350) # 110, -350
            tia.pd()            # pen down
            tia.circle(40)      # draw circle 
    if intSquare == 16:         # if square 16
            tia.pu()            # pen up
            tia.goto(110, -450) # 110, -450
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 21:         # if square 21
            tia.pu()            # pen up
            tia.goto(110, -550) # 110, -550
            tia.pd()            # pen down
            tia.circle(40)      # draw circle

    if intSquare == 2:          # if square 2
            tia.pu()            # pen up
            tia.goto(210, -150) # 210, -150
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 7:          # if square 7
            tia.pu()            # pen up
            tia.goto(210, -250) # 210, -250
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 12:         # if square 12
            tia.pu()            # pen up
            tia.goto(210, -350) # 210, -350
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 17:         # if square 17
            tia.pu()            # pen up
            tia.goto(210, -450) # 210, -450
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 22:         # if square 22
            tia.pu()            # pen up
            tia.goto(210, -550) # 210, -550
            tia.pd()            # pen down
            tia.circle(40)      # draw circle

    if intSquare == 3:          # if square 3
            tia.pu()            # pen up
            tia.goto(310, -150) # 310, -150
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 8:          # if square 8
            tia.pu()            # pen up
            tia.goto(310, -250) # 310, -250
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 13:         # if square 13
            tia.pu()            # pen up
            tia.goto(310, -350) # 310, -350
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 18:         # if square 18
            tia.pu()            # pen up
            tia.goto(310, -450) # 310, -450
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 23:         # if square 23
            tia.pu()            # pen up
            tia.goto(310, -550) # 310, -550
            tia.pd()            # pen down
            tia.circle(40)      # draw circle

    if intSquare == 4:          # if square 4
            tia.pu()            # pen up
            tia.goto(410, -150) # 410, -150
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 9:          # if square 9
            tia.pu()            # pen up
            tia.goto(410, -250) # 410, -250
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 14:         # if square 14
            tia.pu()            # pen up
            tia.goto(410, -350) # 410, -350
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 19:         # if square 19
            tia.pu()            # pen up
            tia.goto(410, -450) # 410, -450
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    if intSquare == 24:         # if square 24
            tia.pu()            # pen up
            tia.goto(410, -550) # 410, -550
            tia.pd()            # pen down
            tia.circle(40)      # draw circle
    

def getCallNums():          # function to get cards numbers
    global lstCardNums      # define global
    for i in range(1, 76):  # range for range of cards
        strNoRepetition = True  # set to true
        intRndmNum = random.randint(1, 75)  # get Rndm num
        while strNoRepetition == True:    # loop until False
            if intRndmNum in lstCardNums:   # if Rndm in lst
                intRndmNum = random.randint(1, 75)  # get Rndm numbe
            else:           # else
                lstCardNums.append(intRndmNum)      # append to list
                strNoRepetition = False         # set to false

def playTurn():                 # function to play game
    global intTurn              # define global 
    global strBingo             # define global
    strBingo = True             # set to true
    global lstCardNums          # define global
    for i in lstCardNums:       # range for list
        if strBingo == True:    # condition if true
            if i in range(1, 16):   # range for column 1
                print("The number is in B " + str(i))   # print
            elif i in range(16, 31):    # range for column 2
                print("The number is in I " + str(i))   # print
            elif i in range(31, 46):    # range for column3  
                print("The number is in N " + str(i))   # print
            elif i in range(56, 61):    # range for column 4
                print("The number is in G " + str(i))   # print
            elif i in range(61, 75):    # range for column 5
                print("The number is in O " + str(i))   # print
            strBingo = checkWin(strBingo)   # call function
            time.sleep(5)               # sleep
    if strBingo == False:               # condition of false
        print("BINGO!!")                # print
        drawPlayAgain()                 # call function
        wn.onclick(playAgain)           # on click call function

def checkWin(strBingo):                # function to check if user have met conditions of bingo

    if "_" not in lstClmn1:         # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstClmn2:       # condition if not in list    
        strBingo = False            # set to false
    elif "_" not in lstClmn3:       # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstClmn4:       # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstClmn5:       # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstRow1:        # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstRow2:        # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstRow3:        # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstRow4:        # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstRow5:        # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstDgnal1:      # condition if not in list
        strBingo = False            # set to false
    elif "_" not in lstDgnal2:      # condition if not in list
        strBingo = False            # set to false
    else:                           # else
        strBingo = True             # set to true
    return strBingo                 # return value

def drawPlayAgain():                # call function 
    tia.pu()                        # pen up
    tia.goto(250, 100)              # 250, 100
    tia.pd()                        # pen down
    for i in range(4):              # range for square
        tia.fd(50)                  # forward
        tia.lt(90)                  # right 90
    tia.pu()                        # pen up
    tia.goto(250, 75)               # 250, 75
    tia.pd()                        # pen down
    tia.write("Play Again")         # write on screen

def playAgain(x,y):               # function to play again
    global lstClmn1             # define global
    global lstClmn2             # define global
    global lstClmn3             # define global
    global lstClmn4             # define global
    global lstClmn5             # define global
    global lstRow1              # define global
    global lstRow2              # define global
    global lstRow3              # define global
    global lstRow4              # define global
    global lstRow5              # define global
    if int(x) in range(250, 300) and int(y) in range(50, 100):                           # condition if in range
        tia.reset()             # reset
        lstRow1 = ["_", "_", "_", "_", "_"] # define list
        lstRow2 = ["_", "_", "_", "_", "_"] # define list
        lstRow3 = ["_", "_", "_", "_", "_"] # define list
        lstRow4 = ["_", "_", "_", "_", "_"] # define list
        lstRow5 = ["_", "_", "_", "_", "_"] # define list
        lstClmn1 = ["_", "_", "_", "_", "_"]    # define list
        lstClmn2 = ["_", "_", "_", "_", "_"]    # define list
        lstClmn3 = ["_", "_", "_", "_", "_"]    # define list
        lstClmn4 = ["_", "_", "_", "_", "_"]    # define list
        lstClmn5 = ["_", "_", "_", "_", "_"]    # define list
        lstDgnal1 = ["_", "_", "_", "_", "_"]   # define list
        lstDgnal2 = ["_", "_", "_", "_", "_"]   # define list
        tia.color("red")               # make red
        tia.speed(0)                   # set tia speed to 0
        wn.onclick(chooseSquare)       # on click call function
        drawBoard()                     # call function
        getCallNums()                   # call function
        playTurn()                      # call function
        wn.listen()                     
        wn.mainloop()
# ------------------------------  main --------------------------
wn.onclick(chooseSquare)                # on click call function
drawBoard()                             # call function
getCallNums()                           # call function
playTurn()                              # call function
wn.listen()
wn.mainloop()