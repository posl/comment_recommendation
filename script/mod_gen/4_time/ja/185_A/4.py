def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print(min(a))

if __name__ == '__main__':
    main()