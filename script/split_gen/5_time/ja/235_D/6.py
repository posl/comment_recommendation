def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 1:
        print(1)
        return
    if n % a == 0:
        count = 0
        while n > 1:
            n //= a
            count += 1
        print(count)
        return
    else:
        count = 0
        while n > 1:
            if n % a == 0:
                n //= a
                count += 1
            else:
                n = int(str(n)[-1] + str(n)[:-1])
                count += 1
        print(count)
        return
