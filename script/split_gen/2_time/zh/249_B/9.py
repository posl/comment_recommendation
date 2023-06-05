def run():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print("draw")
            return
        taka += a
        if taka >= x:
            print("taka")
            return
        aoki += d
        if aoki >= x:
            print("aoki")
            return
        if aoki >= taka:
            print("aoki")
            return
        taka += b
        if taka >= x:
            print("taka")
            return
        aoki += e
        if aoki >= x:
            print("aoki")
            return
        if aoki >= taka:
            print("aoki")
            return
        taka += c
        if taka >= x:
            print("taka")
            return
        aoki += f
        if aoki >= x:
            print("aoki")
            return
        if aoki >= taka:
            print("aoki")
            return
