def main():
    p = list(map(int, input().split()))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(p)):
        print(alphabet[p[i]-1], end='')

if __name__ == '__main__':
    main()