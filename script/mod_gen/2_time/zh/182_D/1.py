def main():
    n = input()
    n = int(n)
    k = len(str(n))
    if k == 1:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        n = str(n)
        count = 0
        for i in range(k):
            count += int(n[i])
        if count % 3 == 0:
            print(0)
        elif k == 2:
            print(-1)
        else:
            count = 0
            for i in range(k):
                count += int(n[i])
                if count % 3 == 0:
                    print(1)
                    break
                else:
                    count = 0
            if count == 0:
                print(-1)
main()
