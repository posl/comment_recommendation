def main():
    S = input()
    index = -1
    for i in range(len(S)):
        if S[i] == 'a':
            index = i + 1
    print(index)

if __name__ == '__main__':
    main()