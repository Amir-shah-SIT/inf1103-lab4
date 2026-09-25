rejected = 0
def load_inventory():
    try:
        with open("output.txt", "r") as file:
            readInventory = file.readlines()
            print(readInventory)
            return readInventory
    except FileNotFoundError:
        with open("inventoryList.txt", "w+") as file:
            readInventory = file.read()
            return []

    
def write_inventory(inventory,newInventory):
    for inMain in inventory:
        for inNew in newInventory:
            if inNew[0] in inMain:
                inMain = int(inMain[2]) + int(inNew[2])
                newInventory.remove(inNew)
    for items in newInventory:
        inventory.append(items)  
    with open("output.txt", "w") as file:
        for row in inventory:
            # Convert elements to strings and join them with a comma
            file.write(", ".join(map(str, row)) + "\n")
    return inventory
            
def get_valid_input():
    while True: 
        global rejected 
        productInput = input("\nEnter product name or quit:\n")
        if productInput.lower() == "quit":
            return productInput.lower()
        elif productInput.isdigit() == False:
            userInput = input("\nInput additional stock value or quit:\n")
            if userInput.isdigit() == True:
                if int(userInput) < 0:
                    rejected += 1
                    print("\nUnacceptable input")
                else:
                    return [productInput,userInput]
            elif userInput.lower() == "quit":
                return userInput.lower()
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
        for items in newInventory:
            if new_value[0] in items:
                items[2] = str(int(new_value[1]) + int(items[2]))
                addedtoExisting = True
        if addedtoExisting == False:
            if len(inventoryTotal) != 0:
                if inventoryTotal[-1][0] >= newInventory[-1][0]:
                    new_value.insert(0,str(int(inventoryTotal[-1][0]) + 1)) 
                else:
                    new_value.insert(0,str(int(newInventory[-1][0]) + 1)) 
                newInventory.append(new_value)
            else:
                new_value.insert(0,str(int(newInventory[-1][0]) + 1)) 
                newInventory.append(new_value)

    print(newInventory)
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
    print(inventory)
    if accepted_Input == 'quit':
        inventory = write_inventory(inventory,newInventory)
        generate_report(inventory,newInventory,rejected)
        tax = calculate_tax(inventory)
        print("\n The tax amount is: $"+ str(round(tax,2)))
        break
    else:
        newInventory = process_delivery(inventory,newInventory,accepted_Input)
        
            
    


