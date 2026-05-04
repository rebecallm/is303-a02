'''
Rebeca Llontop 
IS 303 - A02

Fitness Advisor 
This program recommends an exercise plan based on fitness level and goals

Inputs:
- Name (string)
- Current weight in pounds (float)
- Weight loss goal (float)
- Strength ( beginner, intermediate, advanced)
- Endurance level ( beginner, intermediate, advanced)

Processes:
- Validate weight > 12 and < 1000
- Validate weight loss goal > 0 and < current weight
- recommend and exercise plan based on strength and endurance levels

Outputs:
- Print client's name, current weight, weight loss goal, recommended exercise plan and pound lost per week 
- Print error message if any input is invalid

'''
#INPUTS
name = input("Enter your name: ")
current_weight = float(input("Enter your current weight in pounds: "))
weight_loss_goal = float(input("Enter your weight loss goal in pounds: "))
strength = input("Enter your strength level (beginner, intermediate, advanced): ").lower()
endurance = input("Enter your endurance level (beginner, intermediate, advanced): ").lower()

#VALIDATION 
if current_weight <= 12 or current_weight >= 1000:
    print("Error: Weight must be greater than 12 and less than 1000 pounds.")
    continue_program = False
if weight_loss_goal <= 0 or weight_loss_goal >= current_weight:
    print("Error: Weight loss goal must be greater than 0 and less than current weight.")
    continue_program = False
 #PROCESSSES
if continue_program == True:

    if strength == "beginner" and endurance == "beginner":
        plan = "walking and beginner bodyweight workouts 3 days per week"
        pounds_lost = 0.33
    elif strength == "intermediate" and endurance == "intermediate":
        plan = "moderate strength and cardio training 4 days per week"
        pounds_lost = 0.5
    elif strength == "advanced" and endurance == "advanced":
       plan = "high-intensity strength and cardio training 5 days per week"
       pounds_lost = 0.75
    elif strength == "beginner" and endurance == "intermediate":
        plan = "walking and moderate cardio 3-4 days per week"
        pounds_lost = 0.4
    elif strength == "beginner" and endurance == "advanced":
        plan = "walking and high-intensity cardio 3-5 days per week"
        pounds_lost = 0.6
    elif strength == "intermediate" and endurance == "beginner":
        plan = "moderate strength training and walking 3-4 days per week"
        pounds_lost = 0.5       
    elif strength == "intermediate" and endurance == "advanced":
        plan = "moderate strength training and high-intensity cardio 4-5 days per week"
        pounds_lost = 0.5
    elif strength == "advanced" and endurance == "beginner":
        plan = "high-intensity strength training and walking 4-5 days per week"
        pounds_lost = 0.75
    elif strength == "advanced" and endurance == "intermediate":
        plan = "high-intensity strength training and moderate cardio 4-5 days per week"
        pounds_lost = 0.75
    else:
        plan = "Error: Invalid strength or endurance level. Please enter beginner, intermediate, or advanced."
        pounds_lost = 0

 #OUTPUTS
    print(f"{name}'s Recommended Exercise Plan\n"
      f"Current Weight: {current_weight}lb\n"
      f"Weight Loss Goal: {weight_loss_goal}\n"
      f"Recommended 12-week Exercise Plan: {plan}\n"
      f"Estimated Pounds Lost Per Week: {pounds_lost:.2f}lb/week")

      





