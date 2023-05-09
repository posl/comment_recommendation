def get_patty_count(N, X):
    """Returns the number of patties in the bottom-most X layers from the bottom of a level-N burger."""
    # A level-0 burger is a patty.
    if N == 0:
        return 1
    # A level-L burger (L >= 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
    # For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
    # The burger Mr. Takaha will make is a level-N burger. Lunlun the Dachshund will eat X layers from the bottom of this burger (a layer is a patty or a bun). How many patties will she eat?
    # A level-0 burger is a patty.
    # A level-L burger (L >= 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
    # For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
    # The burger Mr. Takaha will make is a level-N burger. Lunlun the Dachshund will eat X layers from the bottom of this burger (a layer is a patty or a bun). How many patties will she eat?
    # A level-0 burger is a patty.
    # A level-L burger (L >= 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
    # For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
    # The burger Mr. Takaha will make is a level-N burger. Lunlun the D

if __name__ == '__main__':
    get_patty_count()