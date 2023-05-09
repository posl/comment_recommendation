def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    #print(r1, c1, r2, c2)
    # 1. r1, c1, r2, c2が同じ場合
    if r1 == r2 and c1 == c2:
        print(0)
        return
    # 2. r1, c1, r2, c2が同じ色の場合
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        # 2-1. r1, c1, r2, c2が同じ色で、同じ斜め線上にある場合
        if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
            print(1)
            return
        # 2-2. r1, c1, r2, c2が同じ色で、同じ斜め線上にない場合
        else:
            print(2)
            return
    # 3. r1, c1, r2, c2が異なる色の場合
    else:
        # 3-1. r1, c1, r2, c2が異なる色で、r1 + c1 = r2 + c2, r1 - c1 = r2 - c2のどちらかになる場合
        if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
            print(2)
            return
        # 3-2. r1, c1, r2, c2が異なる色で、r1 + c1 = r2 + c2, r1 - c1 = r2 - c2のどちらにもならない場合
        else:
            # 3-2-1. r1, c1, r2, c2が異なる色で、r1 + c1 = r2 + c2, r1 - c1 = r2 - c2の
