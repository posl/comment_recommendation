def main():
    a,b = map(int,input().split())
    g = 1
    t = 0
    while a > g**2:
        t += b
        g += 1
    print(t+(a/g**0.5))
