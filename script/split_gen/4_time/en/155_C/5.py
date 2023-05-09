def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    max = 0
    for i in dic:
        if dic[i] > max:
            max = dic[i]
    for i in dic:
        if dic[i] == max:
            print(i)
