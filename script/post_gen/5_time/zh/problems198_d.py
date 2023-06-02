Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(s1, s2, s3):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2

    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return False

    char_list = list(chars)
    for perm in permutations(range(10), len(chars)):
        d = dict(zip(char_list, perm))
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = sum(d[c] * (10 ** (len(s1) - i - 1)) for i, c in enumerate(s1))
        n2 = sum(d[c] * (10 ** (len(s2) - i - 1)) for i, c in enumerate(s2))
        n3 = sum(d[c] * (10 ** (len(s3) - i - 1)) for i, c in enumerate(s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return True
    return False

s1 = input()
s2 = input()
s3 = input()

=======
Suggestion 2

def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    # 获取所有的不重复字符
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    # 生成所有数字的排列
    from itertools import permutations
    for p in permutations(range(10), len(chars)):
        # 构造映射表
        d = {c: p[i] for i, c in enumerate(chars)}
        # 首位不能为0
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        # 将字符串转换为数字
        n1 = sum([d[s] * 10 ** (len(s1) - i - 1) for i, s in enumerate(s1)])
        n2 = sum([d[s] * 10 ** (len(s2) - i - 1) for i, s in enumerate(s2)])
        n3 = sum([d[s] * 10 ** (len(s3) - i - 1) for i, s in enumerate(s3)])
        # 判断是否满足条件
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

=======
Suggestion 3

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    # s1 + s2 = s3
    # s1 + s2 - s3 = 0
    # s1 + s2 - s3 = 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0

    # s1 + s2 = s3
    # s1 + s2 - s3 = 0
    # s1 + s2 - s3 = 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0
    # 1 2 3 4 5 6 7 8 9 0

    # s1 + s2 = s3
    # s1 + s2 - s3 = 0
    # s1 + s2 - s3 = 0
    # 1 2 3 4 5 6 7 8

=======
Suggestion 4

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
    for i in range(10**(len(s1)-1), 10**len(s1)):
        if len(set(str(i))) != len(str(i)):
            continue
        for j in range(10**(len(s2)-1), 10**len(s2)):
            if len(set(str(j))) != len(str(j)):
                continue
            if i + j == int(s3):
                d1 = {}
                d2 = {}
                for k in range(len(s1)):
                    d1[s1[k]] = str(i)[k]
                for k in range(len(s2)):
                    d2[s2[k]] = str(j)[k]
                if len(d1) != len(d2):
                    continue
                for k in range(len(s3)):
                    if s3[k] in d1.keys():
                        if d1[s3[k]] != str(i)[k]:
                            break
                    if s3[k] in d2.keys():
                        if d2[s3[k]] != str(j)[k]:
                            break
                else:
                    print(i)
                    print(j)
                    print(s3)
                    return
    else:
        print("UNSOLVABLE")

=======
Suggestion 5

def solve(s1, s2, s3):
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return False
    chars = list(chars)
    chars.sort()
    for perm in permutations(range(10), len(chars)):
        if 0 in perm[:len(chars) - 1]:
            continue
        d = dict(zip(chars, perm))
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return True
    return False

=======
Suggestion 6

def to_int(s, d):
    ans = 0
    for i in range(len(s)):
        ans = ans*10 + d[s[i]]
    return ans

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s)>10:
        print("UNSOLVABLE")
        return
    s = list(s)
    c = [0]*26
    for i in range(len(s)):
        c[ord(s[i])-ord('a')] = i
    if len(s)>9:
        for i in range(10):
            c[i] = i
    import itertools
    for p in itertools.permutations([i for i in range(len(s))]):
        if c[ord(s1[0])-ord('a')]!=0 and c[ord(s2[0])-ord('a')]!=0 and c[ord(s3[0])-ord('a')]!=0:
            n1 = n2 = n3 = 0
            for i in range(len(s1)):
                n1 = n1*10+c[ord(s1[i])-ord('a')]
            for i in range(len(s2)):
                n2 = n2*10+c[ord(s2[i])-ord('a')]
            for i in range(len(s3)):
                n3 = n3*10+c[ord(s3[i])-ord('a')]
            if n1+n2==n3:
                print(n1)
                print(n2)
                print(n3)
                return
    print("UNSOLVABLE")

=======
Suggestion 8

def solve(s1,s2,s3):
    if len(s1)>len(s3) or len(s2)>len(s3):
        return "UNSOLVABLE"
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = s1 + '0'*(len(s3)-len(s1))
    s2 = s2 + '0'*(len(s3)-len(s2))
    s3 = s3 + '0'*(len(s3)-len(s3))
    s1 = s1.replace(s1[0],str(0))
    s2 = s2.replace(s2[0],str(0))
    s3 = s3.replace(s3[0],str(0))
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if int(s1.replace(s1[0],str(i))) + int(s2.replace(s2[0],str(j))) == int(s3.replace(s3[0],str(k))):
                    return int(s1.replace(s1[0],str(i))),int(s2.replace(s2[0],str(j))),int(s3.replace(s3[0],str(k)))
    return "UNSOLVABLE"

s1 = input()
s2 = input()
s3 = input()
print(*solve(s1,s2,s3),sep='\n')

=======
Suggestion 9

def solve(s1, s2, s3):
    if len(s1) > len(s3) or len(s2) > len(s3):
        return False
    if len(s1) + len(s2) < len(s3):
        return False
    if len(s1) == 1 and s1 == s3:
        return True
    if len(s2) == 1 and s2 == s3:
        return True
    if len(s3) == 1 and s3 == s1:
        return True
    if len(s3) == 1 and s3 == s2:
        return True

    if len(s1) == 1 and len(s2) == 1:
        if s1 == s3[0] and s2 == s3[1]:
            return True
        if s2 == s3[0] and s1 == s3[1]:
            return True

    if len(s1) == 1:
        for i in range(len(s3)):
            if s1 == s3[i]:
                if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:]):
                    return True
        return False
    if len(s2) == 1:
        for i in range(len(s3)):
            if s2 == s3[i]:
                if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:]):
                    return True
        return False

    if len(s1) == 2:
        for i in range(len(s3)):
            if s1[0] == s3[i]:
                for j in range(len(s3)):
                    if s1[1] == s3[j]:
                        if i < j:
                            if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:j]) and solve(s1, s2, s3[j+1:]):
                                return True
                        else:
                            if solve(s1, s2, s3[:j]) and solve(s1, s2, s3[j+1:i]) and solve(s1, s2, s3[i+1:]):
                                return True
        return False

    if len(s2) == 2:

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    # print(s1, s2, s3)
    # print(len(s1), len(s2), len(s3))
    # print(s1, s2, s3)
    # print(len(s1), len(s2), len(s3))
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** len(s1) - 1, 10 ** (len(s1) - 1) - 1, -1):
        # print(i)
        n1 = str(i)
        if len(n1) != len(s1):
            continue
        flag = True
        for j in range(len(s1)):
            if n1[j] in n1[:j] or n1[j] in n1[j + 1:]:
                flag = False
                break
        if not flag:
            continue
        # print(n1)
        for k in range(10 ** len(s2) - 1, 10 ** (len(s2) - 1) - 1, -1):
            n2 = str(k)
            if len(n2) != len(s2):
                continue
            flag = True
            for j in range(len(s2)):
                if n2[j] in n2[:j] or n2[j] in n2[j + 1:]:
                    flag = False
                    break
            if not flag:
                continue
            # print(n2)
            for l in range(10 ** len(s3) - 1, 10 ** (len(s3) - 1) - 1, -1):
                n3 = str(l)
                if len(n3) != len(s3):
