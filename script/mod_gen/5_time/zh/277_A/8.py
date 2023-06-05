def main():
    line = input()
    n, x = line.split()
    n = int(n)
    x = int(x)
    p = input()
    p = p.split()
    for i in range(len(p)):
        p[i] = int(p[i])
    for j in range(len(p)):
        if p[j] == x:
            print(j+1)
            break

if __name__ == '__main__':
    main()