rejected = 0
def load_inventory():
    with open("inventoryList.txt", "w+") as file:
        readInventory = file.read()
        inventory = readInventory.split(",")
        if inventory[0] == "":
            inventory.pop()
        print(inventory)
        return inventory
    
def write_inventory():
    with open('inventoryList.txt', 'w') as file:
        for item in inventory:
            file.write(','.join(item))
            
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
    
def process_delivery(inventoryTotal, new_value):
    
    if len(inventoryTotal) == 0:
        new_value.insert(0,1001)
    else:
        new_value.insert(0,int(inventoryTotal[-1][0]) + 1) 
    inventoryTotal.append(new_value)
    print(inventoryTotal)
    return inventoryTotal

#def calculate_tax(amount):
    #tax = amount * 2.5 * .10
    #return tax

def generate_report(total_units, failed_attempts):  
    print("\nTotal Deliveries Processed: " + str(total_units))
    print("\nNumber of Failed/Rejected Entries: " + str(failed_attempts))
    return 


inventory = load_inventory()
while True :
    #print("\nTotal Deliveries Processed: " + str(inventory))
    accepted_Input = get_valid_input()
    if accepted_Input == 'quit':
        generate_report(inventory,rejected)
        #tax = calculate_tax(inventory)
        #print("\n The tax amount is: $"+ str(tax))
        break
    else:
        inventory = process_delivery(inventory,accepted_Input)
        #tax = calculate_tax(inventory)
        #print("\n The tax amount is: $"+ str(tax))
        
            
    


