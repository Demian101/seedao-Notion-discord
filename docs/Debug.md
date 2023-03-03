cd  ~Dev/seedao-Notion-discord/python

```
import os
import pickle


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



li = load_or_create_task_list()
li.remove("一起构建程序员的未来，打造ProgrammerX平台")

update_task_list(li)
```

