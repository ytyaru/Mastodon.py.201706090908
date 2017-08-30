#!python3
#encoding: utf-8
import os.path
import mimetypes
from mastodon import Mastodon

domain = "mstdn.jp"
api_base_url = "https://{0}".format(domain)
file_client = "./client/client_{0}_0.txt".format(domain)
file_token = "./client/token_{0}_0.txt".format(domain)

mastodon = Mastodon(
    client_id=file_client,
    access_token=file_token,
    api_base_url=api_base_url)
#media_file_paths = ["./img/pencil.svg"]
message = "#Mastodon.py による画像投稿テスト(PNG形式)。SVG形式はエラー「File content typeは不正な値です」で投稿できず。image/svg+xmlは不可らしい。"
media_file_paths = ["./img/yaru.png"]
for path in media_file_paths:
    print(mimetypes.guess_type(path)[0])

# http://qiita.com/code_monkey/items/e4929ef13e2a2032d467
# https://github.com/halcy/Mastodon.py/blob/master/mastodon/Mastodon.py#L692
# https://docs.python.jp/3/library/mimetypes.html#mimetypes.guess_type
media_files = [mastodon.media_post(media, mimetypes.guess_type(media)[0]) for media in media_file_paths]
print(media_files)
ret = mastodon.status_post(status=message, media_ids=media_files)
print(ret)

# SVG形式はアップロード不可らしい。
# [{'error': 'バリデーションに失敗しました: Filehas contents that are not what they are reported to be, Fileは不正な値です, File content typeは不正な値です'}]
# PNG形式はアップロードされた
