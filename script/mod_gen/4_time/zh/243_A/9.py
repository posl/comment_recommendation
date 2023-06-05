def main():
    v,a,b,c = map(int,input().split())
    while v >= 0:
        if v >= a:
            v -= a
            if v >= b:
                v -= b
                if v >= c:
                    v -= c
                    if v >= 0:
                        continue
                    else:
                        print('T')
                        break
                else:
                    print('C')
                    break
            else:
                print('B')
                break
        else:
            print('A')
            break

if __name__ == '__main__':
    main()