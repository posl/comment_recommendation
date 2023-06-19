def main():
    n = input()
    n1 = list(n)
    n2 = list(n)
    n1.sort(reverse=True)
    n2.sort()
    if n2[0] == '0':
        n2.pop(0)
        n2.append('0')
    n1 = ''.join(n1)
    n2 = ''.join(n2)
    print(int(n1) * int(n2))

if __name__ == '__main__':
    main()