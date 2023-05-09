def main():
    n = int(input())
    a = 0
    for i in range(1, n):
        a += n/(n-i)
    print(a)
