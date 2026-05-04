const wordsData = [
  {
    word: "width",
    reading: "ウィズ / ウィドス",
    meaning: "幅、広さ",
    usage: "要素の「横幅」を指定。",
  },
  {
    word: "height",
    reading: "ハイト",
    meaning: "高さ",
    usage:
      "要素の「縦幅・高さ」を指定。「ヘイト」と読み間違えられやすい。",
  },
  {
    word: "align",
    reading: "アライン",
    meaning: "整列させる",
    usage: "配置（左寄せなど）を指定。「アリグン」と読み間違えやすい。",
  },
  {
    word: "opacity",
    reading: "オパシティ",
    meaning: "不透明、不透明度",
    usage: "要素の透明度を指定する。「オパチティ」と読み間違えやすい。",
  },
  {
    word: "pseudo",
    reading: "スード / スードゥ",
    meaning: "疑似の、見せかけの",
    usage:
      "CSSの pseudo-class（疑似クラス）などで登場。「プセウド」ではない。",
  },
  {
    word: "cache",
    reading: "キャッシュ",
    meaning: "隠し場所",
    usage:
      "データを一時保存して次回素早く読み込む仕組み。「カチェ」ではない。",
  },
  {
    word: "null",
    reading: "ヌル / ナル",
    meaning: "何もない",
    usage: "「値が存在しない」ことを明示する特別な値。",
  },
  {
    word: "boolean",
    reading: "ブーリアン",
    meaning: "ブール代数の",
    usage: "「真(true)」か「偽(false)」の2つの状態のみを持つデータ型。",
  },
  {
    word: "integer",
    reading: "インテジャー",
    meaning: "整数",
    usage: "小数点を含まない数値。略して int (イント) とよく書かれる。",
  },
  {
    word: "void",
    reading: "ボイド",
    meaning: "空っぽの",
    usage: "関数が「何も結果を返さない」ことを示す型。",
  },
  {
    word: "archive",
    reading: "アーカイブ",
    meaning: "記録保管所",
    usage:
      "複数のファイルを一つにまとめたり圧縮保存すること。「アーチブ」ではない。",
  },
  {
    word: "deploy",
    reading: "デプロイ",
    meaning: "配置する",
    usage: "開発したものをサーバーに配置し、利用可能な状態にすること。",
  },
  {
    word: "variable",
    reading: "ヴァリアブル",
    meaning: "変わりやすいもの",
    usage:
      "「変数」（データを入れておく箱）。略して var (ヴァー) と書かれる。",
  },
  {
    word: "schema",
    reading: "スキーマ",
    meaning: "図解、概要、構造",
    usage:
      "データベースの構造定義などのこと。ドイツ語読みの「シェーマ」ではない。",
  },
  {
    word: "query",
    reading: "クエリ",
    meaning: "質問、問い合わせ",
    usage: "データベースへの処理要求のこと。「キューリー」ではない。",
  },
  {
    word: "verbose",
    reading: "バーボース",
    meaning: "言葉数の多い、冗長な",
    usage:
      "ログやエラーメッセージの詳細を出力するモード。「ベルボーズ」ではない。",
  },
  {
    word: "warning",
    reading: "ワーニング",
    meaning: "警告",
    usage:
      "エラーではないが注意すべき状態。日本では「ウォーニング」より「ワーニング」が定着している。",
  },
  {
    word: "default",
    reading: "デフォルト",
    meaning: "初期設定、怠慢",
    usage: "何も指定しない場合に適用される「初期値」。",
  },
  {
    word: "parameter",
    reading: "パラメーター",
    meaning: "媒介変数",
    usage: "関数などに渡す設定値。「パラメータ」とも。",
  },
  {
    word: "argument",
    reading: "アーギュメント",
    meaning: "引数、議論",
    usage: "関数を呼び出す際に実際に渡す値。",
  },
  {
    word: "initialize",
    reading: "イニシャライズ",
    meaning: "初期化する",
    usage:
      "変数などに最初の値を設定すること。略して init (イニット) と呼ばれる。",
  },
  {
    word: "repository",
    reading: "リポジトリ",
    meaning: "貯蔵庫、倉庫",
    usage: "ソースコードなどの保管場所（Gitなど）。",
  },
  {
    word: "directory",
    reading: "ディレクトリ",
    meaning: "住所録、案内板",
    usage:
      "ファイルを分類する入れ物。Windows等でいう「フォルダ」のこと。",
  },
  {
    word: "compile",
    reading: "コンパイル",
    meaning: "翻訳する、まとめる",
    usage:
      "人間が書いたコードを、コンピュータが実行できる機械語に変換すること。",
  },
];

const abbrData = [
  {
    word: "src",
    reading: "ソース",
    meaning: "源 (sourceの略)",
    usage: "外部ファイルの読み込み元を指定。「スルク」ではない。",
  },
  {
    word: "href",
    reading: "エイチレフ",
    meaning: "Hypertext Reference",
    usage: "リンク先のURLを指定。「ハレフ」と呼ぶ人も稀にいる。",
  },
  {
    word: "alt",
    reading: "オルト",
    meaning: "代わりの (alternateの略)",
    usage:
      "代替テキストを指定。ローマ字読みで「アルト」と呼ばれることも多い。",
  },
  {
    word: "async",
    reading: "アシンク",
    meaning: "asynchronous(非同期)の略",
    usage:
      "通信などを待たずに別の処理を進めること。「エイシンク」と読む人もいる。",
  },
  {
    word: "NaN",
    reading: "ナン",
    meaning: "Not a Number",
    usage: "「数値ではない」ことを表す特別な値。",
  },
  {
    word: "GUI",
    reading: "グイ / ジーユーアイ",
    meaning: "Graphical User Interface",
    usage:
      "マウス操作などで直感的に扱える画面。「グイ」と略して読まれることもある。",
  },
  {
    word: "SQL",
    reading: "シークェル / エスキューエル",
    meaning: "Structured Query Language",
    usage: "データベースを操作する言語。「スクル」のようには読まない。",
  },
  {
    word: "CLI",
    reading: "シーエルアイ",
    meaning: "Command Line Interface",
    usage:
      "文字ベースでコマンドを入力して操作する画面や仕組み。GUIの対義語。「クリ」とは読まない。",
  },
];

function renderTable(data, tbodyId, colorTheme) {
  const tbody = document.getElementById(tbodyId);
  data.forEach((item, index) => {
    const tr = document.createElement("tr");
    tr.className =
      index % 2 === 0
        ? `bg-white hover:bg-${colorTheme}-50/50 transition-colors`
        : `bg-gray-50/50 hover:bg-${colorTheme}-50/50 transition-colors`;

    tr.innerHTML = `
      <td class="px-6 py-4 whitespace-nowrap">
        <span class="text-lg font-mono font-bold text-${colorTheme}-700">${item.word}</span>
      </td>
      <td class="px-6 py-4 whitespace-nowrap">
        <span class="text-gray-900 font-medium">${item.reading}</span>
      </td>
      <td class="px-6 py-4 whitespace-nowrap">
        <span class="text-gray-600 text-sm">${item.meaning}</span>
      </td>
      <td class="px-6 py-4 text-sm text-gray-700 leading-relaxed">
        ${item.usage}
      </td>
    `;
    tbody.appendChild(tr);
  });
}

renderTable(wordsData, "words-table-body", "emerald");
renderTable(abbrData, "abbr-table-body", "blue");
