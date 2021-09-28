import json
import uuid
import re
import requests
import datetime
import time
import os

header = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

users = os.environ["users"]
#api = os.environ["api"]
users = json.loads(users)

print('当前时间：', datetime.datetime.now())

for user in users:
    s = requests.session()
    s.post('https://nco.zjgsu.edu.cn/login', data=user, headers=header)
    res = s.get('https://nco.zjgsu.edu.cn/', headers=header)
    content = str(res.content, encoding='utf-8')
    if re.search('当天已报送!', content):
        print(datetime.datetime.now().strftime('%Y-%m-%d'), '报送情况： *主动报送*')
        continue
    data = {}
    try:
        for item in re.findall(R'<input.+?>', content):
            key = re.search(R'name="(.+?)"', item).group(1)
            value = re.search(R'value="(.*?)"', item).group(1)
            check = re.search(R'checked', item)
            if key not in data.keys():
                data[key] = value
            elif check is not None:
                data[key] = value
    except:
        print('出现错误，可能是账号密码不正确')
        continue
    for item in re.findall(R'<textarea.+?>', content):
        key = re.search(R'name="(.+?)"', item).group(1)
        data[key] = ''
    # 为了安全起见，这里还是推荐加上大致的地址和uuid值，虽然经过测试，不填写也可以正常使用
    # ---------------安全线-----------1--#
    data['uuid'] = str(uuid.uuid1())
    if('locationInfo' not in data):
        data['locationInfo'] = '浙江省温州市鹿城区'
    # ---------------安全线-------------#
    res = s.post('https://nco.zjgsu.edu.cn/', data=data, headers=header)
    if re.search('报送成功', str(res.content, encoding='utf-8')) is not None:
        result=datetime.datetime.now().strftime('%Y-%m-%d')+'报送成功'
    else:
        result=datetime.datetime.now().strftime('%Y-%m-%d')+'报送失败'
    print(result)
    time.sleep(10)
    data = {
       "text":result,
       "desp":result
    }
    #requests.post(api,data = data)

