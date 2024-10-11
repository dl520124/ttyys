# 在屏幕中找到局部图片的位置 find方式,先 template 后全分辨率
# 导包
from ascript.android import action
from ascript.android.screen import FindImages
# 导入上下文环境包,方便导入图片地址
from ascript.android.system import R
import numpy as np
import time
import random

from .特征库 import *

tansuo_state = 1
sainum = 0

# 定义突破状态变量
tupo_state = 0
# 定义失败次数
failed = 0
turefaile = 0
last_refresh_time = 0
shuaxinone = 0
number = 0
flag = False

baonum = 0
bossStop = 0
#打多少次小怪转突破
fitguainum = 120

# 时间
xunhuan_time = 0
jiesuan_time = 0
dianxiannum = 0


def bezier(p0, p1, p2, t):
    u = 1 - t
    return u ** 2 * p0 + 2 * u * t * p1 + t ** 2 * p2

ld.日志_设置级别(20)
while True:
    if tansuo_state == 0:  # 探索状态
        path = R.img("kun28.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)

        # 检查 res 是否为 None
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])

            if res["confidence"] > 0.8:
                mu, sigma = res["center_x"], 30  # 均值和标准差
                x = np.random.normal(mu, sigma)

                # 确保 x 在指定范围外
                while res["center_x"] - 100 < x < res["center_x"] + 100:
                    x = np.random.normal(mu, sigma)

                mu, sigma = res["center_y"] + 60, 20  # 均值和标准差
                y = np.random.normal(mu, sigma)

                # 确保 y 在指定范围外
                while res["center_y"] < y < res["center_y"] + 60:
                    y = np.random.normal(mu, sigma)

                print(x, y)
                action.click(x, y)

        path = R.img("悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("悬赏中心坐标:", res["center_x"], res["center_y"])
            print("悬赏相似度:", res["confidence"])
            print("悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x悬赏相似度:", res["confidence"])
                    print("x悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])

        path = R.img("现世悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("现世悬赏中心坐标:", res["center_x"], res["center_y"])
            print("现世悬赏相似度:", res["confidence"])
            print("现世悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x现世悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x现世悬赏相似度:", res["confidence"])
                    print("x现世悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])





        path = R.img("探索.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"]-5,res["center_x"]+5)
                y = res["center_y"]
                action.click(x, y)



        path = R.img("樱饼.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                y = res["center_y"]
                print('在小怪页面')

                path = R.img("boss.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)

                path = R.img("小怪.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)

                path = R.img("内宝箱.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        path = R.img("退出.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None:
                            print("中心坐标:", res["center_x"], res["center_y"])
                            print("相似度:", res["confidence"])
                            print("在屏幕中的范围:", res["rect"])
                            if res["confidence"] > 0.8:
                                x = random.randint(res["center_x"]-3,res["center_x"]+3)
                                y = random.randint(res["center_y"]-3,res["center_y"]+3)
                                action.click(x,y)

                path = R.img("确认.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)



                path = R.img("小怪.png")  # 这里替换为你的图片地址
                res1 = FindImages.find(path)
                path = R.img("boss.png")  # 这里替换为你的图片地址
                res2 = FindImages.find(path)
                path = R.img("内宝箱.png")  # 这里替换为你的图片地址
                res3 = FindImages.find(path)
                path = R.img("确认.png")  # 这里替换为你的图片地址
                res4 = FindImages.find(path)
                path = R.img("自动.png")  # 这里替换为你的图片地址
                res5 = FindImages.find(path)
                if res1["confidence"]<0.8 and res2["confidence"]<0.8 and res3["confidence"] <0.8 and res4["confidence"] <0.8 and res5["confidence"] <0.8:
                    print('该滑动了')
                    # 起始点、控制点和结束点
                    x1 = random.randint(1000, 1200)
                    y1 = random.randint(150, 180)

                    x2 = random.randint(600, 800)
                    y2 = random.randint(200, 400)

                    x3 = random.randint(200, 400)
                    y3 = random.randint(100, 300)
                    print('起始坐标', x1, y1)
                    print('控制坐标', x2, y2)
                    print('结束坐标', x3, y3)

                    start_point = np.array([x1, y1])
                    control_point = np.array([x2, y2])
                    end_point = np.array([x3, y3])

                    # 生成一系列参数值
                    num = random.randint(10, 50)
                    t_values = np.linspace(0, 1, num=num)
                    print('贝塞尔num', num)

                    # 计算贝塞尔曲线上的点
                    points = [bezier(start_point, control_point, end_point, t) for t in t_values]

                    # 发送鼠标左键按下消息
                    action.Touch.down(x1, y1)
                    # 遍历贝塞尔曲线上的点
                    for point in points:
                        print('到这里吗？')
                        x, y = int(point[0]), int(point[1])
                        # 发送鼠标移动消息
                        action.Touch.move(x, y)
                    # 发送鼠标左键释放消息
                    action.Touch.up(x3, y3)
                    sainum = sainum + 1

                if sainum >= 3:
                    print('滑动超过3次，退出')
                    path = R.img("退出.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None:
                        # print("中心坐标:", res["center_x"], res["center_y"])
                        # print("相似度:", res["confidence"])
                        # print("在屏幕中的范围:", res["rect"])
                        if res["confidence"] > 0.8:
                            x = random.randint(res["center_x"] - 3, res["center_x"] + 3)
                            y = random.randint(res["center_y"] - 3, res["center_y"] + 3)
                            action.click(x, y)

















        path = R.img("结算1.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                sainum = 0
                print('结算1点击x=', x, 'y=', y)
                # number = number + 1;
                # jiesuan_time = time.time()
                # print('number=', number);

        path = R.img("结算2.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                print('结算2点击x=', x, 'y=', y)



    if tansuo_state == 1:  # 突破探索模式
        number = 0
        time.sleep(1)

        path = R.img("突破退出.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("突破退出相似度:", res["confidence"])
            path = R.img("少女与面具.png")  # 这里替换为你的图片地址
            res1 = FindImages.find(path,confidence=0.8)
            if res1 is not None:
                print("少女与面具相似度:", res1["confidence"])
                action.click(res["center_x"], res["center_y"])




        path = R.img("庭院突破.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                action.click(res["center_x"], res["center_y"])
                time.sleep(2)

        path = R.img("突破页面.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res["confidence"] > 0.8 :
           print('处于突破页面')

           # 查找有多少个失败，鸡肋，不太准
           if not flag:
               res = FindImages.find_all_template([R.img("打不过.png"),],confidence= 0.81)
               if res is not None:
                   count = 0
                   if res:
                       # 遍历所有找到的结果
                       for i in res:
                           print("中心坐标:", i["center_x"], i["center_y"])
                           print("相似度:", i["confidence"])
                           print("在屏幕中的范围:", i["rect"])
                           count += 1  # 每找到一个结果，计数器加一
                   failed = count
                   print('目前失败',failed,'个')
                   flag = True
               else:
                   failed = count
                   print('目前失败', failed, '个')
                   flag = True


        path = R.img("结算1.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                sainum = 0
                print('结算1点击x=', x, 'y=', y)
                # number = number + 1;
                # jiesuan_time = time.time()
                # print('number=', number);

        path = R.img("结算2.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                print('结算2点击x=', x, 'y=', y)

        path = R.img("失败.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                print('结算2点击x=', x, 'y=', y)

        path = R.img("悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("悬赏中心坐标:", res["center_x"], res["center_y"])
            print("悬赏相似度:", res["confidence"])
            print("悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x悬赏相似度:", res["confidence"])
                    print("x悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])

        path = R.img("现世悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("悬赏中心坐标:", res["center_x"], res["center_y"])
            print("悬赏相似度:", res["confidence"])
            print("悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x悬赏相似度:", res["confidence"])
                    print("x悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])

        path = R.img("进攻.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                action.click(x, y)

        path = R.img("准备.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                action.click(x, y)

        path = R.img("确定.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                action.click(x, y)
                tupo_state = 0
                failed = 0
                turefaile = 0

        path = R.img("灰突破券不足.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.94:
                print('突破券不足',res["confidence"])
                path = R.img("突破退出.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    if res["confidence"] > 0.98:
                        action.click(res["center_x"], (res["center_y"]))
                        jiesuan_time = 0
                        xunhuan_time = 0
                        time.sleep(1.5)
                        path = R.img("庭院突破.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None:
                            if res["confidence"] > 0.8:
                                tansuo_state = 2
                                print('进入探索页面')



        path = R.img("突破页面.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        path = R.img("结算2.png")  # 这里替换为你的图片地址
        res2 = FindImages.find(path)
        if res is not None and res["confidence"] > 0.8:
            path = R.img("结算2.png")  # 这里替换为你的图片地址
            res2 = FindImages.find(path)
            if res2 is not None and res2["confidence"] < 0.8:
                print('正式开始突破')
                # 第一个突破标志
                if tupo_state == 0:
                    last_refresh_time = time.time()
                    turefaile = 0
                    path = R.img("刷新.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None:
                        if res["confidence"] > 0.9:
                            shuaxinone = 1  # 刷新未冷却
                            print('刷新未冷却')

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 139, 473, 273])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)

                        if res:
                            print("突破中心坐标:", res["center_x"], res["center_y"])
                            print("突破相似度:", res["confidence"])
                            print("突破在屏幕中的范围:", res["rect"])

                        if res2:
                            print("进攻中心坐标:", res["center_x"], res["center_y"])
                            print("进攻相似度:", res["confidence"])
                            print("进攻在屏幕中的范围:", res["rect"])
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x,y)
                            print('识别突破1标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 139, 473, 273])
                        if res:
                            print("突破中心坐标:", res["center_x"], res["center_y"])
                            print("突破相似度:", res["confidence"])
                            print("突破在屏幕中的范围:", res["rect"])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[139, 139, 473, 273])
                            if res:
                                print("打不过中心坐标:", res["center_x"], res["center_y"])
                                print("打不过相似度:", res["confidence"])
                                print("打不过在屏幕中的范围:", res["rect"])
                            if res:
                                print("突破1打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破1后failed =', failed)
                                tupo_state = 1
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破1成功,failed =', failed)
                                tupo_state = 1
                        if res is None:
                            print('突破1找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 1

                if tupo_state == 1:
                    print('到突破2了')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 139, 804, 273])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破2标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 139, 804, 273])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[473, 139, 804, 273])
                            if res:
                                print("突破2打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破2后failed =', failed)
                                tupo_state = 2
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破2成功,failed =', failed)
                                tupo_state = 2
                        if res is None:
                            print('突破2找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 2


                if tupo_state == 2:
                    print('到突破3拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 139, 1140, 273])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破3标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    print('不是到这里吗')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 139, 1140, 273])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[807, 139, 1140, 273])
                            if res:
                                print("突破3打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破3后failed =', failed)
                                tupo_state = 3
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破3成功,failed =', failed)
                                tupo_state = 3
                        if res is None:
                            print('突破3找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 3


                if tupo_state == 3:
                    print('到突破4拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 279, 473, 404])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破4标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 279, 473, 404])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[139, 279, 473, 404])
                            if res:
                                print("突破4打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破4后failed =', failed)
                                tupo_state = 4
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破4成功,failed =', failed)
                                tupo_state = 4
                        if res is None:
                            print('突破4找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 4

                if tupo_state == 4:
                    print('到突破5拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 279, 804, 404])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破5标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 279, 804, 404])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[473, 279, 804, 404])
                            if res:
                                print("突破5打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破5后failed =', failed)
                                tupo_state = 5
                            if res is None  or  res is not None and res["confidence"] < 0.9:
                                print('突破5成功,failed =', failed)
                                tupo_state = 5
                        if res is None:
                            print('突破5找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 5

                if tupo_state == 5:
                    print('到突破6拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 279, 1140, 404])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破6标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 279, 1140, 404])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[807, 279, 1140, 404])
                            if res:
                                print("突破6打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破6后failed =', failed)
                                tupo_state = 6
                            if res is None or  res is not None and res["confidence"] < 0.9:
                                print('突破6成功,failed =', failed)
                                tupo_state = 6
                        if res is None:
                            print('突破6找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 6

                if tupo_state == 6:
                    print('到突破7拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 412, 473, 543])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破7标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 412, 473, 543])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[139, 412, 473, 543])
                            if res:
                                print("突破7打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破7后failed =', failed)
                                tupo_state = 7
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破7成功,failed =', failed)
                                tupo_state = 7
                        if res is None:
                            print('突破7找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 7


                if tupo_state == 7:
                    print('到突破8拉')
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        time.sleep(0.5)
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 412, 804, 543])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2["confidence"] < 0.85:
                            x = random.randint(res["center_x"] - 180, res["center_x"])
                            y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                            action.click(x, y)
                            print('识别突破8标志')
                            time.sleep(1)
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res = FindImages.find(path)
                            if res is not None:
                                if res["confidence"] > 0.8:
                                    x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                    y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                    action.click(x, y)
                                    time.sleep(1)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[473, 412, 804, 543])
                        if res is not None and res["confidence"] < 0.9:
                            path = R.img("打不过.png")  # 这里替换为你的图片地址
                            if res:
                                print("突破8打不过相似度:", res["confidence"])
                            if res is not None and res["confidence"] > 0.9:
                                print('突破8后failed =', failed)
                                tupo_state = 8
                            if res is None or res is not None and res["confidence"] < 0.9:
                                print('突破8成功,failed =', failed)
                                tupo_state = 8
                        if res is None:
                            print('突破8找不到突破标志，说明成功/失败了跳过')
                            tupo_state = 8

                if tupo_state == 8:
                    print('到突破9拉')
                    print('failed=', failed)
                    if failed <= 4:
                        failedNum = 4 - failed
                        path = R.img("突破页面.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.8:
                            path = R.img("突破标志.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res2 = FindImages.find(path)
                            if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                "confidence"] < 0.85:
                                x = random.randint(res["center_x"] - 180, res["center_x"])
                                y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                                action.click(x, y)
                                time.sleep(1)
                                print('识别突破9标志,还需要失败', failedNum)

                            while True:
                                path = R.img("突破标志.png")  # 这里替换为你的图片地址
                                res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                                path = R.img("进攻.png")  # 这里替换为你的图片地址
                                res2 = FindImages.find(path)
                                if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                    "confidence"] < 0.85:
                                    x = random.randint(res["center_x"] - 180, res["center_x"])
                                    y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                                    action.click(x, y)
                                    time.sleep(1)

                                path = R.img("进攻.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                        y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                        action.click(x, y)
                                        time.sleep(1)


                                path = R.img("失败.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        # 生成符合指定范围的正态分布的 x 和 y 坐标
                                        mu, sigma = 1200, 30  # 均值和标准差
                                        x = np.random.normal(mu, sigma)
                                        while x < 1144 or x > 1256:
                                            x = np.random.normal(mu, sigma)

                                        mu, sigma = 437, 100  # 均值和标准差
                                        y = np.random.normal(mu, sigma)
                                        while y < 185 or y > 689:
                                            y = np.random.normal(mu, sigma)
                                        action.click(x, y)
                                        print('结算2点击x=', x, 'y=', y)
                                        failed = failed + 1
                                        print(failed)
                                        time.sleep(1)

                                if failed >= 4:
                                    print('失败四次了')
                                    path = R.img("打不过.png")  # 这里替换为你的图片地址
                                    res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                                    path = R.img("进攻.png")  # 这里替换为你的图片地址
                                    res2 = FindImages.find(path)
                                    if res:
                                        print("打不过4次中心坐标:", res["center_x"], res["center_y"])
                                        print("打不过4次相似度:", res["confidence"])
                                        print("打不过4次在屏幕中的范围:", res["rect"])
                                    if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                        "confidence"] < 0.85:
                                        x = random.randint(res["center_x"] - 180, res["center_x"])
                                        y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                                        action.click(x, y)
                                        print('识别突破9标志，打了一次')
                                        turefaile = 1  # 打过一次9了
                                        tupo_state = 9
                                        break

                                path = R.img("打不过.png")  # 这里替换为你的图片地址
                                res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                                path = R.img("进攻.png")  # 这里替换为你的图片地址
                                res2 = FindImages.find(path)
                                if res:
                                    print("打不过中心坐标:", res["center_x"], res["center_y"])
                                    print("打不过相似度:", res["confidence"])
                                    print("打不过在屏幕中的范围:", res["rect"])
                                if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                    "confidence"] < 0.85:
                                    x = random.randint(res["center_x"] - 180, res["center_x"])
                                    y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                                    action.click(x, y)
                                    time.sleep(1)

                                path = R.img("进攻.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 30, res["center_x"] + 30)
                                        y = random.randint(res["center_y"] - 15, res["center_y"] + 15)
                                        action.click(x, y)
                                        time.sleep(1)


                                path = R.img("返回.png")  # 这里替换为你的图片地址
                                res = FindImages.find_template(path)
                                path = R.img("确认.png")  # 这里替换为你的图片地址
                                res2 = FindImages.find(path)
                                if res is not None and res["confidence"] > 0.8 and res2 is not None and res2[
                                    "confidence"] < 0.85:
                                    x = random.randint(res["center_x"] - 2, res["center_x"]+2)
                                    y = random.randint(res["center_y"] -2, res["center_y"] + 2)
                                    action.click(x, y)
                                    time.sleep(1)

                                path = R.img("确认.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path,rect=[653,374,829,473])
                                if res is not None :
                                    if res["confidence"] > 0.9:
                                        x = random.randint(res["center_x"] - 2, res["center_x"] + 2)
                                        y = res["center_y"]
                                        print(x,y)
                                        action.click(x,y)
                                        time.sleep(1)

                    else:
                        print('没到9就失败那么多次')
                        # 这段是测试，可以不用的
                        path = R.img("突破页面.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.8:
                            path = R.img("突破标志.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res2 = FindImages.find(path)
                            if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                "confidence"] < 0.85:
                                path = R.img("刷新.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 15, res["center_x"] + 15)
                                        y = random.randint(res["center_y"] - 5, res["center_y"] + 5)
                                        action.click(x, y)
                                        time.sleep(1)

                        path = R.img("突破页面.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.8:
                            path = R.img("突破标志.png")  # 这里替换为你的图片地址
                            res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                            path = R.img("进攻.png")  # 这里替换为你的图片地址
                            res2 = FindImages.find(path)
                            if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                                "confidence"] < 0.85:
                                x = random.randint(res["center_x"] - 180, res["center_x"])
                                y = random.randint(res["center_y"] + 10, res["center_y"] + 80)
                                action.click(x, y)
                                print('识别突破9标志，打了一次')
                                turefaile = 1  # 打过一次9了
                                tupo_state = 9
                            pass

                if tupo_state == 9:
                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[139, 139, 473, 273])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                            "confidence"] < 0.85:
                            tupo_state = 0
                            failed = 0
                            turefaile = 0
                            print('最后一次已经打过')

                        path = R.img("确认.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None:
                            # print("中心坐标:", res["center_x"], res["center_y"])
                            # print("相似度:", res["confidence"])
                            # print("在屏幕中的范围:", res["rect"])
                            if res["confidence"] > 0.8:
                                x = random.randint(res["center_x"] - 2, res["center_x"] + 2)
                                y = res["center_y"]
                                action.click(x, y)
                                print('点击确定')
                                turefaile = 0
                                tupo_state = 0
                                failed = 0
                                shuaxinone = 0

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("突破标志.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.9 and res2 is not None and res2[
                            "confidence"] < 0.85 and turefaile == 1:
                            print('真失败了')
                            current_time = time.time()
                            print(current_time - last_refresh_time)
                            if shuaxinone == 1:
                                path = R.img("刷新.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 15, res["center_x"] + 15)
                                        y = random.randint(res["center_y"] - 5, res["center_y"] + 5)
                                        action.click(x, y)

                            if current_time - last_refresh_time >= 300:
                                path = R.img("刷新.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 15, res["center_x"] + 15)
                                        y = random.randint(res["center_y"] - 5, res["center_y"] + 5)
                                        action.click(x, y)

                    path = R.img("突破页面.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None and res["confidence"] > 0.8:
                        path = R.img("po.png")  # 这里替换为你的图片地址
                        res = FindImages.find_template(path, rect=[807, 412, 1140, 543])
                        path = R.img("进攻.png")  # 这里替换为你的图片地址
                        res2 = FindImages.find(path)
                        if res is not None and res["confidence"] > 0.80 and res2 is not None and res2[
                            "confidence"] < 0.85:
                            print('突破9成功')
                            current_time = time.time()
                            print(current_time - last_refresh_time)
                            if shuaxinone == 1:
                                path = R.img("刷新.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 15, res["center_x"] + 15)
                                        y = random.randint(res["center_y"] - 5, res["center_y"] + 5)
                                        action.click(x, y)


                            if current_time - last_refresh_time >= 300:
                                path = R.img("刷新.png")  # 这里替换为你的图片地址
                                res = FindImages.find(path)
                                if res is not None:
                                    if res["confidence"] > 0.8:
                                        x = random.randint(res["center_x"] - 15, res["center_x"] + 15)
                                        y = random.randint(res["center_y"] - 5, res["center_y"] + 5)
                                        action.click(x, y)
                                else:
                                    print('找不到刷新')

    if tansuo_state == 2:  # 突破探索模式

        print('准备k28')


        bossStop = 0;  # 初始化boss滑动
        # time.sleep(1)
        print('已经点击', baonum, '次宝箱')
        print('不是探索页面')
        path = R.img("外宝箱2.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            if res["confidence"] > 0.8:
                print('有宝箱')
                path = R.img("突破退出.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    if res["confidence"] > 0.8:
                        print('有退出按钮')
                        action.click(res["center_x"], res["center_y"])
                        time.sleep(1)
                        path = R.img("外宝箱2.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None:
                            if res["confidence"] > 0.8:
                                print('捡宝箱')
                                action.click(res["center_x"], res["center_y"])
                                baonum = baonum + 1

                else:
                    path = R.img("外宝箱.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None:
                        if res["confidence"] > 0.8:
                            action.click(res["center_x"], res["center_y"])
                            baonum = baonum + 1
                            print('已经点击', baonum, '次宝箱')
        if res is  None or res["confidence"] < 0.8:
            print('没有宝箱')
            if number >= fitguainum:
                print('打够', number, '次小怪了')
                path = R.img("突破退出.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    if res["confidence"] > 0.8:
                        action.click(res["center_x"], res["center_y"])
                        time.sleep(1)
                path = R.img("庭院突破.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    if res["confidence"] > 0.8:
                            tansuo_state = 1  # 进入突破状态
                            print('进入突破状态1')

            path = R.img("探索.png")  # 这里替换为你的图片地址
            res = FindImages.find(path)
            if res is not None:
                # print("中心坐标:", res["center_x"], res["center_y"])
                # print("相似度:", res["confidence"])
                # print("在屏幕中的范围:", res["rect"])
                if res["confidence"] > 0.8and number < fitguainum and tansuo_state == 2:
                    x = random.randint(900, 986)
                    y = random.randint(523, 553)
                    action.click(x, y)

            path = R.img("kun28.png")  # 这里替换为你的图片地址
            res = FindImages.find(path)
            if res is not None:
               print('判断K28，已打小怪次数', number)
            if res["confidence"] > 0.80 and number < fitguainum and tansuo_state == 2:
                print('没到这一步吗')
                x = random.randint(res["center_x"] - 53, res["center_x"] + 88)
                y = random.randint(res["center_y"], res["center_y"] + 79)
                action.click(x, y)
                bossStop = 0
                print('下二步')
            print('没有宝箱结束')

        path = R.img("樱饼.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                y = res["center_y"]
                print('在小怪页面')

                path = R.img("boss.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)

                path = R.img("小怪.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)

                path = R.img("内宝箱.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        path = R.img("退出.png")  # 这里替换为你的图片地址
                        res = FindImages.find(path)
                        if res is not None:
                            print("中心坐标:", res["center_x"], res["center_y"])
                            print("相似度:", res["confidence"])
                            print("在屏幕中的范围:", res["rect"])
                            if res["confidence"] > 0.8:
                                x = random.randint(res["center_x"] - 3, res["center_x"] + 3)
                                y = random.randint(res["center_y"] - 3, res["center_y"] + 3)
                                action.click(x, y)

                path = R.img("确认.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    # print("中心坐标:", res["center_x"], res["center_y"])
                    # print("相似度:", res["confidence"])
                    # print("在屏幕中的范围:", res["rect"])
                    if res["confidence"] > 0.8:
                        x = random.randint(res["center_x"] - 5, res["center_x"] + 5)
                        y = res["center_y"]
                        action.click(x, y)

                path = R.img("小怪.png")  # 这里替换为你的图片地址
                res1 = FindImages.find(path)
                path = R.img("boss.png")  # 这里替换为你的图片地址
                res2 = FindImages.find(path)
                path = R.img("内宝箱.png")  # 这里替换为你的图片地址
                res3 = FindImages.find(path)
                path = R.img("确认.png")  # 这里替换为你的图片地址
                res4 = FindImages.find(path)
                path = R.img("自动.png")  # 这里替换为你的图片地址
                res5 = FindImages.find(path)
                if res1["confidence"] < 0.8 and res2["confidence"] < 0.8 and res3["confidence"] < 0.8 and res4[
                    "confidence"] < 0.8 and res5["confidence"] < 0.8:
                    print('该滑动了')
                    # 起始点、控制点和结束点
                    x1 = random.randint(1000, 1200)
                    y1 = random.randint(150, 180)

                    x2 = random.randint(600, 800)
                    y2 = random.randint(200, 400)

                    x3 = random.randint(200, 400)
                    y3 = random.randint(100, 300)
                    print('起始坐标', x1, y1)
                    print('控制坐标', x2, y2)
                    print('结束坐标', x3, y3)

                    start_point = np.array([x1, y1])
                    control_point = np.array([x2, y2])
                    end_point = np.array([x3, y3])

                    # 生成一系列参数值
                    num = random.randint(10, 50)
                    t_values = np.linspace(0, 1, num=num)
                    print('贝塞尔num', num)

                    # 计算贝塞尔曲线上的点
                    points = [bezier(start_point, control_point, end_point, t) for t in t_values]

                    # 发送鼠标左键按下消息
                    action.Touch.down(x1, y1)
                    # 遍历贝塞尔曲线上的点
                    for point in points:
                        print('到这里吗？')
                        x, y = int(point[0]), int(point[1])
                        # 发送鼠标移动消息
                        action.Touch.move(x, y)
                    # 发送鼠标左键释放消息
                    action.Touch.up(x3, y3)
                    sainum = sainum + 1

                if sainum >= 3:
                    print('滑动超过3次，退出')
                    path = R.img("退出.png")  # 这里替换为你的图片地址
                    res = FindImages.find(path)
                    if res is not None:
                        # print("中心坐标:", res["center_x"], res["center_y"])
                        # print("相似度:", res["confidence"])
                        # print("在屏幕中的范围:", res["rect"])
                        if res["confidence"] > 0.8:
                            x = random.randint(res["center_x"] - 3, res["center_x"] + 3)
                            y = random.randint(res["center_y"] - 3, res["center_y"] + 3)
                            action.click(x, y)

        path = R.img("悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("悬赏中心坐标:", res["center_x"], res["center_y"])
            print("悬赏相似度:", res["confidence"])
            print("悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x悬赏相似度:", res["confidence"])
                    print("x悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])

        path = R.img("现世悬赏.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            print("现世悬赏中心坐标:", res["center_x"], res["center_y"])
            print("现世悬赏相似度:", res["confidence"])
            print("现世悬赏在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                path = R.img("x悬赏.png")  # 这里替换为你的图片地址
                res = FindImages.find(path)
                if res is not None:
                    print("x现世悬赏中心坐标:", res["center_x"], res["center_y"])
                    print("x现世悬赏相似度:", res["confidence"])
                    print("x现世悬赏在屏幕中的范围:", res["rect"])
                    action.click(res["center_x"], res["center_y"])

        path = R.img("结算1.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                sainum = 0
                print('结算1点击x=', x, 'y=', y)
                number = number + 1;
                print('number=', number);

        path = R.img("结算2.png")  # 这里替换为你的图片地址
        res = FindImages.find(path)
        if res is not None:
            # print("中心坐标:", res["center_x"], res["center_y"])
            # print("相似度:", res["confidence"])
            # print("在屏幕中的范围:", res["rect"])
            if res["confidence"] > 0.8:
                # 生成符合指定范围的正态分布的 x 和 y 坐标
                mu, sigma = 1200, 30  # 均值和标准差
                x = np.random.normal(mu, sigma)
                while x < 1144 or x > 1256:
                    x = np.random.normal(mu, sigma)

                mu, sigma = 437, 100  # 均值和标准差
                y = np.random.normal(mu, sigma)
                while y < 185 or y > 689:
                    y = np.random.normal(mu, sigma)
                action.click(x, y)
                print('结算2点击x=', x, 'y=', y)









































