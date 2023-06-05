def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = T.pop()
    t2 = 0
    while len(T) > 0:
        if t1 < t2:
            t1 += T.pop()
        else:
            t2 += T.pop()
    print(max(t1, t2))
main()
