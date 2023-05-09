def main():
    A, B = map(int, input().split())
    g = 1
    ans = 0
    while True:
        if g * B + A / (g ** 0.5) < A:
            ans = g * B + A / (g ** 0.5)
            g += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()