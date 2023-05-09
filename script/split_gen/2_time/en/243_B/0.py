def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    A.sort()
    B.sort()
    for i in range(N):
        if A[i] in B:
            count2 += 1
    print(count1)
    print(count2 - count1)
