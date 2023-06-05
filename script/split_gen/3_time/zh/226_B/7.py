def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = [tuple(a[i][1:]) for i in range(n)]
    print(len(set(a)))
