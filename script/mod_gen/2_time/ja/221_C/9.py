def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = int(''.join(N))
    print(N)
    return

if __name__ == '__main__':
    main()