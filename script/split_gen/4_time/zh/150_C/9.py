def main():
    n = int(input())
    p = list(map(int, input().split(" ")))
    q = list(map(int, input().split(" ")))
    print(abs(p.index(1) - q.index(1)))
