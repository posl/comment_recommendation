def main():
    input = input()
    n, a, b = input.split()
    n = int(n)
    a = int(a)
    b = int(b)
    b_count = 0
    r_count = 0
    for i in range(n):
        if (r_count == a + b):
            break
        elif (r_count < a + b):
            if (r_count < a):
                b_count += 1
            else:
                r_count += 1
        else:
            r_count = 0
    print(b_count)

if __name__ == '__main__':
    main()