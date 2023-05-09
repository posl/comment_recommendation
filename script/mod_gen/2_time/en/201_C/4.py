def main():
    s = input()
    count = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == 'o' and pin.find(str(j)) == -1:
                flag = False
                break
            if s[j] == 'x' and pin.find(str(j)) != -1:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()