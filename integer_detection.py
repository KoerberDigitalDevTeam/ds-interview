"""
You are given a list that solely contains integers or list. The same is true for the member lists, thus this nesting
can be arbitrarily deep (but finite of course). Examples are given below, it might help to think of this as some
kind of tree.

- Please, write a function that generates a list. Each member of this list is a tuple of an integer and its
  depth in the nested list (tree). The list must contain one tuple for each integer in the tree.


Examples:
    nested_list([1,2,3]) = [(0, 1), (0, 2), (0, 3)]

    nested_list([[1,2,3]]) = [(1, 1), (1, 2), (1, 3)]

    nested_list([[1,2,3],[4,5]]) = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

    nested_list([[[[0, 1], 2, 3, 4, 5], 6, [ 7, 8, 9, 10, 11], 12, 13, 14], [15, 16], 17, 18]) =
        [(3, 0), (3, 1), (2, 2), (2, 3), (2, 4), (2, 5), (1, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (1, 12),
        (1, 13), (1, 14), (1, 15), (1, 16), (0, 17), (0, 18)]
"""
