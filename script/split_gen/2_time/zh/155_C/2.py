def main():
    n = int(input())
    s = dict()
    for i in range(n):
        tmp = input()
        if tmp not in s:
            s[tmp] = 1
        else:
            s[tmp] += 1
    max = 0
    for key in s.keys():
        if s[key] > max:
            max = s[key]
    for key in s.keys():
        if s[key] == max:
            print(key)
