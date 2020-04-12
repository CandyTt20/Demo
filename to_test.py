from pytodoist.api import TodoistAPI
api = TodoistAPI()
response = api.login('zengwennjnu@163.com', 'zxcv1234')
user_info = response.json()
user_api_token = user_info['token']
response = api.get_productivity_stats(user_api_token)
completed_tasks = response.json()
print(completed_tasks)