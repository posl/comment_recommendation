def solve():
    str = input()
    length = len(str)
    count = 0
    for i in range(int(length/2)):
        if str[i] != str[length - i - 1]:
            count += 1
    print(count)
