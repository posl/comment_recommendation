def main():
    s = input()
    k = int(input())
    s = s.replace(".", " ")
    s = s.split()
    s = [len(x) for x in s]
    s.sort(reverse = True)
    print(s[0] + s[1] + k)

if __name__ == '__main__':
    main()