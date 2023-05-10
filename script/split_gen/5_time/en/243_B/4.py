def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count_1 = 0
    count_2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count_1 += 1
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    count_2 += 1
    print(count_1)
    print(count_2)
