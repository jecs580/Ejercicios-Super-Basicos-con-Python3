# Declaration of variables
# Independent variables
cars=100
space_in_a_car=4.0
drivers=30
passenger=90
# Dependent variables
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passenger/cars_driven

# Imprimiendo todas las variables declaradas
print("There are", cars,"cars availables")
print("There are only", drivers,"drivesrs available.")
print("There will be", cars_not_driven,"empty cars today")
print("We can transport", carpool_capacity,"people_today")
print("We have", passenger,"to carpool today")
print("We need to put about", average_passengers_per_car,"in each car.")