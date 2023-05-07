def main():
    s = input()
    k = int(input())
    s = s.replace('.', ' ')
    s = s.split()
    x = []
    for i in s:
        x.append(len(i))
    x.sort()
    x.reverse()
    print(x[0] + k)

if __name__ == '__main__':
    main()