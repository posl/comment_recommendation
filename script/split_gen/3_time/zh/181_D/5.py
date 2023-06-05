def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if s == '16' or s == '24' or s == '32' or s == '48' or s == '56' or s == '64' or s == '72' or s == '88' or s == '96':
            print('Yes')
        else:
            print('No')
    elif len(s) == 3:
        if s == '168' or s == '184' or s == '328' or s == '368' or s == '488' or s == '528' or s == '648' or s == '688' or s == '728' or s == '816' or s == '824' or s == '856' or s == '864' or s == '888' or s == '968':
            print('Yes')
        else:
            print('No')
    else:
        if s == '1864' or s == '2688' or s == '2888' or s == '3288' or s == '6888':
            print('Yes')
        else:
            print('No')
