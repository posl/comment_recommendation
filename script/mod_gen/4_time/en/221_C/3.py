def main():
    n = input()
    n = list(map(int, n))
    n.sort(reverse=True)
    a, b = 0, 0
    for i in range(len(n)):
        if i % 2 == 0:
            a = a * 10 + n[i]
        else:
            b = b * 10 + n[i]
    print(a * b)

if __name__ == '__main__':
    main()