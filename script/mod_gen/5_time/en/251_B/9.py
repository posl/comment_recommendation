def find_good_integers(N, W, A):
    max_A = max(A)
    max_sum = max_A * 3
    if max_sum < W:
        return N
    else:
        good_integers = [0] * (max_sum + 1)
        for i in range(N):
            for j in range(i, N):
                for k in range(j, N):
                    good_integers[A[i] + A[j] + A[k]] += 1
        return good_integers[:W+1].count(0)
N, W = map(int, input().split())
A = list(map(int, input().split()))
print(find_good_integers(N, W, A))
