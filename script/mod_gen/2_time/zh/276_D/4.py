def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        flag = True
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
                flag = False
                break
        if flag:
            break
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()