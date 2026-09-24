rejected = 0
load_inventory = open("inventoryList", "w+")

def get_valid_input():
    valid_input = False
    while valid_input == False: 
        global rejected
        userInput = input("\nInput additional stock value or quit:\n")
        if userInput.isdigit() == True:
            if int(userInput) < 0:
                rejected += 1
                print("\nUnacceptable input")
            else:
                return userInput
        elif userInput.lower() == "quit":
            return userInput.lower()
        else:
            rejected += 1
            print("Unacceptable input") 
    
def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total

def calculate_tax(amount):
    tax = amount * 2.5 * .10
    return tax

def generate_report(total_units, failed_attempts):  
    print("\nTotal Deliveries Processed: " + str(total_units))
    print("\nNumber of Failed/Rejected Entries: " + str(failed_attempts))
    return 

while True :
    #print("\nTotal Deliveries Processed: " + str(inventory))
    accepted_Input = get_valid_input()
    if accepted_Input == 'quit':
        generate_report(inventory,rejected)
        tax = calculate_tax(inventory)
        print("\n The tax amount is: $"+ str(tax))
        break
    else:
        inventory = process_delivery(inventory,accepted_Input)
        if inventory >= 500:
            generate_report(500,rejected)
            print("\nNumber of Rejected Stock: "+ str(inventory-500))
            tax = calculate_tax(500)
            print("\n The tax amount is: $"+ str(tax))
            break
        tax = calculate_tax(inventory)
        print("\n The tax amount is: $"+ str(tax))
        
            
    


