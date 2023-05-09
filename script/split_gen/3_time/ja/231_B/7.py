def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_set = set(s)
    ans = ''
    ans_num = 0
    for i in s_set:
        if ans_num < s.count(i):
            ans_num = s.count(i)
            ans = i
    print(ans)
