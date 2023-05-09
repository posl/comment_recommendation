def problems237_a():
    n = int(input())
    if n >= -2**31 and n < 2**31:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    problems237_a()