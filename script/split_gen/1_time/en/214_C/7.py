def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    tsum = sum(t)
    for i in range(n):
        if i == 0:
            print(tsum)
        elif i == 1:
            print(tsum)
        else:
            print(tsum - min(s[:i]))
