def main():
    n = int(input())
    s = []
    max_s = 0
    min_s = 0
    for _ in range(n):
        q = input().split()
        if q[0] == '1':
            s.append(int(q[1]))
            if len(s) == 1:
                max_s = s[0]
                min_s = s[0]
            else:
                if max_s < s[-1]:
                    max_s = s[-1]
                if min_s > s[-1]:
                    min_s = s[-1]
        elif q[0] == '2':
            c = int(q[2])
            for _ in range(min(c, s.count(int(q[1])))):
                s.remove(int(q[1]))
            if len(s) == 0:
                max_s = 0
                min_s = 0
            else:
                max_s = max(s)
                min_s = min(s)
        else:
            print(max_s - min_s)
