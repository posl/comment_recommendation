def main():
    n,k = map(int, input().split())
    a = []
    for _ in range(k):
        a.append(list(map(int, input().split()))[1:])
    a = set(sum(a, []))
    print(n-len(a))
