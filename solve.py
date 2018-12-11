import Queue as queue

"""
Instructions:
    - Implement the function `path_exists` below.
    - Save this file as `{first_name}_{last_name}_solve.py`.

Constraints:
    - Your solution will be run in a Python2.7 environment.
    - Only python standard library imports can be used and they must be imported within `path_exists`.
    - The function signature of `path_exists` cannot be modified.
    - Additional functions can be included, but must be defined within `path_exists`.
    - There will be two sets of input, small and large, each with different time limits.
"""


def path_exists(grid, queries):
    """
    Determines whether for every start=(i1, j1) -> end=(i2, j2) query in `queries`,
    there exists a path in `grid` from start to end.

    The rules for a path are as follows:
        - A path consists of only up-down-left-right segments (no diagonals).
        - A path must consist of the same values. i.e. if grid[i1][j1] == 1, the path is comprised of only 1's.

    Examples:
        grid (visual only)

                1 0 0
                1 1 0
                0 1 1

        start     end       answer
        (0, 0) -> (2, 2)    True
        (2, 0) -> (0, 2)    False


    :param grid:        The grid on which `queries` are asked.
    :type grid:         list[list[int]], values can only be [0, 1].
    :param queries:     A set of queries for `grid`. Queries will be non-trivial.
    :type queries:      Iterable, contains elements of type tuple[tuple[int, int]].

    :return:            The result for each query, whether a path exists from start -> end.
    :rtype:             list[bool]
    """
    '''
    get the size of give matrix
    '''
    i = len(grid) - 1
    j = len(grid[0]) - 1
    elements = i * j

    '''
    initialize the stack and dictionary to store visited path 
    '''
    node_stack = queue.LifoQueue(maxsize=elements)
    path_visited = {}

    def goto_next_node_and_store_previous(direction, row, column):
        if direction == 'up' and row > 0:
            row = row - 1
        elif direction == 'down' and row < i:
            row = row + 1
        elif direction == 'left' and column > 0:
            column = column - 1
        elif direction == 'right' and column < j:
            column = column + 1
        else:
            print('End of matrix, there can be no movement')
        return row, column

    # print(next_node('up', 2, 3))

    def verify_and_store_path_in_stack(row, column):
        if grid[row][column] == 1:
            node_stack.put(row, column)
            dict.update({(row, column): grid[row][column]})
        return None

    # raise NotImplementedError


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 1, 1]]
path_exists(grid, None)
