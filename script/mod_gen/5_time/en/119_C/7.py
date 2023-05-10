def find_min_mp(N, A, B, C, l):
    min_mp = 10000
    for a in range(10000):
        for b in range(10000):
            for c in range(10000):
                if a == 0 and b == 0 and c == 0:
                    continue
                mp = 0
                for i in range(N):
                    if l[i] > a:
                        mp += (l[i] - a) * 1
                    elif l[i] < a:
                        mp += (a - l[i]) * 10
                for i in range(N):
                    if l[i] > b:
                        mp += (l[i] - b) * 1
                    elif l[i] < b:
                        mp += (b - l[i]) * 10
                for i in range(N):
                    if l[i] > c:
                        mp += (l[i] - c) * 1
                    elif l[i] < c:
                        mp += (c - l[i]) * 10
                if a == A and b == B and c == C:
                    min_mp = min(min_mp, mp)
    return min_mp

if __name__ == '__main__':
    find_min_mp()