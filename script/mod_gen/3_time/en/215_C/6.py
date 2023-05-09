def permute(s):
    if len(s) == 1:
        return [s]
    else:
        list = []
        for i in range(len(s)):
            c = s[i]
            cs = s[:i] + s[i+1:]
            for p in permute(cs):
                list.append(c+p)
        return list
s, k = input().split()
k = int(k)
list = permute(s)
list.sort()
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = list(itertools.permutations(s))
list.sort()
print(''.join(list[k-1]))
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p in itertools.permutations(s)])
print(list[k-1])
import itertools
s, k = input().split()
k = int(k)
list = sorted([''.join(p) for p

if __name__ == '__main__':
    permute()