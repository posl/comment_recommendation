def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    S = ["".join(s) for s in S]
    T = ["".join(t) for t in T]
    S = "".join(S)
    T = "".join(T)
    #print(S)
    #print(T)
    if S == T:
        print("Yes")
        return
    def rotate(s):
        l = []
        for i in range(N):
            l.append(s[i::N])
        return "".join(l)
    for i in range(3):
        S = rotate(S)
        if S == T:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()