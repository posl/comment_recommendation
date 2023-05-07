def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] != i+1:
            ans += 1
    if ans == 0 or ans == 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()