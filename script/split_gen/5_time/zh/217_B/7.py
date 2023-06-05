def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = set([S_1, S_2, S_3])
    S_all = set(['ABC', 'ARC', 'AGC', 'AHC'])
    S_diff = S_all - S
    print(list(S_diff)[0])
