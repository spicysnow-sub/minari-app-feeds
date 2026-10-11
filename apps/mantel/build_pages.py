"""Mantel の公式ページ（使い方とよくある質問）を5言語で作る（2026-10-11・1.4）.

元データはこのファイルだけ。直すときはここを直して `python3 build_pages.py` → 各言語の index.html が上書きされる。
フォルダ＝ja はこの直下、en/ es/ pt/ zh/ はサブフォルダ。アプリの「使い方とよくある質問」はここへ飛ぶ。
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://tdsms-mnr.github.io/minari-app-feeds/apps/mantel/"
STORE = "https://apps.apple.com/app/id6814138903"

LANGS = [  # (コード, フォルダ, hreflang, 表示名)
    ("ja", "", "ja", "日本語"),
    ("en", "en/", "en", "English"),
    ("es", "es/", "es", "Español"),
    ("pt", "pt/", "pt-BR", "Português"),
    ("zh", "zh/", "zh-Hans", "简体中文"),
]

T = {
"ja": dict(
    title="Mantel — 自分の写真をホーム画面に（写真ウィジェット・サブスクなし）",
    desc="選んだ写真を、ホーム画面のウィジェットで入れ替えて見せる iPhone アプリ。サブスクなし・広告なし・アカウント登録不要。",
    tagline="自分の写真を、ホーム画面に。サブスクなしの写真ウィジェット。",
    lede="Mantel は、選んだ写真をホーム画面のウィジェットで入れ替えて見せるアプリです。犬、友だち、去年の夏の写真——何枚か選ぶだけで、毎日目にする場所に写真が並びます。サブスクはありません。",
    cta="App Store で見る",
    h_howto="使い方",
    steps=["Mantel を開いて「写真を選ぶ」をタップし、ウィジェットに出したい写真を選びます。",
           "ホーム画面の何もないところを長押しし、「編集」→「ウィジェットを追加」から Mantel を選んで置きます。",
           "置いたウィジェットは、1時間ごとに次の写真へ切り替わります。"],
    h_more="もっと使いこなす",
    more=[("写真のどこを見せるか選ぶ", "セットの写真を長押しして「位置を調整」を選び、見せたいところをタップします。ウィジェットでは、そこを中心に切り取って表示します。"),
          ("写真の入れ方を選ぶ", "「枠いっぱい」はウィジェット全体に写真を広げます（写真の端が少し切れることがあります）。「写真全体」は写真を切らずに表示し、まわりに少し余白ができます。"),
          ("時間でセットを切り替える（Pro）", "セットの「決まった時間に出す」をオンにして時間帯と曜日を決めます。次にウィジェットを長押しして「ウィジェットを編集」を開き、「時間で切り替え」を選びます。"),
          ("写真に一言を重ねる（Pro）", "セットの「写真に重ねる文字」に好きな言葉を入れると、ウィジェットの写真の上に表示されます。"),
          ("別の iPhone と同期する（Pro）", "Pro では「iCloud で同期」が最初からオンになっています。同じ Apple アカウントの iPhone で Mantel を開くと、同じセットと写真が表示されます。")],
    h_price="料金",
    price=["無料：セット1つ・1セット12枚まで、Small ウィジェット1枚（1時間ごとに切り替え）。期限はなく、ずっと使えます。",
           "Pro（買い切り。サブスクではありません）：Medium・Large・ロック画面のウィジェット、セットと写真の枚数の上限なし、切り替え間隔（15分／1時間／6時間／1日）とシャッフル、時間で切り替え、写真に一言、iCloud で同期。",
           "広告は表示しません。アカウント登録も不要です。"],
    h_faq="よくある質問",
    faq=[("写真ライブラリ全体へのアクセスは必要ですか？", "いいえ。iPhone 標準の写真選択画面を使うので、Mantel から見えるのは選んだ写真だけです。元の写真には手を加えません。"),
         ("写真はどこかにアップロードされますか？", "開発者のサーバーには送られません。写真は端末の中に保存されます。Pro で「iCloud で同期」がオンのときは、あなた自身の iCloud にも保存されます（設定でオフにできます）。"),
         ("Medium や Large のウィジェットに鍵のマークが出ます。", "Medium・Large・ロック画面のウィジェットは Pro の機能です。無料では Small ウィジェットを1枚使えます。"),
         ("別の iPhone で Pro が使えません。", "購入したときと同じ Apple アカウントで App Store にサインインしているか確かめてから、Mantel の設定にある「購入を復元」を押してください。購入した直後は、反映まで少し時間がかかることがあります。"),
         ("問い合わせはどこからできますか？", "Mantel の設定 →「問い合わせ・不具合の報告」からメールを送れます。アプリと iOS のバージョン、機種が自動で入ります。")],
    h_spec="対応",
    spec=["iPhone（iOS 17 以降）", "日本語・英語・スペイン語・ポルトガル語・中国語（簡体字）"],
    h_privacy="プライバシー",
    privacy="写真やセットの内容を、開発者が受け取ることはありません。",
    privacy_link="プライバシーポリシー",
),
"en": dict(
    title="Mantel — Your own photos on your Home Screen (photo widget, no subscription)",
    desc="An iPhone app that rotates the photos you pick in a Home Screen widget. No subscription, no ads, no account.",
    tagline="Your own photos on your Home Screen. A photo widget with no subscription.",
    lede="Mantel shows the photos you pick in a Home Screen widget and rotates them. Your dog, your friends, last summer — pick a few and they appear right where you look every day. No subscription.",
    cta="View on the App Store",
    h_howto="How to use",
    steps=["Open Mantel, tap “Pick photos” and choose the photos you want in the widget.",
           "Touch and hold an empty spot on your Home Screen, tap “Edit” → “Add Widget”, and add Mantel.",
           "The widget moves to the next photo every hour."],
    h_more="Getting more out of it",
    more=[("Choose which part of a photo shows", "Touch and hold a photo in a set, choose “Adjust position”, and tap the spot you want to keep in view. The widget crops around that spot."),
          ("Fill frame or whole photo", "“Fill frame” fills the widget (the edges of the photo may be cropped). “Whole photo” shows the entire photo without cropping, with a small margin around it."),
          ("Switch sets by time (Pro)", "In a set, turn on “Show at set times” and choose the hours and days. Then touch and hold the widget, open “Edit Widget” and choose “Switch by time”."),
          ("Add words to your photos (Pro)", "In a set, type a short line under “Text on photo”. It appears on top of the photo in your widget."),
          ("Sync with your other iPhone (Pro)", "With Pro, “Sync with iCloud” is on from the start. Open Mantel on another iPhone with the same Apple Account and the same sets and photos appear.")],
    h_price="Pricing",
    price=["Free: one set of up to 12 photos and one Small widget that changes every hour. No time limit.",
           "Pro (one-time purchase, not a subscription): Medium, Large and Lock Screen widgets, unlimited sets and photos, rotation interval (15 min / 1 hour / 6 hours / 1 day) and shuffle, switch by time, words on photos, iCloud sync.",
           "No ads. No account needed."],
    h_faq="FAQ",
    faq=[("Does Mantel need access to my whole photo library?", "No. It uses the standard iPhone photo picker, so Mantel only sees the photos you pick. Your original photos are never changed."),
         ("Are my photos uploaded anywhere?", "They are never sent to the developer's servers. Photos are stored on your device, and — only with Pro and “Sync with iCloud” on — in your own iCloud too (you can turn it off in Settings)."),
         ("There's a lock on my Medium or Large widget.", "Medium, Large and Lock Screen widgets are Pro features. The free version includes one Small widget."),
         ("Pro isn't working on my other iPhone.", "Check that the App Store on that iPhone is signed in with the same Apple Account you bought with, then tap “Restore Purchases” in Mantel's Settings. Right after buying, it can take a little while to show up."),
         ("How do I contact you?", "In Mantel, go to Settings → “Contact / report a problem” to send an email. The app version, iOS version and iPhone model are filled in for you.")],
    h_spec="Requirements",
    spec=["iPhone (iOS 17 or later)", "English, Japanese, Spanish, Portuguese, Chinese (Simplified)"],
    h_privacy="Privacy",
    privacy="The developer never receives your photos or the contents of your sets.",
    privacy_link="Privacy Policy",
),
"es": dict(
    title="Mantel — Tus propias fotos en la pantalla de inicio (widget de fotos sin suscripción)",
    desc="App para iPhone que va rotando las fotos que eliges en un widget de la pantalla de inicio. Sin suscripción, sin anuncios y sin cuenta.",
    tagline="Tus propias fotos en la pantalla de inicio. Un widget de fotos sin suscripción.",
    lede="Mantel muestra las fotos que eliges en un widget de la pantalla de inicio y las va rotando. Tu perro, tus amigos, el verano pasado: elige unas cuantas y aparecen justo donde miras cada día. Sin suscripción.",
    cta="Ver en el App Store",
    h_howto="Cómo usarlo",
    steps=["Abre Mantel, toca «Elegir fotos» y selecciona las fotos que quieres en el widget.",
           "Mantén pulsado un espacio vacío de la pantalla de inicio, toca «Editar» → «Añadir widget» y añade Mantel.",
           "El widget pasa a la siguiente foto cada hora."],
    h_more="Para sacarle más partido",
    more=[("Elegir qué parte de la foto se ve", "Mantén pulsada una foto del conjunto, elige «Ajustar posición» y toca el punto que quieres que se vea. El widget recorta alrededor de ese punto."),
          ("Llenar marco o foto completa", "«Llenar marco» ocupa todo el widget (los bordes de la foto pueden recortarse). «Foto completa» muestra la foto entera sin recortar, con un pequeño margen."),
          ("Cambiar de conjunto según la hora (Pro)", "En un conjunto, activa «Mostrar a ciertas horas» y elige las horas y los días. Luego mantén pulsado el widget, abre «Editar widget» y elige «Cambiar según la hora»."),
          ("Añadir texto a tus fotos (Pro)", "En un conjunto, escribe una frase en «Texto sobre la foto». Aparece encima de la foto en tu widget."),
          ("Sincronizar con tu otro iPhone (Pro)", "Con Pro, «Sincronizar con iCloud» está activado desde el principio. Abre Mantel en otro iPhone con la misma cuenta de Apple y aparecerán los mismos conjuntos y fotos.")],
    h_price="Precio",
    price=["Gratis: un conjunto de hasta 12 fotos y un widget pequeño que cambia cada hora. Sin límite de tiempo.",
           "Pro (pago único, no es una suscripción): widgets mediano, grande y de pantalla bloqueada, conjuntos y fotos ilimitados, intervalo de rotación (15 min / 1 hora / 6 horas / 1 día) y orden aleatorio, cambiar según la hora, texto sobre las fotos, sincronización con iCloud.",
           "Sin anuncios. No necesitas cuenta."],
    h_faq="Preguntas frecuentes",
    faq=[("¿Mantel necesita acceso a toda mi fototeca?", "No. Usa el selector de fotos estándar del iPhone, así que Mantel solo ve las fotos que eliges. Tus fotos originales no se modifican."),
         ("¿Se suben mis fotos a algún sitio?", "Nunca se envían a los servidores del desarrollo. Las fotos se guardan en tu dispositivo y, solo con Pro y «Sincronizar con iCloud» activado, también en tu propio iCloud (puedes desactivarlo en Ajustes)."),
         ("Mi widget mediano o grande muestra un candado.", "Los widgets mediano, grande y de pantalla bloqueada son funciones de Pro. La versión gratuita incluye un widget pequeño."),
         ("Pro no funciona en mi otro iPhone.", "Comprueba que el App Store de ese iPhone use la misma cuenta de Apple con la que compraste y toca «Restaurar compras» en los ajustes de Mantel. Justo después de comprar, puede tardar un poco en aparecer."),
         ("¿Cómo me pongo en contacto?", "En Mantel, ve a Ajustes → «Contacto / informar de un problema» para enviar un correo. La versión de la app, la de iOS y el modelo de iPhone se añaden solos.")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 o posterior)", "Español, inglés, japonés, portugués, chino (simplificado)"],
    h_privacy="Privacidad",
    privacy="Nunca recibimos tus fotos ni el contenido de tus conjuntos.",
    privacy_link="Política de privacidad (en inglés y japonés)",
),
"pt": dict(
    title="Mantel — Suas próprias fotos na tela inicial (widget de fotos sem assinatura)",
    desc="App para iPhone que alterna as fotos que você escolhe em um widget da tela inicial. Sem assinatura, sem anúncios e sem conta.",
    tagline="Suas próprias fotos na tela inicial. Um widget de fotos sem assinatura.",
    lede="O Mantel mostra as fotos que você escolhe em um widget da tela inicial e vai alternando entre elas. Seu cachorro, seus amigos, o verão passado: escolha algumas e elas aparecem bem onde você olha todo dia. Sem assinatura.",
    cta="Ver na App Store",
    h_howto="Como usar",
    steps=["Abra o Mantel, toque em “Escolher fotos” e selecione as fotos que quer no widget.",
           "Toque e segure um espaço vazio da tela inicial, toque em “Editar” → “Adicionar widget” e adicione o Mantel.",
           "O widget passa para a próxima foto a cada hora."],
    h_more="Para aproveitar mais",
    more=[("Escolher qual parte da foto aparece", "Toque e segure uma foto do conjunto, escolha “Ajustar posição” e toque no ponto que quer manter visível. O widget recorta em volta desse ponto."),
          ("Preencher ou foto inteira", "“Preencher” ocupa todo o widget (as bordas da foto podem ser cortadas). “Foto inteira” mostra a foto completa sem cortar, com uma pequena margem."),
          ("Trocar de conjunto conforme o horário (Pro)", "Em um conjunto, ative “Mostrar em certos horários” e escolha os horários e os dias. Depois toque e segure o widget, abra “Editar widget” e escolha “Mudar conforme o horário”."),
          ("Adicionar texto às fotos (Pro)", "Em um conjunto, escreva uma frase em “Texto sobre a foto”. Ela aparece sobre a foto no seu widget."),
          ("Sincronizar com seu outro iPhone (Pro)", "No Pro, “Sincronizar com o iCloud” já vem ativado. Abra o Mantel em outro iPhone com a mesma Conta Apple e os mesmos conjuntos e fotos aparecem.")],
    h_price="Preço",
    price=["Grátis: um conjunto de até 12 fotos e um widget pequeno que muda a cada hora. Sem limite de tempo.",
           "Pro (compra única, não é assinatura): widgets médio, grande e da tela bloqueada, conjuntos e fotos ilimitados, intervalo de troca (15 min / 1 hora / 6 horas / 1 dia) e ordem aleatória, troca conforme o horário, texto nas fotos, sincronização com o iCloud.",
           "Sem anúncios. Não precisa de conta."],
    h_faq="Perguntas frequentes",
    faq=[("O Mantel precisa de acesso a toda a minha fototeca?", "Não. Ele usa o seletor de fotos padrão do iPhone, então o Mantel só vê as fotos que você escolhe. As fotos originais nunca são alteradas."),
         ("Minhas fotos são enviadas para algum lugar?", "Nunca são enviadas aos servidores do desenvolvimento. As fotos ficam no seu aparelho e, só com o Pro e “Sincronizar com o iCloud” ativado, também no seu próprio iCloud (você pode desativar nos Ajustes)."),
         ("Meu widget médio ou grande mostra um cadeado.", "Os widgets médio, grande e da tela bloqueada são recursos do Pro. A versão grátis inclui um widget pequeno."),
         ("O Pro não funciona no meu outro iPhone.", "Verifique se a App Store desse iPhone está com a mesma Conta Apple usada na compra e toque em “Restaurar compras” nos ajustes do Mantel. Logo depois da compra, pode demorar um pouco para aparecer."),
         ("Como entro em contato?", "No Mantel, vá em Ajustes → “Contato / relatar um problema” para enviar um e-mail. A versão do app, a do iOS e o modelo do iPhone já vêm preenchidos.")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 ou posterior)", "Português, inglês, japonês, espanhol, chinês (simplificado)"],
    h_privacy="Privacidade",
    privacy="Nunca recebemos suas fotos nem o conteúdo dos seus conjuntos.",
    privacy_link="Política de privacidade (em inglês e japonês)",
),
"zh": dict(
    title="Mantel — 把自己的照片放上主屏幕（照片小组件・无订阅）",
    desc="把你选的照片放进主屏幕小组件并自动轮换的 iPhone App。无订阅、无广告、无需账户。",
    tagline="把自己的照片放上主屏幕。无订阅的照片小组件。",
    lede="Mantel 会把你选的照片放进主屏幕的小组件里，并自动轮换。你的狗、你的朋友、去年的夏天——挑几张，它们就会出现在你每天都会看的地方。没有订阅。",
    cta="在 App Store 查看",
    h_howto="使用方法",
    steps=["打开 Mantel，点按“选择照片”，选出想放进小组件的照片。",
           "在主屏幕空白处长按，点按“编辑”→“添加小组件”，然后添加 Mantel。",
           "小组件每小时会切换到下一张照片。"],
    h_more="更多用法",
    more=[("选择照片显示的部分", "在照片集中长按照片，选择“调整位置”，然后点按想保留的位置。小组件会以该处为中心裁剪。"),
          ("铺满或完整照片", "“铺满”会让照片填满整个小组件（照片边缘可能被裁掉）。“完整照片”会完整显示照片不裁切，四周会留一点空白。"),
          ("按时间切换照片集（Pro）", "在照片集中打开“在指定时间显示”，选择时段和星期几。然后长按小组件，打开“编辑小组件”，选择“按时间切换”。"),
          ("在照片上加一句话（Pro）", "在照片集的“照片上的文字”中输入一句话，它会显示在小组件的照片上。"),
          ("与另一台 iPhone 同步（Pro）", "使用 Pro 时，“通过 iCloud 同步”默认开启。在登录同一 Apple 账户的另一台 iPhone 上打开 Mantel，就会显示相同的照片集和照片。")],
    h_price="价格",
    price=["免费：一个照片集、最多 12 张照片，以及一个每小时切换的小号小组件。没有使用期限。",
           "Pro（一次性购买，不是订阅）：中号、大号和锁定屏幕小组件，照片集和照片数量不限，轮换间隔（15 分钟／1 小时／6 小时／1 天）和随机顺序，按时间切换，照片上的文字，iCloud 同步。",
           "没有广告，也不需要注册账户。"],
    h_faq="常见问题",
    faq=[("Mantel 需要访问整个照片图库吗？", "不需要。它使用 iPhone 标准的照片选择器，所以 Mantel 只能看到你选的照片。原始照片不会被修改。"),
         ("我的照片会被上传吗？", "不会发送到开发者的服务器。照片保存在你的设备上；只有在使用 Pro 并开启“通过 iCloud 同步”时，才会同时保存在你自己的 iCloud 中（可在设置中关闭）。"),
         ("中号或大号小组件上显示锁的图标。", "中号、大号和锁定屏幕小组件是 Pro 功能。免费版包含一个小号小组件。"),
         ("在另一台 iPhone 上用不了 Pro。", "请确认那台 iPhone 的 App Store 登录的是购买时使用的同一个 Apple 账户，然后在 Mantel 的设置中点按“恢复购买”。刚购买后，可能需要一点时间才能生效。"),
         ("如何联系？", "在 Mantel 中前往 设置 →“联系 / 报告问题”即可发送邮件。App 版本、iOS 版本和 iPhone 型号会自动填入。")],
    h_spec="支持",
    spec=["iPhone（iOS 17 或更高版本）", "简体中文、英语、日语、西班牙语、葡萄牙语"],
    h_privacy="隐私",
    privacy="开发者不会收到你的照片或照片集内容。",
    privacy_link="隐私政策（英文和日文）",
),
}

STYLE = open(os.path.join(HERE, "_style.txt")).read() if os.path.exists(os.path.join(HERE, "_style.txt")) else None


def page(code, folder, hreflang, label):
    t = T[code]
    e = html.escape
    up = "../" if folder else ""
    root = up + "../../"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "name": "Mantel", "alternateName": ["Mantel – Photo Widget"],
         "operatingSystem": "iOS 17 or later", "applicationCategory": "PhotographyApplication",
         "description": t["desc"], "url": BASE + folder, "installUrl": STORE,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "Free with a one-time Pro purchase. Not a subscription."},
         "author": {"@type": "Person", "name": "Minari Taniguchi"}, "inLanguage": hreflang},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
    ]}
    alts = "\n".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (h, BASE, f) for _, f, h, _ in LANGS)
    langs = " · ".join(('<strong>%s</strong>' % e(l)) if c == code else '<a href="%s%s">%s</a>' % (up, f, e(l)) for c, f, _, l in LANGS)
    out = ["<!doctype html>", '<html lang="%s">' % hreflang, '<meta charset="utf-8">',
           '<script src="/minari-app-feeds/legacy-notice.js" defer></script>',
           '<meta name="viewport" content="width=device-width, initial-scale=1">',
           "<title>%s</title>" % e(t["title"]),
           '<meta name="description" content="%s">' % e(t["desc"]),
           '<link rel="canonical" href="%s%s">' % (BASE, folder), alts,
           '<link rel="alternate" hreflang="x-default" href="%sen/">' % BASE,
           STYLE_BLOCK,
           '<script type="application/ld+json">\n%s\n</script>' % json.dumps(ld, ensure_ascii=False, indent=2),
           "", "<h1>Mantel</h1>", '<p class="tagline">%s</p>' % e(t["tagline"]), '<p class="langs">%s</p>' % langs,
           '<p class="lede">%s</p>' % e(t["lede"]), '<a class="cta" href="%s">%s</a>' % (STORE, e(t["cta"])),
           "<h2>%s</h2>" % e(t["h_howto"]), "<ol>" + "".join("<li>%s</li>" % e(s) for s in t["steps"]) + "</ol>",
           "<h2>%s</h2>" % e(t["h_more"])]
    for h, b in t["more"]:
        out.append("<p><strong>%s</strong><br>%s</p>" % (e(h), e(b)))
    out += ["<h2>%s</h2>" % e(t["h_price"]), "<ul>" + "".join("<li>%s</li>" % e(s) for s in t["price"]) + "</ul>",
            "<h2>%s</h2>" % e(t["h_faq"])]
    for q, a in t["faq"]:
        out.append("<p><strong>%s</strong><br>%s</p>" % (e(q), e(a)))
    out += ["<h2>%s</h2>" % e(t["h_spec"]), "<ul>" + "".join("<li>%s</li>" % e(s) for s in t["spec"]) + "</ul>",
            "<h2>%s</h2>" % e(t["h_privacy"]),
            '<p>%s <a href="%sprivacy/mantel/">%s</a></p>' % (e(t["privacy"]), root, e(t["privacy_link"])),
            '<p class="dim" style="margin-top:3rem">\n  <a href="%s">minari-app-feeds</a> · Made by Minari Taniguchi\n</p>' % root, ""]
    return "\n".join(out)


# 見た目（style）は 1.3 までのページのものをそのまま使う。
_src = open(os.path.join(HERE, "index.html")).read()
STYLE_BLOCK = _src[_src.index("<style>"):_src.index("</style>") + len("</style>")] + "\n<style> ol { padding-left: 1.3rem; } ol li { margin: .45rem 0; } </style>"

if __name__ == "__main__":
    for code, folder, hreflang, label in LANGS:
        d = os.path.join(HERE, folder)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(page(code, folder, hreflang, label))
        print("wrote", folder or "(ja)")
