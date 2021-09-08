# Part 1
p = int(input("Please enter the principle: "))
n = int(input("Please enter the number of years: "))
r = float(input("Please enter the rate of interest: "))
simpleInterest = p * n * r / 100
print(simpleInterest)

# Part 2
foodList = ['banana', 'chocolate', 'popcorn', 'ice cream', 'carrots']
print(foodList[2])
foodList.append('apples')
print(foodList)
foodList.insert(2, 'tacos')
print(foodList)

# Part 3
for i in range(1, 6):
    print("I'am a programmer")


def function1():
    for sqrNum in range(1, 10):
        print(sqrNum ** 2)


function1()
