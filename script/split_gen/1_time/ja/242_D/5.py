def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        # S = s
        # for i in range(t):
        #     S = S.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
        # print(S[k-1])
        # ここから解説
        # 0回置換したときのsの各文字の置換後の文字数
        a, b, c = s.count('A'), s.count('B'), s.count('C')
        # 置換回数tに対して、各文字が何回置換されるか
        a_t = t % 3 * a
        b_t = t % 3 * b
        c_t = t % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t2 = (t // 3) % 3 * a
        b_t2 = (t // 3) % 3 * b
        c_t2 = (t // 3) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t3 = (t // 9) % 3 * a
        b_t3 = (t // 9) % 3 * b
        c_t3 = (t // 9) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t4 = (t // 27) % 3 * a
        b_t4 = (t // 27) % 3 * b
        c_t4 = (t // 27) % 3 * c
        # 置換回数tに対して、各文字が何回置換されるか
        a_t5 = (t // 81) % 3 * a
        b_t5 = (t // 81) % 3 * b
