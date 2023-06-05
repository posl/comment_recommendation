def main():
    a,b,w = map(int,input().split())
    min_num = 0
    max_num = 0
    if a > w*1000//b:
        print("UNSATISFIABLE")
    else:
        for i in range(1,w*1000//a+1):
            if a*i <= w*1000 and w*1000 <= b*i:
                if min_num == 0:
                    min_num = i
                max_num = i
        print(min_num,max_num)
    return
