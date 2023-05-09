def main():
    #input
    S = [input() for _ in range(3)]
    #output
    print(*[s for s in ['ABC', 'ARC', 'AGC', 'AHC'] if s not in S], sep='
