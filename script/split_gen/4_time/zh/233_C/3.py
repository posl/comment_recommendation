def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split()))[1:])
    #print(l)
    #print(n, x)
    #print(l)
    #print(l[0])
    #print(l[0][0])
    #print(l[0][1])
    #print(l[0][2])
    #print(l[1])
    #print(l[1][0])
    #print(l[1][1])
    #print(l[1][2])
    #print(l[2])
    #print(l[2][0])
    #print(l[2][1])
    #print(l[2][2])
    res = 0
    for i in range(n):
        for j in range(len(l[i])):
            if x % l[i][j] == 0:
                res += 1
    print(res)
