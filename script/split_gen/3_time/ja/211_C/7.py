def main():
    S = input()
    MOD = 10**9 + 7
    #d = {"c":0, "h":0, "o":0, "k":0, "u":0, "d":0, "a":0, "i":0}
    d = {"c":0, "h":0, "o":0, "k":0, "u":0, "d":0, "a":0, "i":0}
    for i in S:
        if i in d:
            d[i] += 1
    if d["c"] == 0 or d["h"] == 0 or d["o"] == 0 or d["k"] == 0 or d["u"] == 0 or d["d"] == 0 or d["a"] == 0 or d["i"] == 0:
        print(0)
        return
    d = list(d.values())
    d.sort()
    print(d[0])
