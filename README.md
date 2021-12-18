# ReadHinetHypo
read the html file of NIED's Hi-net earthquake catalogue and convert it to Pandas dataframe

## Overview
防災科学技術研究所のHi-netサイトで公開されている震源リストファイル（htmlファイル）から震源情報を取り出し、Pandasのデータフレームに格納して返すPythonライブラリ。

## Description
* ReadHinetHypo.py：防災科学技術研究所のHi-netサイトで公開されている震源リストファイル（htmlファイル）から震源情報を取り出しPandasのデータフレームに格納して返すPythonライブラリ。

Python 3.8で作成。

## Demo
なし

## VS. 
同じ目的のコードはいくらでもあると思いますが、比較したことはありません。
Several researchers (mainly seismologists) will create codes for the same purpose, but I have not compared my codes with others.  

## Requirement
* Python 3系列
* beautifulsoup
* Pandas

## Usage
0. Hi-netのサイトから、震源リストのhtmlファイルをダウンロード（Google Chromeだとうまくいかない。Mac上ではSafariあるいはFirefoxを使用のこと）
1. ReadHinetHypoをimportした上で、変換したいhtmlファイルへのフルパスを引数としてReadHinetHypoを呼ぶ。
3. コードを実行。

# Install
ライブラリ自体をダウンロードするだけのはず。Requirementの項に書かれているライブラリーがない場合には別途インストール。

## Contribution
バグリポート、フィードバックは歓迎します。

## Licence
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Author
堀川晴央 (Horikawa, Haruo)

[seishorihori](https://github.com/seishorihori)
