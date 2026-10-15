"""Todayboard の「使い方とよくある質問」（2026-10-15・1.2）。アプリの設定 › ヘルプ › 使い方とよくある質問 からここへ飛ぶ.

元データはこのファイルだけ。直すときはここを直して `python3 build_faq.py` → 各言語の index.html が上書きされる。
フォルダ＝en はこの直下、ja/ es/ pt/ zh/ はサブフォルダ（Rowmark の faq と同じ並び）。アプリの新しい13言語は英語版を開く。
書いてあることはアプリのコードで確かめた（2026-10-15）：無料＝Small・終日を隠す・左の色の線・会議に参加／Pro＝Medium・Large・ロック画面・
カレンダーの選択（アプリ全体とウィジェットごと）・範囲（今日／今日と明日／7日）。範囲の既定は「今日」。会議の「参加」は開始10分前から。
ウィジェットは予定の始まりと終わり、そして1時間ごとに描き直す。
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = [("en", "", "English"), ("ja", "ja/", "日本語"), ("es", "es/", "Español"), ("pt", "pt/", "Português"), ("zh", "zh/", "简体中文")]
HTML_LANG = {"en": "en", "ja": "ja", "es": "es", "pt": "pt-BR", "zh": "zh-Hans"}
MAIL = "minaritaniguchi@gmail.com"

T = {}

T["en"] = dict(
    title="Todayboard — How to use & FAQ",
    desc="How to add the Todayboard calendar widget, show Google and Outlook calendars, and answers to common questions.",
    sub="How to use & FAQ",
    h_howto="How to use",
    howto=[
        "Open Todayboard and tap Continue, then allow Full Access to your calendars. Todayboard only reads them.",
        "Touch and hold an empty spot on your Home Screen, tap Edit → Add Widget, search for “Todayboard” and add the Small widget (free). In the app, “Add it to your Home Screen” shows how Small, Medium and Large look.",
        "The widget updates on its own — when an event starts or ends, and about every hour. You don't need to open the app.",
        "Under Display in the app you can hide all-day events and the color line beside events (free), and with Pro choose calendars and how many days the widget shows.",
    ],
    h_faq="Frequently asked questions",
    faq=[
        ("Is this a subscription?", "No. The Small widget, the app's today view, hiding all-day events and joining meetings are free. Pro is a one-time purchase that adds Medium, Large and Lock Screen widgets, choosing calendars and showing up to 7 days. It works on all your iPhones and iPads with the same Apple ID."),
        ("My Google or Outlook calendar doesn't show up.", "Todayboard reads the iPhone's Calendar, not the inside of the Google Calendar app. Add the account to your iPhone: Settings → Apps → Calendar → Calendar Accounts → Add Account (on iOS 17: Settings → Calendar → Accounts), and turn on Calendars. If a shared Google calendar is still missing, open calendar.google.com/calendar/syncselect on a computer and tick it. A direct Google connection is planned for a future update."),
        ("A new event doesn't appear on the widget right away.", "The widget redraws itself when an event starts or ends and about every hour. Opening Todayboard updates it immediately."),
        ("My Medium widget only shows today.", "The range is set to Today by default. In the app, under Display, set “Widget shows” to Today + tomorrow or Next 7 days (Pro). Medium shows up to 2 days, Large up to 7."),
        ("There's a lock on my Medium or Large widget.", "Medium, Large and Lock Screen widgets are Pro. The free version includes the Small widget."),
        ("Can each widget show different calendars?", "Yes, with Pro. Touch and hold the widget, tap Edit Widget and pick calendars — for example one widget for work and one for home. Leave it empty to follow the app's settings."),
        ("How do I hide birthdays and holidays?", "Turn on “Hide all-day events” under Display (free). With Pro you can also turn off the Birthdays or holiday calendar under “Show calendars”."),
        ("Can I join a video call from the widget?", "Yes. From 10 minutes before a meeting with a Meet, Zoom or Teams link, a Join button appears. On the Small and Lock Screen widgets, tap the widget itself."),
        ("Tapping the widget opens Todayboard. Can it open Calendar instead?", "Yes. In Settings, turn on “Tapping the widget opens Calendar”."),
        ("I got a new iPhone.", "Open Todayboard › Settings › Restore Purchases, signed in with the same Apple ID you bought with. Your events come from your calendars, so there is nothing else to move."),
        ("Does Todayboard change or upload my events?", "No. It only reads them on your iPhone and never sends them anywhere. See the <a href=\"{privacy}\">privacy policy</a>."),
    ],
    h_contact="Contact",
    contact="Still stuck, or have an idea? In the app, go to Settings › Help › “Contact / report a problem” (the app version and iPhone model are filled in for you), or email <a href=\"mailto:{mail}\">{mail}</a>.",
    about="About Todayboard",
    privacy="Privacy",
)

T["ja"] = dict(
    title="Todayboard — 使い方とよくある質問",
    desc="カレンダーウィジェット Todayboard の置き方、Google・Outlook のカレンダーを出す方法、よくある質問。",
    sub="使い方とよくある質問",
    h_howto="使い方",
    howto=[
        "Todayboard を開いて「次へ」をタップし、カレンダーへのフルアクセスを許可します。Todayboard は予定を読むだけです。",
        "ホーム画面の何もないところを長押しし、「編集」→「ウィジェットを追加」で「Todayboard」を検索して Small（無料）を置きます。アプリの「ホーム画面に置く」で、Small・Medium・Large の見え方を確かめられます。",
        "ウィジェットは、予定が始まるとき・終わるとき、そして1時間ごとに自動で更新されます。アプリを開く必要はありません。",
        "アプリの「表示」では、終日の予定と予定の左の色の線を隠せます（無料）。Pro では、出すカレンダーと何日先まで出すかを選べます。",
    ],
    h_faq="よくある質問",
    faq=[
        ("サブスクですか？", "いいえ。Small ウィジェット、アプリの今日の予定、終日を隠す、会議への参加は無料です。Pro は買い切りで、Medium・Large・ロック画面のウィジェット、カレンダーの選択、7日先までの表示が加わります。同じ Apple ID の iPhone・iPad すべてで使えます。"),
        ("Google・Outlook のカレンダーが出ません。", "Todayboard は iPhone の「カレンダー」を読みます。Google カレンダーのアプリの中は読めません。「設定」→「アプリ」→「カレンダー」→「カレンダーアカウント」→「アカウントを追加」（iOS 17 は「設定」→「カレンダー」→「アカウント」）でアカウントを足し、「カレンダー」をオンにしてください。共有された Google のカレンダーが出ないときは、パソコンで calendar.google.com/calendar/syncselect を開いてチェックを入れます。Google と直接つなぐ機能は今後のアップデートで予定しています。"),
        ("新しく入れた予定が、すぐウィジェットに出ません。", "ウィジェットは予定の始まり・終わりと、1時間ごとに描き直します。Todayboard を開くとすぐに更新されます。"),
        ("Medium ウィジェットに今日しか出ません。", "範囲の初期設定は「今日」です。アプリの「表示」で「ウィジェットの範囲」を「今日と明日」か「7日間」（Pro）にしてください。Medium は2日まで、Large は7日まで出ます。"),
        ("Medium や Large のウィジェットに鍵のマークが出ます。", "Medium・Large・ロック画面のウィジェットは Pro の機能です。無料では Small ウィジェットを使えます。"),
        ("ウィジェットごとに別のカレンダーを出せますか？", "はい、Pro でできます。ウィジェットを長押しして「ウィジェットを編集」からカレンダーを選びます。仕事用と私用でウィジェットを分ける使い方ができます。選ばなければアプリの設定に従います。"),
        ("誕生日や祝日を出したくありません。", "「表示」の「終日の予定を隠す」をオンにしてください（無料）。Pro なら「表示するカレンダー」で誕生日や祝日のカレンダーだけを外すこともできます。"),
        ("ウィジェットからビデオ会議に入れますか？", "はい。Meet・Zoom・Teams のリンクがある予定は、開始10分前から「参加」が出ます。Small とロック画面のウィジェットは、ウィジェットそのものをタップします。"),
        ("ウィジェットをタップすると Todayboard が開きます。カレンダーを開けますか？", "はい。設定の「ウィジェットをタップでカレンダーを開く」をオンにしてください。"),
        ("iPhone を買い替えました。", "購入したときと同じ Apple ID で、Todayboard の設定 →「購入を復元」を押してください。予定はカレンダーから読むので、ほかに移すものはありません。"),
        ("予定を書き換えたり、アップロードしたりしますか？", "いいえ。iPhone の中で読むだけで、どこにも送りません。<a href=\"{privacy}\">プライバシーポリシー</a>もご覧ください。"),
    ],
    h_contact="問い合わせ",
    contact="解決しないとき・欲しい機能があるときは、アプリの設定 → ヘルプ →「問い合わせ・不具合の報告」から送れます（アプリの版と機種が自動で入ります）。メール：<a href=\"mailto:{mail}\">{mail}</a>",
    about="Todayboard について",
    privacy="プライバシー",
)

T["es"] = dict(
    title="Todayboard — Guía y preguntas frecuentes",
    desc="Cómo añadir el widget de calendario Todayboard, mostrar calendarios de Google y Outlook, y respuestas a preguntas frecuentes.",
    sub="Guía y preguntas frecuentes",
    h_howto="Cómo se usa",
    howto=[
        "Abre Todayboard, toca Continuar y permite el acceso total a tus calendarios. Todayboard solo los lee.",
        "Mantén pulsado un espacio vacío de la pantalla de inicio, toca Editar → Añadir widget, busca “Todayboard” y añade el widget pequeño (gratis). En la app, “Añádelo a tu pantalla de inicio” muestra cómo se ven Small, Medium y Large.",
        "El widget se actualiza solo: cuando empieza o termina un evento y más o menos cada hora. No hace falta abrir la app.",
        "En la app, en Visualización, puedes ocultar los eventos de todo el día y la línea de color junto a los eventos (gratis); con Pro eliges calendarios y cuántos días muestra el widget.",
    ],
    h_faq="Preguntas frecuentes",
    faq=[
        ("¿Es una suscripción?", "No. El widget pequeño, la vista de hoy en la app, ocultar eventos de todo el día y unirse a reuniones son gratis. Pro es un pago único que añade los widgets mediano, grande y de pantalla bloqueada, elegir calendarios y ver hasta 7 días. Funciona en todos tus iPhone y iPad con el mismo Apple ID."),
        ("No aparece mi calendario de Google u Outlook.", "Todayboard lee el Calendario del iPhone, no el interior de la app Google Calendar. Añade la cuenta al iPhone: Ajustes → Apps → Calendario → Cuentas de Calendario → Añadir cuenta (en iOS 17: Ajustes → Calendario → Cuentas) y activa Calendarios. Si falta un calendario compartido de Google, abre calendar.google.com/calendar/syncselect en un ordenador y márcalo. Una conexión directa con Google está prevista para una próxima actualización."),
        ("Un evento nuevo no aparece enseguida en el widget.", "El widget se redibuja cuando empieza o termina un evento y más o menos cada hora. Al abrir Todayboard se actualiza al momento."),
        ("Mi widget mediano solo muestra hoy.", "El rango viene en Hoy. En la app, en Visualización, cambia “El widget muestra” a Hoy + mañana o Próximos 7 días (Pro). El mediano muestra hasta 2 días y el grande hasta 7."),
        ("Mi widget mediano o grande tiene un candado.", "Los widgets mediano, grande y de pantalla bloqueada son Pro. La versión gratis incluye el widget pequeño."),
        ("¿Puede cada widget mostrar calendarios distintos?", "Sí, con Pro. Mantén pulsado el widget, toca Editar widget y elige calendarios: por ejemplo, uno para el trabajo y otro para casa. Si lo dejas vacío, sigue los ajustes de la app."),
        ("¿Cómo oculto cumpleaños y festivos?", "Activa “Ocultar eventos de todo el día” en Visualización (gratis). Con Pro también puedes desactivar el calendario de cumpleaños o de festivos en “Mostrar calendarios”."),
        ("¿Puedo unirme a una videollamada desde el widget?", "Sí. Desde 10 minutos antes de una reunión con enlace de Meet, Zoom o Teams aparece el botón Unirse. En el widget pequeño y en el de pantalla bloqueada, toca el propio widget."),
        ("Al tocar el widget se abre Todayboard. ¿Puede abrir Calendario?", "Sí. En Ajustes, activa “Tocar el widget abre Calendario”."),
        ("Tengo un iPhone nuevo.", "Abre Todayboard › Ajustes › Restaurar compras con el mismo Apple ID con el que compraste. Tus eventos vienen de tus calendarios, así que no hay nada más que pasar."),
        ("¿Todayboard cambia o sube mis eventos?", "No. Solo los lee en tu iPhone y nunca los envía a ningún sitio. Consulta la <a href=\"{privacy}\">política de privacidad</a>."),
    ],
    h_contact="Contacto",
    contact="¿Sigues con dudas o tienes una idea? En la app, ve a Ajustes › Ayuda › “Contacto / informar de un problema” (la versión de la app y el modelo de iPhone se rellenan solos) o escribe a <a href=\"mailto:{mail}\">{mail}</a>.",
    about="Sobre Todayboard",
    privacy="Privacidad",
)

T["pt"] = dict(
    title="Todayboard — Como usar e perguntas frequentes",
    desc="Como adicionar o widget de calendário Todayboard, mostrar calendários do Google e do Outlook, e respostas às perguntas mais comuns.",
    sub="Como usar e perguntas frequentes",
    h_howto="Como usar",
    howto=[
        "Abra o Todayboard, toque em Continuar e permita o acesso total aos seus calendários. O Todayboard só faz a leitura.",
        "Toque e segure um espaço vazio na tela de início, toque em Editar → Adicionar Widget, busque “Todayboard” e adicione o widget pequeno (grátis). No app, “Adicione à sua tela de início” mostra como ficam Small, Medium e Large.",
        "O widget se atualiza sozinho: quando um evento começa ou termina e mais ou menos a cada hora. Não é preciso abrir o app.",
        "Em Exibição você pode ocultar eventos de dia inteiro e a linha colorida ao lado dos eventos (grátis); com o Pro, escolhe os calendários e quantos dias o widget mostra.",
    ],
    h_faq="Perguntas frequentes",
    faq=[
        ("É uma assinatura?", "Não. O widget pequeno, a visão de hoje no app, ocultar eventos de dia inteiro e entrar em reuniões são grátis. O Pro é uma compra única que adiciona os widgets médio, grande e da tela bloqueada, escolher calendários e ver até 7 dias. Funciona em todos os seus iPhones e iPads com o mesmo ID Apple."),
        ("Meu calendário do Google ou do Outlook não aparece.", "O Todayboard lê o Calendário do iPhone, não o interior do app Google Agenda. Adicione a conta ao iPhone: Ajustes → Apps → Calendário → Contas de Calendário → Adicionar Conta (no iOS 17: Ajustes → Calendário → Contas) e ative Calendários. Se um calendário compartilhado do Google ainda não aparecer, abra calendar.google.com/calendar/syncselect num computador e marque-o. Uma conexão direta com o Google está prevista para uma próxima atualização."),
        ("Um evento novo não aparece logo no widget.", "O widget se redesenha quando um evento começa ou termina e mais ou menos a cada hora. Abrir o Todayboard atualiza na hora."),
        ("Meu widget médio só mostra hoje.", "O intervalo vem em Hoje. No app, em Exibição, mude “O widget mostra” para Hoje + amanhã ou Próximos 7 dias (Pro). O médio mostra até 2 dias e o grande até 7."),
        ("Aparece um cadeado no meu widget médio ou grande.", "Os widgets médio, grande e da tela bloqueada são Pro. A versão grátis inclui o widget pequeno."),
        ("Cada widget pode mostrar calendários diferentes?", "Sim, com o Pro. Toque e segure o widget, toque em Editar Widget e escolha os calendários — por exemplo, um para o trabalho e outro para casa. Deixe vazio para seguir os ajustes do app."),
        ("Como oculto aniversários e feriados?", "Ative “Ocultar eventos de dia inteiro” em Exibição (grátis). Com o Pro você também pode desligar o calendário de aniversários ou de feriados em “Mostrar calendários”."),
        ("Dá para entrar numa videochamada pelo widget?", "Sim. A partir de 10 minutos antes de uma reunião com link do Meet, Zoom ou Teams, aparece o botão Entrar. Nos widgets pequeno e da tela bloqueada, toque no próprio widget."),
        ("Tocar no widget abre o Todayboard. Pode abrir o Calendário?", "Sim. Nos Ajustes, ative “Tocar no widget abre o Calendário”."),
        ("Comprei um iPhone novo.", "Abra Todayboard › Ajustes › Restaurar compras com o mesmo ID Apple da compra. Seus eventos vêm dos seus calendários, então não há mais nada para transferir."),
        ("O Todayboard altera ou envia meus eventos?", "Não. Ele só lê os eventos no seu iPhone e nunca os envia para lugar nenhum. Veja a <a href=\"{privacy}\">política de privacidade</a>."),
    ],
    h_contact="Contato",
    contact="Ainda com dúvidas ou com uma ideia? No app, vá em Ajustes › Ajuda › “Contato / relatar um problema” (a versão do app e o modelo do iPhone já vêm preenchidos) ou escreva para <a href=\"mailto:{mail}\">{mail}</a>.",
    about="Sobre o Todayboard",
    privacy="Privacidade",
)

T["zh"] = dict(
    title="Todayboard — 使用方法与常见问题",
    desc="如何添加日历小组件 Todayboard、显示 Google 和 Outlook 日历，以及常见问题解答。",
    sub="使用方法与常见问题",
    h_howto="使用方法",
    howto=[
        "打开 Todayboard，点按“继续”，允许完全访问日历。Todayboard 只读取日程。",
        "在主屏幕空白处长按，点按“编辑”→“添加小组件”，搜索“Todayboard”并添加小号小组件（免费）。在 App 的“添加到主屏幕”中可以看到 Small、Medium、Large 的样子。",
        "小组件会在日程开始、结束时以及大约每小时自动更新，无需打开 App。",
        "在 App 的“显示”中可以隐藏全天日程和日程左侧的颜色线（免费）；Pro 可以选择显示哪些日历，以及显示未来几天。",
    ],
    h_faq="常见问题",
    faq=[
        ("是订阅吗？", "不是。小号小组件、App 中的今日日程、隐藏全天日程和加入会议都是免费的。Pro 为一次性购买，增加中号、大号和锁定屏幕小组件，可选择日历并显示最多 7 天。同一 Apple ID 的所有 iPhone 和 iPad 均可使用。"),
        ("看不到我的 Google 或 Outlook 日历。", "Todayboard 读取的是 iPhone 的“日历”，无法读取 Google 日历 App 内部。请把账户添加到 iPhone：“设置”→“App”→“日历”→“日历账户”→“添加账户”（iOS 17：“设置”→“日历”→“账户”），并打开“日历”。如果共享的 Google 日历仍未出现，请在电脑上打开 calendar.google.com/calendar/syncselect 并勾选。与 Google 直接连接的功能计划在之后的更新中提供。"),
        ("新添加的日程没有马上出现在小组件上。", "小组件会在日程开始、结束时以及大约每小时重新绘制。打开 Todayboard 会立即更新。"),
        ("中号小组件只显示今天。", "范围默认为“今天”。请在 App 的“显示”中把“小组件显示”改为“今天 + 明天”或“未来 7 天”（Pro）。中号最多显示 2 天，大号最多 7 天。"),
        ("中号或大号小组件上有锁的标记。", "中号、大号和锁定屏幕小组件属于 Pro。免费版包含小号小组件。"),
        ("每个小组件可以显示不同的日历吗？", "可以（Pro）。长按小组件，点按“编辑小组件”并选择日历，例如工作一个、生活一个。不选择则沿用 App 中的设置。"),
        ("怎样隐藏生日和节假日？", "在“显示”中打开“隐藏全天日程”（免费）。使用 Pro 还可以在“显示的日历”中关闭生日或节假日日历。"),
        ("能从小组件加入视频会议吗？", "可以。带有 Meet、Zoom 或 Teams 链接的会议，在开始前 10 分钟会出现“加入”按钮。小号和锁定屏幕小组件请直接点按小组件。"),
        ("点按小组件会打开 Todayboard，能改为打开“日历”吗？", "可以。在设置中打开“点按小组件打开‘日历’”。"),
        ("换了新 iPhone。", "使用购买时的同一 Apple ID，打开 Todayboard › 设置 › 恢复购买。日程来自你的日历，无需迁移其他内容。"),
        ("Todayboard 会修改或上传我的日程吗？", "不会。它只在你的 iPhone 上读取，绝不会发送到任何地方。请参阅<a href=\"{privacy}\">隐私政策</a>。"),
    ],
    h_contact="联系",
    contact="仍有问题或有想法？请在 App 的设置 › 帮助 ›“联系 / 报告问题”中发送邮件（会自动填入 App 版本和机型），或写信至 <a href=\"mailto:{mail}\">{mail}</a>。",
    about="关于 Todayboard",
    privacy="隐私",
)

CSS = """:root{--ink:#2b2b2b;--dim:#6b6b6b;--line:#e6e4e1;--bg:#faf9f7;--accent:#3B55B5}
@media (prefers-color-scheme:dark){:root{--ink:#ece9e6;--dim:#a09a94;--line:#332f2c;--bg:#171614;--accent:#8FA2F0}}
body{font-family:-apple-system,"Hiragino Sans",sans-serif;max-width:42rem;margin:0 auto;padding:3rem 1.5rem 5rem;line-height:1.8;color:var(--ink);background:var(--bg)}
h1{font-size:1.7rem;margin:0 0 .3rem;letter-spacing:-.01em}.sub{color:var(--accent);font-weight:600;margin:0 0 1.2rem}
.langs{font-size:.85rem;color:var(--dim);margin-bottom:2rem}a{color:var(--accent)}
h2{font-size:1.1rem;margin:2.6rem 0 .4rem;padding-top:1.4rem;border-top:1px solid var(--line)}
h3{font-size:1rem;margin:1.6rem 0 .2rem}p{margin:.2rem 0 .6rem}ol,ul{padding-left:1.3rem}li{margin:.25rem 0}.dim{color:var(--dim);font-size:.9rem}"""


def page(code, folder):
    t = T[code]
    up = "../" if folder else ""                 # faq/ からの深さ
    privacy = up + "../../../privacy/todayboard/"
    about = up + "../" + ("" if code == "ja" else "en/")   # 紹介ページは ja が直下、それ以外は en/
    langs = " · ".join(
        f'<a href="{up}{f}">{name}</a>' if c != code else f"<strong>{name}</strong>" for c, f, name in LANGS)
    out = [f'<!doctype html><html lang="{HTML_LANG[code]}"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(t["title"])}</title><meta name="description" content="{html.escape(t["desc"])}">']
    for c, f, _ in LANGS:
        out.append(f'<link rel="alternate" hreflang="{HTML_LANG[c]}" href="https://tdsms-mnr.github.io/minari-app-feeds/apps/todayboard/faq/{f}">')
    out.append(f'<style>{CSS}</style></head><body><h1>Todayboard</h1><p class="sub">{t["sub"]}</p><div class="langs">{langs}</div>')
    out.append(f'<h2>{t["h_howto"]}</h2><ol>')
    out += [f"<li>{html.escape(x)}</li>" for x in t["howto"]]
    out.append(f'</ol><h2>{t["h_faq"]}</h2>')
    for q, a in t["faq"]:
        out.append(f"<h3>{html.escape(q)}</h3><p>{a.format(privacy=privacy)}</p>")
    out.append(f'<h2>{t["h_contact"]}</h2><p>{t["contact"].format(mail=MAIL)}</p>')
    out.append(f'<p class="dim"><a href="{about}">{t["about"]}</a> · <a href="{privacy}">{t["privacy"]}</a></p></body></html>\n')
    return "\n".join(out)


for code, folder, _ in LANGS:
    d = os.path.join(HERE, folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(page(code, folder))
print("wrote", len(LANGS), "pages")
