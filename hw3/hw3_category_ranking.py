def main():
    cat_dict = {}
    f = open('cat_links.txt')

    for line in f:
        link1,link2 = line.strip().split('\t')
        make_page_cat(cat_dict, int(link1), int(link2))
    f.close()

    cat_count = {}
    for cat in cat_dict:
        cat_count[cat] = len(cat_dict[cat])

    cat_name = {}
    f = open('cats.txt')
    for line in f:
        link1,link2 = line.strip().split('\t')
        cat_name[int(link1)] = link2
    f.close()

    rank_num = 30
    ranking_list =[]
    count = 0
    for cat, page_num in sorted(cat_count.items(), key=lambda x:x[1], reverse=True):
        if count < rank_num:
            ranking_list.append(cat)
            count += 1
        else:
            break

    for item in ranking_list:
        print "カテゴリー名: " + cat_name[item] + "  Wikipediaページからのリンク数: " + str(cat_count[item])

def make_page_cat(G, page, cat):
    if cat not in G:
        G[cat] = {}
    (G[cat])[page] = 1

if __name__ == '__main__':
    main()
