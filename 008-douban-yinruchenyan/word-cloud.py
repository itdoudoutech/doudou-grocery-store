from wordcloud import WordCloud
import jieba


def jieba_():
    # 打开评论数据文件
    content = open('comment.csv', 'rb').read()
    # jieba 分词
    word_list = jieba.cut(content)
    words = []
    # 过滤掉的词
    remove_words = ['的', '在', '有', '是', '了']
    for word in word_list:
        if word not in remove_words:
            words.append(word)
    global word_cloud
    # 用逗号隔开词语
    word_cloud = '，'.join(words)


def cloud():
    # 打开词云背景图
    # cloud_mask = np.array(Image.open('bg.jpg'))
    # 定义词云的一些属性
    wc = WordCloud(
        # 背景图分割颜色为白色
        background_color='white',
        # 背景图样
        # mask=cloud_mask,
        # 显示最大词数
        max_words=200,
        # 显示中文
        font_path='./Alibaba-PuHuiTi-Bold.ttf',
        # 最大尺寸
        max_font_size=100,
        width=600,
        height=600
    )
    global word_cloud
    x = wc.generate(word_cloud)
    image = x.to_image()
    image.show()


jieba_()
cloud()
