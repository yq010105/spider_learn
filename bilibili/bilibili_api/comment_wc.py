from wordcloud import WordCloud
import PIL .Image as image
import jieba


def trans_cn(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result


def wc():
    dir1 = './txt/comment.txt'
    with open(dir1, encoding='utf-8') as f:
        text = f.read()
        text = trans_cn(text)
        WordCloud2 = WordCloud(
            font_path='C:\\windows\\Fonts\\simfang.ttf'
        ).generate(text)
        image_produce = WordCloud2.to_image()
        image_produce.show()
        WordCloud2.to_file('./txt/comment.png')


wc()
