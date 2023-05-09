def main():
    N, M = map(int, input().split())
    ans = "No"
    for i in range(M):
        k, *x = map(int, input().split())
        if len(set(x)) != len(x):
            ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()