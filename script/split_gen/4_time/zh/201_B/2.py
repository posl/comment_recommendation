def main():
    n = int(input())
    h = []
    for i in range(n):
        h.append(input().split())
    h.sort(key=lambda x: int(x[1]), reverse=True)
    print(h[1][0])
