def main():
    n, m = [int(x) for x in input().split()]
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] + '_' + s[j] in t:
                print('-1')
                return
            if s[j] + '_' + s[i] in t:
                print('-1')
                return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                if s[i] + '_' + s[j] + '_' + s[k] in t:
                    print('-1')
                    return
                if s[i] + '_' + s[k] + '_' + s[j] in t:
                    print('-1')
                    return
                if s[j] + '_' + s[i] + '_' + s[k] in t:
                    print('-1')
                    return
                if s[j] + '_' + s[k] + '_' + s[i] in t:
                    print('-1')
                    return
                if s[k] + '_' + s[i] + '_' + s[j] in t:
                    print('-1')
                    return
                if s[k] + '_' + s[j] + '_' + s[i] in t:
                    print('-1')
                    return
    print(s[0] + '__' + s[1] + '___' + s[2] + '____' + s[3])
main()
I don't know if this is the best solution, but it works.
