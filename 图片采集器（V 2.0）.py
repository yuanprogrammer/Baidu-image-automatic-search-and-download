# -*- coding: utf-8 -*-
"""
@author: 袁德伟
@age: 20
@Data: 2021

Created on Wed Feb 10 22:28:28 2021
"""

import os
import time
import shutil
import requests

class image_search():
    
    def __init__(self):
        self.quantity = 0 #页数初始化
        self.word = "" #搜索词
        self.file = "" #文件夹名称
        self.headers = {}   #头部信息
        self.all_list = []   #存放图片链接
        self.parameters = [] #存放每页XHR接口的param
        
    def enter(self,word):
        """
        word：SearchWord
        input：quantity(数量),file(文件名)
        """
        self.word = word
        while True:
            try:
                self.quantity = int(input("请输入下载图片数量（如：100张）："))
                if self.quantity <= 0:
                    print("输入错误···请输入正整数······")
                    continue
            except:
                print("输入错误···请输入整数······")
                continue
            else:
                break
        print("="*100)
        while True:
            self.file = input('请输入图片保存的文件夹名称：')
            if os.path.isdir(self.file): #判断是否存在此文件夹
                print("="*100+"\n"+"-"*10+" 已存在此文件夹······请选择以下其中一种功能（输入选项数字）：")
                while True:
                    try:
                        print("-"*10+" 1、覆盖此文件夹"+"\n"+"-"*10+" 2、输入新的文件夹"+"\n"+"-"*10)
                        choose = int(input("请输入选项："))
                        if choose == 1:
                            shutil.rmtree(self.file) #删除文件夹
                            os.mkdir(self.file) #重新创建文件夹
                            break #退出选项输入循环
                        elif choose != 2:
                            print("-"*10+" 没有此选项······请重新输入···"+"\n"+"="*100)
                            continue #重新输入选项
                        break #退出选项输入循环
                    except:
                        print("-"*10+" 没有此选项······请重新输入···"+"\n"+"="*100)
                        continue #重新输入选项
                if choose == 2:
                    continue #重新输入文件名
                break
            else:
                os.mkdir(self.file) #创建文件夹
                print("-"*10,"《{}》文件夹创建成功".format(self.file)) 
                break #退出文件名输入循环
    def header(self):
        """
        save：headers(请求头)
        """
        self.headers = {
            'Accept':'text/plain,*/*;q=0.01',
            'Accept-Encoding':'gzip,deflate,br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Cookie':'BIDUPSID=A68FD2D76FA3FF45AA5C6EA46CA7925E;'\
                     ' PSTM=1608477972;'\
                     ' BAIDUID=A68FD2D76FA3FF4566F115C31D307BEC:FG=1;'\
                     ' __yjs_duid=1_6ebaf3d96f400502b630824bfb9714a71611502629107;'\
                     ' BDSFRCVID_BFESS=o0uOJexroG3VPYneQkOzU6LnW2KKv3JTDYLE8yu9T4VNR5DVgVCoEG0Pt_ZYMak-XolpogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5;' \
                     ' H_BDCLCKID_SF_BFESS=JRAjoK-XJDv8fJ6xhbo_-D60e2T22-usabRt2hcHMPoosIOK0hr_bq_fXp6Ptf7XQbria-LbWfbUoqRHebrheq3334TNtx3p5acmWh5TtUJM_UcXXtQOqqkehh3yKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjo0jGuO3S;' \
                     ' indexPageSugList=%5B%22%E5%8A%A8%E6%BC%AB%22%2C%22%E7%BE%8E%E5%A5%B3%22%2C%22%E5%A4%A9%E7%A9%BA%22%2C%22%E5%A1%AB%E7%A9%BA%22%2C%22%E9%A3%8E%E6%99%AF%22%5D;' \
                     ' BAIDUID_BFESS=EB9A62B156E862D76F644A88F5A49F58:FG=1;' \
                     ' H_PS_PSSID=33423_33582_33272_31253_33338_26350_33264;' \
                     ' delPer=0;' \
                     ' PSINO=7;' \
                     ' BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;' \
                     ' __yjsv5_shitong=1.0_7_7c0247ed33a839441b7da3a103e7d2acb8b7_300_1612765437616_117.181.162.201_685f4449;' \
                     ' BA_HECTOR=21a0a50h0g8kaka4rt1g21nbn0r;' \
                     ' BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm;' \
                     ' userFrom=null;' \
                     ' firstShowTip=1;' \
                     ' cleanHistoryStatus=0;' \
                     ' BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm;' \
                     ' BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
            'Host':'image.baidu.com',
            'Pragma':'no-cache',
            'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1612230450763_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%8A%A8%E6%BC%AB',
            'sec-ch-ua':'"GoogleChrome";v="87","Not;ABrand";v="99","Chromium";v="87"',
            'sec-ch-ua-mobile':'?0',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }
            
    def param(self,page):
        """
        page：页数
        获取每页的parameters表单
        save：parameters
        """
        pn = str(page*30)
        gsm = hex(page*30)[2:]
        TIME = str(int(time.time()*1000))
    
        parameters = {
            'tn':'resultjson_com',
            'logid':'10440797075334463974',
            'ipn':'rj',
            'ct':'201326592',
            'fp':'result',
            'queryWord':self.word, #搜索词
            'cl':'2',
            'lm':'-1',
            'ie':'utf-8',
            'oe':'utf-8',
            'st':'-1',
            'word':self.word, #搜索词
            'face':'0',
            'istype':'2',
            'nc':'1',
            'pn':pn, #页数
            'rn':'30',
            'gsm':gsm, 
            TIME:'',
        }
        self.parameters.append(parameters)
        print("-"*10,"<第{}页>".format(page),"-"*10,"pn：{}".format(parameters['pn']),"-"*10,"gsm：{}".format(parameters['gsm']),"-"*10,"TIME：{}".format(TIME))
    
    def get(self,count):
        """
        return image_list
        """
        try:
            url_get = requests.get(url="https://image.baidu.com/search/acjson?",params=self.parameters[count],headers=self.headers).json()
            time.sleep(0.1)
            for i in range(0,len(url_get['data'])-1):
                self.all_list.append(url_get['data'][i]['thumbURL'])
            print("-"*10,"<第{}页>图片资源成功······".format(count+1),"-"*20)
        except:
            print("-"*10,"第<{}>页数据请求失败···进行下一页···".format(count+1),"-"*15)
        print("="*100)
   
    def save(self):
        count = 1
        for link in range(self.quantity):
            with open(self.file + "\{}.jpg".format(count),'wb') as jpg:
                response = requests.get(self.all_list[link])
                jpg.write(response.content)
                jpg.close()
                print("-"*15,"第 {} 张图片下载成功······".format(count),"-"*15)
                count += 1
        jpg.close()
        print("="*40,"共 {} 张图片下载完毕······".format(self.quantity),"="*40)
        
if __name__ == '__main__':
    print("*"*42," "*20,"*"*36)
    print("*"*42,"当前的版本为：V 3.0  ","*"*36)
    print("*"*42,"Authors：袁···      ","*"*36)
    print("*"*42,"Created on:         ","*"*36)
    print("*"*42,"Wed Feb 10 2021     ","*"*36)
    print("*"*42," "*20,"*"*36)
    while True:
        print("="*100)
        word = input("请输入想要搜索的图片（回车结束）：")
        print("="*100)
        if word == "":
            break
        else:
            user = image_search()
            user.enter(word)
            user.header()
            
            print("="*100)
            if user.quantity%30 == 0:
                num = int(user.quantity/30)
            else:
                num = int(user.quantity/30) + 1

            for i in range(num):
                user.param(i+1)
                # time.sleep(0.5)
                print("-"*10,"正在获取<第{}页>接口······".format(i+1),"-"*20)        
                user.get(i)
            
            print("-"*10,"获取完毕······准备下载图片···","-"*18+"\n"+"="*100)
            time.sleep(3)
            user.save()
            continue