def main():
    N = int(input())
    W = [input() for _ in range(N)]
    #print(N)
    #print(W)
    # しりとりのルールを守っているかどうか判定
    # しりとりのルールを守っていない場合はループを抜ける
    for i in range(1, N):
        if W[i - 1][-1] != W[i][0] or W[i] in W[:i]:
            print("No")
            break
    else:
        print("Yes")
