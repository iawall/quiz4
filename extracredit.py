array = ["abc",4556,"orange"]
newArray = []
for i in range(len(array)):
   # print(i)
    toStr = str(array[i])
    newArray.append(len(toStr))
print(newArray)

    