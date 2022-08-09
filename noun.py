import MeCab
def nounQ(x):
   t=MeCab.Tagger('-O wakati')
   node=t.parseToNode(x)
   nouns=[]
   while node:
        f=node.feature
        p=f.split(',')[0]
        if p=='名詞':
            nouns.append(node.surface)
        node=node.next
   return tuple(nouns)

def noundic(dict):
    new_dict={}
    for question in dict:
        nouns=nounQ(question)
        new_dict[nouns]=dict[question]
    return new_dict


        



