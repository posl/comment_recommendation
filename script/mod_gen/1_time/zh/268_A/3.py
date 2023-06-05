def main():
    a = input().split()
    b = []
    for i in range(5):
        if a[i] not in b:
            b.append(a[i])
    print(len(b))

if __name__ == '__main__':
    main()