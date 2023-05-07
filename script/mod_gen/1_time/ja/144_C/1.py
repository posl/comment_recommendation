def main():
    N = int(input())
    i = 1
    j = 1
    while True:
        if i * j >= N:
            break
        if i < j:
            i += 1
        else:
            j += 1
    print(i + j - 2)

if __name__ == '__main__':
    main()