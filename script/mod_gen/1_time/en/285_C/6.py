def main():
    import sys
    import math
    from collections import defaultdict
    from collections import deque
    from collections import Counter
    from itertools import accumulate
    from itertools import permutations
    from itertools import combinations
    from itertools import product
    from itertools import combinations_with_replacement
    from bisect import bisect_left
    from bisect import bisect_right
    from heapq import heappop
    from heapq import heappush
    from functools import reduce
    from operator import xor
    from operator import add
    from operator import mul
    from operator import itemgetter
    from operator import attrgetter
    from operator import methodcaller
    from operator import truediv
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    a = input()
    ans = 0
    for i in range(len(a)):
        ans += (ord(a[i])-64) * (26**(len(a)-i-1))
    print(ans)

if __name__ == '__main__':
    main()