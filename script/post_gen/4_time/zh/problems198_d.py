Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入S_1,S_2,S_3
    s1 = input()
    s2 = input()
    s3 = input()

    # 生成字母表
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return

    # 生成S_1,S_2,S_3对应的数字
    char_to_num = {}
    for i, char in enumerate(chars):
        char_to_num[char] = i

    # 将S_1,S_2,S_3转换为数字
    n1 = 0
    for i, char in enumerate(s1):
        n1 += char_to_num[char] * pow(10, len(s1) - i - 1)
    n2 = 0
    for i, char in enumerate(s2):
        n2 += char_to_num[char] * pow(10, len(s2) - i - 1)
    n3 = 0
    for i, char in enumerate(s3):
        n3 += char_to_num[char] * pow(10, len(s3) - i - 1)

    # 求解
    for n_1 in range(pow(10, len(s1))):
        for n_2 in range(pow(10, len(s2))):
            if n_1 + n_2 == n3:
                if n1 == n_1 and n2 == n_2:
                    continue
                else:
                    print(n_1)
                    print(n_2)
                    print(n3)
                    return

    print("UNSOLVABLE")

=======
Suggestion 2

def solve(s1, s2, s3):
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    d = {}
    for c in s1 + s2 + s3:
        d[c] = 0
    if len(d) > 10:
        return "UNSOLVABLE"
    d = list(d.keys())
    for i in range(10 ** len(d)):
        x = str(i).zfill(len(d))
        for j in range(len(d)):
            d[j] = x[j]
        if check(s1, s2, s3, d):
            return "\n".join([s1, s2, s3])
    return "UNSOLVABLE"

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    m = {}
    for i in range(len(s1)):
        if s1[i] in m:
            if m[s1[i]] != s3[i]:
                print("UNSOLVABLE")
                return
        else:
            m[s1[i]] = s3[i]
    for i in range(len(s2)):
        if s2[i] in m:
            if m[s2[i]] != s3[i + len(s1)]:
                print("UNSOLVABLE")
                return
        else:
            m[s2[i]] = s3[i + len(s1)]
    if len(m) > 10:
        print("UNSOLVABLE")
        return
    m = sorted(m.items(), key=lambda x: x[1])
    if m[0][1] == '0':
        print("UNSOLVABLE")
        return
    for i in range(len(m)):
        print(m[i][1], end="")
    print()

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2) or len(s1) > len(s3) or len(s2) > len(s3):
        print("UNSOLVABLE")
        return
    else:
        for i in range(10**(len(s3)-len(s1)), 10**(len(s3)-len(s1)+1)):
            if len(str(i)) != len(s1):
                continue
            else:
                if is_valid(s1, s2, s3, i):
                    print(i)
                    print(i*(10**(len(s3)-len(s2))))
                    print(int(s3))
                    return
        print("UNSOLVABLE")
        return

=======
Suggestion 5

def solve(s1,s2,s3):
    # print(s1, s2, s3)
    # 1. 长度不一样，直接返回
    if len(s1) != len(s2) or len(s1) != len(s3):
        return
    # 2. 重复字符的个数
    s = s1 + s2 + s3
    # print(s)
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    # print(d)
    if len(d) > 10:
        return
    # 3. 重复字符的个数
    # print(s1, s2, s3)
    # 4. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 5. 重复字符的个数
    # print(s1, s2, s3)
    # 6. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 7. 重复字符的个数
    # print(s1, s2, s3)
    # 8. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 9. 重复字符的个数
    # print(s1, s2, s3)
    # 10. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 11. 重复字符的个数
    # print(s1, s2, s3)
    # 12. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 13. 重复字符的个数
    # print(s1, s2, s3)
    # 14. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 15.

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        print('UNSOLVABLE')
        return
    for i in range(10**(len(s3)-len(s1)), 10**(len(s3)-len(s1)+1)):
        s1d = str(i)
        if len(s1d) != len(s1):
            continue
        s2d = str(i * 2)
        if len(s2d) != len(s2):
            continue
        s3d = str(i * 3)
        if len(s3d) != len(s3):
            continue
        d = {}
        for j in range(len(s1d)):
            if s1[j] in d:
                if d[s1[j]] != s1d[j]:
                    break
            else:
                d[s1[j]] = s1d[j]
        else:
            for j in range(len(s2d)):
                if s2[j] in d:
                    if d[s2[j]] != s2d[j]:
                        break
                else:
                    d[s2[j]] = s2d[j]
            else:
                for j in range(len(s3d)):
                    if s3[j] in d:
                        if d[s3[j]] != s3d[j]:
                            break
                    else:
                        d[s3[j]] = s3d[j]
                else:
                    print(s1d)
                    print(s2d)
                    print(s3d)
                    return
    print('UNSOLVABLE')
    return

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s3) < len(s1) or len(s3) < len(s2):
        print("UNSOLVABLE")
        exit()
    used = [False] * 10
    for c in s1 + s2 + s3:
        used[ord(c) - ord('a')] = True
    if sum(used) > 10:
        print("UNSOLVABLE")
        exit()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** len(s1)):
        n1 = str(i).zfill(len(s1))
        if any(n1[ord(c) - ord('a')] == '0' for c in s1):
            continue
        for j in range(10 ** len(s2)):
            n2 = str(j).zfill(len(s2))
            if any(n2[ord(c) - ord('a')] == '0' for c in s2):
                continue
            n3 = str(i + j).zfill(len(s3))
            if any(n3[ord(c) - ord('a')] == '0' for c in s3):
                continue
            if all(n1[ord(c) - ord('a')] == n2[ord(c) - ord('a')] == n3[ord(c) - ord('a')] for c in s1 + s2 + s3):
                print(i)
                print(j)
                print(i + j)
                exit()
    print("UNSOLVABLE")

=======
Suggestion 8

def get_int(str):
    return reduce(lambda x,y:10*x+y, map(lambda x:ord(x)-ord('a'), str))

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            k = i + j
            if len(str(k)) != len(s3):
                continue
            d = {}
            for m in range(len(s1)):
                if s1[m] not in d:
                    d[s1[m]] = str(i)[m]
                elif d[s1[m]] != str(i)[m]:
                    break
            else:
                for m in range(len(s2)):
                    if s2[m] not in d:
                        d[s2[m]] = str(j)[m]
                    elif d[s2[m]] != str(j)[m]:
                        break
                else:
                    for m in range(len(s3)):
                        if s3[m] not in d:
                            d[s3[m]] = str(k)[m]
                        elif d[s3[m]] != str(k)[m]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(k)
                        return
    else:
        print("UNSOLVABLE")

=======
Suggestion 10

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set()
    for c in s1:
        s.add(c)
    for c in s2:
        s.add(c)
    for c in s3:
        s.add(c)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    n = len(s)
    for i in range(10 ** n):
        a = str(i).zfill(n)
        if len(set(a)) < n:
            continue
        m = {}
        for j in range(n):
            m[s[j]] = a[j]
        if m[s1[0]] == '0' or m[s2[0]] == '0' or m[s3[0]] == '0':
            continue
        n1 = 0
        n2 = 0
        n3 = 0
        for c in s1:
            n1 = n1 * 10 + int(m[c])
        for c in s2:
            n2 = n2 * 10 + int(m[c])
        for c in s3:
            n3 = n3 * 10 + int(m[c])
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')
