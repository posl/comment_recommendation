def main():
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[0]==num_list[1] and num_list[1]==num_list[2] and num_list[3]==num_list[4]:
        print('Yes')
    elif num_list[0]==num_list[1] and num_list[2]==num_list[3] and num_list[3]==num_list[4]:
        print('Yes')
    else:
        print('No')
