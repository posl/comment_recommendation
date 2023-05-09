def main():
    N = int(input())
    S = input()
    new_S = ""
    for i in range(N):
        if S[i] == ",":
            if i%2 == 0:
                new_S = new_S + ","
            else:
                new_S = new_S + "."
        else:
            new_S = new_S + S[i]
    print(new_S)

if __name__ == '__main__':
    main()