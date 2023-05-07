def main():
    s = input()
    s = s + s
    min = s
    max = s
    for i in range(len(s)):
        if s[i:i+len(s)//2] < min:
            min = s[i:i+len(s)//2]
        if s[i:i+len(s)//2] > max:
            max = s[i:i+len(s)//2]
    print(min)
    print(max)

if __name__ == '__main__':
    main()