def main():
    S = input()
    S = list(S)
    S = [int(i) for i in S]
    for i in range(10):
        if i not in S:
            print(i)
            break

if __name__ == '__main__':
    main()