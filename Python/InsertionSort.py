def insertion_sort(sequence: iter) -> iter:
    """
    Sorts data using an insertion sort algorithm
    Insertion sort is a stable sort algorithm
    It is an in-place sort
    Insertion sort runs in O(n^2) time, nested loops are expensive in time
    It is efficient to use for small datasets and performs well when data is mostly sorted

    @param sequence: iterable sequence
    @return: sorted iterable sequence
    """
    for i in range(1, len(sequence)):
        desired_item = sequence[i]
        # shifting elements to make space to place our desired item
        j = i-1
        while j >= 0 and desired_item < sequence[j]:
            sequence[j+1] = sequence[j]
            j -= 1

        # desired_item goes in its spot
        sequence[j+1] = desired_item

    return sequence
