
## csv形式を作成するプログラムの例

```python
import csv
import io

# スクレイピングで取得したデータはリスト（配列）で保管されているものとします。
fruits = ["りんご", "バナナ", "オレンジ", "ぶどう"]

# メモリ上にCSV出力（1行にする）
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(fruits)

# CSV文字列として取得
csv_string = output.getvalue()
output.close()

# 表示
print(csv_string)
```


## JSON形式作成するプログラムの例

```python
import json

# スクレイピングで取得したデータは2次元のリスト（配列）で保管されているものとします。
raw_data = [
    ["東京", "晴れ", "25℃"],
    ["大阪", "くもり", "22℃"],
    ["札幌", "雨", "18℃"]
]

# 辞書形式に変換
weather_data = []
for row in raw_data:
    city, condition, temperature = row
    weather_data.append({
        "city": city,
        "condition": condition,
        "temperature": temperature
    })

# 全体をラップ
data = {"weather": weather_data}

# JSON文字列に変換
json_string = json.dumps(data, ensure_ascii=False, indent=2)

# 表示
print(json_string)
```
