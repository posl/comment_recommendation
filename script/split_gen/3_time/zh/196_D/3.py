def main():
    h,w,a,b = map(int,input().split())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k in range(h):
                for l in range(w):
                    if (i >> k & 1 or j >> l & 1) == 0:
                        cnt += 1
            if cnt == a+b:
                ans += 1
    print(ans)
