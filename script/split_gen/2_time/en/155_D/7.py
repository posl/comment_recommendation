def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 0以下の個数をカウント
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    # 0以下の個数がk個以下なら、0以下のもの同士の積を考える
    if count >= k:
        a.sort()
        ans = 1
        for i in range(k):
            ans *= a[i]
    # 0以下の個数がk個より多いなら、0以下のもの同士の積を考える
    else:
        # 0以下と0以上で組み合わせを考える
        # 0以上の個数をカウント
        count2 = 0
        for i in a:
            if i >= 0:
                count2 += 1
        # 0以上の個数がk個より多いなら、0以上のもの同士の積を考える
        if count2 >= k:
            a.sort(reverse=True)
            ans = 1
            for i in range(k):
                ans *= a[i]
        # 0以上の個数がk個以下なら、0以上のもの同士の積を考える
        else:
            # 0の個数をカウント
            count3 = 0
            for i in a:
                if i == 0:
                    count3 += 1
            # 0の個数がk個より多いなら、0を考える
            if count3 >= k:
                ans = 0
            # 0の個数がk個以下なら、0以下と0以上の組み合わせを考える
            else:
                # 0以下の個数が偶数なら、0以下のもの同士の積を考える
                if count % 2 == 0:
                    a.sort()
                    ans = 1
                    for i in
