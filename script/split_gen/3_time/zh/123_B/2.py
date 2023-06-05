def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min([A,B,C,D,E], key=lambda x: x % 10) + sum([10 * ((x - 1) // 10 + 1) for x in [A,B,C,D,E]]))
