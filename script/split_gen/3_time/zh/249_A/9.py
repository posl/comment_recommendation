def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka > x and aoki > x:
            print("DRAW")
            break
        elif taka > x:
            print("AOKI")
            break
        elif aoki > x:
            print("TAKAHASHI")
            break
        else:
            taka += a
            aoki += d
            if taka > x and aoki > x:
                print("DRAW")
                break
            elif taka > x:
                print("AOKI")
                break
            elif aoki > x:
                print("TAKAHASHI")
                break
            else:
                taka += b
                aoki += e
                if taka > x and aoki > x:
                    print("DRAW")
                    break
                elif taka > x:
                    print("AOKI")
                    break
                elif aoki > x:
                    print("TAKAHASHI")
                    break
                else:
                    taka += c
                    aoki += f
