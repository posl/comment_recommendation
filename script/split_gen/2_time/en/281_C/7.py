def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= T:
            print(i+1, T - sum + A[i])
            break
