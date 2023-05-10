def main():
    n, k = map(int, input().split())
    cnt = 0
    for i in range(k):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            if A[j] == i+1:
                cnt += 1
    print(n - cnt)
