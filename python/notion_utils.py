import json


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

def Notion_filter_offering_a_reward_task_list(res, reward_flag="招募中"):
    try:
        # print('len(res_list)', len(res_list))
        # print('res[0]', res[0])  # ["properties"]["悬赏状态"]["select"]["name"]
        task_list = [item["properties"]["悬赏名称"]["title"][0]["plain_text"] 
                        for item in res 
                            if item["properties"]["悬赏状态"]["select"]["name"] == "招募中"]
        return task_list
    except Exception as e:
        raise Exception 

def _deal_with_properties_rich_text(dict_, field="任务说明"):
    """
    处理富文本可能为空的情况
      'properties': {
        '任务说明': {'id': 'Bzg%40', 'rich_text': [], 'type': 'rich_text'},
    """
    if len(dict_["properties"][field]["rich_text"]) == 0:
        return "暂无【"+str(field)+"】，请到 Notion 查看。"
    else: 
        return dict_["properties"][field]["rich_text"][0]["plain_text"]

def _deal_with_properties_title(dict_, field="悬赏名称"):
    """
    处理标题可能为空的情况
      'properties': {
        '悬赏名称': {
            'title': [{'annotations': { .. },
                        'plain_text': 'Web3 PBL共学小组招募！',
    """
    if len(dict_["properties"][field]["title"]) == 0:
        return "暂无【"+str(field)+"】，请到 Notion 查看。"
    else: 
        return dict_["properties"][field]["title"][0]["plain_text"]

def _deal_with_properties_rollup(dict_, field):
    """ 处理 rollup 可能为空的情况 
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
    if len(dict_["properties"][field]["rollup"]["array"][0]["rich_text"]) == 0:
        return None
    else:
        li = dict_["properties"][field]["rollup"]["array"]
        return "; ".join([item["rich_text"][0]["plain_text"] for item in li])




def Notion_filter_task_detail(res, new_task):
    # new_task = '【治理公会】协调小组重启招募'
    try:
        task_list = [item for item in res 
                        if item["properties"]["悬赏名称"]["title"][0]["plain_text"]  == new_task]
        
        name        = _deal_with_properties_title(task_list[0], )
        description = _deal_with_properties_rich_text(task_list[0], )
        recruit_ddl = _deal_with_properties_rich_text(task_list[0], "招募截止时间")
        reward      = _deal_with_properties_rich_text(task_list[0], "贡献报酬")
        contact_dis = _deal_with_properties_rollup(task_list[0], "联络方式：Discord")
        contact_wx  = _deal_with_properties_rollup(task_list[0], "联络方式：微信")
        url         =  task_list[0]["url"]
        return (name, description, recruit_ddl, reward, contact_dis, contact_wx, url)

    except Exception as e:
        raise Exception("Notion form field has changed, pls check it.")

