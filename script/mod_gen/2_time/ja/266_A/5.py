def main():
    S = input()
    if len(S) % 2 == 0:
        print('error')
    else:
        print(S[len(S) // 2])

if __name__ == '__main__':
    main()