position = tuple[int, int]


def position_create(row: int, col: int) -> position:
    if (type(row) is int and row >= 0) and (type(col) is int and col >= 0):
        return row, col
    else:
        raise ValueError('position_create: invalid arguments')


def position_is(pos: position) -> bool:
    if type(pos) is tuple:
        return True
    else:
        return False


def position_row(pos: position) -> int:
    if type(pos) is tuple:
        return pos[0]
    else:
        raise ValueError('position_row: invalid arguments')


def position_col(pos: position) -> int:
    if type(pos) is tuple:
        return pos[1]
    else:
        raise ValueError('position_col: invalid arguments')


def position_equal(pos1: position, pos2: position) -> bool:
    if type(pos1) and type(pos2) is tuple:
        if pos1 == pos2:
            return True
        else:
            return False
    else:
        raise ValueError('position_equal: invalid arguments')


def position_str(pos: position) -> str:
    if type(pos) is position_is(pos):
        return '(' + str(pos[0]) + ',' + str(pos[1]) + ')'
    else:
        raise ValueError('‘position_str: invalid arguments')
