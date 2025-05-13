def quick_sort(sequence: iter) -> iter:
    """
    Sorts data using a quick sort algorithm
    Quick sort is not a stable sort algorithm
    It requires additional memory and is not performed in-place
    Quick sort runs in O(n log(n)) to O(n^2) time, O(n^2) is worst case
    Recursive calls are expensive in space/memory
    Efficient for large datasets when stability is not of concern, general-purpose sorting

    @param sequence: iterable sequence
    @return: sorted iterable sequence after recursive calls
    """
    # base case
    if len(sequence) <= 1:
        return sequence

    # picking pivot wisely
    pivot = sequence[len(sequence)//2]

    # I learned a cool way to make sub lists
    left = [x for x in sequence if x < pivot]
    middle = [x for x in sequence if x == pivot]
    right = [x for x in sequence if x > pivot]

    # now the recursive call
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)
