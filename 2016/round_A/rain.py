T = int(input())

output = []

for case in range(T):
    shape = [int(var) for var in input().split(" ")]
    H = []
    for i in range(shape[0]):
        H.append([int(var) for var in input().split(" ")]) 
    W = []
    # FIND W

    sum = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            sum += H[i][j]-W[i][j]
    output.append(sum)

for i, val in enumerate(output):
    print("Case #"+str(i + 1)+": "+val)