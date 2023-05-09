def main():
    n = int(input())
    #print(n)
    s_list = []
    for i in range(n):
        s = input()
        s_list.append(s)
    #print(s_list)
    s_list_unique = list(set(s_list))
    #print(s_list_unique)
    if len(s_list) == len(s_list_unique):
        print('Yes')
    else:
        print('No')
