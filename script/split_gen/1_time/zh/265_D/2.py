def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # N, P, Q, R = 10, 5, 7, 5
    # A = [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]
    # N, P, Q, R = 9, 100, 101, 100
    # A = [31, 41, 59, 26, 53, 58, 97, 93, 23]
    # N, P, Q, R = 7, 1, 1, 1
    # A = [1, 1, 1, 1, 1, 1, 1]
    min_A = []
    max_A = []
    min_A.append(A[0])
    max_A.append(A[0])
    for i in range(1, N):
        min_A.append(min(min_A[i - 1], A[i]))
        max_A.append(max(max_A[i - 1], A[i]))
    max_P = P
    max_Q = Q
    max_R = R
    for i in range(1, N):
        max_P = max(max_P, P * A[i])
        max_Q = max(max_Q, max_P + Q * A[i])
        max_R = max(max_R, max_Q + R * A[i])
    print(max_R)
    print(max_A)
    print(min_A)
    if max_R == max_A[-1] and min_A[-1] == 1:
        print('Yes')
    else:
        print('No')
