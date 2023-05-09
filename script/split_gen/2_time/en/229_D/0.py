def main():
    s = input()
    k = int(input())
    l = []
    count = 0
    for i in range(len(s)):
        if s[i] == 'X':
            count += 1
        else:
            l.append(count)
            count = 0
    l.append(count)
    if k >= len(l):
        print(len(s))
    else:
        print(max([sum(l[i:i+k+1]) for i in range(len(l)-k)]))
