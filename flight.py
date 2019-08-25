#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   flight.py
@Time    :   2019/08/24 20:18:02
@Author  :   Xu Xiangyu
'''
# here put the import lib
import requests
import time


s = requests.Session()


class Flight():

    # 构造函数
    def __init__(self, src, dest, date):
        self.src = src
        self.dest = dest
        self.date = date
        self.citycode = {'阿勒泰': 'AAT', '沙市': 'SHS', '西安': 'XIY', '安庆': 'AQG', '秦皇岛': 'SHP', '康定': 'KGT', '吐鲁番': 'TLQ', '榆林': 'UYN', '三亚': 'SYX', '池州': 'JUH', '石河子': 'SHF', '沈阳': 'SHE', '上海浦东': 'PVG', '上海虹桥': 'SHA', '延吉': 'YNJ', '延安': 'ENY', '烟台': 'YNT', '思茅': 'SYM', '盐城': 'YNZ', '南宁': 'NNG', '马尼拉': 'MNL', '万州':
                         'WXN', '银川': 'INC', '新加坡': 'SIN', '保山': 'BSD', '淮安': 'HIA', '临汾': 'LFQ', '大连': 'DLC', '长春': 'CGQ', '郑州': 'CGO', '雅加达': 'CGK', '衢州': 'JUZ', '吉隆坡': 'KUL', '南阳': 'NNY', '常德': 'CGD', '锦州': 'JNZ', '大理': 'DLU', '林芝': 'LZY', '佛山': 'FUO', '兴义': 'ACX', '贵阳': 'KWE', '合肥': 'HFE', '泸州': 'LZO', '济宁': 'JNG', '兰州': 'LHW', '杭州': 'HGH', '伦敦': 'LHR', '深圳': 'SZX', '建三江': 'JSJ', '敦煌': 'DNH', '攀枝花': 'PZI', '厦门': 'XMN', '成都': 'CTU', '南充': 'NAO', '石家庄': 'SJW', '恩施': 'ENH', '桂林': 'KWL', '札幌': 'CTS', '阜阳': 'FUG', '广汉': 'GHN', '海拉尔': 'HLD', '梅县': 'MXZ', '天水': 'THQ', '乌兰浩特': 'HLH', '乌海': 'WUA', '南京': 'NKG', '义乌': 'YIW', '重庆': 'CKG', '武汉': 'WUH', '武夷山': 'WUS', '洛阳': 'LYA', '忻州': 'WUT', '太原': 'TYN', '梧州': 'WUZ', '临沂': 'LYI', '连云港': 'LYG', '毕节': 'BFJ', '无锡': 'WUX', '襄阳': 'XFN', '百色': 'AEB', '哈密': 'HMI', '九寨沟': 'JZH', '约翰内斯堡': 'JNB', '佳木斯': 'JMU', '布尔津': 'KJI', '常州': 'CZX', '安顺': 'AVA', '黄山': 'TXN', '日照': 'RIZ', '东京羽田': 'HND', '柳州': 'LZH', '丽江': 'LJG', '汉中': 'HZG', '广元': 'GYS', '六盘山': 'GYU', '黎平': 'HZH', '大阪': 'KIX', '绵阳': 'MIG', '北海': 'BHY', '怀化': 'HJJ', '泉州': 'JJN', '朝阳': 'CHG', '中国香港': 'HKG', '通辽': 'TGO', '漠河': 'OHE', '迪庆': 'DIG', '揭阳': 'SWA', '黄岩': 'HYN', '鸡西': 'JXA', '巴彦淖尔':
                         'RLK', '南昌': 'KHN', '荔波': 'LLB', '长治': 'CIH', '宜昌': 'YIH', '张家界': 'DYG', '赤峰': 'CIF', '永州': 'LLF', '喀什': 'KHG', '富蕴': 'FYN', '普吉岛': 'HKT', '拉萨': 'LXA', '伊宁': 'YIN', '西昌': 'XIC', '抚远': 'FYJ', '宜春': 'YIC', '那拉提': 'NLT', '伊尔施': 'YIE', '日喀则': 'RKZ', '锡林浩特': 'XIL', '邵阳': 'WGN', '鄂尔多斯': 'DSN', '珠海': 'ZUH', '舟山': 'HSN', '景洪': 'JHG', '中国澳门': 'MFM', '昭通': 'ZAT', '徐州': 'XUZ', '塔城': 'TCG', '赣州': 'KOW', '达州': 'DAX', '金边': 'PNH', '格尔木': 'GOQ', '大同': 'DAT', '吉安': 'KNC', '曼谷': 'BKK', '名古屋': 'NGO', '临沧': 'LNJ', '阿坝': 'AHJ', '巴中': 'BZX', '青岛': 'TAO', '海口': 'HAK', '狮泉河': 'NGQ', '吉林': 'JIL', '河内': 'HAN', '黔江': 'JIQ', '九江': 'JIU', '宁波': 'NGB', '潍坊': 'WEF', '威海': 'WEH', '昆明': 'KMG', '惠州': 'HUZ', '阿克苏': 'AKU', '牡丹江': 'MDG', '满洲里': 'NZH', '铜仁': 'TEN', '松原': 'YSQ', '乌鲁木齐': 'URC', '运城': 'YCU', '五大连池': 'DTU', '十堰': 'WDS', '腾冲': 'TCZ', '天津': 'TSN', '六盘水': 'LPF', '和田': 'HTN', '井冈山': 'JGS', '嘉峪关': 'JGN', '安康': 'AKA', '中国台北': 'TPE', '开罗': 'CAI', '长白山': 'NBS', '遵义茅台': 'WMT', '芭提雅': 'UTP', '乌兰察布': 'UCB', '玉树': 'YUS', '邯郸': 'HDG',
                         '广州': 'CAN', '福州': 'FOC', '呼和浩特': 'HET', '丹东': 'DDG', '库车': 'KCA', '景德镇': 'JDZ', '东京成田': 'NRT', '长沙': 'CSX', '库尔勒': 'KRL', '衡阳': 'HNY', '扬州': 'YTY', '宜宾': 'YBP', '克拉玛依': 'KRY', '黑河': 'HEK', '东营': 'DOY', '通化': 'TNH', '北京': 'PEK', '大庆': 'DQA', '昌都': 'BPX', '龙岩': 'LCX', '芒市': 'LUM', '济南': 'TNA', '庆阳': 'IQN', '齐齐哈尔': 'NDG', '槟城': 'PEN', '且末': 'IQM', '温州': 'WNZ', '芜湖': 'WHU', '湛江': 'ZHA', '哈尔滨': 'HRB', '稻城': 'DCY', '文山': 'WNH', '邢台': 'XNT', '中卫': 'ZHY', '西宁': 'XNN', '首尔': 'ICN', '南通': 'NTG', '河池': 'HCJ', '包头': 'BAV', '琼海': 'BAR'}

    # 获取city和citycode对应信息，因为对应信息是固定的，所以接下来的程序不会调用这个函数，直接使用结果
    def getCityCode():
        headers = {
            'Host': 'shenzhenair.com',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Content-Type': 'application/json; charset=gbk',
            'Origin': 'http://shenzhenair.com',
            'Referer': 'http://shenzhenair.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'AlteonP=A2kGWG9ADgoyTHoPPLOvBQ$$; sign_cookie=cbd3c9736ff0bf3c130f2f42826b79ff; sign_flight=c78cef70795145b09e2fb265a22cc975; CoreSessionId=91f3f08a0b6120fb312cf3c25c881f7e9e8c46d0a8f56e97; _g_sign=527ea3ab9d44a5ad5288df345ed8b1d8; _dx_uzZo5y=1566713130104JnJfQyMH8swGxDQHXID92poDOWkrTeSJ; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%2C%22%24device_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%7D; sajssdk_2015_cross_new_user=1',
        }
        data = {"paat": 'B2C'}
        url = 'http://shenzhenair.com/szair_B2C/getCitys.action?plat=B2C'
        # url = 'http://shenzhenair.com/szair_B2C/getCitys.action'
        r = s.post(url=url, headers=headers, data=data)
        # print(r.status_code)
        # 将city和citycode信息添加到字典
        dit_citycode = {}
        for x in r.json()['cityDto']['cityMap'].values():
            dit_citycode.update({x[0]['fullName']: x[0]['shortName']})
        print(dit_citycode)
        # return dit_citycode

    # 获取referer

    def getindex(self):
        headers = {
            'Cache-Control': 'max-age=0',
            'Host': 'shenzhenair.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'http://shenzhenair.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'JSESSIONID=18CA42A2B2D39F9A06EF50C331EA5C57; AlteonP=A2kGWG9ADgoyTHoPPLOvBQ$$; sign_cookie=cbd3c9736ff0bf3c130f2f42826b79ff; sign_flight=c78cef70795145b09e2fb265a22cc975; CoreSessionId=91f3f08a0b6120fb312cf3c25c881f7e9e8c46d0a8f56e97; _g_sign=527ea3ab9d44a5ad5288df345ed8b1d8; _dx_uzZo5y=1566713130104JnJfQyMH8swGxDQHXID92poDOWkrTeSJ; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%2C%22%24device_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%7D; sajssdk_2015_cross_new_user=1; fromPage=%7BfromPage%3A%22index%22%7D',
        }
        data = {
            'hcType': 'DC',
            'constId': '',
            'type': '单程',
            'orgCity': self.src,
            'orgCityCode': self.citycode.get(self.src),
            'dstCity': self.dest,
            'dstCityCode': self.citycode.get(self.dest),
            'orgDate': self.date,
            'dstDate': self.date,
            'quiz': 'Y',
            'quiz': '1',
        }
        url = 'http://shenzhenair.com/szair_B2C/flightsearch.action'
        r = s.get(url=url, headers=headers, params=data)
        # print(r.text)
        print(r.url)
        return r.url

    # 获取航班信息
    def getfilgth(self):

        # js_url = ['http://shenzhenair.com/szair_B2C/static/js/utils.js?t=1566726', 'http://shenzhenair.com/szair_B2C/static/js/uedjs/uedFlightSearch.js?t=1566726955', 'http://shenzhenair.com/szair_B2C/static/js/utils.js?t=1566726']

        referer = Flight.getindex(self)
        headers = {
            'Host': 'shenzhenair.com',
            'Connection': 'keep-alive',
            'Content-Length': '148',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://shenzhenair.com',
            'Referer': referer,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'JSESSIONID=18CA42A2B2D39F9A06EF50C331EA5C57; AlteonP=A2kGWG9ADgoyTHoPPLOvBQ$$; sign_cookie=cbd3c9736ff0bf3c130f2f42826b79ff; sign_flight=c78cef70795145b09e2fb265a22cc975; CoreSessionId=91f3f08a0b6120fb312cf3c25c881f7e9e8c46d0a8f56e97; _g_sign=527ea3ab9d44a5ad5288df345ed8b1d8; _dx_uzZo5y=1566713130104JnJfQyMH8swGxDQHXID92poDOWkrTeSJ; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%2C%22%24device_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%7D; sajssdk_2015_cross_new_user=1; fromPage=%7BfromPage%3A%22index%22%7D; _gscu_1739384231=667131472hw2jy74; _gscbrs_1739384231=1; _gscs_1739384231=66713147hyb4q674|pv:1',
            'Cookie': 'JSESSIONID=EEC4DB8CD292C90E272C84661E27CD54; sign_flight=c78cef70795145b09e2fb265a22cc975; CoreSessionId=91f3f08a0b6120fb312cf3c25c881f7e9e8c46d0a8f56e97; _g_sign=527ea3ab9d44a5ad5288df345ed8b1d8; _dx_uzZo5y=1566713130104JnJfQyMH8swGxDQHXID92poDOWkrTeSJ; sajssdk_2015_cross_new_user=1; _gscu_1739384231=667131472hw2jy74; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%2C%22%24device_id%22%3A%2216cc7612cd8653-05ea7b678a99b3-7373e61-2073600-16cc7612cd9166%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; agbrowser_id=db28187ead1043dcdb1163d3b08f79c7; X-TOKEN=df5a97ea-43ff-4af8-909c-a8c0b38ad546; AlteonP=A/zDcm9ADgp0LCsM103feQ$$; sign_cookie=cbd3c9736ff0bf3c130f2f42826b79ff; fromPage=%7BfromPage%3A%22index%22%7D; _gscbrs_1739384231=1; _gscs_1739384231=66721665reryke74|pv:5',
        }
        data = {
            'condition.orgCityCode': self.citycode.get(self.src),
            'condition.dstCityCode': self.citycode.get(self.dest),
            'condition.hcType': 'DC',
            'condition.orgDate': self.date,
            'condition.dstDate': self.date,
            'condition.constId': ''
        }

        # for js in js_url:
        #     s.get(url=js, headers=headers)

        url = 'http://shenzhenair.com/szair_B2C/flightSearch.action'
        r = s.post(url=url, headers=headers, data=data)
        print(r.status_code)
        # print(r.text)
        return r.json()['flightSearchResult']['flightInfoList']

    # 解析json数据
    def parse(self):
        # 所有航班
        allflight = Flight.getfilgth(self)
        for flightde in allflight:
            flightNo = flightde['flightNo']  # 航班号
            for level in flightde['pageClassInfoMap'].values():  # 航班信息
                seatlist = []
                seatlevel = {'0': '公务舱', '1': '超值公务舱',
                             '2': '舒适经济舱', '3': '经济舱'}
                seatle = seatlevel.get(level['classType'])  # 仓位级别
                # 剩余座位数
                seatno = '大于9' if level['storage'] == 'A' else level['storage']
                price = level['ticketPrice']  # 票价
                seatlist.append(
                    {'仓位': seatle, '座位余数': seatno, '票价': price})
            print({flightNo: seatlist})


if __name__ == "__main__":
    flight = Flight('深圳', '北京', '2019-08-26')
    flight.parse()
