def main():
    S = input()
    K = int(input())
    if S[0] != '1':
        print(S[0])
    else:
        cnt = 0
        for s in S:
            if s == '1':
                cnt += 1
            else:
                break
        if K <= cnt:
            print('1')
        else:
            print(S[cnt-1])
