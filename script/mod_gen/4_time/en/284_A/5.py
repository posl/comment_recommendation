def main():
    N = int(input())
    strings = []
    for i in range(N):
        strings.append(input())
    strings.reverse()
    for string in strings:
        print(string)

if __name__ == '__main__':
    main()