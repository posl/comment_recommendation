def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    for i in range(w):
        count = 0
        for j in range(h):
            if s[j][i] == '#':
                count += 1
        print(count, end=' ')
main()
from itertools import accumulate
h,w=map(int,input().split())
s=[input() for _ in range(h)]
for i in accumulate([s[j][i]=='#'for i in range(w)for j in range(h)]):
    if i%h==0:print(i//h,end=' ')
h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
s = [input() for _ in range(h)]
for i in range(w):
    print(sum(s[j][i] == '#' for j in range(h)), end=' ')
h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')
h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')
h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count += 1
    print(count, end=' ')
h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(w):
    count = 0
    for j in range(h):
        if s[j][i] == '#':
            count +=

if __name__ == '__main__':
    main()