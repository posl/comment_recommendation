def main():
    s = input()
    max = 0
    tmp = 0
    for c in s:
        if c in ['A', 'C', 'G', 'T']:
            tmp += 1
            if tmp > max:
                max = tmp
        else:
            tmp = 0
    print(max)

if __name__ == '__main__':
    main()