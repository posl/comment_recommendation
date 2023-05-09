def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    #print(xyr)
    #print(sx, sy, tx, ty)
    # 経路が存在するかチェックする
    # 経路が存在する場合は、経路の長さを返す
    def check(x1, y1, x2, y2, xyr):
        #print("check", x1, y1, x2, y2)
        # 経路が存在するかチェックする
        # 経路が存在する場合は、経路の長さを返す
        def check(x1, y1, x2, y2, xyr):
            #print("check", x1, y1, x2, y2)
            if (x1, y1) == (x2, y2):
                return 0
            # 経路が存在するかチェックする
            # 経路が存在する場合は、経路の長さを返す
            def check(x1, y1, x2, y2, xyr):
                #print("check", x1, y1, x2, y2)
                if (x1, y1) == (x2, y2):
                    return 0
                #print("check", x1, y1, x2, y2)
                # 経路が存在するかチェックする
                # 経路が存在する場合は、経路の長さを返す
                def check(x1, y1, x2, y2, xyr):
                    #print("check", x1, y1, x2, y2)
                    if (x1, y1) == (x2, y2):
                        return 0
                    #print("check", x1, y1, x2, y2)
                    # 経路が存在するかチェックする
                    # 経路が存在する場合は、経路の
