import os.path
from mastodon import Mastodon

domain = "mstdn.jp"
api_base_url = "https://{0}".format(domain)
file_client = "./client/client_{0}_0.txt".format(domain)
file_token = "./client/token_{0}_0.txt".format(domain)
mail_address = "メールアドレス"
password = "パスワード"

if not os.path.isfile(file_client):
    Mastodon.create_app("test_app",
                        api_base_url = api_base_url,
                        to_file = file_client)
if not os.path.isfile(file_token):
    mastodon = Mastodon(
        client_id = file_client,
        api_base_url = api_base_url)
    mastodon.log_in(
        mail_address,
        password,
        to_file = file_token)

