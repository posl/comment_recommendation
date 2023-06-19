def main():
    h = int(input())
    k = 0
    while h > 0:
        h = h // 2
        k += 1
    print(2 ** k - 1)
main()
