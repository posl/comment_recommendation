def check(h):
    for i in range(1,len(h)):
        if h[i-1] > h[i]:
            h[i] += 1
    if sorted(h) == h:
        return True
    else:
        return False
n = int(input())
h = list(map(int, input().split()))
