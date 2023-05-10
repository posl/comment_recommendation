def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                count += 1
    
    if count <= 2:
        print(count)
        return
    
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                if i != 0:
                    if S[i-1][j] == '-':
                        S[i-1] = S[i-1][:j] + 'o' + S[i-1][j+1:]
                        S[i] = S[i][:j] + '-' + S[i][j+1:]
                        count += 1
                        continue
                if i != H-1:
                    if S[i+1][j] == '-':
                        S[i+1] = S[i+1][:j] + 'o' + S[i+1][j+1:]
                        S[i] = S[i][:j] + '-' + S[i][j+1:]
                        count += 1
                        continue
                if j != 0:
                    if S[i][j-1] == '-':
                        S[i] = S[i][:j-1] + 'o' + S[i][j:]
                        S[i] = S[i][:j] + '-' + S[i][j+1:]
                        count += 1
                        continue
                if j != W-1:
                    if S[i][j+1] == '-':
                        S[i] = S[i][:j+1] + 'o' + S[i][j+2:]
                        S[i] = S[i][:j] + '-' + S[i][j+1:]
                        count += 1
                        continue
    print(count)

if __name__ == '__main__':
    main()