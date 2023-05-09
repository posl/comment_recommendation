def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        ans = t[i]
        for j in range(n):
            if t[(i+j)%n] < ans:
                break
            ans = t[(i+j)%n] + s[(i+j)%n]
        print(ans)

if __name__ == '__main__':
    main()