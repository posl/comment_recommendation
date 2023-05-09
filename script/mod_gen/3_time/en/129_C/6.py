def get_input():
    N, M = map(int, input().split())
    broken_steps = []
    for _ in range(M):
        broken_steps.append(int(input()))
    return N, broken_steps

if __name__ == '__main__':
    get_input()