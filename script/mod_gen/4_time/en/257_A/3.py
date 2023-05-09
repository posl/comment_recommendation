def get_char(n, x):
    n = int(n)
    x = int(x)
    if x <= n:
        return chr(ord('A') + x - 1)
    else:
        return get_char(n, x - n) 
n, x = input().split()
print(get_char(n, x))

if __name__ == '__main__':
    get_char()