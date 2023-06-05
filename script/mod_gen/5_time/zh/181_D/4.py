def main():
    s = input()
    s = list(s)
    s.sort()
    for i in range(0, len(s)):
        if s[i] == '0':
            continue
        else:
            break
    s.insert(0, s.pop(i))
    s = int(''.join(s))
    if s % 8 == 0:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()