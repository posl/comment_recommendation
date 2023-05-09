def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a*100
    s = sum(b)
    k = x//s*len(b)
    r = x%s
    for i in range(len(b)):
        if r < 0:
            break
        r -= b[i]
        k += 1
    print(k)
