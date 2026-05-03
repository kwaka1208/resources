import pandas as pd


def main():
    # 1. サンプルCSVファイルの読み込み
    # （実際のファイル名やパスに合わせて変更してください）
    try:
        left_df = pd.read_csv("users.csv")
        right_df = pd.read_csv("scores.csv")
    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません。 {e}")
        return

    # 2. データの結合 (LEFT JOIN)
    # on='id' で 'id' 列をキーとして指定します。
    # how='left' を指定することで、左側(left_df)の全行を保持し、
    # 右側(right_df)に一致する id がない場合は NaN になります。
    joined_df = pd.merge(left_df, right_df, on="id", how="left")

    # 3. 空のセル (NaN) を 0 で埋める
    joined_df = joined_df.fillna(0)

    # 4. 結果を新しいCSVファイルに出力
    output_filename = "joined.csv"
    joined_df.to_csv(output_filename, index=False)

    # 実行結果の確認用表示
    print(f"データのLEFT JOINが完了し、'{output_filename}' として保存されました。")
    print("\n--- 結合後のデータプレビュー ---")
    print(joined_df)


if __name__ == "__main__":
    main()
