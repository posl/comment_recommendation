def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()