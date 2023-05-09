def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N):
        if H[i] == max(H):
            print(i+1)
            break

if __name__ == '__main__':
    main()