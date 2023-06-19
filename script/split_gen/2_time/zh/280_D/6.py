def main():
    k = int(input())
    if k % 2 != 0:
        print(k)
        return
    else:
        i = 2
        while True:
            if k % (i ** 2) == 0:
                i += 1
                continue
            elif k % i == 0:
                print(i)
                return
            else:
                print(k)
                return
