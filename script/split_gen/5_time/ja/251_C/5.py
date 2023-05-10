def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    #print(s)
    #print(t)
    #print("--------------")
    # オリジナルな提出のみに絞る
    # その中で最も得点が高い提出が最優秀賞
    # その中で最も提出が早いものを最優秀賞とする
    # オリジナルな提出のみに絞る
    original = []
    for i in range(n):
        if s.count(s[i]) == 1:
            original.append(i)
    #print(original)
    # その中で最も得点が高い提出が最優秀賞
    # その中で最も提出が早いものを最優秀賞とする
    max = 0
    for i in original:
        if t[i] > max:
            max = t[i]
            best = i
    #print(best)
    print(best+1)
