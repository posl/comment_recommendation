def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_ = float('inf')
    max_ = 0
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            min_ = min(min_,i)
            max_ = max(max_,i)
    if min_ == float('inf'):
        print('UNSATISFIABLE')
    else:
        print(min_,max_)

if __name__ == '__main__':
    main()