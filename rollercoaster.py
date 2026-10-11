print("Welcome to the RollerCoaster")
height = int(input("What's your height in cm?\n"))

bill = 0

if(height >= 120):
    print("You can ride the rollercoaster")
    age = int(input("What's your age?\n"))
    if(age < 12):
        bill += 5
        print("You have the child ticket for $5")
    elif(age <= 18):
        bill += 7
        print("You have the youth ticket for $7")
    elif (age >= 45 and age <= 55):
        print("You can have a free ride, It on us")
    else:
        bill += 12
        print("You have the adult ticket for $12")

    photo_price = input("Do you want a photo? Y or N\n")
    if(photo_price == "Y"):
        bill +=3
        print(f"Your bill is $ {bill}")
    else:
        bill = bill
        print(f"Your bill is $ {bill}")
else:
    print("Sorry, you need to grow taller!")
