def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i+1] < H[i]:
            H[i+1] += 1
    if H == sorted(H):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()