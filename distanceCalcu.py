print("Destination Calculator")
startingLocation = str(input("Enter Starting Location: "))
Destination = str(input("Enter Destination: "))
modeTransfort = str(input("Enter Mode of Transfortation: "))

distance = float(input("Enter Distance in KiloMeter: "))
speed = float(input("Enter speed as km/h: "))

travelTime =  distance/speed
travelTimeRounded = round(travelTime, 2)

hours = int(travelTime)
minutes = round((travelTime - hours) * 60)

print(f"The travel time is {hours} hours and {minutes} minutes")

class finalDestination:
    def almanyak(self):
        destinationText = f"The destination is {Destination}, it will start at {startingLocation} and the tranfortation vehicle is {modeTransfort}"
        travelDetails = f"The travel distance is {distance}km, the estimated time of arrival is {hours} hours and {minutes} minutes"
        print(destinationText)
        print(travelDetails)

class Morethan5Hours:
    def restStop(self, travelObj):
        print("A stop is recommended if the travel time is greater than 5 hours.")
        restStop = str(input("Do you need a rest stop? Yes or No: "))      
        if restStop.lower() == "yes":
            restStopTime = hours + 1
            travelObj.almanyak()
            print(f" plus the rest stop of 1 hour is will be {restStopTime}")
            
        else:
            print(f"The travel time is {hours} hours and {minutes} minutes")
            travelObj.almanyak()

class lessThan5Hours:
    def noRestStop(self, travelObj):
        print("The travel is less than  5 hrs!")
        travelObj.almanyak()


longTrip = Morethan5Hours()
travel = finalDestination()
shortTrip = lessThan5Hours()

if hours >= 5:
    longTrip.restStop(travel)
else:   
    shortTrip.noRestStop(travel)