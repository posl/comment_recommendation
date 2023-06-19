def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    s_list = [S_1, S_2, S_3, S_4]
    if len(s_list) == len(set(s_list)):
        print('Yes')
    else:
        print('No')
