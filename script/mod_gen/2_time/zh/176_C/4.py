def main():
    n = input()
    total = 0
    for i in n:
        total += int(i)
    if total % 9 == 0:
        print('Yes')
    else:
        print('No')
main()
