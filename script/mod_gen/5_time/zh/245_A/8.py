def get_up_early(a,b,c,d):
    if a<c:
        print("高桥")
    elif a==c:
        if b<d:
            print("高桥")
        elif b==d:
            print("同一时间")
        else:
            print("青木")
    else:
        print("青木")
    return

if __name__ == '__main__':
    get_up_early()