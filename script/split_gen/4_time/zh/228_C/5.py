def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p = sorted(p, key=lambda x: sum(x), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")
