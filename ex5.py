name = "Sam Jarvis"
age = 26  # not a lie
height = 169  # centimeters
weight = 100  # kilogramms
eyes = "blue"
teeth = "white"
hair = "brown"

print(f"let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"he's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

height_inch = height * 0.39701
weight_lbs = weight * 2.20462

print(f"My height: {height}cm would be {round((height * 0.39701))} in inches.")
print(f"My weight: {weight}kg would be {round(weight_lbs)} in pounds.")
