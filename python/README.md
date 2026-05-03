# Pandas CSV処理スクリプト

このリポジトリ（フォルダ）には、Pythonのデータ分析ライブラリである pandas を使用して、複数のCSVファイルを操作する2つのサンプルスクリプトが含まれています。

## 前提条件

スクリプトを実行するには、Python環境に pandas がインストールされている必要があります。

インストールされていない場合は、以下のコマンドを実行してください。

```
pip install pandas
```

## 1. CSVの連結（縦方向の結合）

スクリプト名: merge_csv.py

2つのCSVファイルを縦方向に連結（Concat）し、1つのCSVファイルとして出力します。異なるファイルで一致しない列がある場合や、元から空のセルがある場合は、すべて 0 で補完されます。

### サンプルデータ

* data1.csv  
```
  id,name,score1,score2  
  1,Alice,80,  
  2,Bob,90,85
```

* data2.csv  
```
  id,name,score1,score3  
  3,Charlie,,70  
  4,Dave,60,95
```

### 実行方法

```
python merge_csv.py
```

### 実行結果

- merged.csv が生成されます。
- score2 や score3 のように片方にしか存在しない列の欠損部分や、元の空セルが 0 で埋められます。

## 2. CSVの結合（特定の列をキーにしたLEFT JOIN）

スクリプト名: join_csv.py

2つのCSVファイルを、共通の列（id）をキーにして横方向に結合（Merge / LEFT JOIN）します。

左側のデータ（ベースとなるデータ）を全て残し、右側のデータに一致するキーがない場合や元から空のセルがある場合は、すべて 0 で補完されます。

### サンプルデータ

* users.csv (左側 / ベースデータ)  
```
  id,name,department  
  1,Alice,Sales  
  2,Bob,Engineering  
  3,Charlie,Marketing  
  4,Dave,HR
```

* scores.csv (右側 / 結合するデータ)  
```
  id,math,english  
  1,80,90  
  2,,85  
  5,100,100
```

### 実行方法

```
python join_csv.py
```

### 実行結果

- joined.csv が生成されます。
- scores.csv に存在しない id=3, 4 の成績データや、元の空セル（id=2のmath）が 0 で埋められます。
- scores.csv にのみ存在する id=5 のデータは、LEFT JOINのため除外されます。
