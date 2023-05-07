def main():
    S = input()
    if S == "0":
        print(1)
        return
    print((len(S) - 1) + (len(S) - 1) // 2)

if __name__ == '__main__':
    main()