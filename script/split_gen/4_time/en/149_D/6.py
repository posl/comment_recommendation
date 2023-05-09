def main():
    n,k = map(int, input().split())
    r,s,p = map(int, input().split())
    t = input()
    point = 0
    for i in range(n):
        if t[i] == "r" and i < k:
            point += p
        elif t[i] == "r" and i >= k and t[i-k] != "r":
            point += p
        elif t[i] == "s" and i < k:
            point += r
        elif t[i] == "s" and i >= k and t[i-k] != "s":
            point += r
        elif t[i] == "p" and i < k:
            point += s
        elif t[i] == "p" and i >= k and t[i-k] != "p":
            point += s
    print(point)
