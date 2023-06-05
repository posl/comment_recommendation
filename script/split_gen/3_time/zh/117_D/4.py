def input():
    line1 = input().split()
    line2 = input().split()
    n = int(line1[0])
    k = int(line1[1])
    a = []
    for i in range(n):
        a.append(int(line2[i]))
    return n, k, a
