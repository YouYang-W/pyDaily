import jieba
import matplotlib.pyplot as plt
import wordcloud
import networkx as nx
import matplotlib
import jieba.posseg as psg
matplotlib.rcParams['font.sans-serif']=['SimHei']
#读取文本
def read_txt():
    file=open('连城诀【三联版】.txt','r+',encoding='gbk')
    txt=file.read()
    file.close()
    return txt

#词性统计（写入文档）
def sda():
    import jieba.posseg as psg
    text=open("连城诀【三联版】.txt", encoding='gbk', errors='ignore').read() 
    seg=psg.cut(text) 
    file=open("词性.txt",'a+')
    for ele in seg:
        file.writelines(ele)
  
#停词文档
def stopwordslist(filepath):
    stopwords=[line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
    return stopwords

#分词生成人物（写入文档）
def write_txt():
    words = jieba.lcut(read_txt())     # 使用精确模式对文本进行分词counts = {}     # 通过键值对的形式存储词语及其出现的次数
    counts={}
    stopwords=stopwordslist('stop.txt')
    for word in words:
        if len(word) == 1:    # 单个词语不计算在内
            continue
        elif word not in stopwords:
            counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

    f=open("词频统计.txt","w")#写入文件
    for i in range(len(items)):
        word, count = items[i]
        f.writelines("{0:<5}{1:>5}\n".format(word, count))
    f.close()

#生成词云
def creat_wordcloud():
    f_0=open("词频统计.txt",'r')
    bg_pic=plt.imread('张国荣.jpg')
    text=f_0.read()
    f_0.close()
    wcloud=wordcloud.WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",
                           background_color="white",width=1000,
                           max_words=500,
                           mask=bg_pic,
                           height=860,
                           margin=2,
                           ).generate(text)

    wcloud.to_file("连城诀cloud.jpg")
    plt.imshow(wcloud)
    plt.axis('off')
    plt.show()


#生成人物关系图（全按书上抄的）
def creat_relationship():
    Names=['狄云', '水笙', '万震山', '丁典', ' 戚芳', ' 万圭 ', '花铁干' ,' 血刀老祖 ', '戚长发', ' 言达平' , '宝象',' 汪啸风' ,'水岱']
    relations={}
    lst_para=(read_txt()).split('\n')#lst_para是每一段
    for text in lst_para:
        for name_0 in Names:
            if name_0 in text:
                for name_1 in Names:
                    if name_1 in text and name_0!=name_1 and (name_1,name_0) not in relations:
                        relations[(name_0,name_1)]=relations.get((name_0,name_1),0)+1
    maxRela=max([v for k,v in relations.items()])
    relations={k:v /  maxRela for k,v in relations.items()}
    #return relations


    plt.figure(figsize=(15,15))
    G=nx.Graph()
    for k,v in relations.items():
        G.add_edge(k[0],k[1],weight=v)
        #筛选权重大于0.6的边
    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']>0.6]
    #筛选权重大于0.3小于0.6的边
    emidle=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight']>0.3) & (d['weight']<=0.6)]
    #筛选权重小于0.3的边
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']<=0.3]
    #设置图形布局
    pos=nx.spring_layout(G)
    #设置节点样式
    nx.draw_networkx_nodes(G,pos,alpha=0.8, node_size=1200)
    #设置大于0.6的边的样式
    nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2.5,alpha=0.9,edge_color='g')
    #0.3~0.6
    nx.draw_networkx_edges(G,pos,edgelist=emidle, width=1.5,alpha=0.6,edge_color='y')
    #<0.3
    nx.draw_networkx_edges(G,pos,edgelist=esmall, width=1,alpha=0.4,edge_color='b',style='dashed')
    nx.draw_networkx_labels(G,pos,font_size=12)

    plt.axis('off')
    plt.title("连城诀人物权重图")
    plt.show()

def main():
    write_txt()
    creat_wordcloud()
    creat_relationship()

if __name__ == '__main__':
    main()
