def numUniqueChars(name):
    name = name.replace(' ','')
    if len(name) <= 1:
        return len(name)
    return numUniqueChars(name.replace(name[0],'')) + 1
T = int(input())
output = [0]*T
for i in range(T):
    N = int(input())
    max = 0
    for j in range(N):
        name = input()
        numUniqueChar = numUniqueChars(name)
        if max < numUniqueChar:
            max = numUniqueChar
            output[i] = name
        if max == numUniqueChar:
            output[i] = min(name, output[i])

for i, val in enumerate(output):
    print("Case #"+str(i + 1)+": "+val)