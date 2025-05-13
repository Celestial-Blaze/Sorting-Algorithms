def merge_sort(sequence: iter) -> iter:
    """
    Sorts data using a merge sort algorithm
    Merge sort is a stable sort algorithm
    It requires additional memory and is not performed in-place
    Merge sort runs in O(n log(n)) time, recursive calls are expensive in space/memory
    Efficient for large datasets when stable sorting is required, general-purpose sorting

    @param sequence: iterable sequence
    @return: sorted iterable sequence after recursive calls
    """
    # base case
    if len(sequence) <= 1:
        return sequence

    # split list
    mid_point = len(sequence)//2
    left_half = sequence[:mid_point]
    right_half = sequence[mid_point:]

    # recursive call merge_sort to sort smaller and smaller right and left halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left: iter, right: iter) -> iter:
    """
        Merges two sorted lists for merge sort
        @param left: left sorted list
        @param right: right sorted list
        @return: merged list
        """
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # add remaining elements from both lists
    merged.extend(left[i:])  # apparently append wouldn't get the job done
    merged.extend(right[j:])  # so I learned to use extend, it's pretty cool

    return merged
