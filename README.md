# AUTO FUCK NCO ZJGSU

浙江工商大学 云战役 自动报送 Github全自动版

魔改自[FUCK NCO ZJGSU](https://github.com/Hukeqing/FUCK-NCO-ZJGSU)。利用Github的Actions，让你不用准备任何东西，只需要白嫖微软的服务器，就能实现每天自动签到。

默认设置凌晨十二点半和早八点各打卡一次。

## 使用方法

1. 点右上角Fork本项目。

2. 进入项目的设置，添加签到用户信息：
     - Settings -> Secrets -> New reponsitory secret
     - Name: users
     - Value(example):
        ````Json
        [
            {
                "name": "your_student_num",
                "psswd": "your_password"
            },
            {
                "name": "your_student_num",
                "psswd": "your_password",
                "locationInfo": "浙江省杭州市金沙港生活区"
            }
        ]
        ````

3. 进入Actions，允许运行

## ~~本体不是我写的，出问题别打我，传送门再给你一次，打[hkq](https://github.com/Hukeqing/FUCK-NCO-ZJGSU)去。~~


