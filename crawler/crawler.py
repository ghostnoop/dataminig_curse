import json
import time

import networkx as nx
import matplotlib.pyplot as plt

from services import get_page_links, get_page_links_v2

url = 'https://freelance.habr.com/tasks'

if __name__ == '__main__':
    print('start')
    # all_links = {}
    # links = []
    # li = []
    URL = "https://pythonworld.ru/"
    # all_links[URL] = li
    # max_depth = 2
    # get_page_links(URL, 0, all_links, links, max_depth)
    #
    # G = nx.DiGraph()
    # for link, links in all_links.items():
    #     for li in links:
    #         print("parent " + str(link) + " child " + str(li))
    #         G.add_edge(str(link), str(li))
    #
    # plt.figure(figsize=(40, 40))
    # nx.draw_networkx(G, node_color='green')
    # plt.show()
    st = time.monotonic()
    # get_page_links_v2(URL, 1)
    print(time.monotonic() - st)

    with open("data_file.json", "r") as read_file:
        data:dict = json.load(read_file)

    G = nx.DiGraph()
    for link, links in data.items():
        for link in links:
            for link_,links_ in link.items():
                for link__ in links:
                    pass



