import json
from PIL import Image
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.bda.v20200324 import bda_client, models
import base64

SecretId = ''
SecretKey = ''


def cut(img_path):
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    cred = credential.Credential(SecretId, SecretKey)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "bda.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    client = bda_client.BdaClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.SegmentPortraitPicRequest()
    params = {
        'Action': 'SegmentPortraitPic',
        'Version': '2020-03-24',
        'Region': 'ap-guangzhou,',
        "Image": str(img, encoding='utf-8')
    }
    req.from_json_string(json.dumps(params))
    result = json.loads(client.SegmentPortraitPic(req).to_json_string())

    img_data = base64.b64decode(result['ResultImage'])
    to_img_path = 'bg.png'
    with open(to_img_path, 'wb') as f:
        f.write(img_data)


def save_new_img(img_path):
    img = Image.open(img_path)
    r, g, b, a = img.split()
    width, height = img.size
    bg = Image.new("RGBA", (width, height), 'red')
    bg.paste(img, (0, 0), mask=a)
    bg.save('result.png')


save_new_img('./bg.png')
