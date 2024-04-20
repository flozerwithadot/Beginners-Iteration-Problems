tries = 0
correct = False
while not correct:
    answer = input("Enter password: ")
    if answer == "yippee":
        correct = True
    else:
        tries += 1
    if tries == 3:
        print("Locked")
        exit()
print("Yippee!!")