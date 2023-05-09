def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    print(L[0], R[-1] + 1)

if __name__ == '__main__':
    main()