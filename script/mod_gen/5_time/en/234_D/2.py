def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(n-k+1):
        ans.append(max(p[i:i+k]))
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()