def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    result = 0
    for i in range(N):
        if A[i] > result:
            print(result)
            break
        else:
            result += A[i]
    else:
        print(result)
