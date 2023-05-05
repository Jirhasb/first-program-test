
evenNum = []
oddNum = []

for i in range(10):
    num = int(input("Enter number: "))
    if num %2 == 0:
        evenNum.append(num)
    else:
        oddNum.append(num)

print("Even numbers are: " + str(evenNum))
print("Odd numbers are: " + str(oddNum))

