def main():
    N = int(input())
    A = list(map(int, input().split()))
    count_list = [0] * N
    for i in range(N):
        count_list[A[i]-1] += 1
    total = 0
    for i in range(N):
        total += count_list[i] * (count_list[i]-1) // 2
    for i in range(N):
        print(total - (count_list[A[i]-1]-1))
