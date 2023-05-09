def main():
    S = [input() for _ in range(4)]
    print('Yes' if len(set(S)) == 4 else 'No')
