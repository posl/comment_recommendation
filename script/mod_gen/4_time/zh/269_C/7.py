def main():
    N = int(input())
    for i in range(1<<15):
        x = 0
        for j in range(15):
            if i&(1<<j):
                x += 1<<(j*4)
        if N&x == x:
            print(x)

if __name__ == '__main__':
    main()