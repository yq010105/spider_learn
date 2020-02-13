import jieba
 
from wordcloud import WordCloud
 
 
with open("./bi.txt") as fp:
    txt = fp.read()  # 读取文本
 
words = jieba.lcut(txt)  # 精确分词
 
nextword = ' '.join(words)    #空格连接字符
 
wordshow = WordCloud(background_color='white',
                     width=800,
                     height=800,
                     max_words=800,
                     max_font_size=100,
                     font_path="msyh.ttc",    #用微软雅黑作为字体显示效果
 
                     ).generate(nextword)
 
wordshow.to_file('bilibili_rank.png')  #转换成图片
