def main():
    T = int(input())
    for i in range(0,T):
        N = int(input())
        A = list(map(int,input().split()))
        count = 0
        for j in range(0,N):
            if A[j] % 2 == 1:
                count += 1
        print(count)
