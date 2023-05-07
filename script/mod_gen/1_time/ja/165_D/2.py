def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        x = B-1
    else:
        x = N
    ans = (A*x)//B - A*(x//B)
    print(ans)

if __name__ == '__main__':
    main()