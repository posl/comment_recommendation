def main():
    x = int(input())
    for i in range(-200, 200):
        for j in range(-200, 200):
            if i**5 - j**5 == x:
                print(i, j)
                return
main()

if __name__ == '__main__':
    main()