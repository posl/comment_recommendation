def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    c = 0
    for i in range(len(b)):
        c = max(c, a.count(b[i]))
    print(n-c)
