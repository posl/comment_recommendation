def merge_slimes(slimes):
    merged_slimes = []
    prev_slime = None
    for slime in slimes:
        if prev_slime is None:
            prev_slime = slime
        elif prev_slime == slime:
            pass
        else:
            merged_slimes.append(prev_slime)
            prev_slime = slime
    merged_slimes.append(prev_slime)
    return merged_slimes
