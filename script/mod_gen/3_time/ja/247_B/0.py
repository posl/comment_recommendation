def main():
    N = int(input())
    s = [0] * N
    t = [0] * N
    for i in range(N):
        s[i], t[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print("No")
                    exit()
    print("Yes")

if __name__ == '__main__':
    main()