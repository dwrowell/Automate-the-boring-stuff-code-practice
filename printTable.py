#! Python3
# print table function, takes strings in a list of lists and arranges in a neat table
# columns right justified

# tableData =[['apples', 'oranges', 'bananas', 'kiwis', 'strawberries'],
 #           ['Tom', 'Joe', 'Redban', 'Bert', 'Greg'],
#            ['Ferrari', 'Porsche', 'BMW', 'Mercedes','Audi'],
 #           ['Ape', 'Monkey', 'Wolf', 'Tiger','Coyote']]



tableData =['apples', 'oranges', 'bananas', 'kiwis', 'strawberries']
items=len(tableData)
var1=len(tableData[1])
list1=[]
for i in range(items):
            var1=len(tableData[i])
            list1.append(var1)
list1.sort()
longColWidth=list1[-1]
print(list1)
print(longColWidth)
for i in range(items):
    print(tableData[i].rjust(longColWidth,'.'))
            
