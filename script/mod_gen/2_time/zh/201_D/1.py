def main():
    s = input()
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        if all([i[int(j)] == s[int(j)] for j in range(len(s)) if s[int(j)] in '0123456789']):
            count += 1
    print(count)

if __name__ == '__main__':
    main()