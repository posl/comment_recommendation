def solution(n):
    if n == 0:
        return 0
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append("0")
            n //= -2
        else:
            ans.append("1")
            n = (n-1) // -2
    ans.reverse()
    return "".join(ans)

if __name__ == '__main__':
    solution()