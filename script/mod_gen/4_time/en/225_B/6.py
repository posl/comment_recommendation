def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        line = input().split()
        a.append(int(line[0]))
        b.append(int(line[1]))
    a = set(a)
    b = set(b)
    if len(a) == 1 and len(b) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()