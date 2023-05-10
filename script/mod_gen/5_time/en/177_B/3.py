def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)-len(t)+1):
        count_temp = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count_temp += 1
        if count == 0:
            count = count_temp
        elif count > count_temp:
            count = count_temp
    print(count)

if __name__ == '__main__':
    main()