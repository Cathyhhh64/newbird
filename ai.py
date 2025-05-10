import json
import requests


def askai(ques):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "stream": False,
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content": ques + "提取其中的主要事件，10个字以内"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-yykagogyehzosyhobgpidtjpcajpnlxauikrxdowyuaawant",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jh=response.text

    data = json.loads(jh)
    # 提取 content 部分
    content = data["choices"][0]["message"]["content"]
    return content
def date(ques):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "stream": False,
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content": ques + "提取其中的主要事件的日期，格式参照：2023-05-23_2023-05-24，不要有具体解释，不要有多余符号"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-yykagogyehzosyhobgpidtjpcajpnlxauikrxdowyuaawant",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jh=response.text

    data = json.loads(jh)
    # 提取 content 部分
    content = data["choices"][0]["message"]["content"]
    return content
def time(ques):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "stream": False,
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content":ques +"。提取其中的主要事件的时间，判断是否有多个时间：如果只有单个时间，输出格式参照：15:30-16:30；如果有多个时间，再判断这几个时间是同一件事需要多个时间段完成，还是几件不同的事情各自的时间段。如果是前者，输出参考格式：15:30-16:30and17:30-18:30。如果是后者，输出参考格式：15:30-16:30：四级考试；17:50-18:49：六级考试。如果没有具体时间，回复‘时间未知’,不要输出日期。"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-yykagogyehzosyhobgpidtjpcajpnlxauikrxdowyuaawant",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jh=response.text

    data = json.loads(jh)
    # 提取 content 部分
    content = data["choices"][0]["message"]["content"]
    return content
def places(ques):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "stream": False,
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.5,
        "top_p": 0.5,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content":ques + "提取其中的主要事件的地点.如果没有具体地点，回复‘地点未知’，如果有多个地点，输出格式参照：四级考试：西土城校区教一楼321室;六级考试：沙河教学楼。不要有*这样的符号，也不要markdown格式"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-yykagogyehzosyhobgpidtjpcajpnlxauikrxdowyuaawant",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jh=response.text

    data = json.loads(jh)
    # 提取 content 部分
    content = data["choices"][0]["message"]["content"]
    return content

def note(ques):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Qwen/Qwen2.5-VL-72B-Instruct",
        "stream": False,
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.5,
        "top_p": 0.5,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content":ques + "提取其中的注意事项，尽量精简.纯文字，不要markdown格式，直接给结果，不要多余的东西"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-yykagogyehzosyhobgpidtjpcajpnlxauikrxdowyuaawant",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jh=response.text

    data = json.loads(jh)
    # 提取 content 部分
    content = data["choices"][0]["message"]["content"]
    return content




try:
    with open('output.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        i=0
        port=[]
        for item in data:
            i=i+1
            title=item["title"]
            dates=item["content"]
            print(item["title"])
            print(item["content"])

            anser=askai(title)
            yearday=date(dates)
            timeday=time(dates)
            place=places(dates)
            notes=note(dates)
            print(anser)
            print(yearday)
            print(timeday)
            print(place)
            record={
                'name':anser,
                'day':yearday,
                'time':timeday,
                'classroom':place,
                'note':notes
            }
            port.append(record)
            if(i>2):break
except FileNotFoundError:
    print("未找到 output.json 文件，请检查文件路径。")
except json.JSONDecodeError:
    print("无法解析 JSON 文件，请确保文件内容是有效的 JSON 格式。")
except KeyError:
    print("JSON 对象中不存在 'title' 字段。")

print(port)

with open('dataoutput.json', 'w', encoding='utf-8') as f:
    json.dump(port, f, ensure_ascii=False, indent=4)