def main():
    x = int(input())
    for a in range(10**5):
        for b in range(10**5):
            if a**5-b**5 == x:
                print(a,b)
                return

if __name__ == '__main__':
    main()