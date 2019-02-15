# coding: UTF-8
from src import vorkers

client = vorkers.Vorkers()
company_ids = client.fetch_company_ids("クラウドワークス")

for company_id in company_ids:
    result = client.fetch_company_by_id(company_id)
    print(result)
