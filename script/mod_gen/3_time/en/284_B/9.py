def get_input():
    test_cases = int(input())
    for test_case in range(test_cases):
        input()
        yield input().split()

if __name__ == '__main__':
    get_input()