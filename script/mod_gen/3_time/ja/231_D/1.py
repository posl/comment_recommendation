def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 'Yes'
    for i in range(M):
        if abs(A[i] - B[i]) == 1:
            continue
        else:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()