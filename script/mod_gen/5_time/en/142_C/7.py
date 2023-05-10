def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = [0] * N
    for i in range(N):
        Bs[As[i]-1] = i+1
    print(*Bs)

if __name__ == '__main__':
    main()