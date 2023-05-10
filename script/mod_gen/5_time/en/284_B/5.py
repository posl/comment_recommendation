def count_odd_number(N, A):
    odd_number_count = 0
    for i in range(N):
        if A[i] % 2 == 1:
            odd_number_count += 1
    return odd_number_count
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(count_odd_number(N, A))

if __name__ == '__main__':
    count_odd_number()