def swap_sequence(sequence, swap1, swap2):
    temp = sequence[swap1:swap2]
    sequence[swap1:swap2] = sequence[swap2:]
    sequence[swap2:] = temp
    return sequence

if __name__ == '__main__':
    swap_sequence()