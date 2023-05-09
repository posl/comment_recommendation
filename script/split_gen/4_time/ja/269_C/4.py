def main():
    N = int(input())
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_bin_cnt = N_bin.count('1')
    ans = []
    for i in range(2**N_bin_cnt):
        ans_bin = bin(i)
        ans_bin = ans_bin[2:]
        ans_bin = ans_bin.zfill(N_bin_cnt)
        ans_bin = ans_bin[::-1]
        tmp = ''
        for j in range(len(ans_bin)):
            if ans_bin[j] == '1':
                tmp += '1'
            else:
                tmp += '0'
        if tmp in N_bin:
            ans.append(i)
    for i in ans:
        print(i)
