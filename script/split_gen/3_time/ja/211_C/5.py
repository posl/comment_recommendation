def main():
    S = input()
    mod = 10**9+7
    cc = 0
    hc = 0
    oc = 0
    kc = 0
    uc = 0
    dc = 0
    ac = 0
    ic = 0
    for s in S:
        if s == 'c':
            cc += 1
        elif s == 'h':
            hc = (hc+cc)%mod
        elif s == 'o':
            oc = (oc+hc)%mod
        elif s == 'k':
            kc = (kc+oc)%mod
        elif s == 'u':
            uc = (uc+kc)%mod
        elif s == 'd':
            dc = (dc+uc)%mod
        elif s == 'a':
            ac = (ac+dc)%mod
        elif s == 'i':
            ic = (ic+ac)%mod
    print(ic)
