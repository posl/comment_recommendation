def main():
    S = input()
    T = input()
    for i in range(len(T)):
        if T[i] != S[i]:
            print(i+1)
            break

if __name__ == '__main__':
    main()