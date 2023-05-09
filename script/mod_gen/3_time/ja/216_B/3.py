def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(S) != len(set(S)) or len(T) != len(set(T)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()