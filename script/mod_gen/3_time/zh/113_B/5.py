def get_input():
    n = int(input())
    t, a = map(int, input().split())
    h_list = list(map(int, input().split()))
    return n, t, a, h_list

if __name__ == '__main__':
    get_input()