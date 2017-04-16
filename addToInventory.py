
vault = {'spinmetal':120, 'hadrium flakes':23, 'Spirit Bloom':174, 'relic iron': 87, 'weapon parts': 43, 'armour materials':211}
crotaLoot = ['spinmetal', 'hadrium flakes', 'hadrium flakes', 'hadrium flakes', 'hadrium flakes', 'hadrium flakes',
             'weapon parts','weapon parts','weapon parts','weapon parts']


print(crotaLoot)
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory[i]+=1
        
def displayInventory(vault):
    print('Inventory:')
    ref = 1
    item_Total = 0
    for i in vault.keys():
        
        print (str(ref) + ': ', end='')
        print (vault[i] , end='')
        print (' ' + i)
        ref = ref + 1
        item_Total = item_Total + vault[i]
    print('Total number of items: ' + str(item_Total))
    
addToInventory(vault, crotaLoot)       
displayInventory(vault)

