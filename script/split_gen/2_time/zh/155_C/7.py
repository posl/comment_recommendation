def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s = input()
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    max = 0
    for key in dic:
        if dic[key] > max:
            max = dic[key]
    ans = []
    for key in dic:
        if dic[key] == max:
            ans.append(key)
    ans.sort()
    for s in ans:
        print(s)
