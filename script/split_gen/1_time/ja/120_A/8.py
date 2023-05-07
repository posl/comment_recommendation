def main():
    # n = int(input())
    a, b, c = map(int, input().split())
    # s = input()
    # l = list(map(int, input().split()))
    # l = [list(map(int,input().split())) for _ in range(n)]
    if a * c <= b:
        print(c)
    else:
        print(b // a)
