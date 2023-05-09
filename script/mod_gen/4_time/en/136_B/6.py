def main():
    n = input()
    print(len([i for i in range(1, n+1) if len(str(i)) % 2 == 1]))

if __name__ == '__main__':
    main()