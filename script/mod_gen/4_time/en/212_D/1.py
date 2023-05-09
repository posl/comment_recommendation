def main():
    n = int(input())
    a = []
    for i in range(n):
        x = input().split()
        if int(x[0]) == 1:
            a.append(int(x[1]))
        elif int(x[0]) == 2:
            a = [i + int(x[1]) for i in a]
        else:
            print(min(a))
            a.remove(min(a))

if __name__ == '__main__':
    main()