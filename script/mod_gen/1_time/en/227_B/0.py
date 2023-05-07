def main():
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if 4 * s[i] + 3 * s[j] == 3 * s[i] + 4 * s[j]:
                print("YES")
                return
    print("NO")

if __name__ == '__main__':
    main()