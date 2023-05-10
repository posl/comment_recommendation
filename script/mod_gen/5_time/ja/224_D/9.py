def main():
    M = int(input())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    p = list(map(int, input().split()))
    #print(M)
    #print(u)
    #print(v)
    #print(p)
    #print(len(p))
    #print(len(set(p)))
    #print(list(set(p)))
    if len(p) != len(set(p)):
        print(-1)
        return
    if len(p) == 1:
        print(0)
        return
    if len(p) == 2:
        print(1)
        return
    if len(p) == 3:
        print(2)
        return
    if len(p) == 4:
        print(3)
        return
    if len(p) == 5:
        print(4)
        return
    if len(p) == 6:
        print(5)
        return
    if len(p) == 7:
        print(6)
        return
    if len(p) == 8:
        print(7)
        return
    if len(p) == 9:
        print(8)
        return
    if len(p) == 10:
        print(9)
        return
    if len(p) == 11:
        print(10)
        return
    if len(p) == 12:
        print(11)
        return
    if len(p) == 13:
        print(12)
        return
    if len(p) == 14:
        print(13)
        return
    if len(p) == 15:
        print(14)
        return
    if len(p) == 16:
        print(15)
        return
    if len(p) == 17:
        print(16)
        return
    if len(p) == 18:
        print(17)
        return
    if len(p) == 19:
        print(18)
        return
    if len(p) == 20:
        print(19)
        return
    if len(p) == 21:
        print(20)
        return
    if len(p) == 22:
        print(21)
        return
    if len(p) == 23:

if __name__ == '__main__':
    main()