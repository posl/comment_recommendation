def main():
    H,W,N = map(int,input().split())
    a_list = []
    b_list = []
    for i in range(N):
        a,b = map(int,input().split())
        a_list.append(a)
        b_list.append(b)
    a_list = list(set(a_list))
    b_list = list(set(b_list))
    a_list.sort()
    b_list.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a_list)):
        a_dict[a_list[i]] = i+1
    for i in range(len(b_list)):
        b_dict[b_list[i]] = i+1
    for i in range(N):
        print(a_dict[a_list[i]],b_dict[b_list[i]])

if __name__ == '__main__':
    main()