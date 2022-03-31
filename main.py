import cmpt120image

colors_data = open("colours.csv")
lines = colors_data.read().splitlines()
color_dict = {}

for line in lines:
    line_split = line.split(",")
    name = line_split[0]
    r,g,b = line_split[1:]
    color_dict[(r,g,b)] = name 

print(color_dict)

running = True

while running:
    print("\n1. Load Colour File\n2. Print All Colours\n3. Select Colour\n4. Find Closest Colour\n5. Display (Save) Colour Scheme\n0. Quit")
    option = int(input("\nSelect the option: "))
    
    if option == 0:
        running = False
        print("Quitting the program!")
    if option == 1:

        print("The file has been processed and 10 colours were entered into the dictionary")
    if option == 2:
        pass
    if option == 3:
        pass
    if option == 4:
        pass
    if option == 5:
        pass

    



