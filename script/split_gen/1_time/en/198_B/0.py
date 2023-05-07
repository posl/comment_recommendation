def main():
    n = input()
    n = n[::-1]
    while n[0] == '0':
        n = n[1:]
    if n == n[::-1]:
        print('Yes')
    else:
        print('No')
