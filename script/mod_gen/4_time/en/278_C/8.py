def main():
    n,q = map(int,input().split())
    user_list = []
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            if (a,b) not in user_list:
                user_list.append((a,b))
        elif t == 2:
            if (a,b) in user_list:
                user_list.remove((a,b))
        elif t == 3:
            if (a,b) in user_list and (b,a) in user_list:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()