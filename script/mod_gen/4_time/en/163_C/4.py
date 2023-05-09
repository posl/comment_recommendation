def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in a:
        ans[i - 1] += 1
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()