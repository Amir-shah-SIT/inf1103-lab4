rejected = 0
def load_inventory():
    try:
        with open("output.txt", "r") as file:
            readInventory = file.readlines()
            inventory = []
            for perIndex in readInventory:   
                invetoryIndex = [item.strip() for item in perIndex.split(",")]
                inventory.append(invetoryIndex)
            print("=====================================")
            print("Current order: ")
            for items in inventory:
                print(", ".join(items))
            return inventory
    except FileNotFoundError:
        with open("inventoryList.txt", "w+") as file:
            readInventory = file.read()
            return []
    
def write_inventory(inventory,newInventory):
    print("=====================================")
    print("All order: ")
    for inNew in newInventory:
        maxLimit = len(inventory)
        counterLimit = 0
        for inMain in inventory:
            counterLimit += 1
            if inNew[0] in inMain:
                inMain[2] = str(int(inMain[2]) + int(inNew[2]))
                newInventory.remove(inNew)
                break
        if counterLimit == maxLimit:    
            inventory.append(inNew)
    for each in inventory:
        print(", ".join(each))
    with open("output.txt", "w") as file:
        for row in inventory:
            # Convert elements to strings and join them with a comma
            file.write(", ".join(map(str, row)) + "\n")
    
    print("Inventory saved to output.txt")
    return inventory
            
def get_valid_input():
    while True: 
        backInput = False
        global rejected 
        productInput = input("\nEnter product name or quit:\n")
        if productInput.lower() == "quit":
            return productInput.lower()
        elif productInput.isdigit() == False and productInput != "":
            while backInput == False:
                userInput = input("\nInput additional stock value, back or quit:\n")
                if userInput.isdigit() == True:
                    if int(userInput) < 0:
                        rejected += 1
                        print("\nUnacceptable input")
                    else:
                        return [productInput,str(userInput)]
                elif userInput.lower() == "quit":
                    return userInput.lower()
                elif userInput.lower() == "back":
                    backInput = True
                else:
                    rejected += 1
                    print("Unacceptable input")
        else:
            rejected += 1
            print("Unacceptable input")
def process_delivery(inventoryTotal,newInventory,new_value):
    if len(inventoryTotal) == 0 and len(newInventory) == 0:
        new_value.insert(0,"1001")
        newInventory.append(new_value)
    else:
        addedtoExisting = False
        #check if item exists in newinventory if so increase the amount of stock
        for items in newInventory:
            if new_value[0] in items:
                items[2] = str(int(new_value[1]) + int(items[2]))
                return newInventory
            #check if old inventory empty if empty we will increment from new inventory
     #check if item is in old inventory if it is copy the index
        for items in inventoryTotal:
            if new_value[0] == items[1]:
                new_value.insert(0,str(int(items[0]))) 
                newInventory.append(new_value)
                return newInventory
        if len(inventoryTotal) == 0:
            new_value.insert(0,str(int(newInventory[-1][0]) + 1)) 
            newInventory.append(new_value)
        #check if new inventory is empty if it is we increment from old
        elif len(newInventory) == 0:
            new_value.insert(0,str(int(inventoryTotal[-1][0]) + 1))
            newInventory.append(new_value)
        else:
            if inventoryTotal[-1][0] >= newInventory[-1][0]:
                new_value.insert(0,str(int(inventoryTotal[-1][0]) + 1)) 
            else:
                new_value.insert(0,str(int(newInventory[-1][0]) + 1)) 
            newInventory.append(new_value)
    return newInventory

def calculate_tax(inventory):
    if inventory != []:
        tax = 0
        for items in inventory:
            tax += int(items[2]) * 3 *.10 
    return tax

def generate_report(total_units,new_units, failed_attempts):
    totalitems = 0
    for items in new_units:
        totalitems += int(items[2]) 
    print("=== Audit Report ===")

    print("Total transaction recorded: " + str(len(total_units)))
    print("New Units processed: " + str(totalitems))
    print("\nNumber of Failed/Rejected Entries: " + str(failed_attempts))
    return 


inventory = load_inventory()
newInventory = []
while True :
    #print("\nTotal Deliveries Processed: " + str(inventory))
    accepted_Input = get_valid_input()
    #print(inventory)
    if accepted_Input == 'quit':
        inventory = write_inventory(inventory,newInventory)
        generate_report(inventory,newInventory,rejected)
        tax = calculate_tax(inventory)
        print("\n The tax amount is: $"+ str(round(tax,2)))
        break
    else:
        newInventory = process_delivery(inventory,newInventory,accepted_Input)
        print("=====================================")
        print("Current order: ")
        for perItem in newInventory:
            print(", ".join(perItem))
        
            
    


