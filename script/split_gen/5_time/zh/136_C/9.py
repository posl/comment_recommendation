def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(1, n):
        if h[i-1] - h[i] >= 2:
            print("No")
            exit(0)
        elif h[i-1] - h[i] == 1:
            h[i-1] -= 1
    print("Yes")
