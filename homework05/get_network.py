import time
from typing import Optional
import config
import igraph
import requests
import numpy as np
from igraph import Graph, plot
from homework05.api import get_friends, get_names


def get_network(all_ids, as_edgelist=True):
    """ Building a friend graph for an arbitrary list of users """


def plot_graph(vertices, edges):
    # Создание графа
    g = Graph(vertex_attrs={"label":vertices},
              edges=edges, directed=False)


    # Задаем стиль отображения графа
    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
        maxiter=1000,
        area=N ** 3,
        repulserad=N ** 3)
    # Отрисовываем граф
    g.simplify(multiple=True, loops=True)
    plot(g, **visual_style)


if __name__ == '__main__':
    fr = get_friends(245200958, 'first_name')
    friends1 = [item['id'] for item in fr['response']['items']]
    vert, edg = get_network(friends1)
    plot_graph(vert, edg)
