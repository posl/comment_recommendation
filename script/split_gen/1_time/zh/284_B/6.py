def main():
    n = int(input())
    for i in range(n):
        a = input()
        b = input()
        c = b.split()
        d = 0
        for j in c:
            if int(j) % 2 != 0:
                d += 1
        print(d)
main()
