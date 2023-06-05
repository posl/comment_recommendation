def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n-1):
        if s[i] == 'L':
            a.insert(0, i+2)
        else:
            a.append(i+2)
    print(" ".join(map(str, a)))

if __name__ == '__main__':
    main()