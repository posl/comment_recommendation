def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = [A, B, C, D, E]
    time.sort()
    print(10 * (len(time) - 1) + time[-1])
