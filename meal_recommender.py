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
- Validate dietary preference (must be gluten-free, dairy-free, or none) can't be both gluten-free and dairy-free
- Recommend a meal based on the inputs from a predefined list of meal options

Outputs:
- print customer's name, time of day, dietary preference, budget, and recommended meal
- Print error message if any input is invalid
'''
#COLLECTING INPUTS
name = input("What is your name? ").title()
time_of_day = input("Time of day: ").lower()
dietary_preference = input("what is your dietary preference? gluten-free/dairy-free/none: ").lower()
budget = input("Please enter your budget: low/medium/high: ").lower()
#VALIDATION of inputs
continue_program = True

if time_of_day not in ["breakfast", "lunch", "dinner"]:
    print("Error: Invalid time of day. Please enter breakfast, lunch, or dinner.")
    continue_program = False
elif dietary_preference not in ["gluten-free", "dairy-free", "none"]:
    print("Error: Invalid dietary preference. Please enter gluten-free, dairy-free, or none.")
    continue_program = False
elif budget not in ["low", "medium", "high"]:
    print("Error: Invalid budget. Please enter low, medium, or high.")
    continue_program = False
else:
    continue_program = True
#PROCESSES
if continue_program == True:  
    if time_of_day == "breakfast" and dietary_preference == "gluten-free" and budget == "low":
        meal = "a bowl of gluten-free oatmeal topped with fresh fruit and a drizzle of honey"
    elif time_of_day == 'breakfast' and dietary_preference == "none" and budget == "low":
        meal = "scrambled eggs with toast and a side of fruit"
    elif time_of_day == "breakfast" and dietary_preference == "dairy-free" and budget == "low":
        meal = "oatmeal made with almond milk, topped with sliced bananas and peanut butter"
    elif time_of_day == "breakfast" and dietary_preference == "gluten-free" and budget == "medium":
        meal= "a gluten-free avocado toast with a poached egg, and a side of fresh fruit"
    elif time_of_day == "breakfast" and dietary_preference == "gluten-free" and budget == "high":
        meal = "a smoked salmon and goat cheese frittata with a side of mixed greens"
    elif time_of_day == "breakfast" and dietary_preference == "dairy-free" and budget == "high":
        meal = "acai bowl made with blended frozen berries, banana, and coconut milk, topped with granola and sliced almonds"
    elif time_of_day == "breakfast" and dietary_preference == "none" and budget == "medium":
        meal = "bacon, egg, and cheese breakfast sandwich on a croissant, served with a side of hash browns"
    elif time_of_day == "breakfast" and dietary_preference == "none" and budget == "high":
        meal = "eggs benedict with smoked salmon, served with a side of mixed greens"
    elif time_of_day == "lunch" and dietary_preference == "none" and budget == "low":
        meal = "a turkey and avocado sandwich on whole wheat bread, served with a side of carrot sticks"
    elif time_of_day == "lunch" and dietary_preference == "none" and budget == "medium":
        meal = "a grilled chicken Caesar salad with romaine lettuce, croutons, and Caesar dressing"
    elif time_of_day == "lunch" and dietary_preference == "none" and budget == "high":
        meal = "stuffed salmon wtih imitation crab, served with a side of roasted potatoes and asparagus"
    elif time_of_day == "lunch" and dietary_preference == "gluten-free" and budget == "low":
        meal = "grilled chicken breast with a side of quinoa and steamed broccoli"
    elif time_of_day == "lunch" and dietary_preference == "gluten-free" and budget == "medium":
        meal = "a gluten-free turkey and avocado wrap with a side of mixed greens"
    elif time_of_day == "lunch" and dietary_preference == "gluten-free" and budget == "high":
        meal = "a stuffed salmon with spinach and feta, served with a side of roasted potatoes and asparagus"
    elif time_of_day == "lunch" and dietary_preference == "dairy-free" and budget == "low":
        meal = "a quinoa salad with mixed vegetables, chickpeas, and a lemon vinaigrette dressing"
    elif time_of_day == "lunch" and dietary_preference == "dairy-free" and budget == "medium":
        meal = "a fried chicken sandwich, served with a side of sweet potato fries"
    elif time_of_day == "lunch" and dietary_preference == "dairy-free" and budget == "high":
        meal = "lasagna made with dairy-free cheese and a side of garlic bread"
    elif time_of_day == "dinner" and dietary_preference == "none" and budget == "low":
        meal = "a simple spaghetti with marinara sauce and a side of garlic bread"
    elif time_of_day == "dinner" and dietary_preference == "none" and budget == "medium":
        meal = "a grilled chicken breast with a side of roasted vegetables and quinoa"
    elif time_of_day == "dinner" and dietary_preference == "none" and budget == "high":
        meal = "a wagyu steak served with a side of truffle mashed potatoes and sautéed mushrooms"
    elif time_of_day == "dinner" and dietary_preference == "gluten-free" and budget == "low":
        meal= "a stir-fry with tofu, mixed vegetables, and gluten-free soy sauce, served over rice"
    elif time_of_day == "dinner" and dietary_preference == "gluten-free" and budget == "medium":
        meal = "a grilled chicken breast with a side of roasted vegetables and quinoa"
    elif time_of_day == "dinner" and dietary_preference == "gluten-free" and budget == "high":
        meal = "gluten-free pasta with a tomato and basil sauce, topped with grilled shrimp and a side of garlic bread"
    elif time_of_day == "dinner" and dietary_preference == "dairy-free" and budget == "low":
        meal = "a vegetable stir-fry with tofu, served over rice"
    elif time_of_day == "dinner" and dietary_preference == "dairy-free" and budget == "medium":
        meal = "chicken alfredo made with a dairy-free sauce, served over gluten-free pasta and a side of steamed broccoli and bacon"
    elif time_of_day == "dinner" and dietary_preference == "dairy-free" and budget == "high":
        meal = "a grilled picahna steak with chimichurri sauce, served with a side of roasted potatoes and asparagus"
    else:
        meal = "a mixed green salad with a variety of toppings and a light vinaigrette dressing. "
#OUTPUTS
    print(f"{name}'s Meal Recommendation\n"
          f"Time of Day: {time_of_day}\n"
          f"Dietary Preference: {dietary_preference}\n"
          f"Budget: {budget}\n"
          f"Recommended Meal: {meal}")        