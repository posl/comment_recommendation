def main():
    s = input()
    count = 0
    for i in range(10000):
        tmp = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in tmp:
                break
            if s[j] == 'x' and str(j) in tmp:
                break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()