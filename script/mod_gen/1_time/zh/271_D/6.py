def main():
    N, S = map(int, input().split())
    card = []
    for i in range(N):
        card.append(list(map(int, input().split())))
    if S == 0:
        print("Yes")
        print("T"*N)
        return
    for i in range(2**N):
        s = 0
        a = []
        for j in range(N):
            if (i>>j)&1:
                s += card[j][0]
                a.append("H")
            else:
                s += card[j][1]
                a.append("T")
        if s == S:
            print("Yes")
            print("".join(a))
            return
    print("No")

if __name__ == '__main__':
    main()