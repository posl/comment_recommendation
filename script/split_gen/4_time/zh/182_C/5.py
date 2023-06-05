def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return
    else:
        for i in range(1, len(str(n))):
            if n % 3 == 0:
                print(i)
                return
            else:
                n = int(str(n)[:-1])
        print(-1)
        return
