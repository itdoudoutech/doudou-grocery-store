import requests, time, random, pandas as pd
from lxml import etree

cookies = {'your cookie...'}
headers = {'User-Agent': 'your agent...'}


def get_content_by_url(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    return response.content


def parse():
    # 初始化 4 个 list 分别存用户名、评星、时间、评论文字
    users = []
    stars = []
    times = []
    content = []
    for i in range(0, 600, 20):
        url = F'https://movie.douban.com/subject/35131346/comments?start={i}&limit=20&status=P&sort=new_score'
        comment_text = get_content_by_url(url)
        time.sleep(random.random())
        selector = etree.HTML(comment_text)
        # 获取单页所有评论
        comments = selector.xpath('//div[@class="comment"]')
        for comment in comments:
            # 用户名
            user = comment.xpath('.//h3/span[2]/a/text()')[0]
            # 评星
            star = comment.xpath('.//h3/span[2]/span[2]/@class')[0][7:8]
            # 时间
            date_time = comment.xpath('.//h3/span[2]/span[3]/@title')
            # 有的时间为空，需要判断下
            if len(date_time) != 0:
                date_time = date_time[0]
            else:
                date_time = None
            comment_text = comment.xpath('.//p/span/text()')[0].strip()
            users.append(user)
            stars.append(star)
            times.append(date_time)
            content.append(comment_text)

        comment_dic = {'user': users, 'star': stars, 'time': times, 'comments': content}
        comment_df = pd.DataFrame(comment_dic)
        # 保存数据
        comment_df.to_csv('data.csv')
        comment_df['comments'].to_csv('comment.csv', index=False)


parse()
