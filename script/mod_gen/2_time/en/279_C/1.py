def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    if H % 2 == 0 and W % 2 == 0:
        print("No")
        return
    if H % 2 == 0:
        for i in range(H):
            for j in range(W//2):
                if S[i][j] != S[i][W-1-j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        for i in range(H):
            for j in range(W//2):
                if T[i][j] != T[i][W-1-j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        print("No")
        return
    if W % 2 == 0:
        for i in range(H//2):
            for j in range(W):
                if S[i][j] != S[H-1-i][j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        for i in range(H//2):
            for j in range(W):
                if T[i][j] != T[H-1-i][j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        print("No")
        return
    for i in range(H//2):
        for j in range(W//2):
            if S[i][j] != S[H-1-i][W-1-j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    for i in range(H//2):
        for j in range(W//2):
            if T[i][j] != T[H-1-i][W-1-j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
    return
main()
