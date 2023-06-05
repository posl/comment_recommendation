def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x and aoki >= x:
            print('draw')
            break
        elif taka >= x:
            print('aoki')
            break
        elif aoki >= x:
            print('taka')
            break
        else:
            taka += a
            aoki += d
            if taka >= x and aoki >= x:
                print('draw')
                break
            elif taka >= x:
                print('taka')
                break
            elif aoki >= x:
                print('aoki')
                break
            else:
                taka += b
                aoki += e
                if taka >= x and aoki >= x:
                    print('draw')
                    break
                elif taka >= x:
                    print('taka')
                    break
                elif aoki >= x:
                    print('aoki')
                    break
                else:
                    taka += c
                    aoki += f
                    if taka >= x and aoki >= x:
                        print('draw')
                        break
                    elif taka >= x:
                        print('taka')
                        break
                    elif aoki >= x:
                        print('aoki')
                        break
