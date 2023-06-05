def main():
    a,b,w=map(int,input().split())
    w=w*1000
    min=w//b
    max=w//a
    if w%a==0:
        if w//a==w//b:
            print(w//a,w//a)
        elif w//a!=w//b:
            print(w//a,w//b)
    else:
        if w//a==w//b:
            print('UNSATISFIABLE')
        elif w//a!=w//b:
            print(w//a+1,w//b)

if __name__ == '__main__':
    main()