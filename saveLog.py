import requests
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED,as_completed
import random
import json

executor = ThreadPoolExecutor(max_workers=10)


def save_log(timestamp: int, skill_id: str, eventName: str, eventType: str):
    url = 'http://172.16.222.253:7776/aiwarning/api/vas/v1/analysisResult'

    data = {
        "deviceId": "69583104-a258-45f1-8502-18db6195db75",
        "domain": "default",
        "skillId": skill_id,
        "taskId": "55edcee7-3785-493f-b046-b912dff5ba4a",
        "timestamp": timestamp,
        "events":
            [
                {
                    "compliance": True,
                    "eventName": eventName,
                    "eventType": eventType,
                    "eventInfo":
                        {
                            "type": "int",
                            "value": "10"
                        }
                }
            ],
        "annotatedImg": "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"
    }

    try:
        json_str = json.dumps(data)
        r = requests.post(url, data=json_str)
        print(r.json())
    except Exception as e:
        print(repr(e))


class Event:
    def __init__(self, eventType: str, eventName: str):
        self.eventType = eventType
        self.eventName = eventName


class Skill:
    def __init__(self, skillID: str, eventList: list):
        self.skillID = skillID
        self.eventList = eventList


class Parameter:
    def __init__(self, timestamp: int, skillID: str, eventType: str, eventName: str):
        self.timestamp = timestamp
        self.skillID = skillID
        self.eventType = eventType
        self.eventName = eventName

    pass


skillList = [Skill("26", [Event("ycjw", "引车就位"), Event("aqfh", "安全防护"), Event("aqjc", "安全检查"), Event("xqqr", "卸前确认"),
                          Event("ypjx", "油品接卸"), Event("jxjh", "接卸监护"), Event("jhys", "进货验收"), Event("xhcl", "卸后处理")]),
             Skill("25", [Event("smoke", "吸烟"), Event("phone", "打电话")]),
             Skill("24", [Event("nightCar", "夜间来车")]),
             Skill("23", [Event("rltjIn", "便利店人流统计-进"), Event("rltjOut", "便利店人流统计-出")]),
             Skill("22", [Event("pcjy", "私家车自主加油")])]

if __name__ == '__main__':
    # timetstamp = 123123
    # skill = random.choice(skillList)
    # event = random.choice(skill.eventList)
    # save_log(timetstamp, skill.skillID, event.eventName, event.eventType)
    timetstamp = 1618467895

    params = []
    for i in range(1000):
        timetstamp -= i * 1800
        skill = random.choice(skillList)
        event = random.choice(skill.eventList)
        for _ in range(10):
            params.append(Parameter(timetstamp, skill.skillID, event.eventType, event.eventName))

    all_task = [executor.submit(save_log, param.timestamp, param.skillID, param.eventName, param.eventType) for param
                in params]
    print(len(all_task))
    for future in as_completed(all_task):
        data = future.result()
        # print("in main: save log {}s success".format(data))

    wait(all_task, return_when=ALL_COMPLETED)

    # executor.submit(save_log, (timetstamp, skill.skillID, event.eventName, event.eventType))
