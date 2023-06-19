def main():
    N = int(input())
    x = 0
    while True:
        x += 1
        if x * (x + 1) / 2 >= N:
            break
    print(x)
main()
