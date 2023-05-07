def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    ans = []
    while K > 0:
        ans.append(S.pop(K % len(S) - 1))
        K = (K // len(S)) if K % len(S) == 0 else (K // len(S)) + 1
    ans = ans + S
    print(''.join(ans))

if __name__ == '__main__':
    main()