Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    count = [0] * 10
    for i in range(len(s)):
        count[int(s[i])] += 1
    for i in range(112, 1000, 8):
        c = [0] * 10
        c[int(str(i)[0])] += 1
        c[int(str(i)[1])] += 1
        c[int(str(i)[2])] += 1
        flag = True
        for j in range(10):
            if c[j] > count[j]:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def solve():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0:
            print('Yes')
        elif int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    # 3桁以上の場合
    from collections import Counter
    c = Counter(s)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - c:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    S = input()
    if len(S) == 1:
        if S == '8':
            print('Yes')
        else:
            print('No')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(112, 1000, 8):
            if not len(set(str(i))) == 3:
                continue
            if not set(str(i)) <= set(S):
                continue
            print('Yes')
            break
        else:
            print('No')

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    count = [0] * 10
    for i in range(len(s)):
        count[int(s[i])] += 1
    for i in range(112, 1000, 8):
        tmp = [0] * 10
        tmp[i % 10] += 1
        tmp[(i % 100) // 10] += 1
        tmp[i // 100] += 1
        flag = True
        for j in range(10):
            if tmp[j] > count[j]:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    s = list(input())
    if len(s) == 1:
        if s[0] == "8":
            print("Yes")
        else:
            print("No")
    elif len(s) == 2:
        if int(s[0]+s[1]) % 8 == 0 or int(s[1]+s[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        ans = "No"
        for i in range(100, 1000):
            if i % 8 == 0:
                if str(i)[0] in s and str(i)[1] in s and str(i)[2] in s:
                    ans = "Yes"
        print(ans)

=======
Suggestion 6

def solve():
    from collections import Counter
    s = input()
    if len(s) == 1:
        if int(s) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    if len(s) >= 3:
        c = Counter(s)
        for i in range(112, 1000, 8):
            if not Counter(str(i)) - c:
                print('Yes')
                return
        print('No')
        return

=======
Suggestion 7

def solve():
    from collections import Counter
    s = input()
    if len(s) == 1:
        if int(s) % 8 == 0:
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        cnt = Counter(s)
        for i in range(112, 1000, 8):
            if not Counter(str(i)) - cnt:
                print('Yes')
                return
        print('No')

=======
Suggestion 8

def solve():
    s = input()
    if len(s) == 1:
        print("Yes" if s == "8" else "No")
        return
    if len(s) == 2:
        print("Yes" if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 else "No")
        return
    counts = [0] * 10
    for c in s:
        counts[int(c)] += 1
    for i in range(112, 1000, 8):
        if not is_valid(i, counts):
            continue
        print("Yes")
        return
    print("No")

=======
Suggestion 9

def main():
    from collections import Counter
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if int(s) % 8 == 0:
            print("Yes")
        elif int(s[1] + s[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    cnt = Counter(s)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 10

def is_ok(n):
    return n%8==0
