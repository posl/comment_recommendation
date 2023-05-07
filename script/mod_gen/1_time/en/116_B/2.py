def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1]%2 == 0:
            a.append(a[-1]//2)
        else:
            a.append(3*a[-1]+1)
        if a[-1] in a[:-1]:
            print(len(a))
            break

if __name__ == '__main__':
    main()