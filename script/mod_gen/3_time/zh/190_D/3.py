def main():
    n = int(input())
    count = 0
    for i in range(1, 10**6):
        if i*(i-1) == 2*n:
            count += 1
        elif i*(i-1) > 2*n:
            break
    print(count*2)

if __name__ == '__main__':
    main()