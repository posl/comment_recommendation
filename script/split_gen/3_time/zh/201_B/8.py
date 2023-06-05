def problems201_b():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: -int(x[1]))
    print(mountains[1][0])
