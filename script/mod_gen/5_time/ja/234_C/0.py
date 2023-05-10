def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b)+str(n%b)
    return str(n%b)
K = int(input())
print(int(base10to(K, 9).replace("8", "2")))

if __name__ == '__main__':
    base10to()