def bubble_sort(sequence: iter) -> iter:
    """
    Sorts data using a bubble sort algorithm
    Bubble sort is a stable sort algorithm
    It is an in-place sort
    Bubble sort runs in O(n^2) time, nested loops are expensive in time
    It would be used in small datasets where simplicity is more important than efficiency

    @param sequence: iterable sequence
    @return: sorted iterable sequence
    """
    for i in range(len(sequence)):
        for j in range(0, len(sequence)-1):  # since the last element gets sorted each pass
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

    return sequence
