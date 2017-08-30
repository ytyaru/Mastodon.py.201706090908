# このソフトウェアについて

Mastodon.pyで画像をtootする。

PNG形式で成功した。しかし、SVG形式は失敗した。image/svg+xmlは不可らしい。

> [{'error': 'バリデーションに失敗しました: Filehas contents that are not what they are reported to be, Fileは不正な値です, File content typeは不正な値です'}]

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
    * requests-oauthlib 0.8.0
        * requests 2.2.1
        * oauthlib 2.0.1
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * requests-oauthlib 0.8.0
            * requests 2.17.3
            * oauthlib 2.0.2

## WebService

* [マストドン鯖一覧](http://k52.org/mastodon/)
    * [Mastodon (mstdn.jp)](https://mstdn.jp/)
* [マストドンWebAPI](https://github.com/tootsuite/documentation/blob/master/Using-the-API/API.md)

# 準備

## アカウント取得する

[前回のReadMe.md](https://github.com/ytyaru/Python.Mastodon.API.201706071450)参照

## HomeTimelineをすべて取得してみる

### 編集

1. `MediaPost.py`ファイルを開く
1. 以下の部分で送信したいメッセージとファイルパスを指定する

```python
message = "#Mastodon.py による画像投稿テスト(PNG形式)。SVG形式はエラー「File content typeは不正な値です」で投稿できず。image/svg+xmlは不可らしい。"
media_file_paths = ["./img/yaru.png"]
```

### 実行

```sh
$ python3 MediaPost.py
```

対象ユーザとして指定画像とメッセージがTootされる。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[Mastodon.py](https://github.com/halcy/Mastodon.py)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2016 Lorenz Diener](https://github.com/halcy/Mastodon.py/blob/master/LICENSE)

