def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        a = str(i)
        if len(a) % 2 == 0:
            if a[:len(a)//2] == a[len(a)//2:]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()