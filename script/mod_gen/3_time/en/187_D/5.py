def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    diff = [A[i] + B[i] for i in range(N)]
    diff.sort(reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += diff[i]
        else:
            aoki += diff[i]
    if takahashi > aoki:
        print(N)
    else:
        for i in range(N):
            if takahashi - diff[i] + A[i] > aoki - B[i]:
                print(i + 1)
                break

if __name__ == '__main__':
    main()