def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ""
    while n != 0:
        ans = str(n%(-2)) + ans
        if n%(-2) == -1:
            n = n//(-2) + 1
        else:
            n = n//(-2)
    print(ans)
