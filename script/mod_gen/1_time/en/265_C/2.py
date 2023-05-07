def move(i, j, d):
    if d == 'U':
        i -= 1
    elif d == 'D':
        i += 1
    elif d == 'L':
        j -= 1
    else:
        j += 1
    return i, j
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
i, j = 0, 0
visited = [[0] * W for _ in range(H)]
visited[0][0] = 1
while True:
    d = grid[i][j]
    i, j = move(i, j, d)
    if i < 0 or i >= H or j < 0 or j >= W:
        print(i + 1, j + 1)
        exit()
    if visited[i][j]:
        print(-1)
        exit()
    visited[i][j] = 1
I'm trying to make a program that will take the input of a number and print out the number in words. For example, if the user inputs 123, the program will output "one hundred twenty three". I have tried to make this program using a dictionary, but I can't seem to get it to work. I have also tried using if statements, but I can't figure out how to make it work with numbers over 100. I have also tried using a list, but I can't figure out how to make it print out the words in the correct order. I would appreciate any help!

if __name__ == '__main__':
    move()