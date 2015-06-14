def main():
    wiki_dict ={}
    f = open('links.txt')

    for line in f:
        link1,link2 = line.strip().split('\t')
        make_link_wiki(wiki_dict, int(link1), int(link2))
    f.close()

    word_dict ={}
    word_reverse_dict = {}
    f = open('pages.txt')

    for line in f:
        link1,link2 = line.strip().split('\t')
        word_dict[int(link1)] = link2
        word_reverse_dict[link2] = int(link1)
    f.close()

    while True:
        word_1 = input_word("1つ目のWikipedia項目: ", word_reverse_dict)
        word_2 = input_word("2つ目のWikipedia項目: ", word_reverse_dict)

        best_route = BFS_wiki(wiki_dict,word_1,word_2)
        for path in best_route:
            print word_dict[path]
        c = raw_input("もう一回やる？・ω・(Y/n) : ")
        if c.lower() == "n":
            return

def input_word(prompt, word_reverse_dict):
    while True:
        word = raw_input(prompt)
        if word in word_reverse_dict:
            return word_reverse_dict[word]
        print "Wikipediaにありません。もう一回！"

def make_link_wiki(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1


def BFS_wiki(G,word_1,word_2):
    prev_dict = {}
    queue = [word_1]
    old_label = ""
    best_route = [word_2]

    while queue:
        label = queue.pop(0)
        if label not in G:
            continue
        if word_2 in G[label]:
            prev_dict[word_2]=label
            break
        for new in G[label]:
            if new not in prev_dict:
                queue.append(new)
                prev_dict[new]=label

    start = word_2
    while prev_dict[start] != word_1:
        start = prev_dict[start]
        best_route.insert(0,start)
    best_route.insert(0,word_1)

    return best_route

if __name__ == '__main__':
    main()
