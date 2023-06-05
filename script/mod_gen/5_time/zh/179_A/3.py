def main():
    S = input()
    if S[-1] == "s":
        S = S + "es"
    else:
        S = S + "s"
    print(S)

if __name__ == '__main__':
    main()