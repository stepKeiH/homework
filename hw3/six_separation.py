from collections import deque
from random import randint

LINK_MAX = 52973671
PAGE_MAX = 1483277

def main():
    f = open('links.txt')

    wiki_dict ={}
    for line in f:
        link1,link2 = line.strip().split('\t')
        make_link_wiki(wiki_dict, int(link1), int(link2))
    f.close()

    new_G = {}
    check_list = [randint(0,PAGE_MAX-1) for i in range(10)]

    for link in check_list:
        BFS_wiki_six(wiki_dict,link)

def outgoing_ranking(G, new_G, check_list):
    for link in G:
        new_G[link] = len(G[link])


def make_link_wiki(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1


def BFS_wiki_six(G,link):
    prev_dict = {link:link}
    print "Randomly chosen link ID: " + str(link)
    best_route =[]
    queue = deque([link])

    while queue:
        label = queue.popleft()
        if label not in G:
            continue
        for new in G[label]:
            if new not in prev_dict:
                queue.append(new)
                prev_dict[new]=label

    start = label
    while prev_dict[start] != link:
        start = prev_dict[start]
        best_route.insert(0,start)
    best_route.insert(0,link)

    print "Lengh of the longest path: " + str(len(best_route))
    print "Number of total pages visited: " + str(len(prev_dict))

if __name__ == '__main__':
    main()
