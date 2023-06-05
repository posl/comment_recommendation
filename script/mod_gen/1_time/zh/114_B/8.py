def main():
    s = input()
    x = 0
    for i in range(4, len(s)+1):
        for j in range(len(s)-i+1):
            x = int(s[j:j+i])
            if abs(x-753) < abs(x-753):
                x = abs(x-753)
    print(x)

if __name__ == '__main__':
    main()