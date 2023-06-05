def main():
    S = input()
    for i in range(0, len(S)):
        if (i % 2 == 0 and S[i] == 'L') or (i % 2 == 1 and S[i] == 'R'):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()