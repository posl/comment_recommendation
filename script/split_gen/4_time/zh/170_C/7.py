def main():
    #input
    x,n = map(int,input().split())
    p_list = list(map(int,input().split()))
    #process
    if n == 0:
        print(x)
    else:
        p_list.sort()
        for i in range(0,100):
            if x - i not in p_list:
                print(x - i)
                break
            elif x + i not in p_list:
                print(x + i)
                break
