def main():
    n = int(input())
    h = list(map(int, input().split()))
    m = 0
    t = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            t += 1
        else:
            m = max(t, m)
            t = 0
    m = max(t, m)
    print(m)
