def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == len(set(T)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()