def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
    print(max)
