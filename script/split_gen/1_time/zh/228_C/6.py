def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append([int(i) for i in input().split()])
    for i in range(n):
        p[i].sort(reverse=True)
        if sum(p[i][:k]) >= 300:
            print("Yes")
        else:
            print("No")
