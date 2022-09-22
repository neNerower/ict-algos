
def get_sub_matrix(matrix, rows, cols):
    res = []

    for i in range(len(matrix)):
        if i not in rows:
            continue
        
        lst = []

        for j in range(len(matrix[i])):
            if j not in cols:
                continue

            lst.append(matrix[i][j])
        
        res.append(lst)

    return res


def get_minor_value(m) -> int:
    if len(m) == len(m[0]):
        size = len(m)
    else:
        raise "Wrong minor size"

    if size == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    res = 0
    for col in range(size):
        res += (-1 if col%2 !=0 else 1) * m[0][col] * get_minor_value(get_sub_matrix(m, [i for i in range(size) if i != 0], [i for i in range(size) if i != col]))
    
    return res
    


def get_matrix_rank(m):
    rows_amount = len(m)
    cols_amount = len(m[0])

    minor_rows = [0]
    minor_cols = [0]

    is_ranked = True

    while is_ranked:
        is_ranked = False

        for i in range(rows_amount):
            if i in minor_rows:
                continue

            for j in range(cols_amount):
                if j in minor_cols:
                    continue

                if get_minor_value(get_sub_matrix(m, [*minor_rows, i], [*minor_cols, j])) != 0:
                    minor_rows.append(i)
                    minor_cols.append(j)
                    is_ranked = True

                if is_ranked:
                    break
            
            if is_ranked:
                    break

    return len(minor_rows)


if __name__ == "__main__":
    m = [
        [1, -1, 2],
        [2, -2, 4],
        [-1, 1, -1]
    ]

    print(get_matrix_rank(m))
