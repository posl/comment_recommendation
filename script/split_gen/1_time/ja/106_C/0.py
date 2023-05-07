def main():
    S = input()
    K = int(input())
    S = S.replace('1','1 ').replace('2','22 ').replace('3','333 ').replace('4','4444 ').replace('5','55555 ').replace('6','666666 ').replace('7','7777777 ').replace('8','88888888 ').replace('9','999999999 ')
    S = S.split()
    ans = ''
    for i in range(K):
        ans += S[i]
    print(ans[K-1])
