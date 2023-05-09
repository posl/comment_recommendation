def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    if n == 1:
        print(t[0])
    else:
        print(t[0] + sum(t[1:]) - t[0])
