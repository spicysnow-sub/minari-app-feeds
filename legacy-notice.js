// 旧アドレス（spicysnow-sub.github.io）で開かれたときだけ、移転のお知らせを上部に出す。
// 新旧どちらにも同じファイルを push しているので、ホスト名で出し分ける（2026-10-09）。
// 旧ページは、旧 URL を読む旧版アプリの利用者がいなくなったら公開を止める。
(function () {
  var LEGACY = "spicysnow-sub.github.io";
  var CURRENT = "tdsms-mnr.github.io";
  if (location.hostname !== LEGACY) return;

  var ja = (navigator.language || "").toLowerCase().indexOf("ja") === 0;
  var t = ja
    ? { title: "このページは新しいアドレスに移りました",
        body: "アプリを最新版にアップデートしてください。最新版では新しいページが開きます。",
        link: "新しいページを開く →" }
    : { title: "This page has moved.",
        body: "Please update the app to the latest version. The latest version opens the new page.",
        link: "Open the new page →" };
  var dest = "https://" + CURRENT + location.pathname + location.search + location.hash;

  var css = document.createElement("style");
  css.textContent =
    ".legacy-notice{--ln-ink:#2b2b2b;--ln-dim:#6b6b6b;--ln-bg:#f1ebe6;--ln-accent:#8a6a56;" +
    "box-sizing:border-box;margin:0 0 2rem;padding:1rem 1.15rem;border-left:3px solid var(--ln-accent);" +
    "background:var(--ln-bg);color:var(--ln-ink);border-radius:4px;" +
    "font-family:-apple-system,\"Hiragino Sans\",sans-serif;line-height:1.7;}" +
    "@media (prefers-color-scheme: dark){.legacy-notice{--ln-ink:#ece9e6;--ln-dim:#a09a94;--ln-bg:#262220;--ln-accent:#d3987e;}}" +
    ".legacy-notice strong{display:block;font-size:1rem;margin:0 0 .25rem;}" +
    ".legacy-notice p{margin:0 0 .5rem;font-size:.92rem;color:var(--ln-dim);}" +
    ".legacy-notice a{color:var(--ln-accent);font-weight:600;font-size:.92rem;}";
  document.head.appendChild(css);

  function show() {
    var box = document.createElement("div");
    box.className = "legacy-notice";
    box.setAttribute("role", "note");
    var s = document.createElement("strong"); s.textContent = t.title;
    var p = document.createElement("p"); p.textContent = t.body;
    var a = document.createElement("a"); a.href = dest; a.textContent = t.link;
    box.appendChild(s); box.appendChild(p); box.appendChild(a);
    document.body.insertBefore(box, document.body.firstChild);
  }
  if (document.body) show(); else document.addEventListener("DOMContentLoaded", show);
})();
