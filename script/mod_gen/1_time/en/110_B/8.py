def main():
    #input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #compute
    if max(x) < min(y) and max(x) < Y and X < min(y):
        ans = "No War"
    else:
        ans = "War"
    #output
    print(ans)

if __name__ == '__main__':
    main()