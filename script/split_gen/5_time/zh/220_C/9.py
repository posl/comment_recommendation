def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a * 10**100
    s = 0
    for i in range(len(b)):
        s += b[i]
        if s > x:
            print(i+1)
            break
