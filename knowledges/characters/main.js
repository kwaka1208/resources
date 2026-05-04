const symbolsData = [
  {
    symbol: ":",
    name: "コロン",
    en: "Colon",
    usage:
      "オブジェクトのキーと値の区切り(JSON, JavaScript等)、型注釈(TypeScript等)。",
    jis: "「: / *」",
    us: "Shift + 「; / :」",
  },
  {
    symbol: ";",
    name: "セミコロン",
    en: "Semicolon",
    usage: "文（ステートメント）の終わりを表す(C, Java, JavaScript等)。",
    jis: "「; / +」",
    us: "「; / :」",
  },
  {
    symbol: ".",
    name: "ピリオド / ドット",
    en: "Period / Dot",
    usage:
      "メソッドやプロパティの呼び出し、オブジェクトの階層の指定、小数点。",
    jis: "「. / >」",
    us: "「. / >」",
  },
  {
    symbol: ",",
    name: "カンマ / コンマ",
    en: "Comma",
    usage: "関数の引数の区切り、配列やオブジェクトの要素の区切り。",
    jis: "「, / <」",
    us: "「, / <」",
  },
  {
    symbol: "'",
    name: "シングルクォート",
    en: "Single Quote",
    usage: "文字列の定義。HTMLの属性やSQLでもよく使用される。",
    jis: "Shift + 「7 / '」",
    us: "「' / \"」",
  },
  {
    symbol: '"',
    name: "ダブルクォート",
    en: "Double Quote",
    usage: "文字列の定義。JSONではキーも値も必須で使用する。",
    jis: 'Shift + 「2 / "」',
    us: "Shift + 「' / \"」",
  },
  {
    symbol: "`",
    name: "バッククォート",
    en: "Backtick / Backquote",
    usage:
      "テンプレート文字列(JavaScript等)、コマンド置換(シェルスクリプト)。",
    jis: "Shift + 「@ / `」",
    us: "「` / ~」 (Escの下)",
  },
  {
    symbol: "/",
    name: "スラッシュ",
    en: "Slash / Forward Slash",
    usage:
      "割り算の演算子、ファイルパスの区切り、コメントアウト(// または /*)。",
    jis: "「/ / ?」",
    us: "「/ / ?」",
  },
  {
    symbol: "\\",
    name: "バックスラッシュ",
    en: "Backslash",
    usage:
      "エスケープ処理(改行\\nなど)、Windows環境のファイルパスの区切り。※",
    jis: "「\\ / _」 または 「¥」",
    us: "「\\ / |」",
    note: "※JIS配列(Mac/Win)では環境によって円記号(¥)として表示・入力されることがありますが、プログラム上は同じ意味を持ちます。",
  },
  {
    symbol: "~",
    name: "チルダ",
    en: "Tilde",
    usage:
      "ホームディレクトリを表すシェル記号(~/Documents等)、正規表現での近似マッチ、JavaScriptのビット否定演算子。",
    jis: "Shift + 「^ / ~」",
    us: "Shift + 「` / ~」(Escの下)",
  },
  {
    symbol: "|",
    name: "パイプ / 縦棒",
    en: "Pipe / Vertical Bar",
    usage:
      "シェルのパイプ(コマンドの出力を次のコマンドへ渡す)、論理OR演算子(||)、TypeScriptのユニオン型。",
    jis: "Shift + 「¥ / |」",
    us: "Shift + 「\\ / |」",
  },
  {
    symbol: "{}",
    name: "波括弧 / 中括弧",
    en: "Curly Braces",
    usage:
      "コードブロック、オブジェクトリテラルの定義、テンプレート文字列の変数展開(${})。",
    jis: "{ : Shift + 「[ / {」 <br>} : Shift + 「] / }」",
    us: "{ : Shift + 「[ / {」 <br>} : Shift + 「] / }」",
  },
  {
    symbol: "[]",
    name: "角括弧",
    en: "Square Brackets",
    usage:
      "配列の定義、配列要素へのアクセス(arr[0])、オブジェクトのブラケット記法でのプロパティアクセス。",
    jis: "[ : 「[ / {」 <br>] : 「] / }」",
    us: "[ : 「[ / {」 <br>] : 「] / }」",
  },
  {
    symbol: "<>",
    name: "山括弧 / アングルブラケット",
    en: "Angle Brackets",
    usage:
      "HTML/XMLのタグ囲み(&lt;div&gt;等)、比較演算子、TypeScriptのジェネリクス型引数(Array&lt;string&gt;等)に使用。<br>&lt; は「小なり」：左辺が右辺より小さい。<br>&gt; は「大なり」：左辺が右辺より大きい。",
    jis: "&lt; : Shift + 「, / &lt;」 <br>&gt; : Shift + 「. / &gt;」",
    us: "&lt; : Shift + 「, / &lt;」 <br>&gt; : Shift + 「. / &gt;」",
  },
  {
    symbol: "@",
    name: "アットマーク",
    en: "At Sign",
    usage:
      "メールアドレスの区切り、JavaやTypeScriptのデコレーター、CSSの@ルール(@media, @import等)。",
    jis: "「@ / `」",
    us: "Shift + 「2 / @」",
  },
  {
    symbol: "#",
    name: "ハッシュ / シャープ",
    en: "Hash / Number Sign",
    usage:
      "PythonやシェルスクリプトのコメントアウトおよびShebang(#!/...)、CSSのIDセレクター、SNSのハッシュタグ。",
    jis: "Shift + 「3 / #」",
    us: "Shift + 「3 / #」",
  },
  {
    symbol: "^",
    name: "キャレット",
    en: "Caret",
    usage:
      "正規表現での行頭マッチ、XOR(排他的OR)演算子、package.jsonの互換バージョン指定(^1.2.3)。",
    jis: "「^ / ~」",
    us: "Shift + 「6 / ^」",
  },
  {
    symbol: "*",
    name: "アスタリスク",
    en: "Asterisk",
    usage:
      "掛け算の演算子、ワイルドカード、JavaScriptのジェネレーター関数(function*)、べき乗演算子(**)。",
    jis: "Shift + 「: / *」",
    us: "Shift + 「8 / *」",
  },
  {
    symbol: "_",
    name: "アンダースコア / アンダーバー",
    en: "Underscore",
    usage:
      "変数名・関数名の区切り(snake_case)、プライベート変数の慣例的なプレフィックス(_var)、不使用変数の明示。",
    jis: "Shift + 「\\ / _」(ろキー)",
    us: "Shift + 「- / _」",
  },
];

function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

const container = document.getElementById("symbols-container");

symbolsData.forEach((item) => {
  const card = document.createElement("div");
  card.className =
    "bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow flex flex-col h-full";

  card.innerHTML = `
    <div
      class="text-6xl font-mono text-center text-indigo-600 mb-5 bg-indigo-50/50 py-6 rounded-lg cursor-pointer hover:bg-indigo-100 transition-colors relative group select-none"
      onclick="copyToClipboard('${escapeHtml(item.symbol.replace(/\\/g, "\\\\"))}')"
      title="クリックしてコピー"
    >
      ${escapeHtml(item.symbol)}
      <span class="absolute right-2 top-2 text-xs font-sans bg-indigo-200 text-indigo-800 px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">
        コピー
      </span>
    </div>
    <div class="flex-grow">
      <h2 class="text-xl font-bold text-gray-800 flex items-baseline gap-2">
        ${item.name}
        <span class="text-xs font-medium text-gray-400 font-mono">${item.en}</span>
      </h2>
      <p class="text-gray-600 mt-3 text-sm leading-relaxed">
        <span class="font-semibold text-gray-700">用途:</span><br>
        ${item.usage}
      </p>
      ${item.note ? `<p class="text-xs text-amber-600 mt-2 bg-amber-50 p-2 rounded">${item.note}</p>` : ""}
    </div>
    <div class="mt-5 pt-5 border-t border-gray-100">
      <h3 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">キーボード入力</h3>
      <ul class="text-sm text-gray-600 space-y-2">
        <li class="flex items-center">
          <span class="inline-block w-14 font-semibold text-gray-500 text-xs">JIS配列:</span>
          <kbd>${item.jis}</kbd>
        </li>
        <li class="flex items-center">
          <span class="inline-block w-14 font-semibold text-gray-500 text-xs">US配列:</span>
          <kbd>${item.us}</kbd>
        </li>
      </ul>
    </div>
  `;
  container.appendChild(card);
});
