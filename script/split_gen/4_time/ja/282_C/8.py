def solve():
    N = int(input())
    S = input()
    # " の数
    cnt = 0
    for s in S:
        if s == '"':
            cnt += 1
    # " が偶数個でない場合はエラー
    if cnt % 2 != 0:
        print("error")
        return
    # " の数を 2 倍したもの
    cnt *= 2
    # 括られた文字の中の , の数
    cnt2 = 0
    # 括られた文字の中の , でない文字の数
    cnt3 = 0
    # 括られた文字の中の , でない文字の数を数える
    for s in S:
        if s == '"':
            cnt2 += 1
        elif s == ',' and cnt2 % 2 == 0:
            cnt3 += 1
    # 括られた文字の中の , でない文字の数を 2 倍したもの
    cnt3 *= 2
    # 括られた文字の中の , でない文字の数を 2 倍したものが " の数と等しくない場合はエラー
    if cnt2 != cnt3:
        print("error")
        return
    # 括られた文字の中の , でない文字の数を 2 倍したものが " の数と等しい場合は , のうち、括られた文字でないものを . に置き換える
    ans = ""
    for s in S:
        if s == ',' and cnt2 % 2 == 0:
            ans += "."
        else:
            ans += s
    print(ans)
