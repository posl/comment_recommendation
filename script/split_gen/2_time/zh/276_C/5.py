def get_next_permutation(a):
    for i in range(len(a)-2, -1, -1):
        if a[i] < a[i+1]:
            target = i
            break
    else:
        return False
    for i in range(len(a)-1, target, -1):
        if a[i] > a[target]:
            a[i], a[target] = a[target], a[i]
            break
    a[target+1:] = reversed(a[target+1:])
    return True
n = int(input())
p = list(map(int, input().split()))
p = [0] + p
q = p[:]
