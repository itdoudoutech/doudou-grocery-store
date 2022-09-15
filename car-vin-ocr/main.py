import json, base64, os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models

SecretId = ''
SecretKey = ''

# 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
cred = credential.Credential(SecretId, SecretKey)
httpProfile = HttpProfile()
httpProfile.endpoint = "ocr.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)
req = models.LicensePlateOCRRequest()
img_path = os.path.abspath(os.curdir) + '/car.jpg'
f = open(img_path, 'rb')
img = base64.b64encode(f.read())
params = {
    'Action': 'LicensePlateOCR',
    'Version': '2018-11-19',
    'Region': 'ap-guangzhou,',
    "ImageBase64": str(img, encoding='utf-8')
}
req.from_json_string(json.dumps(params))
resp = client.LicensePlateOCR(req)
print(resp.to_json_string())
