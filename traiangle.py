# for i in range(5):
#     print("*" * (i+1))
#     i += 1
a = int(input("enter a: "))
b = int(input("enter b: "))
def swapVal(x,y):
    x=x+y
    y=x-y
    x=x-y
    return x,y

swappedNumbers = swapVal(a,b)
print(swappedNumbers[0], end=" ")
print(swappedNumbers[1])
