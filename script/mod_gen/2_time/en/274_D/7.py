def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.insert(0, 0)
    # print(A)
    for i in range(1, N+2):
        for j in range(i+1, N+2):
            if i == j:
                continue
            for k in range(j+1, N+2):
                if k == j or k == i:
                    continue
                if i == 1 and j == 2 and k == 3:
                    continue
                if i == 1 and j == 3 and k == 2:
                    continue
                if i == 2 and j == 1 and k == 3:
                    continue
                if i == 2 and j == 3 and k == 1:
                    continue
                if i == 3 and j == 1 and k == 2:
                    continue
                if i == 3 and j == 2 and k == 1:
                    continue
                # print(i, j, k)
                if (A[j] - A[i]) * (A[k] - A[j]) == (y - 0) * (x - A[j]):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()