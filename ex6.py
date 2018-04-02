types_of_people = 10  # assign 10 to the variable types_of_people
x = f"There are {types_of_people} types of people."
# assign the f-string to x, insert the variable types_of_people into the string

binary = "binary"  # assign variable binary as the string "binary"
do_not = "don't"  # assign variable do_not as "don't"
y = f"Those who know {binary} and those who {do_not}."
# assign y as the f-string, inserting the variables "binary" and "do_not"
# (string inside a string 1)
print(x)  # output x
print(y)  # output y

print(f"I said: {x}")  # output the f-string with the variable x
# (string inside a string 2)
print(f"I also said: '{y}'")  # output f-string with y
# (string inside a string 3)

hilarious = False  # assign variable hilarious to bool value false
joke_evaluation = "Isn't that joke so funny?! {}"  # assign variable to string

print(joke_evaluation.format(hilarious))
print(f"I also said: '{y}'")
# output variable in .format string with assigned bool value

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)  # (string inside a string 4)
# output concatanation of 2 strings with the + operator
