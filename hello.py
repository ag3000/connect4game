#setup
import random
import numpy as np
a = "player 1"
b= "player 2"
firstgo = random.choice([a,b])
print("It is %s's turn" % (firstgo))
activeplayer = firstgo
counterdict = {a : 1, b: 2}
currentboard = np.zeros([6,7],dtype=int)
counterdict[activeplayer]
previousboard = [currentboard]

#function returns true if the column is already full
def columnfull(testspace):
    if currentboard[0,testspace] != 0:
        return True
    else:
        return False

#function to check if board is full
def boardfull(currentboard):
    if np.count_nonzero(currentboard) == 42:
        return True
    else:
        return False

#function where user picks a valid column, returns the column index the player has chosen
def pickcolumn():
    while True:
        selectspace = input("Choose which column to drop your token")
        try:
            testspace = int(selectspace) - 1
        except ValueError:
            print("Not a valid column, please enter a number between 1 and 7")
        if columnfull(testspace):
            print ("Column full, pick another column")
        else:
            break
    return testspace
#function switches the active player, returns the new activeplayer
def switchplayer(activeplayer):
    if activeplayer == a:
        activeplayer = b
    else:
        activeplayer = a
    print("It is now %s's turn"% (activeplayer))
    return activeplayer

#function to place counter at next available spot, returns the new board
def placecounter(currentboard,testspace,counterdict,activeplayer):
    for i in reversed(range(6)):
        if currentboard[i,testspace] == 0:
            currentboard[i,testspace] = counterdict[activeplayer]
            break
    return currentboard

#check for 4 consecutive numbers in a list, returns true if there are 4 consecutive numbers and the indices of those numbers
def conseclist(list1):
    m = 1
    list2 = []
    for i in range(len(list1)-1):
        if list1[i+1] == list1[i] +1:
            m += 1
            list2.append(i)
            if m ==4:
                list2.append(i+1)
                return( [True, list2] )
        else:
            m = 1
            list2 = []
    m=1
    list2 = []
    for i in range(len(list1)-1):
        if list1[i+1] == list1[i] -1:
            m += 1
            list2.append(i)
            if m ==4:
                list2.append(i+1)
                return([True,list2])
        else:
            m = 1
            list2 = []
    return(False,"No 4 consecutive numbers")

#function checks if there is a winner
def winner(currentboard,counterdict,activeplayer):
    #result outputs two arrays, the first is of the row indices, the second is the column indices
    result = np.where(currentboard == counterdict[activeplayer])
    #check for horizontal win
    for m in result[0]:
        if (result[0] == m).sum() >= 4:
            list1 = []
            for i in list(np.where(result[0] == m)[0]):
                list1.append(result[1][i])
            if conseclist(list1)[0] == True:
                return(True)
    #check for vertical win
    for m in result[1]:
        if (result[1] == m).sum() >= 4:
            list1 = []
            for i in list(np.where(result[1] == m)[0]):
                list1.append(result[0][i])
            if conseclist(list1)[0] == True:
                return(True)
    #check for diagonal left win
    coord = list(zip(result[0],result[1]))
    for i,j in coord:
        match1 = [(i+1,j+1),(i+2,j+2),(i+3,j+3)]
        match2 = [(i+1,j-1),(i+2,j-2),(i+3,j-3)]
        if set(match1).issubset(set(coord)) == True or set(match2).issubset(set(coord)) == True:
            return(True)
    return(False)

    #undo function
    #def undo():
    #    currentboard = previousboard[-1]
    #    print(currentboard)

while True:
    print(currentboard)
    testspace = pickcolumn()
    currentboard = placecounter(currentboard,testspace,counterdict,activeplayer)
    previousboard.append(currentboard)
    if winner(currentboard,counterdict,activeplayer) == True:
        print("%s is the winner!"%(activeplayer))
        break
    if boardfull(currentboard) == True:
        print("Tie")
        break
    activeplayer = switchplayer(activeplayer)
