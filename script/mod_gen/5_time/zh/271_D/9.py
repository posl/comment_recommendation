def main():
    N,S = map(int,input().split())
    a,b = [],[]
    for i in range(N):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    # print(N,S,a,b)
    # print(sum(a))
    # print(sum(b))
    if S > sum(a) and S > sum(b):
        print("No")
        return
    if S == sum(a):
        print("Yes")
        print("".join(["H" for i in range(N)]))
        return
    if S == sum(b):
        print("Yes")
        print("".join(["T" for i in range(N)]))
        return
    if S < sum(a):
        # print("a")
        # print(a)
        # print(b)
        # print(S)
        for i in range(N):
            if a[i] == S:
                print("Yes")
                print("".join(["H" for i in range(i)] + ["T" for i in range(i,N)]))
                return
            elif a[i] < S:
                S -= a[i]
            else:
                print("No")
                return
        print("No")
        return
    if S < sum(b):
        # print("b")
        # print(a)
        # print(b)
        # print(S)
        for i in range(N):
            if b[i] == S:
                print("Yes")
                print("".join(["T" for i in range(i)] + ["H" for i in range(i,N)]))
                return
            elif b[i] < S:
                S -= b[i]
            else:
                print("No")
                return
        print("No")
        return

if __name__ == '__main__':
    main()