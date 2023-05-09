def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if H[i-1] < H[i]:
            H[i] -= 1
        if H[i-1] > H[i]:
            ans = 1
    if ans == 0:
        print("Yes")
    else:
        print("No")
