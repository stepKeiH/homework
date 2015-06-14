f = open('links.txt')
wiki_name = {}
new_file = open('subgraph_links.txt','w')

for line in f:
    link1,link2 = line.strip().split('\t')
    if int(link1) < 10000 and int(link2) < 10000:
        print >> new_file, line.strip()

f.close()
new_file.close()
