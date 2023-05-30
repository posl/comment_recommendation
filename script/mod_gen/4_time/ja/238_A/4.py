def is_greater(a,b):
    if a>b:
        return "Yes"
    else:
        return "No"
n = int(input())
print(is_greater(2**n, n**2))
