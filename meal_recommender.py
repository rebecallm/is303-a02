'''
Rebeca Llontop
IS 303 - A02

Meal Recommender
Suggests a meal based on time of day, dietary preference and budget

Inputs:
- Customer name (string)
- Time of day: breakfast, lunch, or dinner (string)
- Dietary preference: vegetarian, vegan, or none (string)
- Budget: low, medium, or high (string)

Processes:
- Validate time of day (must be breakfast, lunch, or dinner)
- Validate dietary preference (must be vegetarian, vegan, or none)
- Recommend a meal based on the inputs

Outputs:
- print customer's name, time of day, dietary preference, budget, and recommended meal
- Print error message if any input is invalid
'''
#INPUTS
name = input("What is your name? ")
time_of_day = input("Time of day: ")
dietary_preference = input("what is your dietary preference? vegetarian/vegan/none: ")
budget = input("Please enter your budget: low/medium/high: ")
#VALIDATION
if time_of_day not in ["breakfast", "lunch", "dinner"]:
    print("Error: Invalid time of day. Please enter breakfast, lunch, or dinner.")
    continue_program = False
elif dietary_preference not in ["vegetarian", "vegan", "none"]:
    print("Error: Invalid dietary preference. Please enter vegetarian, vegan, or none.")
    continue_program = False
elif budget not in ["low", "medium", "high"]:
    print("Error: Invalid budget. Please enter low, medium, or high.")
    continue_program = False
else:    continue_program = True
#PROCESSES
if continue_program == True:        
    