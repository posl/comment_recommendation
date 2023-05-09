def main():
    n = int(input())
    s = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            s.append(int(q[1]))
        elif q[0] == '2':
            x = int(q[1])
            c = int(q[2])
            for i in range(c):
                if x in s:
                    s.remove(x)
        elif q[0] == '3':
            print(max(s) - min(s))

if __name__ == '__main__':
    main()