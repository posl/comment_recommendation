def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    
    #print(n)
    #print(s)
    #print(t)
    
    # sの横幅と縦幅を取得
    sw = len(s[0])
    sh = len(s)
    # tの横幅と縦幅を取得
    tw = len(t[0])
    th = len(t)
    
    #print(sw, sh)
    #print(tw, th)
    
    # sの左上の#の位置を取得
    for i in range(sh):
        for j in range(sw):
            if s[i][j] == "#":
                sx = j
                sy = i
                break
    #print(sx, sy)
    
    # tの左上の#の位置を取得
    for i in range(th):
        for j in range(tw):
            if t[i][j] == "#":
                tx = j
                ty = i
                break
    #print(tx, ty)
    
    # sの左上の#の位置とtの左上の#の位置が一致するか確認
    if sx == tx and sy == ty:
        #print("Yes")
        # sの左上の#の位置とtの左上の#の位置が一致する場合、sの#の位置とtの#の位置が一致するか確認
        for i in range(sh):
            for j in range(sw):
                if s[i][j] == "#" and t[i][j] == "#":
                    continue
                elif s[i][j] == "." and t[i][j] == ".":
                    continue
                else:
                    print("No")
                    return
        print("Yes")
    else:
        print("No")
        return
    
    #print("Yes")
