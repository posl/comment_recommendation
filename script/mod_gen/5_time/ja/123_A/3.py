def main():
    # a, b, c, d, e, k = map(int, input().split())
    # print("Yay!" if e-a <= k else ":(")
    a, b, c, d, e, k = [int(input()) for i in range(6)]
    print("Yay!" if e-a <= k else ":(")

if __name__ == '__main__':
    main()