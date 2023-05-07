def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    print(max_h)
