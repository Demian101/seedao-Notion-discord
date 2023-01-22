from fetch_notion import fetch_with_retry 
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os

# Docs： https://pypi.org/project/discord-webhook/

load_dotenv()
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

"""
  多个 url（向多个 channel 推送信息）： webhook_urls = ['webhook url 1', 'webhook url 2']
"""



def send_to_webhook_url(name, description, recruit_ddl, reward, contact_dis, contact_wx, url):
    """ send Webhook to Discord 
      有时候会失败，需要多做几次，直到成功？"""

    content = """
铛铛！有新悬赏发布啦！还不来看看？ @悬赏猎人
悬赏名称：{}
悬赏说明：{}
贡献报酬：{}
截止时间：{}
联系方式#Discord：{}
联系方式#Wechat：{}
任务 Notion 链接：{}
"""
    webhook = DiscordWebhook(
        url=WEBHOOK_URL,
        content=content.format(
            name, description, reward, recruit_ddl, contact_dis, contact_wx, url))
    response = webhook.execute()
    return response

    


# fetch_with_retry(post_content_to_discord)