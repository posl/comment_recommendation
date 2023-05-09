def main():
    N = int(input())
    A = input().split()
    A = list(map(int, A))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                count += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                count += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                count += 1
    print(count)
