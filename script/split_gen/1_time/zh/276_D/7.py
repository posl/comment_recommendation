def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)
