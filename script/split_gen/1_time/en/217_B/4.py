def main():
    S = [input() for _ in range(3)]
    T = ['ABC', 'ARC', 'AGC', 'AHC']
    for s in S:
        T.remove(s)
    print(T[0])
