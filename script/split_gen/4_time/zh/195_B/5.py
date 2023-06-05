def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min_num = 1000000
    max_num = 0
    for i in range(a,b+1):
        if i * w % 1000 == 0:
            min_num = min(min_num,i * w // 1000)
            max_num = max(max_num,i * w // 1000)
    if min_num == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)
