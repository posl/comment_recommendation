def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(x)
    #print(n)
    #print(s)
    x_dict = {}
    for i in range(len(x)):
        x_dict[x[i]] = i
    #print(x_dict)
    #print(x_dict['a'])
    for i in range(n):
        s[i] = s[i][::-1]
    #print(s)
    s.sort()
    #print(s)
    for i in range(n):
        s[i] = s[i][::-1]
    #print(s)
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = i
    #print(s_dict)
    #print(s_dict['a'])
    s_dict_keys = list(s_dict.keys())
    s_dict_keys.sort()
    #print(s_dict_keys)
    for i in range(n):
        print(s[s_dict[s_dict_keys[i]]])
