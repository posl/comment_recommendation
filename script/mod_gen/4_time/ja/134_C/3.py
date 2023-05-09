def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

if __name__ == '__main__':
    main()