def main():
    #入力
    K = int(input())
    S = input()
    #Sの長さがKを上回っているならば、先頭K文字だけを切り出し、末尾に...を付加して出力
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")
