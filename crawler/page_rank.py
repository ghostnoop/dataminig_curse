import numpy

from matrix_generator import matrix_from_graph


def summary_page_rank(matrix, height, width, G_LIST):
    # своe значение
    n = height
    POW = 20

    beta = 0.85

    k = (1 - beta) / n

    M_matrix = matrix

    v_vector = numpy.matrix([1 / n for i in range(height)])

    M_matrix_powed = M_matrix
    v_vector.dot(M_matrix_powed)
    for i in range(POW):
        M_matrix_powed.dot(M_matrix)

    M_matrix_final = v_vector.dot(M_matrix_powed)

    MATRIX_RESULT_MxV = M_matrix_final.dot(beta)
    # MATRIX_RESULT_MxV = M_matrix_final

    # заполняется единицами
    e = numpy.ones(height)

    e = e.dot(k)

    result = MATRIX_RESULT_MxV + e

    print("result :::::::::::::::::")
    print(result)

    TCUT = 5
    a_ = numpy.sort(result).tolist()[0]

    a_ = a_[-TCUT:]
    b_ = numpy.argsort(result).tolist()[0][-TCUT:]
    G_LIST = list(G_LIST)
    arr = []
    for i in range(TCUT):
        arr.append(
            f"{TCUT - i} {a_[i]} {G_LIST[b_[i]]}"
        )

    print('result page rank')
    print(result.sum())

    print('----------')
    print('top', TCUT)
    for i in arr:
        print(i)


if __name__ == '__main__':
    matrix, height, width, G_LIST = matrix_from_graph()
    summary_page_rank(matrix, height, width, G_LIST)
