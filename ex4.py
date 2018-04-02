cars = 100  # number of cars int
space_in_a_car = 4  # number of seats in a car float
drivers = 30  # number of drivers
passengers = 90  # number of passengers
cars_not_driven = cars - drivers  # cars that are empty
cars_driven = drivers  # cars that are used
carpool_capacity = cars_driven * space_in_a_car
# total number of seats available
average_passengers_per_car = passengers // cars_driven
# mean amount of seats taken


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")


print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
