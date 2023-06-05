def main():
    str = input()
    k = int(input())
    i = 0
    while i < k:
        if str[i] == '1':
            i += 1
        else:
            str = str.replace(str[i], str[i] * int(str[i]), 1)
            i += int(str[i])
    print(str[k - 1])
main()
