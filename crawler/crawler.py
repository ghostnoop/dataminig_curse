import time

from graph_generator import generator_by_json
from matrix_generator import matrix_from_graph
from page_rank import summary_page_rank
from services import get_page_links_v2

# url = 'https://mangalib.me/otherworldly-evil-monarch?section=info'

if __name__ == '__main__':
    print('start')

    URL = "https://spring.io/"

    st = time.monotonic()

    d = get_page_links_v2(URL, 1)

    print(time.monotonic() - st)

    generator_by_json(d)

    matrix, height, width = matrix_from_graph()

    summary_page_rank(matrix, height, width)
