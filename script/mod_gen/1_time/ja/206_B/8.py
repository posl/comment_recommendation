def main():
    n = int(input())
    i = 1
    while i*(i+1)//2 < n:
        i += 1
    print(i)
    return

if __name__ == '__main__':
    main()