import os.path
from mastodon import Mastodon

domain = "mstdn.jp"
api_base_url = "https://{0}".format(domain)
file_client = "./client/client_{0}_0.txt".format(domain)
file_token = "./client/token_{0}_0.txt".format(domain)

mastodon = Mastodon(
    client_id=file_client,
    access_token=file_token,
    api_base_url=api_base_url)
mastodon.toot("""Mastodon.py で #Mastodon #API を 実行してみる。
http://qiita.com/ignis_fatuus/items/f4b7213ad887af2cf71c""")

