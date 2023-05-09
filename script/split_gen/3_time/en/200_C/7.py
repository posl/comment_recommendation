def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod200 = []
    for i in range(N):
        mod200.append(A[i] % 200)
    count = 0
    for i in range(200):
        count += mod200.count(i) * (mod200.count(i) - 1) // 2
    print(count)
