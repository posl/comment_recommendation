def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == 'A' or i == 'C' or i == 'G' or i == 'T':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
main()
