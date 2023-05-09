def count_chars(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
N = int(input())
S = [input() for _ in range(N)]
S = list(map(count_chars, S))
S = list(map(lambda x: tuple(sorted(x.items())), S))
S = list(map(lambda x: hash(x), S))
S = list(map(lambda x: (x, S.count(x)), S))
print(sum(map(lambda x: x[1] * (x[1] - 1) // 2, S)))
