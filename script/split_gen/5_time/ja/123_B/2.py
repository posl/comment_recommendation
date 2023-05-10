def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    
    array = [A, B, C, D, E]
    max_time = max(array)
    if max_time % 10 == 0:
        print(max_time)
    else:
        print(max_time + (10 - max_time % 10))
