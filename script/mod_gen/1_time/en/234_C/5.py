def main():
    K = int(input())
    i = 0
    j = 2
    while True:
        if i == K:
            print(j)
            break
        if j % 2 == 0:
            j *= 10
        else:
            j += 1
        i += 1

if __name__ == '__main__':
    main()