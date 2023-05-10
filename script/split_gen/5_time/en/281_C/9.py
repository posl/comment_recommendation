def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # 1. 1回ループするまでの時間を求める
    total = 0
    for i in range(n):
        total += a[i]
    # 2. 1回ループする回数を求める
    count = t // total
    # 3. 1回ループした後に残る時間を求める
    remain = t % total
    # 4. 1回ループした後に残る時間を使って、何番目の曲が再生されているか求める
    index = 0
    for i in range(n):
        if remain >= a[i]:
            remain -= a[i]
            index += 1
        else:
            break
    # 5. 4.で求めた曲が何秒目に再生されているか求める
    time = remain
    print(index + 1, time)
