#   -*- coding = utf8 -*-
import requests
import urllib.parse
import bs4


class Crawler(object):
    # 定义爬取类
    def __init__(self, name):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        self.cookies = ""
        self.result = {}
        self.instance = name
        self._get_result_id = 0  # 定义一个私有变量来存储 get_result_id 的值

    def update_headers(self, new_headers: dict):
        self.headers.update(new_headers)

    # 设置cookies
    def set_cookie(self, cookie):
        self.cookies = cookie

    # 设置headers
    def set_header(self, header):
        self.headers = header

    # 发送请求
    def get(self, url) -> int:
        # 由于使用私有变量来存储 get_result_id 的值，函数首次判断功能无意义
        # sentinel = getattr(self.get, 'has_run', False)
        # if sentinel:
        #     print("非首次次运行")
        # else:
        #     # setattr(self.get, 'has_run', True)
        #     self.get.__dict__["has_run"] = True
        #     print("首次运行")
        #     result_id = 1
        try:
            if self.headers.get('Cookie') is None:  # 更新cookie
                self.headers.update({"Cookie": self.cookies})
            r = requests.get(url, headers=self.headers)
            tmp_id = self._get_result_id
            self._get_result_id += 1
            self.result.update({tmp_id: r})
            return tmp_id
        except Exception as e:
            print(e)
            return None  # 返回一个默认值
        finally:
            pass

    def get_result_id(self, pr=False):
        """返回私有变量 _result_id 的值"""
        if pr:
            print("私有变量 _result_idself得值为：", self._get_result_id)
            return self._get_result_id
        return self._get_result_id

    def set_result_id(self, value=None):
        """修改私有变量 _result_id 的值"""
        temp = self._get_result_id
        try:
            if value is None:
                self._get_result_id = int(input("请输入数字："))
            else:
                self._get_result_id = int(value)
        except Exception as e:
            print(e)
            self._get_result_id = temp
            print("参数错误，result_id未更改")
        finally:
            pass

    # 查看响应头
    def view_resHeader(self, result_id) -> str:
        return_text = ''
        response = self.result[result_id]
        # 解析URL
        url = urllib.parse.urlparse(response.url)
        # return_text += "\n".join([f"Domain: {url.netloc}", f"URL: {response.url}", f"Path: {url.path}"])

        # 遍历并打印所有请求头
        headers = response.headers
        return_text += "\n".join([f"{key}: {value}" for key, value in headers.items()])
        return return_text

    # 查看请求头
    def view_reqHeader(self, result_id) -> str:
        return_text = ''
        response = self.result[result_id]
        # 解析URL
        url = urllib.parse.urlparse(response.url)

        # 遍历并打印所有请求头
        headers = response.request.headers
        return_text += "\n".join([f"{key}: {value}" for key, value in headers.items()])
        return return_text

    # 判断返回是否正常
    def is_normal(self, r):
        if r.status_code == 200:
            print("请求正常")
        else:
            print("请求异常")

    def view_status_code(self, result_id) -> str:
        response = self.result[result_id]
        # 获取状态码
        status_code = response.status_code
        # 打印状态码
        print(f"Status Code: {status_code}: ", end='')

        values = {200: "请求成功", 301: "请求的资源已永久移动到新位置", 302: "请求的资源临时移动到新位置",
                  303: "请求的资源可在其他位置获得", 304: "请求的资源没有更改", 307: "请求的资源临时移动到新位置",
                  400: "请求是非法的，服务器无法理解", 401: "当前请求需要用户验证", 403: "服务器拒绝处理此请求",
                  404: "请求的资源不存在", 500: "服务器发生内部错误，无法完成请求", 502: "网关错误",
                  "else": "未知状态码"}
        for key, value in values.items():
            if key == status_code:
                print(value)
                return value
        print(values["else"])
        return values["else"]

    def view_resBody(self, result_id) -> str:
        html = self.result[result_id].content.decode('utf-8')
        return bs4.BeautifulSoup(html, 'html.parser').prettify()


if __name__ == '__main__':
    s = Crawler(name="s")
    s.get(url="http://baidu.com")
    print(s.result)
    s.view_status_code(0)
    print(s.view_resBody(0))
