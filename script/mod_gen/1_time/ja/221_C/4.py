def main():
    n = input()
    n = [int(i) for i in n]
    n.sort(reverse=True)
    a = n[0]
    b = 0
    for i in n[1:]:
        b = b*10 + i
    print(a*b)

if __name__ == '__main__':
    main()