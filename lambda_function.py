# coding: UTF-8
import requests
import json
post_url = 'https://hooks.slack.com/services/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'
    
def test(event, context):
     # slack送信Sample
     requests.post(post_url, data = json.dumps({
            'text': 'event{}\n\n\ncontext{}'.format(event, context), # 投稿するテキスト
            'username': 'github', # 投稿のユーザー名
            'link_names': 1, # メンションを有効にする
            'channel': 'github_to_slack', # チャンネル
            'icon_emoji': 'icon', # アイコン
        }))

def lambda_handler(event, context):
    # TODO implement
    test(event, context)
    return { 'statusCode': 200, 'body': json.dumps(event) }
