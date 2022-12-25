#Function to calculate endurance
def endurance_calc(Fuel, Fuel_consumption):
    try:
        #Try block to execute below code for trial
        endurance = Fuel/Fuel_consumption
    except:
        #If any exceotions are found in try code then code executes except block
        print("Fuel_consumption is zero!")
    else:
        #If everything is alright and try code block has worked without any exceptions then it executes else
        print(f"Endurance is {endurance}")
    finally:
        # finally block is executed when all blocks are executed accordingly to give final results 
        print(f"Finally Endurance is calculated as {endurance} as per given fuel and fuel consumption")

endurance_calc(Fuel=20, Fuel_consumption=5)



     
