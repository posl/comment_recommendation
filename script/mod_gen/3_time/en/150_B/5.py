def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()