# minari-app-feeds

個人開発 iOS アプリが読む、静的なデータ配信の置き場。

- `classicallog/concerts.json` — クラシック演奏会の公演と**発売日**（[ClassicalLog](https://apps.apple.com/jp/app/id6801409117)）
- `ganpuku/seed.json` — 国宝・重要文化財・浮世絵の展示（眼福）

## 約束

- **事実だけを置く。** 日付・会場・演目・指定区分といった事実で、解説文や画像は含めない
- **出典を必ず添える。** 各ファイルの `attribution` に入れている
- **低頻度。** 生成は週1回、アプリからの取得は1日1回まで
- 掲載についてお申し出があれば止めます。Issue でご連絡ください

## 形

すべて封筒つきの JSON で、`schema` / `generatedAt` / `attribution` を持つ。
アプリ側は取り込む前に検査し、**古い・壊れている・出典が無いものは採らずに同梱データのまま動く**。

## `apps/` — アプリ紹介ページ

- [Datto](https://spicysnow-sub.github.io/minari-app-feeds/apps/datto/)
- [Kotoba](https://spicysnow-sub.github.io/minari-app-feeds/apps/kotoba/)

**なぜ置いたか（2026-09-07）**：ChatGPT にアプリを推薦させて実測したところ、
App Store の**プロモーション文を逐語で引用**し、さらに競合1位については
**公式サイトの文面も引用**していた。Datto には公式サイトが無かったので、同じ条件に並べるために置いた。

★このため `robots.txt` は `/apps/` だけ `Allow` にしてある。
**JSON のデータ配信は今までどおり検索エンジンに載せない**（そこは変えていない）。
