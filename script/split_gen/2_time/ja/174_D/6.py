def main():
    N = int(input())
    stones = input()
    white = stones.count("W")
    red = stones.count("R")
    white_stones = stones[:white]
    red_stones = stones[white:]
    print(min(white_stones.count("R"), red_stones.count("W")))
