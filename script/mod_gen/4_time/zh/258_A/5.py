def main():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m = 0
            h += 1
    print(str(h).zfill(2) + ':' + str(m).zfill(2))

if __name__ == '__main__':
    main()