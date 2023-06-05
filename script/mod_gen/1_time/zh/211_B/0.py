def main():
    s_list = []
    for i in range(4):
        s_list.append(input())
    if 'H' in s_list and '2B' in s_list and '3B' in s_list and 'HR' in s_list:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()