def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s = list(input())
        s.sort()
        s = ''.join(s)
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    ans = 0
    for key in dic:
        ans += dic[key]*(dic[key]-1)//2
    print(ans)
