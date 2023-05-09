def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt2 = 0
    cnt3 = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            cnt2 += 1
        while a % 3 == 0:
            a //= 3
            cnt3 += 1
    if all(a == A[0] for a in A):
        print(cnt2 + cnt3)
    else:
        print(-1)

if __name__ == '__main__':
    main()