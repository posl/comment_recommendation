def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

if __name__ == '__main__':
    main()