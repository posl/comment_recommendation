def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            print(abs(x-a))
        else:
            if x < a:
                if d > 0:
                    print(min(abs(x-a),abs(x-a-d*(n-1))))
                else:
                    print(abs(x-a))
            else:
                if d > 0:
                    print(abs(x-a))
                else:
                    print(min(abs(x-a),abs(x-a-d*(n-1))))
main()
