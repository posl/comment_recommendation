def problems243_a():
    v,a,b,c = map(int,input().split())
    shampoo = [a,b,c]
    shampoo.sort()
    shampoo.reverse()
    while v>0:
        for i in range(3):
            v -= shampoo[i]
            if v<=0:
                if i == 0:
                    print('F')
                elif i == 1:
                    print('M')
                else:
                    print('T')
                return
    return

if __name__ == '__main__':
    problems243_a()