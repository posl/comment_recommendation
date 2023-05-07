def main():
    v,a,b,c = map(int,input().split())
    x = v//a
    y = v//b
    z = v//c
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i*a + j*b + k*c == v:
                    print("F" if i < j < k else "M" if i < k < j else "T")
                    return

if __name__ == '__main__':
    main()