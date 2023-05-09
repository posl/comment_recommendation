def main():
    n = int(input())
    x = 0
    while True:
        if x**3 > n:
            break
        x += 1
    print(x-1)
