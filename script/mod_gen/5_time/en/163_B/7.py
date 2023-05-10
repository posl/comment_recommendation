def calc_days(N, M, A):
    if N < sum(A):
        return -1
    return N - sum(A)
N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(calc_days(N, M, A))

if __name__ == '__main__':
    calc_days()