tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestWord(row): 
    longestWord = 0
    for words in row:
        if longestWord < len(words):
            longestWord = len(words)
    return longestWord
"""
def makingNewList(tableData,i ):
    newList = []
    for array in tableData:
        j = 0
        for word in array :
           
            if j == i:
                newList.append(word)
            j += 1


    return newList

"""

def printTable(tableData):
    for i in range(len(tableData[0])):
        print(tableData[i][i].rjust(arrayOfLongestWords[i]-len(tableData[i][i]) + ))



arrayOfLongestWords = []
for each in  tableData :
    arrayOfLongestWords.append(findLongestWord(each))



