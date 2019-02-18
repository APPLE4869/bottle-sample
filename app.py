# coding: UTF-8
'''
開発環境への入り方
$ python -m venv heroku_env
$ source heroku_env/bin/activate
'''

import os
from bottle import route, run, template
from src import vorkers

@route('/company/<name>')
def index(name):
    client = vorkers.Vorkers()
    company_ids = client.fetch_company_ids(name)

    templates = "検索してヒットした企業情報<br>"
    for company_id in company_ids:
        result = client.fetch_company_by_id(company_id)
        templates += "タイトル : " + result["title"] + "<br>"
        templates += "評価 : " + result["rate"] + "<br>"
        templates += "レビュー件数 : " + str(result["review_count"]) + "<br>"
        templates += "レビュー例 :<br>"
        for review in result["reviews"]:
            templates += " " + review + "<br>"
        templates += "<br><br>"

    return template(templates)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
