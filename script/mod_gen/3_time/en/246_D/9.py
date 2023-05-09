def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    for i in range(1, 2000):
        if i**3 - N >= 0:
            print(i**3)
            return
main()

if __name__ == '__main__':
    main()