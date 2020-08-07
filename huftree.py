import numpy as np
from comp1 import make_sentence
from collections import Counter

class Node:
    def __init__(self, data, value):
        self.data = data
        self.value=value
        self.left = None
        self.right = None

class huftree:
    def __init__(self, sentence):
        str_list=list(sentence)
        count=Counter(str_list)
        count=dict(count)
        self.sentence=sentence
        self.root=None
        self.decode_dict={}
        self.insert(count) #文字をいれる
    def insert(self,count):
        count=sorted(count.items(), key=lambda x:x[1]) #頻度順にソート
        node_list=[]
        for c in count:
            node_list.append(Node(c[0],c[1]))
        #print(node_list)
        while len(node_list)>=2:
            node_list=sorted(node_list, key=lambda x:x.value)
            #print(node_list)
            min1=node_list[0]
            min2=node_list[1]
            r=Node(min1.data+min2.data,min1.value+min2.value)
            r.left=min1
            r.right=min2
            node_list.append(r)
            node_list.remove(min1)
            node_list.remove(min2)
        self.root=node_list[0]
        return
    def coding(self,node,search,co):
        if node.data==search:
            print(co)
            result=co
            self.decode_dict[node.data]=co
            return result
        elif node==None:
            print("error")
            return
        else:
            if node.right is not None:
                self.coding(node.right,search,co+"0")
            if node.left is not None:
                self.coding(node.left,search,co+"1")
    def make_code(self):
        sentence=self.sentence
        str_list=list(sentence)
        count=Counter(str_list)
        count=dict(count)
        #code_dict=[]
        for c in count:
            self.coding(self.root,c[0],"")
            #print(code_result)
            #code_dict.append((c,code_result))
        print(self.decode_dict)
        code_sentence=""
        #code_dict=dict(code_dict)
        for sent in str_list:
            code_sentence+=self.decode_dict[sent]
        return code_sentence

if __name__ == '__main__':
    #sentence=make_sentence(100)
    sentence="1010101010101210101012121010101234321232321010101012321232321212121212321012101012343454565656765454545434323432323234323212323432101012123456765656565432101010123432101010121234345434343232101012121010101210121234543212345654567678987676789898765654567678987898987676765454567898789898789878767656543454345676565454565432123234343232321210121010101012343234323234543434343232345676787876767876787876789876543432323210101012345454567898767676787678789898987876789876567678787678789898989898765676765656567898989898987654567654545434567654321210101210121234321010121212343456765456543434543232345654567678787876787876567876789878787878989878987678767898989898789878987878987678765676767898987898789878987678765456545454545434545456767876545656567656767876789878987876545678987678767676767654567678987676565432321232321010101212101010101010121232323212101012321210121010121210101012323432123454343212121010101210101010101010101010121012123454323212323434545654543434323454545678989898989898789898989876"
    print(sentence)
    print(len(sentence))
    huftree1=huftree(sentence)
    aa=huftree(sentence)
    print(huftree1.make_code())
    print("-------")

    sentence2="3462676410128256318354730848044460204343115813223838789281759219789263553987637169794150181074603182864734426914189628381962347719834592576592161892400947385822895707647341166473538744897303513899093440955354337952339731905135871112996808722486500664130915686689915013624064261072470258949521944977226095725421754768233054875654547532057130672955228878265170783752724050460038459900482057015290015952363841339099492732701081183197098264959000631362542082411267031995334932794307016861542123935314768740924803474591000124541851123844604978262203348202825907616195151853054161265750240539991512791002631971345652424547772526334959513722439692104957598087863725943333371058268798003757352032972207639306059629997158296920761670831060207768891160707503044457445677275032268424355304511326661156269275403164800647332129847744505673801536508665709974282584989327518391544794610257781400941907702755190479644870718744453362624712124854245778452633550115976327535707537305919170457543543735567464541812328979"
    print(sentence2)
    print(len(sentence2))
    huftree2=huftree(sentence2)
    print(huftree2.make_code())

    str_list=list(sentence2)
    count=Counter(str_list)
    count=dict(count)
    print(count)
    count=sorted(count.items(), key=lambda x:x[1])
    count.reverse()
    print(count)
    entropy=0
    for c in count:
        entropy+=c[1]/1000*(np.log2(c[1]/1000)+len(huftree1.decode_dict[c[0]]))
    print(entropy)
