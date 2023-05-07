def main():
    N, K = map(int, input().split())
    a = [N]
    for i in range(K):
        if a[i] == 0:
            break
        a.append(int(''.join(sorted(str(a[i]), reverse=True))) - int(''.join(sorted(str(a[i])))))
    print(a[-1])
