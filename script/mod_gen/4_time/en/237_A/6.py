def problems237_a():
    n = int(input())
    if -2**31 <= n <= 2**31 - 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problems237_a()