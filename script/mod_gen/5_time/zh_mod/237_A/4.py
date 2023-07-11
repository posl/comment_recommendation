def problem237_a(n):
    if n >= -2**31 and n <= 2**31-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problem237_a()