# -*- coding: utf-8 -*-





#有效期为30天---请自行获取
#参考  https://ai.baidu.com/docs#/OCR-API-Access/top

access_token="***************************************************"


import base64
import requests


url="https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"


def getCode(img_path):
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def read_img():
        with open(img_path, "rb")as f:
            return base64.b64encode(f.read()).decode()

    image = read_img()
    response = requests.post(url=url, data={"image": image, "access_token": access_token},
                             headers=header)
    res_json= response.json()
    res_str=""
    for word in res_json.get("words_result"):
        res_str+=word.get("words")
    return res_str



if __name__ == '__main__':

    res=getCode('detial.png')
    print(res)

