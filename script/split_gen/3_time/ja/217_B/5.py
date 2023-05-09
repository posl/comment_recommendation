def main():
    S = [input() for _ in range(3)]
    T = ['ABC', 'ARC', 'AGC', 'AHC']
    for t in T:
        if t not in S:
            print(t)
