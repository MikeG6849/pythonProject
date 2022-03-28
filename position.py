position = tuple[int, int]


def position_create(row: int, col: int) -> position:
    if (type(row) is int and row >= 0) and (type(col) is int and col >= 0):
        return row, col
    else:
        raise ValueError('position_create: invalid arguments')



