def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = max(H)
    for i in range(N):
        if H[i] == max_h:
            print(i+1)
            break
