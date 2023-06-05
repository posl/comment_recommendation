def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        if p == max_a and q == max_a and r == max_a:
            print('Yes')
        else:
            print('No')
        return
    if p == min_a:
        start = a.index(min_a)
    elif q == min_a:
        start = a.index(min_a) + 1
    elif r == min_a:
        start = a.index(min_a) + 2
    else:
        print('No')
        return
    if start + 2 >= n:
        print('No')
        return
    if p == min_a:
        if p == q:
            if p == r:
                print('Yes')
                return
            else:
                if a[start + 2] == r:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == q and a[start + 2] == r:
                print('Yes')
                return
            else:
                print('No')
                return
    elif q == min_a:
        if q == r:
            if q == p:
                print('Yes')
                return
            else:
                if a[start + 2] == p:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == r and a[start + 2] == p:
                print('Yes')
                return
            else:
                print('No')
                return
    elif r == min_a:
        if r == p:
            if r == q:
                print('Yes')
                return
            else:
                if a[start + 2] == q:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == p and a[start + 2] == q:
                print('Yes')
                return
            else:
                print('No')
                return
    else:
        print('No')
        return
