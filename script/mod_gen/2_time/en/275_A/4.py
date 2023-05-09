def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = max(H)
    for i in range(N):
        if H[i] == maxH:
            print(i+1)
            break

if __name__ == '__main__':
    main()