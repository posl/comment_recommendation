def main():
    #入力
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    #最小値を求める
    min = 10000
    for i in range(2 ** D):
        #2進数に変換
        b = format(i, 'b')
        #0埋め
        b = b.zfill(D)
        #print(b)
        #問題数
        num = 0
        #合計点
        sum = 0
        #最後の問題を解く
        last = -1
        #print(b)
        for j in range(D):
            #print(b[j])
            #print(b[j] == '1')
            if b[j] == '1':
                num += pc[j][0]
                sum += pc[j][0] * 100 * (j + 1) + pc[j][1]
            else:
                last = j
        #print(sum)
        #print(num)
        if sum < G:
            if last >= 0:
                for k in range(pc[last][0]):
                    sum += 100 * (last + 1)
                    num += 1
                    if sum >= G:
                        break
        if sum >= G:
            if num < min:
                min = num
    print(min)

if __name__ == '__main__':
    main()