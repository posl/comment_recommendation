def main():
    n = int(input())
    w_list = []
    for i in range(n):
        w_list.append(input())
    for i in range(n):
        if i != 0:
            if w_list[i] in w_list[0:i]:
                print('No')
                exit()
        if i != n-1:
            if w_list[i][-1] != w_list[i+1][0]:
                print('No')
                exit()
    print('Yes')
