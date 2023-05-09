def max_move(n, h):
    max_move = 0
    current_move = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            current_move += 1
        else:
            current_move = 0
        if current_move > max_move:
            max_move = current_move
    return max_move
n = int(input())
h = list(map(int, input().split()))
print(max_move(n, h))

if __name__ == '__main__':
    max_move()