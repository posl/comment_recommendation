def main():
    k = int(input())
    h = 21
    m = 0
    m = m + k
    if m >= 60:
        h = h + 1
        m = m - 60
    if m < 10:
        print(str(h) + ':0' + str(m))
    else:
        print(str(h) + ':' + str(m))

if __name__ == '__main__':
    main()