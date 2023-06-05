def main():
    n,x = map(int, input().split())
    xl = list(map(int, input().split()))
    xl.append(x)
    xl.sort()
    d = xl[1] - xl[0]
    for i in range(1, n):
        d = min(d, xl[i+1] - xl[i])
    print(d)
