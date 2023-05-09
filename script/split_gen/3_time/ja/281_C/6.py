def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    time = T % sum_A
    for i in range(N):
        if time >= A[i]:
            time -= A[i]
        else:
            print(i+1, time)
            break
