def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        flag = True
        for j in range(N):
            if i == j:
                continue
            if A[j] % A[i] == 0:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()