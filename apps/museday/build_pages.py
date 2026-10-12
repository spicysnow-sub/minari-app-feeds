"""Museday の公式ページ（使い方とよくある質問）を5言語で作る（2026-10-12・1.3・Mantel の build_pages.py の型）.

元データはこのファイルだけ。直すときはここを直して `python3 build_pages.py` → 各言語の index.html が上書きされる。
フォルダ＝ja はこの直下、en/ es/ pt/ zh/ はサブフォルダ。アプリの「使い方とよくある質問」はここへ飛ぶ。
ja・en の見出し・紹介文・よくある質問は 1.2 までの手書きページの文をそのまま引き継いだ。es・pt・zh は Claude の訳（2026-10-12 本人指示）。
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://tdsms-mnr.github.io/minari-app-feeds/apps/museday/"
STORE = "https://apps.apple.com/app/id6816428852"

LANGS = [  # (コード, フォルダ, hreflang, 表示名)
    ("ja", "", "ja", "日本語"),
    ("en", "en/", "en", "English"),
    ("es", "es/", "es", "Español"),
    ("pt", "pt/", "pt-BR", "Português"),
    ("zh", "zh/", "zh-Hans", "简体中文"),
]

# プライバシーポリシーは ja（先頭）と en（#en）だけ＝es/pt/zh は #en へ。
PRIVACY_ANCHOR = {"ja": "", "en": "#en", "es": "#en", "pt": "#en", "zh": "#en"}

T = {
"ja": dict(
    title="Museday — 毎日1枚の名画をホーム画面に｜買い切り・広告なし・オフライン",
    desc="Museday は、毎日1枚の名画をホーム画面のウィジェットに届ける iPhone アプリです。ファン・ゴッホ、フェルメール、レンブラントなど280人以上の画家によるパブリックドメインの名画511枚を同梱しているので、通信なしで使えます。サブスクなし・広告なし・アカウント不要。Pro は買い切りです。",
    tagline="毎朝、ホーム画面に1枚の名画を。",
    lede="Museday は、毎日1枚の名画をホーム画面のウィジェットに届ける iPhone アプリです。0時になると新しい絵に替わるので、スマホを開くたびに、小さな美術館をひとめぐりできます。",
    cta="App Store で見る",
    h_howto="使い方",
    steps=["Museday を開くと、今日の絵が出ます。「この絵について」から、美術館による作品の解説が読めます。",
           "ホーム画面の何もないところを長押しし、「編集」→「ウィジェットを追加」から Museday を選んで置きます。",
           "置いたウィジェットは、毎日0時に次の絵へ替わります。朝・昼・夕・夜で、絵のまわりの台紙の色も少しずつ変わります。"],
    h_more="もっと楽しむ",
    more=[("絵をさがす", "今日の画面の「絵をさがす」から、風景・人物・花と静物・海と水辺・動物・街と建物のテーマや、時代・所蔵館ごとに、すべての絵を一覧で見られます。開けるのは直近7日に出た絵まで、それより前の絵は Pro で開けます。"),
          ("お気に入りに残す", "今日の画面や絵の詳細で ♡ をタップすると、お気に入りに残ります。今日の画面の「お気に入り」から見返せます。"),
          ("本物を見に行く", "絵の詳細にある美術館の名前をタップすると、マップでその美術館が開きます。展示替えなどで見られない時期もあるので、お出かけ前に美術館のサイトをご確認ください。"),
          ("Large で解説の一文も（Pro）", "Large ウィジェットには、題名・作者・年に加えて、解説の最初の一文が添えられます。"),
          ("ウィジェットに出す絵を選ぶ（Pro）", "ウィジェットを長押しして「ウィジェットを編集」を開き、「表示する絵」から、お気に入り・テーマ・時代・所蔵館を選びます。ウィジェットごとに違う絵を出せます。Medium と Large は「見せ方」で「絵と題名」か「絵のみ」も選べます。"),
          ("これまでの絵と絞り込み（Pro）", "今日の画面の「これまでの絵」から、どの日の絵も開けます。時代・所蔵館・作者で絞り込めます。")],
    h_price="料金",
    price=["無料：今日の絵を出す Small ウィジェット、ロック画面のウィジェット、美術館の解説、お気に入り、直近7日、絵をさがす（一覧）、本物を見に行く。期限はなく、ずっと使えます。",
           "Pro（買い切り。サブスクではありません）：Medium と Large のウィジェット（絵と題名／絵のみ）、お気に入りやテーマ・時代・所蔵館を選んで出すウィジェット、これまでの全部の絵と絞り込み。",
           "広告は表示しません。アカウント登録も不要です。"],
    h_faq="よくある質問",
    faq=[("サブスクですか？", "いいえ。ダウンロードは無料で、Pro は1回だけの買い切りです。サブスクではなく、自動で更新されることもありません。"),
         ("広告は出ますか？", "出ません。無料版にも Pro にも、広告は一切ありません。"),
         ("アカウントや通信は必要ですか？", "アカウントは要りません。511枚の絵と解説をすべてアプリに同梱しているので、通信がなくても毎日絵が替わります。"),
         ("Medium や Large のウィジェットに「Museday Pro」と出ます。", "Medium と Large のウィジェットは Pro の機能です。無料のときは絵がぼかして表示され、題名の場所に「Museday Pro」と出ます。タップすると Pro の案内が開きます。"),
         ("別の iPhone で Pro が使えません。", "購入したときと同じ Apple アカウントで App Store にサインインしているか確かめてから、Museday の設定にある「購入を復元」を押してください。購入した直後は、反映まで少し時間がかかることがあります。"),
         ("絵はどこから来ていますか？", "画像はシカゴ美術館・メトロポリタン美術館・アムステルダム国立美術館・ワシントン・ナショナル・ギャラリーがパブリックドメイン（CC0）として公開しているものです。解説はシカゴ美術館の文章（CC BY 4.0）とアムステルダム国立美術館の文章（CC0）で、翻訳は Museday によるものです。"),
         ("問い合わせはどこからできますか？", "Museday の設定 →「問い合わせ・不具合の報告」からメールを送れます。アプリと iOS のバージョン、機種が自動で入ります。")],
    h_spec="対応",
    spec=["iPhone（iOS 17 以降）", "日本語・英語・スペイン語・ポルトガル語（ブラジル）・中国語（簡体字）"],
    h_privacy="プライバシー",
    privacy="お気に入りや設定は端末の中だけに保存します。どの絵を見たかを記録することはありません。送るのは匿名の利用状況だけで、設定から止められます。",
    privacy_link="プライバシーポリシー",
),
"en": dict(
    title="Museday — Art of the Day widget for iPhone (one-time purchase, no ads, works offline)",
    desc="Museday is an art-of-the-day app for iPhone: a famous painting appears in your Home Screen widget every day. 511 public-domain masterpieces by Van Gogh, Vermeer, Rembrandt and more than 280 other artists are built in, so it works offline. No subscription, no ads, no account. Pro is a one-time purchase.",
    tagline="A masterpiece on your Home Screen, every morning.",
    lede="Museday is an art-of-the-day app for iPhone. Each night at midnight, a new painting takes its place in your Home Screen widget — a quiet museum visit every time you unlock your phone.",
    cta="View on the App Store",
    h_howto="How to use",
    steps=["Open Museday to see today’s painting. Tap “About this painting” to read the museum’s own story of the work.",
           "Touch and hold an empty spot on your Home Screen, tap “Edit” → “Add Widget”, and add Museday.",
           "The widget changes to the next painting every day at midnight. The mat around the painting shifts a little through morning, day, evening and night."],
    h_more="Getting more out of it",
    more=[("Browse paintings", "Tap “Browse paintings” on the Today screen to see every painting by theme — landscapes, people, flowers & still life, sea & water, animals, towns & buildings — or by period or museum. Paintings shown in the last 7 days open for free; earlier ones open with Pro."),
          ("Keep your favorites", "Tap ♡ on the Today screen or on a painting’s page to keep it. Find them again under “Favorites” on the Today screen."),
          ("See it in person", "Tap the museum’s name on a painting’s page to open the museum in Maps. Paintings aren’t always on display, so check the museum’s website before you visit."),
          ("A line of the story on Large (Pro)", "The Large widget adds the first line of the painting’s story under its title, artist and year."),
          ("Choose what a widget shows (Pro)", "Touch and hold the widget, open “Edit Widget”, and under “Show” pick your favorites, a theme, a period or a museum. Each widget can show different paintings. On Medium and Large, “Style” lets you choose “Painting and title” or “Painting only”."),
          ("Every past day, with filters (Pro)", "Open any day’s painting from “Past days” on the Today screen, and filter by period, museum and artist.")],
    h_price="Pricing",
    price=["Free: today’s painting in a Small widget, Lock Screen widgets, the museum text, favorites, the last 7 days, Browse paintings (the list), and See it in person. No time limit.",
           "Pro (one-time purchase, not a subscription): Medium and Large widgets (painting and title, or painting only), widgets that show your favorites or a chosen theme, period or museum, and every painting so far with filters.",
           "No ads. No account needed."],
    h_faq="FAQ",
    faq=[("Is Museday a subscription?", "No. Museday is free to download, and Pro is a single one-time purchase. There is no subscription and nothing renews."),
         ("Does Museday show ads?", "No. There are no ads anywhere in the app, in the free version or in Pro."),
         ("Do I need an account or an internet connection?", "No account is needed. All 511 paintings and their texts are built into the app, so the widget keeps changing every day even offline."),
         ("My Medium or Large widget says “Museday Pro”.", "Medium and Large widgets are part of Pro. In the free version the painting is blurred, with “Museday Pro” where the title would be. Tap it to see what Pro includes."),
         ("Pro isn’t working on my other iPhone.", "Check that the App Store on that iPhone is signed in with the same Apple Account you bought with, then tap “Restore Purchases” in Museday’s Settings. Right after buying, it can take a little while to show up."),
         ("Where do the paintings come from?", "The images are public-domain (CC0) releases from the Art Institute of Chicago, The Metropolitan Museum of Art, the Rijksmuseum and the National Gallery of Art. The texts are by the Art Institute of Chicago (CC BY 4.0) and the Rijksmuseum (CC0); translations are by Museday."),
         ("How do I contact you?", "In Museday, go to Settings → “Contact / report a problem” to send an email. The app version, iOS version and iPhone model are filled in for you.")],
    h_spec="Requirements",
    spec=["iPhone (iOS 17 or later)", "English, Japanese, Spanish, Portuguese (Brazil), Simplified Chinese"],
    h_privacy="Privacy",
    privacy="Your favorites and settings stay on your iPhone. Museday never records which paintings you look at. It sends only anonymous usage records, which you can turn off in Settings.",
    privacy_link="Privacy Policy",
),
"es": dict(
    title="Museday — Widget con una obra maestra al día para iPhone (pago único, sin anuncios, sin conexión)",
    desc="Museday es una app para iPhone que pone una obra maestra en el widget de tu pantalla de inicio cada día. Incluye 511 obras de dominio público de Van Gogh, Vermeer, Rembrandt y más de 280 artistas, así que funciona sin conexión. Sin suscripción, sin anuncios, sin cuenta. Pro es un pago único.",
    tagline="Una obra maestra en tu pantalla de inicio, cada mañana.",
    lede="Museday es una app para iPhone con una obra de arte al día. Cada medianoche, una nueva pintura ocupa su lugar en el widget de tu pantalla de inicio: una visita tranquila al museo cada vez que desbloqueas el teléfono.",
    cta="Ver en el App Store",
    h_howto="Cómo usar",
    steps=["Abre Museday para ver la obra de hoy. Toca «Sobre esta obra» para leer la historia de la obra contada por el museo.",
           "Mantén pulsado un espacio vacío de la pantalla de inicio, toca “Editar” → “Añadir widget” y añade Museday.",
           "El widget cambia a la siguiente obra cada día a medianoche. El paspartú alrededor de la pintura cambia un poco por la mañana, el día, la tarde y la noche."],
    h_more="Saca más partido",
    more=[("Explorar obras", "Toca “Explorar obras” en la pantalla de hoy para ver todas las obras por tema —paisajes, personas, flores y bodegones, mar y agua, animales, ciudades y edificios—, por época o por museo. Las obras de los últimos 7 días se abren gratis; las anteriores, con Pro."),
          ("Guarda tus favoritas", "Toca ♡ en la pantalla de hoy o en la página de una obra para guardarla. Las encontrarás en “Favoritas”, en la pantalla de hoy."),
          ("Verla en persona", "Toca el nombre del museo en la página de una obra para abrirlo en Mapas. Las obras no siempre están expuestas: consulta la web del museo antes de tu visita."),
          ("Una frase de la historia en el widget grande (Pro)", "El widget grande añade la primera frase del texto sobre la obra, debajo del título, el artista y el año."),
          ("Elige qué muestra cada widget (Pro)", "Mantén pulsado el widget, abre “Editar widget” y, en “Mostrar”, elige tus favoritas, un tema, una época o un museo. Cada widget puede mostrar obras distintas. En el mediano y el grande, en “Estilo” puedes elegir “Obra y título” o “Solo la obra”."),
          ("Todos los días anteriores, con filtros (Pro)", "Abre la obra de cualquier día desde “Días anteriores”, en la pantalla de hoy, y filtra por época, museo y artista.")],
    h_price="Precio",
    price=["Gratis: la obra de hoy en un widget pequeño, widgets para la pantalla bloqueada, el texto del museo, favoritas, los últimos 7 días, Explorar obras (la lista) y Verla en persona. Sin límite de tiempo.",
           "Pro (pago único, no es una suscripción): widgets mediano y grande (obra y título, o solo la obra), widgets que muestran tus favoritas o un tema, una época o un museo, y todas las obras hasta hoy con filtros.",
           "Sin anuncios. No necesitas cuenta."],
    h_faq="Preguntas frecuentes",
    faq=[("¿Museday es una suscripción?", "No. Museday se descarga gratis y Pro es un único pago. No hay suscripción y nada se renueva."),
         ("¿Museday muestra anuncios?", "No. No hay anuncios en ninguna parte de la app, ni en la versión gratuita ni en Pro."),
         ("¿Necesito una cuenta o conexión a internet?", "No necesitas cuenta. Las 511 obras y sus textos vienen dentro de la app, así que el widget sigue cambiando cada día aunque no tengas conexión."),
         ("Mi widget mediano o grande dice “Museday Pro”.", "Los widgets mediano y grande son parte de Pro. En la versión gratuita la pintura aparece difuminada, con “Museday Pro” donde iría el título. Tócalo para ver qué incluye Pro."),
         ("Pro no funciona en mi otro iPhone.", "Comprueba que el App Store de ese iPhone use la misma cuenta de Apple con la que compraste y luego toca “Restaurar compras” en los Ajustes de Museday. Justo después de comprar, puede tardar un poco en aparecer."),
         ("¿De dónde vienen las obras?", "Las imágenes son de dominio público (CC0), publicadas por el Art Institute of Chicago, The Metropolitan Museum of Art, el Rijksmuseum y la National Gallery of Art. Los textos son del Art Institute of Chicago (CC BY 4.0) y del Rijksmuseum (CC0); las traducciones son de Museday."),
         ("¿Cómo me pongo en contacto?", "En Museday, ve a Ajustes → “Contacto / informar de un problema” para enviar un correo. La versión de la app, la de iOS y el modelo de iPhone se rellenan solos.")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 o posterior)", "Inglés, japonés, español, portugués (Brasil) y chino simplificado"],
    h_privacy="Privacidad",
    privacy="Tus favoritas y ajustes se quedan en tu iPhone. Museday nunca registra qué obras miras. Solo envía datos de uso anónimos, que puedes desactivar en Ajustes.",
    privacy_link="Política de privacidad (en inglés)",
),
"pt": dict(
    title="Museday — Widget com uma obra-prima por dia para iPhone (compra única, sem anúncios, offline)",
    desc="Museday é um app para iPhone que coloca uma obra-prima no widget da sua tela de início todos os dias. Traz 511 obras em domínio público de Van Gogh, Vermeer, Rembrandt e mais de 280 artistas, por isso funciona offline. Sem assinatura, sem anúncios, sem conta. O Pro é uma compra única.",
    tagline="Uma obra-prima na sua tela de início, toda manhã.",
    lede="Museday é um app para iPhone com uma obra de arte por dia. Toda meia-noite, uma nova pintura ocupa o widget da sua tela de início — uma visita tranquila ao museu toda vez que você desbloqueia o celular.",
    cta="Ver na App Store",
    h_howto="Como usar",
    steps=["Abra o Museday para ver a obra de hoje. Toque em “Sobre esta obra” para ler a história da obra contada pelo museu.",
           "Toque e segure um espaço vazio da tela de início, toque em “Editar” → “Adicionar widget” e adicione o Museday.",
           "O widget muda para a próxima obra todo dia à meia-noite. O passe-partout ao redor da pintura muda um pouco de manhã, de dia, à tarde e à noite."],
    h_more="Aproveite mais",
    more=[("Explorar obras", "Toque em “Explorar obras” na tela de hoje para ver todas as obras por tema — paisagens, pessoas, flores e naturezas-mortas, mar e água, animais, cidades e edifícios — ou por época e museu. As obras dos últimos 7 dias abrem grátis; as anteriores, com o Pro."),
          ("Guarde suas favoritas", "Toque em ♡ na tela de hoje ou na página de uma obra para guardá-la. Elas ficam em “Favoritas”, na tela de hoje."),
          ("Veja pessoalmente", "Toque no nome do museu na página de uma obra para abri-lo no Mapas. As obras nem sempre estão em exposição: confira o site do museu antes da visita."),
          ("Uma frase da história no widget grande (Pro)", "O widget grande traz a primeira frase do texto sobre a obra, abaixo do título, do artista e do ano."),
          ("Escolha o que cada widget mostra (Pro)", "Toque e segure o widget, abra “Editar widget” e, em “Mostrar”, escolha suas favoritas, um tema, uma época ou um museu. Cada widget pode mostrar obras diferentes. No médio e no grande, em “Estilo” você escolhe “Obra e título” ou “Só a obra”."),
          ("Todos os dias anteriores, com filtros (Pro)", "Abra a obra de qualquer dia em “Dias anteriores”, na tela de hoje, e filtre por época, museu e artista.")],
    h_price="Preço",
    price=["Grátis: a obra de hoje em um widget pequeno, widgets da tela bloqueada, o texto do museu, favoritas, os últimos 7 dias, Explorar obras (a lista) e Veja pessoalmente. Sem prazo.",
           "Pro (compra única, não é assinatura): widgets médio e grande (obra e título, ou só a obra), widgets que mostram suas favoritas ou um tema, uma época ou um museu, e todas as obras até hoje com filtros.",
           "Sem anúncios. Não precisa de conta."],
    h_faq="Perguntas frequentes",
    faq=[("O Museday é uma assinatura?", "Não. O Museday é gratuito para baixar e o Pro é uma única compra. Não há assinatura e nada é renovado."),
         ("O Museday mostra anúncios?", "Não. Não há anúncios em nenhuma parte do app, nem na versão grátis nem no Pro."),
         ("Preciso de conta ou de internet?", "Não precisa de conta. As 511 obras e seus textos vêm dentro do app, então o widget continua mudando todo dia mesmo offline."),
         ("Meu widget médio ou grande mostra “Museday Pro”.", "Os widgets médio e grande fazem parte do Pro. Na versão grátis a pintura aparece desfocada, com “Museday Pro” no lugar do título. Toque para ver o que o Pro inclui."),
         ("O Pro não funciona no meu outro iPhone.", "Verifique se a App Store desse iPhone está com a mesma Conta Apple usada na compra e toque em “Restaurar compras” nos Ajustes do Museday. Logo após a compra, pode levar um tempinho para aparecer."),
         ("De onde vêm as obras?", "As imagens são de domínio público (CC0), publicadas pelo Art Institute of Chicago, pelo The Metropolitan Museum of Art, pelo Rijksmuseum e pela National Gallery of Art. Os textos são do Art Institute of Chicago (CC BY 4.0) e do Rijksmuseum (CC0); as traduções são do Museday."),
         ("Como entro em contato?", "No Museday, vá em Ajustes → “Contato / relatar um problema” para enviar um e-mail. A versão do app, a do iOS e o modelo do iPhone já vêm preenchidos.")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 ou posterior)", "Inglês, japonês, espanhol, português (Brasil) e chinês simplificado"],
    h_privacy="Privacidade",
    privacy="Suas favoritas e ajustes ficam no seu iPhone. O Museday nunca registra quais obras você vê. Ele envia apenas dados de uso anônimos, que você pode desativar nos Ajustes.",
    privacy_link="Política de privacidade (em inglês)",
),
"zh": dict(
    title="Museday — 每天一幅名画的 iPhone 小组件（买断制、无广告、可离线）",
    desc="Museday 是一款 iPhone App，每天把一幅名画放进你的主屏幕小组件。内置梵高、维米尔、伦勃朗等 280 多位画家的 511 幅公有领域名画，无需联网即可使用。没有订阅、没有广告、无需账户。Pro 为一次性买断。",
    tagline="每天早上，主屏幕上的一幅名画。",
    lede="Museday 是一款每天一幅名画的 iPhone App。每到午夜，新的画作就会出现在你的主屏幕小组件里——每次解锁手机，都像安静地逛一趟美术馆。",
    cta="在 App Store 查看",
    h_howto="使用方法",
    steps=["打开 Museday，就能看到今日画作。点按“关于这幅画”，可以阅读美术馆对这件作品的介绍。",
           "在主屏幕空白处长按，点按“编辑”→“添加小组件”，然后添加 Museday。",
           "小组件每天午夜换成下一幅画。画作周围的卡纸颜色，也会随早上、白天、傍晚和夜晚稍稍变化。"],
    h_more="更多玩法",
    more=[("浏览画作", "在今日画面点按“浏览画作”，可按主题（风景、人物、花卉与静物、海与水边、动物、城镇与建筑）、时代或美术馆查看全部画作。最近 7 天出现过的画可以免费打开，更早的画用 Pro 打开。"),
          ("收藏喜欢的画", "在今日画面或画作页面点按 ♡ 即可收藏。可以在今日画面的“收藏”里再次查看。"),
          ("去看原作", "在画作页面点按美术馆名称，即可在地图中打开这家美术馆。画作并非一直展出，出发前请先查看美术馆官网。"),
          ("大尺寸小组件附上介绍的第一句（Pro）", "大尺寸小组件会在标题、艺术家和年代下面，附上画作介绍的第一句。"),
          ("选择小组件显示的画（Pro）", "长按小组件，打开“编辑小组件”，在“显示”中选择你的收藏、某个主题、某个时代或某家美术馆。每个小组件都可以显示不同的画。中、大尺寸还可以在“样式”中选择“画作与标题”或“仅画作”。"),
          ("全部往日画作与筛选（Pro）", "在今日画面的“往日画作”中打开任何一天的画，还能按时代、美术馆和艺术家筛选。")],
    h_price="价格",
    price=["免费：显示今日画作的小尺寸小组件、锁定屏幕小组件、美术馆的介绍、收藏、最近 7 天、浏览画作（列表），以及“去看原作”。没有期限。",
           "Pro（一次性买断，不是订阅）：中、大尺寸小组件（画作与标题／仅画作），显示收藏或指定主题、时代、美术馆的小组件，以及至今全部画作与筛选。",
           "没有广告，也无需注册账户。"],
    h_faq="常见问题",
    faq=[("Museday 是订阅制吗？", "不是。Museday 可免费下载，Pro 只需购买一次。没有订阅，也不会自动续费。"),
         ("Museday 有广告吗？", "没有。无论免费版还是 Pro，App 里都没有任何广告。"),
         ("需要账户或联网吗？", "不需要账户。511 幅画和介绍都内置在 App 中，即使不联网，小组件也会每天更换。"),
         ("中、大尺寸小组件上显示“Museday Pro”。", "中、大尺寸小组件属于 Pro。免费版的画作会模糊显示，标题的位置显示“Museday Pro”。点按即可查看 Pro 包含的内容。"),
         ("在另一台 iPhone 上用不了 Pro。", "请确认那台 iPhone 在 App Store 登录的是购买时使用的同一个 Apple 账户，然后在 Museday 的设置中点按“恢复购买”。刚购买后，可能需要稍等片刻才会生效。"),
         ("画作从哪里来？", "图像来自芝加哥艺术博物馆、大都会艺术博物馆、荷兰国立博物馆和美国国家美术馆以公有领域（CC0）公开的作品。介绍文字出自芝加哥艺术博物馆（CC BY 4.0）和荷兰国立博物馆（CC0），译文由 Museday 提供。"),
         ("如何联系你们？", "在 Museday 中前往设置 →“联系 / 报告问题”即可发送邮件。App 版本、iOS 版本和 iPhone 型号会自动填好。")],
    h_spec="支持",
    spec=["iPhone（iOS 17 或更高版本）", "英语、日语、西班牙语、葡萄牙语（巴西）、简体中文"],
    h_privacy="隐私",
    privacy="你的收藏和设置只保存在你的 iPhone 上。Museday 从不记录你看了哪些画。它只发送匿名的使用情况，你可以在设置中关闭。",
    privacy_link="隐私政策（英文）",
),
}

def page(code, folder, hreflang, label):
    t = T[code]
    e = html.escape
    up = "../" if folder else ""
    root = up + "../../"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "name": "Museday", "alternateName": ["Museday – Daily Art Widget"],
         "operatingSystem": "iOS 17 or later", "applicationCategory": "LifestyleApplication",
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
           "", "<h1>Museday</h1>", '<p class="tagline">%s</p>' % e(t["tagline"]), '<p class="langs">%s</p>' % langs,
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
            '<p>%s <a href="%sprivacy/museday/%s">%s</a></p>' % (e(t["privacy"]), root, PRIVACY_ANCHOR[code], e(t["privacy_link"])),
            '<p class="dim" style="margin-top:3rem">\n  <a href="%s">minari-app-feeds</a> · Made by Minari Taniguchi\n</p>' % root, ""]
    return "\n".join(out)


# 見た目（style）は 1.2 までのページのものをそのまま使う。
_src = open(os.path.join(HERE, "index.html")).read()
STYLE_BLOCK = _src[_src.index("<style>"):_src.index("</style>") + len("</style>")] + "\n<style> ol { padding-left: 1.3rem; } ol li { margin: .45rem 0; } </style>"

if __name__ == "__main__":
    for code, folder, hreflang, label in LANGS:
        d = os.path.join(HERE, folder)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(page(code, folder, hreflang, label))
        print("wrote", folder or "(ja)")
