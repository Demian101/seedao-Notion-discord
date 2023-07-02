import interactions
import time
from fetch_notion import query_database
from notion_utils import Notion_filter_offering_all_task_list, fetch_with_retry
from pprint import pprint
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

slash_command_token = os.environ.get("APP_BOT_TOKEN_FOR_SLASH_CMD")

bot = interactions.Client(token=slash_command_token)

def get_all_task_from_database():
    res = query_database()
    lis_res = Notion_filter_offering_all_task_list(res)
    return lis_res

def retry_request(retry_limit = 5):
    retry_count = 0
    while True:
        try:
            res = get_all_task_from_database()
            return res

        except Exception as e:
            retry_count += 1
            if retry_count > retry_limit:
                raise Exception  # Exception("Retry limit exceeded")
            print("query notion database failed, retrying in 1 seconds...")
            time.sleep(1)

contents = """
铛铛！这是最近发布的 10 个悬赏！快看看吧！
{}
"""


@bot.command(
    name="bounty_list", 
    description="列出最近的 10 条悬赏，如果报错可能是网络问题，请点击右上角 Retry",)

async def my_first_command(ctx: interactions.CommandContext):
    res, li = retry_request(), []
    # print("lis_res: \n", res)

    for i, item in enumerate(res):
        if i >= 10: break
        try:
            # print(item['task'], item['url'])
            s = "【{}】 {}   [{}]".format(item['type'], item['task'], item['url'])
        except: continue
        li.append(s)
    await ctx.defer() # 防止 Discord 3s 不返回就报错
    # 等待 10 秒钟
    await asyncio.sleep(10)
    await ctx.send(contents.format("\n".join(li),))


if __name__ == "__main__":
    bot.start()