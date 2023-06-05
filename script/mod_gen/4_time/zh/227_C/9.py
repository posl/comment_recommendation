def solve():
    #先输入数据
    n = int(input())
    #开始解题
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if a * b * c <= n:
                    if a == b and b == c:
                        count += 1
                    elif a == b or b == c:
                        count += 3
                    else:
                        count += 6
    print(count)

if __name__ == '__main__':
    solve()