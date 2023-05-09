def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    count = 1
    sum = 0
    for i in range(N):
        sum = sum + L[i]
        if sum <= X:
            count = count + 1
    print(count)
