# create bus class
#bus should have route number and destination
#bus should have drive method that returns string "brum brum"

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = [ ]

    def drive(self):
        return "Brum brum"
    
# give the bus class a new property "passengers"- should be a list which starts off empty
# add a method to the bus class which returns how many passengers are on the bus

    def passenger_count(self):
        return len(self.passengers)
    
# add a method to the bus class which takes in a Person and appends it to the list of passengers. The method could look something like bus.pick_up(self, passenger_1)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

# add a method that drops off a passenger and removes them from the list. Could look like bus.drop_off(self, passenger_2)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

# Add an empty_bus() method to remove all of the passengers- this might be used when the bus reaches its destination, or if the bus breaks down. It should remove all of the passengers from the list.

    def empty_bus(self):
        self.passengers.clear()
