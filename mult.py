positive = False
while not positive:
    number = int(input("Enter a number: "))
    if number > 0:
        positive = True
    else:
        print("Not a positive integer.")
name = input("Enter your name: ")
for x in range(number):
    print(name)