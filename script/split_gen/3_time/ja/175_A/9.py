def main():
    S = input()
    print(max(len(x) for x in S.split('S')))
