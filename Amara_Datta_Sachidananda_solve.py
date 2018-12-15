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

    class Cell(object):
        def __init__(self, position):
            self.position = position
            self.parent = None

            self.f = 0
            self.g = 0
            self.h = 0

        def __eq__(self, different):
            return self.position == different.position

        def __ne__(self, different):
            return self.position != different.position

    start_point = queries[0]
    end_point = queries[1]

    def astar(start, end):
        '''

        :param start: start of the path
        :param end: end of the path
        :return: True or False based on path exists or not
        '''

        open_cells = []
        closed_cells = []
        surrounding_cells = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        start_cell = Cell(start)
        end_cell = Cell(end)
        start_cell.f = 0
        start_cell.g = 0
        start_cell.h = 0

        def heuristic_calculated(destination_cell, source_cell):
            '''
            Calculate the heuristic value and then compute the weight for the traversal
            :param destination_cell: the cell to which we will move to
            :param source_cell: the cell which we are moving from
            :return: the destination cell with attached weight
            '''
            destination_cell.g = source_cell.g + 1
            destination_cell.h = abs(((destination_cell.position[0] - end_cell.position[0]) * 10) + (
                    (destination_cell.position[1] - end_cell.position[1]) * 10))
            destination_cell.f = destination_cell.g + destination_cell.h
            return destination_cell

        def path_is_one(next_cell_to_be_added):
            '''
            to check if the path is comprised of '1'
            :param next_cell_to_be_added: the adjacent cell to the current cell
            :return: True or False base on what the cell value is
            '''
            if grid[next_cell_to_be_added.position[0]][next_cell_to_be_added.position[1]] == 1:
                return True
            else:
                return False

        def check_child__not_in_closed_cells_list(child):
            '''
            checks if the child or the surrounding cell has already been traveled through or not
            :param child: surrounding cell
            :return: True or false base on travel history
            '''
            for each_closed_cell in closed_cells:

                if child == each_closed_cell:
                    return False
                else:
                    continue

            return True

        def check_result(cell):
            '''
            check if we reached the end point
            :param cell: the current cell which we are on
            :return: True only if we have reached the end point
            '''
            if cell == end_cell:
                return True

        def get_new_cell_position(current_cell_position):
            for next_cell_to_go in surrounding_cells:
                temp_cell = current_cell_position.position[0] + next_cell_to_go[0], current_cell_position.position[1] + \
                            next_cell_to_go[1]

                if (temp_cell[0] <= len(grid) - 1) and (temp_cell[0] >= 0):

                    if (temp_cell[1] <= len(grid) - 1) and (temp_cell[1] >= 0):

                        if path_is_one(Cell(temp_cell)):
                            new_cell = Cell(temp_cell)
                            children.append(new_cell)
                            open_cells.append(new_cell)

                        else:
                            new_cell = Cell(temp_cell)
                            closed_cells.append(new_cell)
                continue

            return children

        def sort_children(current_cell_position):
            children_list = get_new_cell_position(current_cell_position)

            for each_child in children_list:
                calculated_cell = heuristic_calculated(each_child, current_cell_position)

                if calculated_cell.f <= current_cell_position.f and check_child__not_in_closed_cells_list(each_child):
                    each_child.parent = current_cell
                    each_child.f = calculated_cell.f
                    each_child.g = calculated_cell.g
                    each_child.h = calculated_cell.h
                    return each_child

                else:
                    continue

            return False

        open_cells.append(start_cell)
        initial_hueristic_calc = heuristic_calculated(start_cell, start_cell)
        start_cell.h = initial_hueristic_calc.h
        start_cell.f = initial_hueristic_calc.f

        for iteration_stopper in range(len(grid) ** 2):
            if len(open_cells) > 0:

                current_cell = open_cells[0]
                current_index = 0

                for index, item in enumerate(open_cells):

                    if item.f < current_cell.f:
                        current_cell = item
                        current_index = index

                open_cells.pop(current_index)
                closed_cells.append(current_cell)

                if check_result(current_cell):
                    return True

                children = []

                next_cell = sort_children(current_cell)

                if next_cell is not False:
                    open_cells.append(next_cell)

                else:
                    continue
            else:
                return False

    if astar(start_point, end_point):
        return True
    else:
        return False


# maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze = [[1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]]

start = (2, 0)
end = (0, 2)
print(start, end)
print(path_exists(maze, (start, end)))


