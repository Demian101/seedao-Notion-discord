# pip3 install discord-webhook


# import argparse
import time
from notion_utils import Notion_filter_offering_a_reward_task_list, Notion_filter_task_detail
from send_webhook import *
from pprint import pprint
from notion_client import Client
from dotenv import load_dotenv
import os
import pickle


load_dotenv()
notion = Client(auth=os.environ.get("NOTION_KEY"))
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

# print(os.environ.get("NOTION_KEY"))
# print(notion)
# print(DATABASE_ID)


"""
list users
"""
# list_users_response = notion.users.list()
# pprint(list_users_response)

# 查询数据库
# pprint(len(list_dbs['results'])) # 3. task counts. 
"""
 list_dbs[i]['properties']: 
 list_dbs[i]['properties']['任务说明']
"""


def query_database():
    list_dbs = notion.databases.query(
        **{
         "database_id": DATABASE_ID
    })['results']
    # print('-'*50)
    # pprint(list_dbs)
    # print('-'*50)
    return list_dbs

def data_process():
    res = query_database()
    new_task_list = Notion_filter_offering_a_reward_task_list(res)
    task_list = load_or_create_task_list()
    # 求差集，在 new_task_list 中但不在 A 中
    new_item = list(set(new_task_list).difference(set(task_list)))
    print('data_process task_list', new_item)
    retry_count = 0
    for item in new_item:
        name, description, recruit_ddl, reward, contact_dis, contact_wx, url = Notion_filter_task_detail(res, item)
        print('info..', name, url, description[:13], recruit_ddl, reward[:13])
        
        while True:
            try:
                send_to_webhook_url(name, description, recruit_ddl, reward, contact_dis, contact_wx, url)
                break
            except Exception as e:
                if retry_count > 5:
                    raise Exception("Please check the internet connection with Discord.")  # Exception("Retry limit exceeded")
                print(str(send_to_webhook_url.__name__)+" failed, retrying in 1 seconds...")
                time.sleep(1)
        
    task_list += new_item
    update_task_list(task_list)


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

def load_or_create_task_list(file_name="notion_task_list.pkl"):
    """
     加载本地存储的 Notion list 相关信息。
    """
    task_list = []
    if os.path.exists(file_name):
        with open(file_name, 'rb') as file:
            task_list = pickle.load(file)
    else:
        with open(file_name, 'wb') as file:
            pickle.dump(task_list, file)
    return task_list

def update_task_list(task_list, file_name="notion_task_list.pkl"):
    with open(file_name, 'wb') as file:
        pickle.dump(task_list, file)

def keep_calling_fetch():
    """
      检查 Notion 内容更新情况。
      1. Check 
    """
    while True:
        fetch_with_retry(data_process)

        time.sleep(300.0) # Sleep for 5 minutes (300 seconds)
    

def test_load_or_create_task_list():
    task_list = load_or_create_task_list()
    task_list.append("2sdsd")
    update_task_list(task_list)

    task_list = load_or_create_task_list()
    print("task_list", task_list)


if __name__ == "__main__":
    #[test]
    # test_load_or_create_task_list()
    keep_calling_fetch()






"""
Todo : 
 0. Diff 函数：
    每隔 x min fetch() Notion Content
    filter 悬赏状态 === "招募中", 对比现有的并存储到文件；
    - 如果发现是新的： 向 Webhook 发布内容。
    - 旧的： 什么也不做。
 1. Webhook 的构建.

"""