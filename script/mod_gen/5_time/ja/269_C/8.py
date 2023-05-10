def main():
    n = int(input())
    for i in range(2**15):
        x = 0
        for j in range(15):
            if i>>j&1:
                x += 2**j
        if x&n == x:
            print(x)

if __name__ == '__main__':
    main()