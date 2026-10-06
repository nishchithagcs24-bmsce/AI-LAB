room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()

location = input("Enter vacuum location (A/B): ").upper()

print("\nInitial State:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Location:", location)

print("\nActions:")

while room_A == "Dirty" or room_B == "Dirty":

   
    if location == "A":

        if room_A == "Dirty":
            print("Suck")
            room_A = "Clean"

        else:
            print("Move Right")
            location = "B"

    
    elif location == "B":

        if room_B == "Dirty":
            print("Suck")
            room_B = "Clean"

        else:
            print("Move Left")
            location = "A"


print("\nFinal State:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Location:", location)
print("Both rooms are clean.")
