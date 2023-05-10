def main():
    n, a, b = map(int, input().split())
    s = input()
    min_cost = 0
    for i in range(n//2):
        if s[i] == s[-i-1]:
            continue
        elif s[i] == 'a' or s[-i-1] == 'a':
            min_cost += a
        else:
            print(-1)
            exit()
    if n%2 == 1 and s[n//2] != 'a':
        min_cost += a
    print(min_cost)

if __name__ == '__main__':
    main()