def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    for i in range(n):
        print(s_list[-1-i])

if __name__ == '__main__':
    main()