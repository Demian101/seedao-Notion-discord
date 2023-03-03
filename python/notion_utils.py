import time
from pprint import pprint

"""
json_data = [{
      "archived": false, 
      "properties": {
        "悬赏状态": {
          "id": "ArpA", 
          "select": {
            "color": "yellow", "id": "2d5c85be-12ec-4a41-89ab-3cfd82a6a75b", 
            "name": "招募中"}
          }
        }, 
        "url": "https://www.notion.so/e9ee03abe3d5440ba6ba7476a923d930"
    }, 
    {
      "archived": false, 
      "properties": {
        "悬赏状态": {
          "id": "ArpA", 
          "select": {
            "color": "yellow", 
            "id": "2d5c85be-12ec-4a41-89ab-3cfd82a6a75b", 
            "name": "招募中"
          }
        }
      }, 
      "url": "https://www.notion.so/e9ee03abe3d5440ba6ba7476a923d930"
    }, ]
"""
# json_data = [{"archived": false, "properties": {"悬赏状态": {"id": "ArpA", "select": {"color": "yellow", "id": "2d5c85be-12ec-4a41-89ab-3cfd82a6a75b", "name": "招募中"}}}, "url": "https://www.notion.so/e9ee03abe3d5440ba6ba7476a923d930"}, {"archived": false, "properties": {"悬赏状态": {"id": "ArpA", "select": {"color": "yellow", "id": "2d5c85be-12ec-4a41-89ab-3cfd82a6a75b", "name": "招募中"}}}, "url": "https://www.notion.so/e9ee03abe3d5440ba6ba7476a923d930"}]

def fetch_with_retry(retry_function, retry_limit=3, ):
    print('fetch_with_retry', retry_function)
    retry_count = 0
    while True:
        try:
            retry_function()
            break
            
        except Exception as e:
            retry_count += 1
            if retry_count > retry_limit:
                raise Exception  # Exception("Retry limit exceeded")
            print(str(retry_function.__name__)+" failed, retrying in 1 seconds...")
            time.sleep(1)


def Notion_filter_offering_a_reward_task_list(res, reward_flag="招募中"):
    """ 获取所有 “招募中” 的 [task, task2, task3, ... ] """
    try:
        li_res = Notion_filter_offering_all_task_list(res, )
        return [i["task"] for i in li_res]
            
    except Exception as e:
        raise Exception 

def Notion_filter_offering_all_task_list(res, reward_flag="招募中"):
    try:
        li_res = []
        for item in res :
            di = {}
            # print("item....", item)
            if len(item["properties"]["悬赏名称"]["title"]) == 0 or item["properties"]["悬赏状态"]["select"] is None:
                continue

            if item["properties"]["悬赏状态"]["select"]["name"] == reward_flag:
                #if len(item["properties"]["悬赏类型"]["multi_select"]) == 0:
                #    di['type'] = ""
                #else: 
                #    li = item["properties"]["悬赏类型"]["multi_select"]
                #    di['type'] = ", ".join([item["name"] for item in li])
                di['type'] = _deal_with_properties_multi_select(item,)

                #title_lis = item["properties"]["悬赏名称"]["title"]
                #di['task'] = "".join([i["plain_text"] for i in title_lis])
                di['task'] = _deal_with_properties_title(item,)

                di['url']  = item["url"]
                li_res.append(di)
        # print("li_res", li_res)
        return li_res
    except Exception as e:
        raise Exception 

def _deal_with_properties_multi_select(dict_, field="悬赏类型"):
    if len(dict_["properties"]["悬赏类型"]["multi_select"]) == 0:
        return ""
    else: 
        li = dict_["properties"]["悬赏类型"]["multi_select"]
        return ", ".join([i["name"] for i in li])

def _deal_with_properties_rich_text(dict_, field="任务说明"):
    """
    处理富文本可能为空的情况
      'properties': {
        '任务说明': {'id': 'Bzg%40', 'rich_text': [], 'type': 'rich_text'},

    '任务说明': {
      'rich_text': [
          { 
            'type': 'text', 
            'text': {'content': '我们希望...', 'link': None}, 
            'annotations': "xx", 
            'plain_text': '我们希望通过城市联络人计划，来实现SeeDAO在物理世界的全球连接。这种连接不是基于一个个物理空间，而是基于空间里的人。——SeeDAO的城市联络人在哪里，SeeDAO的线下据点就在哪里。来成为这张大航海世界地图的连接者吧！\n\nhttps://mirror.xyz/seedao.eth/qLGgLUlYGwXK9xGgENTeviePIuZmOfc7gyPO7z0Dsxg', 'href': None
          }
        ]
    },
    """
    if len(dict_["properties"][field]["rich_text"]) == 0:
        return ""
    else: 
        res_list = dict_["properties"][field]["rich_text"] # a list
        return "".join([i["plain_text"] for i in res_list])

def _deal_with_properties_title(dict_, field="悬赏名称"):
    """
    处理标题可能为空的情况
      'properties': {
        '悬赏名称': {
            'title': [{'annotations': { .. },
                        'plain_text': 'Web3 PBL共学小组招募！',

    ...............

    {'悬赏名称': 
      {'id': 'title',
        'title': [{'annotations': {'bold': False,
                                  'code': False,
                                  'color': 'default',
                                  'italic': False,
                                  'strikethrough': False,
                                  'underline': False},
                  'href': None,
                  'plain_text': '【新手任务】',
                  'text': {'content': '【新手任务】', 'link': None},
                  'type': 'text'},
                  {'annotations': {'bold': True,
                                  'code': False,
                                  'color': 'default',
                                  'italic': False,
                                  'strikethrough': False,
                                  'underline': False},
                  'href': None,
                  'plain_text': 'SeeDAO口述史项目招募采访者！',
                  'text': {'content': 'SeeDAO口述史项目招募采访者！', 'link': None},
                  'type': 'text'}],
        'type': 'title'}}
    """
    if len(dict_["properties"][field]["title"]) == 0:
        return ""
    else:
        title_lis = dict_["properties"][field]["title"]
        return "".join([i["plain_text"] for i in title_lis])



def _deal_with_properties_rollup(dict_, field):
    """ 处理 rollup（联系人） 可能为空的情况 
    'properties': {
   '联络方式：Discord': {
      'id': 'uSj%7D',
      'rollup': {
          'array': [
            {
              'rich_text': [{
                  'plain_text': '栗子#8207',
                  'type': 'text'}],
              'type': 'rich_text'
            },
            {
              'rich_text': [{
                'plain_text': 'Fivea#9602',
                'type': 'text'}],
              'type': 'rich_text'
            }],
        'function': 'show_original', 
        'type': 'array'
      },
     'type': 'rollup'
    },
   '联络方式：微信': {
      'id': '%40kmc',
      'rollup': {
        'array': [{
          'rich_text': [], 'type': 'rich_text'
       }],
       'function': 'show_original',
       'type': 'array'
     },
     'type': 'rollup'
   },
    """
    if len(dict_["properties"][field]["rollup"]["array"]) == 0:
        return ""
    if len(dict_["properties"][field]["rollup"]["array"][0]["rich_text"]) == 0:
        return ""
    else:
        li = dict_["properties"][field]["rollup"]["array"]
        return "; ".join([item["rich_text"][0]["plain_text"] for item in li])


def Notion_filter_task_detail(res, new_task):
    # new_task = '【治理公会】协调小组重启招募'
    try:
        # 根据任务名称进行筛选
        for item in res:
            if _deal_with_properties_title(item, "悬赏名称")  == new_task:                        
                btype       = _deal_with_properties_multi_select(item, "悬赏类型")
                name        = _deal_with_properties_title(item, )
                description = _deal_with_properties_rich_text(item, )
                recruit_ddl = _deal_with_properties_rich_text(item, "招募截止时间")
                reward      = _deal_with_properties_rich_text(item, "贡献报酬")
                contact_dis = _deal_with_properties_rollup(item, "联络方式：Discord")
                contact_wx  = _deal_with_properties_rollup(item, "联络方式：微信")
                url         =  item["url"]
                return (btype, name, description, recruit_ddl, reward, contact_dis, contact_wx, url)

    except Exception as e:
        raise Exception("Notion form field has changed, pls check it.")

