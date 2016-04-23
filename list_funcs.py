def rotate(sequence, i):
    if len(sequence) < 1:
        return sequence
    i = i % len(sequence)
    return sequence[i:] + sequence[:i]
