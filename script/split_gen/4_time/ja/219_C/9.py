def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    #print(s)
    #print(x)
    x_dict = {}
    for i in range(len(x)):
        x_dict[x[i]] = chr(ord('a') + i)
    #print(x_dict)
    s_dict = {}
    for i in range(n):
        tmp = ''
        for j in range(len(s[i])):
            tmp += x_dict[s[i][j]]
        s_dict[tmp] = s[i]
    #print(s_dict)
    s_dict = sorted(s_dict.items())
    #print(s_dict)
    for i in range(n):
        print(s_dict[i][1])
