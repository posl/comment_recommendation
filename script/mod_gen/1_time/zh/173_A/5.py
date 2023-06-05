def change(n):
    if n <= 1000:
        return 1000-n
    else:
        return change(n-1000)
print(change(int(input())))
