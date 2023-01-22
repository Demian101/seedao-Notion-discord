### Variables: 

```
database_id = 9fde4409e01d4a37bf24b394b2becb36
Notion_API_KEY = (见 .env 环境变量)
```



### Usage:

```bash
$ python3 fetch_notion.py
```



### 目录说明

```python
└── python
    ├── fetch_notion.py         # Notion Web API 交互, 获取 Database 数据
    ├── notion_utils.py         # Notion Json 脏数据处理相关
    ├── send_webhook.py         # Discord 发送 Webhook 接口
    └── notion_task_list.pkl    # 本地存储 "悬赏中" 的 task, 防止意外中止后再次运行时导致重复信息发送
```



### Query Database Response:

```json
 [{'archived': False,
  'cover': {'external': {'url': 'https://www.notion.so/images/page-cover/rijksmuseum_claesz_1628.jpg'},
            'type': 'external'},
  'created_by': {'id': '2891c6f6-1313-4f2e-94b3-8e634dfe976c',
                 'object': 'user'},
  'created_time': '2023-01-13T12:07:00.000Z',
  'icon': None,
  'id': 'b4c8346f-40d5-426a-a083-4eb3561e09e3',
  'last_edited_by': {'id': 'ba18d312-c494-41bc-9235-c7ae058f0715',
                     'object': 'user'},
  'last_edited_time': '2023-01-17T01:31:00.000Z',
  'object': 'page',
  'parent': {'database_id': '73d83a0a-258d-4ac5-afa5-7a997114755a',
             'type': 'database_id'},
  'properties': {'上新时间': {'created_time': '2023-01-13T12:07:00.000Z',
                          'id': 'ThTF',
                          'type': 'created_time'},
                 '任务说明': {'id': 'Bzg%40',
                          'rich_text': [{'annotations': {'bold': False,
                                                         'code': False,
                                                         'color': 'default',
                                                         'italic': False,
                                                         'strikethrough': False,
                                                         'underline': False},
                                         'href': None,
                                         'plain_text': '1、招募一位小伙伴，做一个DC机器人。该DC机器人，连接notion数据库，每当Notion悬赏看板中有任务更新时，就会自动将所有看板上的所有任务同步到DC悬赏酒馆频道中，并标注出相较上次同步所更新的任务。\n'
                                                       '2、提供相对通用的接口服务：A. '
                                                       '如果以后Notion还需要同步其他页面内容到DC，改机器人可以复用或演进支持；B. '
                                                       '可以支持后续自动向八爪鱼同步悬赏信息；C. '
                                                       '期待这个DC机器人可以基于现有DC机器人演进；\n'
                                                       '3、时限1-2周内完成。',
                                         'text': {'content': '1、招募一位小伙伴，做一个DC机器人。该DC机器人，连接notion数据库，每当Notion悬赏看板中有任务更新时，就会自动将所有看板上的所有任务同步到DC悬赏酒馆频道中，并标注出相较上次同步所更新的任务。\n'
                                                             '2、提供相对通用的接口服务：A. '
                                                             '如果以后Notion还需要同步其他页面内容到DC，改机器人可以复用或演进支持；B. '
                                                             '可以支持后续自动向八爪鱼同步悬赏信息；C. '
                                                             '期待这个DC机器人可以基于现有DC机器人演进；\n'
                                                             '3、时限1-2周内完成。',
                                                  'link': None},
                                         'type': 'text'}],
                          'type': 'rich_text'},
                 '悬赏名称': {'id': 'title',
                          'title': [{'annotations': {'bold': False,
                                                     'code': False,
                                                     'color': 'default',
                                                     'italic': False,
                                                     'strikethrough': False,
                                                     'underline': False},
                                     'href': None,
                                     'plain_text': '实现一个自动同步Notion悬赏看板的DC机器人',
                                     'text': {'content': '实现一个自动同步Notion悬赏看板的DC机器人',
                                              'link': None},
                                     'type': 'text'}],
                          'type': 'title'},
                 '悬赏状态': {'id': 'ArpA',
                          'select': {'color': 'orange',
                                     'id': '751da14f-d022-45be-80fe-fcc6073a7f19',
                                     'name': '已认领'},
                          'type': 'select'},
                 '悬赏类型': {'id': 'GJ%3DR',
                          'multi_select': [{'color': 'orange',
                                            'id': 'e10e98a4-5cb3-4e90-8f6b-806b2e6c4e43',
                                            'name': '项目招募'}],
                          'type': 'multi_select'},
                 '技能要求': {'id': '~B%3C%7D',
                          'rich_text': [{'annotations': {'bold': False,
                                                         'code': False,
                                                         'color': 'default',
                                                         'italic': False,
                                                         'strikethrough': False,
                                                         'underline': False},
                                         'href': None,
                                         'plain_text': '具备DC机器人开发能力，最好对SeeDAO现有的DC机器人有了解',
                                         'text': {'content': '具备DC机器人开发能力，最好对SeeDAO现有的DC机器人有了解',
                                                  'link': None},
                                         'type': 'text'}],
                          'type': 'rich_text'},
                 '招募截止时间': {'id': 'iSkG',
                            'rich_text': [{'annotations': {'bold': False,
                                                           'code': False,
                                                           'color': 'default',
                                                           'italic': False,
                                                           'strikethrough': False,
                                                           'underline': False},
                                           'href': None,
                                           'plain_text': '2023年1月31日',
                                           'text': {'content': '2023年1月31日',
                                                    'link': None},
                                           'type': 'text'}],
                            'type': 'rich_text'},
                 '联络方式：Discord': {'id': 'uSj%7D',
                                  'rollup': {'array': [{'rich_text': [{'annotations': {'bold': False,
                                                                                       'code': False,
                                                                                       'color': 'default',
                                                                                       'italic': False,
                                                                                       'strikethrough': False,
                                                                                       'underline': False},
                                                                       'href': None,
                                                                       'plain_text': '栗子#8207',
                                                                       'text': {'content': '栗子#8207',
                                                                                'link': None},
                                                                       'type': 'text'}],
                                                        'type': 'rich_text'}],
                                             'function': 'show_original',
                                             'type': 'array'},
                                  'type': 'rollup'},
                 '联络方式：微信': {'id': '%40kmc',
                             'rollup': {'array': [{'rich_text': [],
                                                   'type': 'rich_text'}],
                                        'function': 'show_original',
                                        'type': 'array'},
                             'type': 'rollup'},
                 '贡献报酬': {'id': '_zm%5E',
                          'rich_text': [{'annotations': {'bold': False,
                                                         'code': False,
                                                         'color': 'default',
                                                         'italic': False,
                                                         'strikethrough': False,
                                                         'underline': False},
                                         'href': None,
                                         'plain_text': '积分：5000-8000 + '
                                                       '酒馆添砖人SBT',
                                         'text': {'content': '积分：5000-8000 + '
                                                             '酒馆添砖人SBT',
                                                  'link': None},
                                         'type': 'text'}],
                          'type': 'rich_text'},
                 '👫 对接人': {'has_more': False,
                           'id': 'ax%5C%5C',
                           'relation': [{'id': '5e854232-cb58-465f-8915-6aff983ecf38'}],
                           'type': 'relation'},
                 '👫 认领人': {'has_more': False,
                           'id': '%5C%5BT%3B',
                           'relation': [{'id': 'af875c01-1dd7-4c96-b508-6cf1d4fd2e9a'}],
                           'type': 'relation'}},
  'url': 'https://www.notion.so/Notion-DC-b4c8346f40d5426aa0834eb3561e09e3'},
]
```



#### 联系方式('type': 'rollup'):

```json
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
```





向 Discord 发消息: 

- webook  chnl_id



WebHook 发送模拟器: https://discohook.org/



Python3 Discord Library : 

- [discord_webhook](https://pypi.org/project/discord-webhook/)



/list   built-in





需求链接 : https://www.notion.so/seedao/148c0fdcaf6849828d26d9b2d1084c98

交互 : 

-  https://github.com/star8ks/dFlower-discord



`http://dflower-discord/index.ts` 



```rust
config()
const CLIENT_ID = process.env.CLIENT_ID

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages
  ]
})


const rest = new REST({ version: '10' }).setToken(process.env.TOKEN)

if (process.env.ENV === 'dev') {
  const agent = new ProxyAgent({
    uri: 'http://127.0.0.1:1087',
  })

  client.rest.setAgent(agent)
  rest.setAgent(agent)
}

client.on('ready', () => {
  console.log(`Logged in as ${client?.user?.tag}!`)
})

```

