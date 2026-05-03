import pandas as pd

def main():
    # 1. サンプルCSVファイルの読み込み
    # （実際のファイル名やパスに合わせて変更してください）
    try:
        df1 = pd.read_csv('data1.csv')
        df2 = pd.read_csv('data2.csv')
    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません。 {e}")
        return

    # 2. データの連結 (縦方向に結合)
    # ignore_index=True でインデックスを振り直します
    # df1とdf2で異なる列がある場合、存在しない列は NaN（欠損値）になります
    merged_df = pd.concat([df1, df2], ignore_index=True, sort=False)

    # 3. 空のセル (NaN) を 0 で埋める
    merged_df = merged_df.fillna(0)

    # 4. 結果を新しいCSVファイルに出力
    # index=False で行番号(インデックス)が出力されるのを防ぎます
    output_filename = 'merged.csv'
    merged_df.to_csv(output_filename, index=False)

    # 実行結果の確認用表示
    print(f"データの連結が完了し、'{output_filename}' として保存されました。")
    print("\n--- 連結後のデータプレビュー ---")
    print(merged_df)

if __name__ == "__main__":
    main()
