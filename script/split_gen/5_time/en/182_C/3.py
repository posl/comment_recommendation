def main():
    n = input()
    n = list(map(int, n))
    n.sort()
    n = n[::-1]
    total = sum(n)
    if total % 3 == 0:
        print(0)
    else:
        if total % 3 == 1:
            for i in range(len(n)):
                if n[i] % 3 == 1:
                    n.pop(i)
                    break
            if len(n) == 0:
                print(-1)
            else:
                print(1)
        else:
            for i in range(len(n)):
                if n[i] % 3 == 2:
                    n.pop(i)
                    break
            if len(n) == 0:
                print(-1)
            else:
                print(1)
