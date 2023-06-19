def main():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(1,N):
        if S[i-1] == 'L':
            ans.insert(0,i)
        else:
            ans.append(i)
    print(*ans)
