def solve():
    W = int(input())
    N = 300
    A = [1, 2, 3]
    for i in range(4, W+1):
        if i%6 == 0:
            A.append(i)
    print(N)
    print(" ".join(map(str, A)))
