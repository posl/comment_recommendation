def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                print(a, b)
                return
    print(0, 0)

if __name__ == '__main__':
    main()