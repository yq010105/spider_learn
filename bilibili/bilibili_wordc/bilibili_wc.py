from wordcloud import WordCloud
import PIL .Image as image
import numpy as np # 自定义图片
import jieba # 中文

def trans_cn(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result

dir = './bi.txt'

with open(dir) as fp:
    text = fp.read()
    # print(text)
    # exit()
    text = trans_cn(text)
    mask = np.array(image.open('F:\download\\1.png'))
    WordCloud = WordCloud(
        mask = mask,
        font_path ='C:\\windows\\Fonts\\msyh.ttc'
    ).generate(text)
    image_produce = WordCloud.to_image()
    image_produce.show()
    WordCloud.to_file('bilibili_rank.png')