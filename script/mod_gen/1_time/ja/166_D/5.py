def main():
    x = int(input())
    for i in range(-300, 300):
        for j in range(-300, 300):
            if i**5-j**5 == x:
                print(i, j)
                return
main()

if __name__ == '__main__':
    main()