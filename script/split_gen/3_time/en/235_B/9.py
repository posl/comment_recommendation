def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    max_height = h[0]
    for i in range(1,n):
        if h[i] >= max_height:
            max_height = h[i]
    print(max_height)
