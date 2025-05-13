def selection_sort(sequence: iter) -> iter:
    """
    Sorts data using a selection sort algorithm
    Selection sort is not a stable sort algorithm
    It is an in-place sort
    Selection sort runs in O(n^2) time, nested loops are expensive in time
    It would be used in small datasets where simplicity is more important than efficiency

    @param sequence: iterable sequence
    @return: sorted iterable sequence
    """
    for i in range(len(sequence)):
        min_index = i

        # find minimum value index
        for j in range(i+1, len(sequence)):  # smallest value sorted already
            if sequence[j] < sequence[min_index]:
                min_index = j

        # swap found minimum value with where it should be
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]

    return sequence
