Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max_product(a,b,c,d):
    if a*c > a*d:
        if a*c > b*c:
            if a*c > b*d:
                return a*c
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d
    else:
        if a*d > b*c:
            if a*d > b*d:
                return a*d
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 3

def max_product(a,b,c,d):
    """返回整数a,b,c,d的最大可能值"""
    # 1. 先把所有可能的值算出来
    # 2. 然后找出最大值
    # 3. 返回最大值
    # 4. 确保a,b,c,d都是整数
    # 5. 确保a<=b, c<=d
    # 6. 确保a<=x<=b, c<=y<=d
    # 7. 确保x,y都是整数
    # 8. 确保x*y是整数
    # 9. 确保x*y<=2^63-1
    # 10. 确保x*y>=-2^63
    # 11. 确保x*y是最大值
    # 12. 返回x*y
    if a > b or c > d:
        return None
    if a <= 0 and b >= 0 and c <= 0 and d >= 0:
        return 0
    if a <= 0 and b >= 0:
        return max(a*c, a*d, b*c, b*d, 0)
    if c <= 0 and d >= 0:
        return max(a*c, a*d, b*c, b*d, 0)
    return max(a*c, a*d, b*c, b*d)

=======
Suggestion 4

def max_product(a,b,c,d):
    return max(a*c,a*d,b*c,b*d)

a,b,c,d = map(int,input().split())
print(max_product(a,b,c,d))

=======
Suggestion 5

def max(a, b):
    if a > b:
        return a
    else:
        return b
