def solve():
    n = int(input())
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append("0")
        else:
            ans.append("1")
            n -= 1
        n //= -2
    ans.reverse()
    if ans:
        print("".join(ans))
    else:
        print("0")
