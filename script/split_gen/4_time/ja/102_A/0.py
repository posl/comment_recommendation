def main():
    n = int(input())
    ans = 0
    if n % 2 == 0:
        ans = n
    else:
        ans = n * 2
    print(ans)
