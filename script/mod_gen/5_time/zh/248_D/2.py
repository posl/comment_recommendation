def count_number_of_x_in_a(L, R, X, a):
    count = 0
    for i in range(L-1, R):
        if a[i] == X:
            count += 1
    return count
N = int(input())
a = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    print(count_number_of_x_in_a(L, R, X, a))
