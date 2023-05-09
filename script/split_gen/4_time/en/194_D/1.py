def main():
    n = int(input())
    res = 0
    for i in range(1,n):
        res += n/(n-i)
    print(res)
