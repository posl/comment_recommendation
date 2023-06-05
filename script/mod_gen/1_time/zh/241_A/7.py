def main():
    a = list(map(int, input().split()))
    b = [0]
    for i in range(100):
        b.append(a[b[-1]])
    print(b[3])

if __name__ == '__main__':
    main()