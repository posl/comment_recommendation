def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if(A[j]%A[i]==0):
                count += 1
                break
    print(N-count)
