Synthesizing 10/10 solutions

=======
Suggestion 1

def is753(n):
    if '7' in str(n) and '5' in str(n) and '3' in str(n):
        return True
    else:
        return False

=======
Suggestion 2

def check753(num):
    if num < 357:
        return False
    if num % 2 == 0:
        return False
    if num % 5 == 0:
        return False
    if num % 3 == 0:
        return False
    str_num = str(num)
    if "0" in str_num:
        return False
    if "1" in str_num:
        return False
    if "2" in str_num:
        return False
    if "4" in str_num:
        return False
    if "6" in str_num:
        return False
    if "8" in str_num:
        return False
    if "9" in str_num:
        return False
    return True

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            ans += 1
    print(ans)

=======
Suggestion 4

def check753(n):
    if n%3 == 0:
        return False
    else:
        return True

=======
Suggestion 5

def is753(x):
    s = str(x)
    return s.count("7") > 0 and s.count("5") > 0 and s.count("3") > 0

=======
Suggestion 6

def is753(num):
    # 7,5,3がそれぞれ1回以上入っているかチェック
    if num.count('7') > 0 and num.count('5') > 0 and num.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 7

def is753(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False

=======
Suggestion 8

def count753(num):
    count = 0
    for i in range(1, num+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

=======
Suggestion 9

def is753(num):
    if num < 357:
        return False
    if num > 357 and num < 375:
        return False
    if num > 375 and num < 537:
        return False
    if num > 537 and num < 573:
        return False
    if num > 573 and num < 735:
        return False
    if num > 735 and num < 753:
        return False
    if num > 753 and num < 3357:
        return False
    if num > 3357 and num < 3375:
        return False
    if num > 3375 and num < 3537:
        return False
    if num > 3537 and num < 3557:
        return False
    if num > 3557 and num < 3573:
        return False
    if num > 3573 and num < 3575:
        return False
    if num > 3575 and num < 3577:
        return False
    if num > 3577 and num < 3735:
        return False
    if num > 3735 and num < 3753:
        return False
    if num > 3753 and num < 3757:
        return False
    if num > 3757 and num < 3773:
        return False
    if num > 3773 and num < 5373:
        return False
    if num > 5373 and num < 5375:
        return False
    if num > 5375 and num < 5377:
        return False
    if num > 5377 and num < 5537:
        return False
    if num > 5537 and num < 5557:
        return False
    if num > 5557 and num < 5573:
        return False
    if num > 5573 and num < 5575:
        return False
    if num > 5575 and num < 5577:
        return False
    if num > 5577 and num < 5733:
        return False
    if num > 5733 and num < 5735:
        return False
    if num > 5735 and num < 5737:
        return False
    if num > 5737 and num <

=======
Suggestion 10

def dfs(i, use3, use5, use7, n):
    if i > n:
        return 0
    ret = 1 if use3 and use5 and use7 else 0
    ret += dfs(i * 10 + 3, True, use5, use7, n)
    ret += dfs(i * 10 + 5, use3, True, use7, n)
    ret += dfs(i * 10 + 7, use3, use5, True, n)
    return ret

n = int(input())
print(dfs(0, False, False, False, n))
