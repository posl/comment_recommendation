def main():
    x = int(input())
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                print("{} {}".format(a,b))
                return

if __name__ == '__main__':
    main()