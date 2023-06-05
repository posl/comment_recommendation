def main():
    line1 = input()
    line2 = input()
    line1 = line1.split()
    line2 = line2.split()
    N = int(line1[0])
    P = int(line1[1])
    a = []
    for i in range(N):
        a.append(int(line2[i]))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

if __name__ == '__main__':
    main()