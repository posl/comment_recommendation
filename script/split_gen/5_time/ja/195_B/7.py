def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_num = 0
    max_num = 0
    for i in range(1,1000001):
        if a*i <= w and w <= b*i:
            if min_num == 0:
                min_num = i
            max_num = i
    if min_num == 0:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)
