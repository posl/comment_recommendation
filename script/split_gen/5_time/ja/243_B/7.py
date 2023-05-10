def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans_1 = 0
    ans_2 = 0
    for i in range(N):
        if A[i] == B[i]:
            ans_1 += 1
    for i in range(N):
        for j in range(N):
            if A[i] == B[j]:
                ans_2 += 1
    print(ans_1)
    print(ans_2-ans_1)
