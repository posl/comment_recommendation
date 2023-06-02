Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num = int(input())
    count = 0
    for i in range(1, num + 1):
        if i < 1000:
            continue
        elif i < 1000000:
            count += 1
        elif i < 1000000000:
            count += 2
        elif i < 1000000000000:
            count += 3
        elif i < 1000000000000000:
            count += 4
        elif i < 1000000000000000000:
            count += 5
        elif i < 1000000000000000000000:
            count += 6
        elif i < 1000000000000000000000000:
            count += 7
        elif i < 1000000000000000000000000000:
            count += 8
        elif i < 1000000000000000000000000000000:
            count += 9

=======
Suggestion 2

def get_comma_cnt(n):
    comma_cnt = 0
    n_str = str(n)
    n_len = len(n_str)
    for i in range(n_len):
        if i % 3 == 0 and i != 0:
            comma_cnt += 1
    return comma_cnt

=======
Suggestion 3

def main():
    n = int(input())
    i = 1
    count = 0
    while n >= 1000:
        count += i * (n - 999)
        n //= 1000
        i += 1
    print(count)

=======
Suggestion 4

def f(n):
    s = 0
    while n > 0:
        s += 1
        n //= 10
    return s

=======
Suggestion 5

def problem195_c():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    if n < 1000:
        print(0)
    else:
        num = 0
        for i in range(1, 16):
            if i == 1:
                num += 0
            elif i == 2:
                num += n - 999
            else:
                num += (n - 10**(3*(i-2)) + 1) * (i - 1)
        print(num)

=======
Suggestion 7

def main():
    n = int(input())
    s = str(n)
    l = len(s)
    ans = 0
    if l < 4:
        print(0)
        return
    elif l >= 4 and l < 7:
        ans = (n - 999) * 1
    elif l >= 7 and l < 10:
        ans = (999999 - 999) * 1 + (n - 999999) * 2
    elif l >= 10 and l < 13:
        ans = (999999999 - 999999) * 1 + (n - 999999999) * 2 + (n - 999999999) * 3
    elif l >= 13 and l < 16:
        ans = (999999999999 - 999999999) * 1 + (n - 999999999999) * 2 + (n - 999999999999) * 3 + (n - 999999999999) * 4
    elif l >= 16 and l < 19:
        ans = (999999999999999 - 999999999999) * 1 + (n - 999999999999999) * 2 + (n - 999999999999999) * 3 + (n - 999999999999999) * 4 + (n - 999999999999999) * 5
    elif l >= 19 and l < 22:
        ans = (999999999999999999 - 999999999999999) * 1 + (n - 999999999999999999) * 2 + (n - 999999999999999999) * 3 + (n - 999999999999999999) * 4 + (n - 999999999999999999) * 5 + (n - 999999999999999999) * 6
    elif l >= 22 and l < 25:
        ans = (999999999999999999999 - 999999999999999999) * 1 + (n - 999999999999999999999) * 2 + (n - 999999999999999999999) * 3 + (n - 999999999999999999999

=======
Suggestion 8

def solution(n):
    # 1. 递归求解
    # 2. 递归求解
    # 3. 递归求解
    # 4. 递归求解
    # 5. 递归求解
    # 6. 递归求解
    # 7. 递归求解
    # 8. 递归求解
    # 9. 递归求解
    # 10. 递归求解
    # 11. 递归求解
    # 12. 递归求解
    # 13. 递归求解
    # 14. 递归求解
    # 15. 递归求解
    # 16. 递归求解
    # 17. 递归求解
    # 18. 递归求解
    # 19. 递归求解
    # 20. 递归求解
    # 21. 递归求解
    # 22. 递归求解
    # 23. 递归求解
    # 24. 递归求解
    # 25. 递归求解
    # 26. 递归求解
    # 27. 递归求解
    # 28. 递归求解
    # 29. 递归求解
    # 30. 递归求解
    # 31. 递归求解
    # 32. 递归求解
    # 33. 递归求解
    # 34. 递归求解
    # 35. 递归求解
    # 36. 递归求解
    # 37. 递归求解
    # 38. 递归求解
    #

=======
Suggestion 9

def count_commas(number):
    if number < 1000:
        return 0
    else:
        return int(number / 1000) + count_commas(int(number/1000))

=======
Suggestion 10

def comma_count(n):
    if n < 1000:
        return 0
    else:
        return int((n-1000)/1000) + 1 + comma_count(int((n-1000)/1000)*1000 + 999)

print(comma_count(int(input())))
