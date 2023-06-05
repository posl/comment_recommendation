def problem161_b():
    n = 0
    m = 0
    a = []
    while True:
        try:
            line = input()
            if line:
                if n == 0:
                    n = int(line.split(' ')[0])
                    m = int(line.split(' ')[1])
                else:
                    a = line.split(' ')
            else:
                break
        except:
            break
    a = [int(i) for i in a]
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print('是')
    else:
        print('否')
