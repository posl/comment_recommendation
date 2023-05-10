def main():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            t1, l1, r1 = tlr[i]
            t2, l2, r2 = tlr[j]
            if t1 == 1:
                if t2 == 1:
                    if l1 <= l2 <= r1:
                        ans += 1
                    elif l1 <= r2 <= r1:
                        ans += 1
                    elif l2 <= l1 <= r2:
                        ans += 1
                    elif l2 <= r1 <= r2:
                        ans += 1
                elif t2 == 2:
                    if l1 <= l2 < r1:
                        ans += 1
                    elif l1 <= r2 < r1:
                        ans += 1
                    elif l2 < l1 <= r2:
                        ans += 1
                    elif l2 < r1 <= r2:
                        ans += 1
                elif t2 == 3:
                    if l1 < l2 <= r1:
                        ans += 1
                    elif l1 < r2 <= r1:
                        ans += 1
                    elif l2 <= l1 < r2:
                        ans += 1
                    elif l2 <= r1 < r2:
                        ans += 1
                elif t2 == 4:
                    if l1 < l2 < r1:
                        ans += 1
                    elif l1 < r2 < r1:
                        ans += 1
                    elif l2 < l1 < r2:
                        ans += 1
                    elif l2 < r1 < r2:
                        ans += 1
            elif t1 == 2:
                if t2 == 1:
                    if l1 < l2 <= r1:
                        ans += 1
                    elif l1 < r2 <= r1:
                        ans += 1
                    elif l2 <= l1 < r2:
                        ans += 1
                    elif l2 <= r1 < r2:
                        ans += 1
                elif t2 == 2:
                    if l1 < l2 < r1:
