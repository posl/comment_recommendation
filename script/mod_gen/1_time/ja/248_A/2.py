def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            return

if __name__ == '__main__':
    main()