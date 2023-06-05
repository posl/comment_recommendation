def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_time = min(a%10,b%10,c%10,d%10,e%10)
    if min_time == 0:
        min_time = 10
    print(str((a//10+1)*10)+str((b//10+1)*10)+str((c//10+1)*10)+str((d//10+1)*10)+str((e//10+1)*10))
    #print((a//10+1)*10)
