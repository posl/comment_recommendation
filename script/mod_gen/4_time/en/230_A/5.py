def main():
    n = int(input())
    if n >= 42:
        print('AGC' + str(n + 1))
    else:
        print('AGC' + str(n).zfill(3))
main()
