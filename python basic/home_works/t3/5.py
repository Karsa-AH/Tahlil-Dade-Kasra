a = input("Enter a str:")
for o in range(0, len(a)):
    if a[o].isalpha() == True:
        print(a[o], end=" ")
print("")
for i in range(0, len(a)):
    if a[i].isdigit() == True:
        print(a[i], end=" ")
