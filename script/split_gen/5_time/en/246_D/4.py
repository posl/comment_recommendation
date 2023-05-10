def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    x = 0
    while x < n:
        x += 1
        if x**3 + x**2 + x + 1 > n:
            break
    print(x)
