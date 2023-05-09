def main():
    S = input()
    K = int(input())
    
    # 1の数を数える
    one_cnt = 0
    for s in S:
        if s == '1':
            one_cnt += 1
        else:
            break
    
    if K <= one_cnt:
        print(1)
    else:
        print(S[one_cnt])

if __name__ == '__main__':
    main()