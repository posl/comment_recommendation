def main():
    n = int(input())
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for c in s:
        result += alphabet[(alphabet.index(c) + n) % 26]
    print(result)

if __name__ == '__main__':
    main()