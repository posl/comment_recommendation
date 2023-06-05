def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append([int(i) for i in input().split()])
    AB.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print("No")
            return
    print("Yes")
