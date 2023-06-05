def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(input().split())
    l = list(map(lambda x: x[1:], l))
    l = list(map(lambda x: ''.join(x), l))
    print(len(set(l)))
