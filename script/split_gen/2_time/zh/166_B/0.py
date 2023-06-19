def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        d = int(input())
        a.append(list(map(int, input().split())))
    print(n - len(set(sum(a, []))))
