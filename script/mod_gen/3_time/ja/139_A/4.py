def main():
    s = input()
    t = input()
    hit = 0
    for i in range(3):
        if s[i] == t[i]:
            hit += 1
    print(hit)

if __name__ == '__main__':
    main()