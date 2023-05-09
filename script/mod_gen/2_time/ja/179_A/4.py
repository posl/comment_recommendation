def main():
    S = input()
    if S[-1] != "s":
        print(S + "s")
    else:
        print(S + "es")

if __name__ == '__main__':
    main()