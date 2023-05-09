def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)
