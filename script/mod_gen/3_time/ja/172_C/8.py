def solve():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum_time = 0
    sum_book = 0
    while sum_time <= K:
        if len(A) == 0 and len(B) == 0:
            break
        elif len(A) == 0:
            sum_time += B.pop(0)
            sum_book += 1
        elif len(B) == 0:
            sum_time += A.pop(0)
            sum_book += 1
        else:
            if A[0] <= B[0]:
                sum_time += A.pop(0)
                sum_book += 1
            else:
                sum_time += B.pop(0)
                sum_book += 1
    print(sum_book - 1)

if __name__ == '__main__':
    solve()