def main():
    x,y = map(int, input().split())
    if (x+y)%3!=0:
        print(0)
        return
    else:
        if x<y:
            x,y = y,x
        num = (x+y)//3
        if x>2*num:
            print(0)
            return
        else:
            x = x-num
            y = y-2*num
            ans = 1
            for i in range(1,x+1):
                ans = ans*(num-x+i)//i
            print(ans%1000000007)
            return
