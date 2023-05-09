def main():
    x = int(input())
    a, b = 0, 0
    for i in range(-200, 200):
        for j in range(-200, 200):
            if i**5 - j**5 == x:
                a, b = i, j
                break
    print(a, b)

if __name__ == '__main__':
    main()