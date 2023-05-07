def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #compute
    ans = min(B) - max(A) + 1
    if ans < 0:
        ans = 0
    #output
    print(ans)

if __name__ == '__main__':
    main()