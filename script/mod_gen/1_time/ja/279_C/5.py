def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()