#! Python3
# print table function, takes strings in a list of lists and arranges in a neat table
# columns right justified

list =[['apples', 'oranges', 'bananas', 'kiwis', 'strawberries'],
           ['Tom', 'Joe', 'Redban', 'Bert', 'Greg'],
          ['Ferrari', 'Porsche', 'BMW', 'Mercedes','Audi'],
           ['Ape', 'Monkey', 'Wolf', 'Tiger','Coyote']]

def printTable(tableData, items):
    
    
    colNum=len(tableData)
    var1=len(tableData[1])
    list1=[]
    
    for i in range(colNum):
        for v in range(items):
                var1=len(tableData[i][v])
                list1.append(var1)
    list1.sort()
    longColWidth=list1[-1]
    print('List of lists'.center((longColWidth*colNum),'*'))
    print()
    for v in range(items):
        for i in range(colNum):    
            print(tableData[i][v].rjust(longColWidth,'.'),end='')
        print()
            
printTable(list, 5)
