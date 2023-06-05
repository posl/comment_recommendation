def get_ABCD(n):
    if n <= 999:
        return "ABC"
    else:
        return "ABD"
    
n = int(input())
print(get_ABCD(n))
