def main():
    s = input()
    s = s.split(' ')
    a = int(s[0])
    b = int(s[1])
    count = 0
    for i in range(0, a+1):
        for j in range(0, a+1):
            for k in range(0, a+1):
                if i+j+k <= a and i*j*k <= b:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()