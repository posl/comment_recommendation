def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    if n < 100:
        print(9)
        return
    if n < 1000:
        print(9 + n - 99)
        return
    if n < 10000:
        print(9 + 900)
        return
    if n < 100000:
        print(9 + 900 + n - 9999)
        return
    print(9 + 900 + 90000)
main()
