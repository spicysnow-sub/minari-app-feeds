"""Weekly Bump の公式ページ（使い方とよくある質問）を6言語で作る（2026-10-12・1.1・Museday の build_pages.py の型）.

元データはこのファイルだけ。直すときはここを直して `python3 build_pages.py` → 各言語の index.html が上書きされる。
フォルダ＝ja はこの直下、en/ th/ ko/ pt/ es/ はサブフォルダ。アプリの「使い方とよくある質問」はここへ飛ぶ。
1.1 の内容（パートナーと共有・Small 無料・ふたご／みつご・花びら・ローズ／ピオニー）。ja・en は 1.0 の手書きページを引き継いで書き直し、th/ko/pt/es は Claude の訳。
★店頭・ページで「Bloom」の語は使わない（妊娠アプリに同名が13本・2026-10-12 調べ）。医療上の助言はしない。
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://tdsms-mnr.github.io/minari-app-feeds/apps/weeklybump/"
STORE = "https://apps.apple.com/app/id6815057854"

LANGS = [  # (コード, フォルダ, hreflang, 表示名)
    ("ja", "", "ja", "日本語"),
    ("en", "en/", "en", "English"),
    ("th", "th/", "th", "ไทย"),
    ("ko", "ko/", "ko", "한국어"),
    ("pt", "pt/", "pt-BR", "Português"),
    ("es", "es/", "es", "Español"),
]

# プライバシーポリシーは ja（先頭）と en（#en）だけ。
PRIVACY_ANCHOR = {"ja": "", "en": "#en", "th": "#en", "ko": "#en", "pt": "#en", "es": "#en"}

T = {
"ja": dict(
    title="Weekly Bump — 妊娠週数をホーム画面に。ひと月1枚の花びらで（サブスクなし）",
    desc="Weekly Bump は、妊娠週数と予定日まであと何日かをホーム画面のウィジェットに置く iPhone アプリです。ひと月に1枚ずつ花びらが色づき、10枚で40週。パートナーのウィジェットにも今週とおなかの写真を届けられます。ふたご・みつごにも対応。サブスクなし・広告なし・アカウント不要。",
    tagline="妊娠週数を、ひと月1枚の花びらで。",
    lede="予定日を一度入れれば、いま何週何日か、予定日まであと何日かが毎日0時に更新されます。ひと月ごとに花びらが1枚ずつ色づき、10枚そろうと40週です。",
    cta="App Store で見る",
    h_howto="使い方",
    steps=["Weekly Bump を開き、予定日（または最終月経の開始日）を入れます。ふたご・みつごのときは人数を選び、呼び名を人数ぶん入れられます。",
           "ホーム画面の何もないところを長押しし、「編集」→「ウィジェットを追加」から Weekly Bump を選んで置きます。Small は無料です。",
           "ウィジェットは毎日0時に更新されます。花びらは、今月の1枚が週ごとに少しずつ色づいていきます。"],
    h_more="もっと楽しむ",
    more=[("パートナーと共有（Pro）", "本体の「パートナーと共有」からリンクを送ると、相手の iPhone のウィジェットに今週と、アルバムに入れた今週のおなかの写真が届きます。1回の購入で2人とも Pro です。相手も Weekly Bump を入れてリンクを開いてください。"),
          ("花の色を選ぶ", "設定の「外観」で、ローズとピオニーから選べます。ウィジェットも同じ色になります。"),
          ("おなかの写真アルバム（Pro）", "1週に1枚、40週を1か所に。スライドショーで見返せます。"),
          ("節目のカウントダウン（Pro）", "産休やベビーシャワーなど、自分の節目まであと何日かをウィジェットに出せます。"),
          ("記録を閉じる", "設定の「記録を閉じる」で、予定日・写真・節目を消し、ウィジェットを空に戻せます。パートナーと共有していたら、相手の画面からも消えます。")],
    h_price="料金",
    price=["無料：アプリの中の週数・あと何日・花びら、Small ウィジェット、花の色。期限はありません。",
           "Pro（買い切り・サブスクではありません）：パートナーと共有、Medium・Large・ロック画面のウィジェット、おなかの写真アルバム、節目、花のシェア画像、週替わりのお知らせ。",
           "広告なし・アカウント不要。"],
    h_faq="よくある質問",
    faq=[("サブスクですか？", "いいえ。ダウンロードは無料で、Pro は1回だけの買い切りです。自動で更新されることはありません。"),
         ("パートナーも Pro を買う必要がありますか？", "いいえ。誘う側が Pro なら、リンクを開いた相手も Pro として使えます。"),
         ("パートナーと共有すると、予定日はどこに送られますか？", "あなた自身の iCloud に保存され、リンクを開いた人にだけ表示されます。開発者のサーバーには送られず、開発者が見ることもできません。共有しない限り、端末の外には出ません。"),
         ("ふたご・みつごに使えますか？", "使えます。人数を選ぶと、呼び名を人数ぶん入れられます。週数と予定日は1つです。"),
         ("リンクを開いても何も起きません。", "相手の iPhone に Weekly Bump が入っているか確かめてから、もう一度リンクを開いてください。iCloud にサインインしている必要があります。"),
         ("医療上の助言をしますか？", "しません。予定日から週数とあと何日かを出すだけです。"),
         ("問い合わせ先は？", "Weekly Bump の設定 →「問い合わせ・不具合の報告」からメールを送れます。アプリの版・iOS の版・機種が入った状態で開きます（予定日・呼び名・写真は入りません）。")],
    h_spec="対応",
    spec=["iPhone（iOS 17 以降）", "日本語・英語・タイ語・韓国語・ポルトガル語（ブラジル）・スペイン語"],
    h_privacy="プライバシー",
    privacy="予定日・呼び名・写真は端末の中にあります。パートナーと共有を選んだときだけ、あなたの iCloud を通って相手に届きます。送るのは匿名の利用状況だけで、設定から止められます。",
    privacy_link="プライバシーポリシー",
),
"en": dict(
    title="Weekly Bump — your pregnancy week on the Home Screen, one petal a month (no subscription)",
    desc="Weekly Bump puts your pregnancy week and days to go on your iPhone Home Screen. One petal fills in each month — ten petals, forty weeks. Share your week and this week's bump photo with your partner's widget. Twins and triplets supported. No subscription, no ads, no account.",
    tagline="Your pregnancy week, one petal a month.",
    lede="Add your due date once, and your Home Screen shows how far along you are and how many days to go, updated every midnight. One petal fills in each month; ten petals make forty weeks.",
    cta="View on the App Store",
    h_howto="How to use",
    steps=["Open Weekly Bump and enter your due date (or the first day of your last period). For twins or triplets, choose the number of babies and add a nickname for each.",
           "Touch and hold an empty area of your Home Screen, tap Edit → Add Widget, and add Weekly Bump. The Small widget is free.",
           "The widget updates every midnight. This month's petal fills in a little more each week."],
    h_more="More to enjoy",
    more=[("Share with your partner (Pro)", "Send a link from “Share with your partner”, and your partner's widget shows your week and this week's bump photo from your album. One purchase covers you both. Your partner needs Weekly Bump installed to open the link."),
          ("Choose a flower color", "In Settings → Appearance, choose Rose or Peony. Your widgets follow."),
          ("Bump album (Pro)", "One photo a week, all forty in one place, with a slideshow."),
          ("Milestone countdowns (Pro)", "Show days to go until maternity leave, a baby shower or your own milestones on your widget."),
          ("Close tracking", "Settings → “Close tracking” removes your due date, photos and milestones and clears your widgets. If you shared with your partner, it disappears from their screen too.")],
    h_price="Pricing",
    price=["Free: your week, days to go and petals in the app, the Small widget, and flower colors. No time limit.",
           "Pro (one-time purchase, not a subscription): sharing with your partner, Medium, Large and Lock Screen widgets, the bump album, milestones, a shareable flower card, and a weekly note.",
           "No ads. No account."],
    h_faq="FAQ",
    faq=[("Is it a subscription?", "No. Weekly Bump is free to download, and Pro is a single one-time purchase. Nothing renews."),
         ("Does my partner need to buy Pro too?", "No. If you have Pro, the person who opens your link gets Pro as well."),
         ("Where does my due date go when I share?", "It's stored in your own iCloud and shown only to people who open your link. It's never sent to the developer's servers, and the developer can't see it. Unless you share, it never leaves your device."),
         ("Does it work for twins or triplets?", "Yes. Choose the number of babies and add a nickname for each. There's one week count and one due date."),
         ("Nothing happens when my partner opens the link.", "Check that Weekly Bump is installed on their iPhone and open the link again. They need to be signed in to iCloud."),
         ("Is it medical advice?", "No. Weekly Bump only shows your week and days to go from your due date."),
         ("How do I contact you?", "In Weekly Bump, go to Settings → “Contact / report a problem” to send an email. The app version, iOS version and iPhone model are filled in (never your due date, nicknames or photos).")],
    h_spec="Requirements",
    spec=["iPhone (iOS 17 or later)", "English, Japanese, Thai, Korean, Portuguese (Brazil) and Spanish"],
    h_privacy="Privacy",
    privacy="Your due date, nicknames and photos stay on your device. Only when you choose to share do they go to your partner, through your own iCloud. The app sends only anonymous usage records, which you can turn off in Settings.",
    privacy_link="Privacy Policy",
),
"th": dict(
    title="Weekly Bump — อายุครรภ์บนหน้าจอโฮม เดือนละหนึ่งกลีบ (ไม่มีสมัครสมาชิก)",
    desc="Weekly Bump แสดงอายุครรภ์และจำนวนวันที่เหลือถึงวันกำหนดคลอดบนวิดเจ็ตหน้าจอโฮมของ iPhone กลีบดอกเติมสีเดือนละหนึ่งกลีบ สิบกลีบเท่ากับ 40 สัปดาห์ แชร์สัปดาห์และรูปท้องของสัปดาห์นี้ไปที่วิดเจ็ตของคู่ได้ รองรับแฝดสองและแฝดสาม ไม่มีสมัครสมาชิก ไม่มีโฆษณา ไม่ต้องมีบัญชี",
    tagline="อายุครรภ์ของคุณ เดือนละหนึ่งกลีบ",
    lede="ใส่วันกำหนดคลอดครั้งเดียว หน้าจอโฮมจะแสดงว่าคุณตั้งครรภ์กี่สัปดาห์และเหลืออีกกี่วัน อัปเดตทุกเที่ยงคืน กลีบดอกเติมสีเดือนละหนึ่งกลีบ ครบสิบกลีบคือ 40 สัปดาห์",
    cta="ดูใน App Store",
    h_howto="วิธีใช้",
    steps=["เปิด Weekly Bump แล้วใส่วันกำหนดคลอด (หรือวันแรกของประจำเดือนครั้งสุดท้าย) ถ้าเป็นแฝด เลือกจำนวนทารกและใส่ชื่อเล่นได้ทุกคน",
           "แตะค้างที่ที่ว่างบนหน้าจอโฮม แตะ แก้ไข → เพิ่มวิดเจ็ต แล้วเลือก Weekly Bump วิดเจ็ต Small ใช้ได้ฟรี",
           "วิดเจ็ตอัปเดตทุกเที่ยงคืน กลีบของเดือนนี้จะเติมสีขึ้นทีละนิดทุกสัปดาห์"],
    h_more="ใช้ได้อีกมาก",
    more=[("แชร์กับคู่ของคุณ (Pro)", "ส่งลิงก์จาก “แชร์กับคู่ของคุณ” วิดเจ็ตของคู่จะแสดงสัปดาห์และรูปท้องของสัปดาห์นี้จากอัลบั้มของคุณ ซื้อครั้งเดียวใช้ได้ทั้งสองคน คู่ของคุณต้องติดตั้ง Weekly Bump เพื่อเปิดลิงก์"),
          ("เลือกสีดอกไม้", "ในการตั้งค่า → รูปลักษณ์ เลือกกุหลาบหรือโบตั๋นได้ วิดเจ็ตจะใช้สีเดียวกัน"),
          ("อัลบั้มรูปท้อง (Pro)", "สัปดาห์ละหนึ่งรูป ครบ 40 สัปดาห์ในที่เดียว พร้อมสไลด์โชว์"),
          ("นับถอยหลังวันสำคัญ (Pro)", "แสดงจำนวนวันถึงวันลาคลอด งานเบบี้ชาวเวอร์ หรือวันสำคัญของคุณบนวิดเจ็ต"),
          ("ปิดการบันทึก", "การตั้งค่า → “ปิดการบันทึก” จะลบวันกำหนดคลอด รูป และวันสำคัญ แล้วล้างวิดเจ็ต ถ้าแชร์กับคู่ไว้ จะหายจากหน้าจอของคู่ด้วย")],
    h_price="ราคา",
    price=["ฟรี: สัปดาห์ วันที่เหลือ และกลีบดอกในแอป วิดเจ็ต Small และสีดอกไม้ ไม่มีกำหนดเวลา",
           "Pro (ซื้อครั้งเดียว ไม่ใช่สมัครสมาชิก): แชร์กับคู่ วิดเจ็ต Medium, Large และหน้าจอล็อก อัลบั้มรูปท้อง วันสำคัญ การ์ดดอกไม้สำหรับแชร์ และการแจ้งเตือนรายสัปดาห์",
           "ไม่มีโฆษณา ไม่ต้องมีบัญชี"],
    h_faq="คำถามที่พบบ่อย",
    faq=[("เป็นแบบสมัครสมาชิกไหม", "ไม่ใช่ ดาวน์โหลดฟรี และ Pro ซื้อครั้งเดียว ไม่มีการต่ออายุอัตโนมัติ"),
         ("คู่ของฉันต้องซื้อ Pro ด้วยไหม", "ไม่ต้อง ถ้าคุณมี Pro คนที่เปิดลิงก์ของคุณจะใช้ Pro ได้ด้วย"),
         ("เมื่อแชร์ วันกำหนดคลอดถูกส่งไปที่ไหน", "เก็บไว้ใน iCloud ของคุณเอง และแสดงเฉพาะคนที่เปิดลิงก์ของคุณ ไม่ถูกส่งไปยังเซิร์ฟเวอร์ของผู้พัฒนา และผู้พัฒนามองไม่เห็น ถ้าไม่แชร์ ข้อมูลจะไม่ออกจากเครื่อง"),
         ("ใช้กับแฝดสองหรือแฝดสามได้ไหม", "ได้ เลือกจำนวนทารกแล้วใส่ชื่อเล่นได้ทุกคน อายุครรภ์และวันกำหนดคลอดมีอย่างละหนึ่ง"),
         ("คู่เปิดลิงก์แล้วไม่มีอะไรเกิดขึ้น", "ตรวจสอบว่า iPhone ของคู่ติดตั้ง Weekly Bump แล้ว จากนั้นเปิดลิงก์อีกครั้ง ต้องลงชื่อเข้าใช้ iCloud ด้วย"),
         ("แอปให้คำแนะนำทางการแพทย์ไหม", "ไม่ Weekly Bump แสดงเพียงอายุครรภ์และวันที่เหลือจากวันกำหนดคลอด"),
         ("ติดต่ออย่างไร", "ใน Weekly Bump ไปที่ การตั้งค่า → “ติดต่อ / แจ้งปัญหา” เพื่อส่งอีเมล ระบบจะใส่เวอร์ชันแอป เวอร์ชัน iOS และรุ่น iPhone ให้ (ไม่มีวันกำหนดคลอด ชื่อเล่น หรือรูป)")],
    h_spec="รองรับ",
    spec=["iPhone (iOS 17 ขึ้นไป)", "ไทย อังกฤษ ญี่ปุ่น เกาหลี โปรตุเกส (บราซิล) และสเปน"],
    h_privacy="ความเป็นส่วนตัว",
    privacy="วันกำหนดคลอด ชื่อเล่น และรูปอยู่ในเครื่องของคุณ จะส่งถึงคู่ผ่าน iCloud ของคุณเองเฉพาะเมื่อคุณเลือกแชร์ แอปส่งเฉพาะข้อมูลการใช้งานแบบไม่ระบุตัวตน ซึ่งปิดได้ในการตั้งค่า",
    privacy_link="นโยบายความเป็นส่วนตัว (ภาษาอังกฤษ)",
),
"ko": dict(
    title="Weekly Bump — 임신 주수를 홈 화면에, 한 달에 꽃잎 한 장 (구독 없음)",
    desc="Weekly Bump는 임신 주수와 예정일까지 남은 날을 iPhone 홈 화면 위젯에 보여 주는 앱이에요. 한 달에 꽃잎 한 장씩 물들고, 열 장이면 40주. 파트너의 위젯에도 이번 주와 배 사진을 보낼 수 있어요. 쌍둥이·세쌍둥이 지원. 구독 없음·광고 없음·계정 불필요.",
    tagline="임신 주수를, 한 달에 꽃잎 한 장으로.",
    lede="예정일을 한 번 넣으면 지금 몇 주 며칠인지, 예정일까지 며칠 남았는지 매일 0시에 업데이트돼요. 한 달마다 꽃잎이 한 장씩 물들고, 열 장이 모이면 40주예요.",
    cta="App Store에서 보기",
    h_howto="사용법",
    steps=["Weekly Bump를 열고 예정일(또는 마지막 생리 시작일)을 넣어요. 쌍둥이·세쌍둥이라면 아기 수를 고르고 태명을 아기 수만큼 넣을 수 있어요.",
           "홈 화면의 빈 곳을 길게 누르고 편집 → 위젯 추가에서 Weekly Bump를 골라 놓아요. Small 위젯은 무료예요.",
           "위젯은 매일 0시에 업데이트돼요. 이번 달 꽃잎은 주마다 조금씩 물들어 가요."],
    h_more="더 즐기기",
    more=[("파트너와 공유 (Pro)", "“파트너와 공유”에서 링크를 보내면 상대의 위젯에 이번 주와 앨범에 넣은 이번 주 배 사진이 떠요. 한 번 구매로 둘 다 Pro예요. 상대도 Weekly Bump를 설치하고 링크를 열어야 해요."),
          ("꽃 색 고르기", "설정 → 화면 스타일에서 장미와 작약 중에 고를 수 있어요. 위젯도 같은 색이 돼요."),
          ("배 사진 앨범 (Pro)", "매주 한 장, 40주를 한곳에. 슬라이드쇼로 돌아볼 수 있어요."),
          ("기념일 카운트다운 (Pro)", "출산휴가나 베이비 샤워 등 나만의 기념일까지 남은 날을 위젯에 띄울 수 있어요."),
          ("기록 닫기", "설정 → “기록 닫기”로 예정일·사진·기념일을 지우고 위젯을 비울 수 있어요. 파트너와 공유했다면 상대 화면에서도 사라져요.")],
    h_price="요금",
    price=["무료: 앱 안의 주수·남은 날·꽃잎, Small 위젯, 꽃 색. 기한 없음.",
           "Pro (한 번 구매·구독 아님): 파트너와 공유, Medium·Large·잠금 화면 위젯, 배 사진 앨범, 기념일, 꽃 공유 이미지, 주간 알림.",
           "광고 없음·계정 불필요."],
    h_faq="자주 묻는 질문",
    faq=[("구독인가요?", "아니요. 다운로드는 무료이고 Pro는 한 번만 구매해요. 자동으로 갱신되지 않아요."),
         ("파트너도 Pro를 사야 하나요?", "아니요. 보내는 사람이 Pro라면 링크를 연 상대도 Pro로 쓸 수 있어요."),
         ("공유하면 예정일은 어디로 가나요?", "내 iCloud에 저장되고 링크를 연 사람에게만 보여요. 개발자 서버로 보내지 않으며 개발자는 볼 수 없어요. 공유하지 않으면 기기 밖으로 나가지 않아요."),
         ("쌍둥이·세쌍둥이도 쓸 수 있나요?", "네. 아기 수를 고르면 태명을 아기 수만큼 넣을 수 있어요. 주수와 예정일은 하나예요."),
         ("링크를 열어도 아무 일도 일어나지 않아요.", "상대 iPhone에 Weekly Bump가 설치되어 있는지 확인한 뒤 링크를 다시 열어 주세요. iCloud에 로그인되어 있어야 해요."),
         ("의학적 조언을 하나요?", "아니요. 예정일로부터 주수와 남은 날만 보여 줘요."),
         ("문의는 어디로 하나요?", "Weekly Bump 설정 → “문의 / 문제 신고”에서 메일을 보낼 수 있어요. 앱 버전·iOS 버전·기종이 들어간 상태로 열려요(예정일·태명·사진은 들어가지 않아요).")],
    h_spec="지원",
    spec=["iPhone (iOS 17 이상)", "한국어·영어·일본어·태국어·포르투갈어(브라질)·스페인어"],
    h_privacy="개인정보",
    privacy="예정일·태명·사진은 기기 안에 있어요. 공유를 선택했을 때만 내 iCloud를 거쳐 파트너에게 전달돼요. 앱이 보내는 것은 익명의 이용 기록뿐이며 설정에서 끌 수 있어요.",
    privacy_link="개인정보 처리방침 (영어)",
),
"pt": dict(
    title="Weekly Bump — sua semana de gravidez na Tela de Início, uma pétala por mês (sem assinatura)",
    desc="O Weekly Bump mostra sua semana de gravidez e quantos dias faltam para a data prevista em um widget na Tela de Início do iPhone. Uma pétala ganha cor a cada mês — dez pétalas, quarenta semanas. Compartilhe sua semana e a foto da barriga com o widget do seu parceiro. Suporte a gêmeos e trigêmeos. Sem assinatura, sem anúncios, sem conta.",
    tagline="Sua semana de gravidez, uma pétala por mês.",
    lede="Informe a data prevista uma vez e a Tela de Início mostra de quantas semanas você está e quantos dias faltam, atualizado toda meia-noite. Uma pétala ganha cor a cada mês; dez pétalas são quarenta semanas.",
    cta="Ver na App Store",
    h_howto="Como usar",
    steps=["Abra o Weekly Bump e informe a data prevista (ou o primeiro dia da última menstruação). Para gêmeos ou trigêmeos, escolha o número de bebês e dê um apelido para cada um.",
           "Toque e segure um espaço vazio da Tela de Início, toque em Editar → Adicionar Widget e adicione o Weekly Bump. O widget Small é grátis.",
           "O widget é atualizado toda meia-noite. A pétala do mês ganha um pouco mais de cor a cada semana."],
    h_more="Mais para aproveitar",
    more=[("Compartilhe com seu parceiro (Pro)", "Envie um link em “Compartilhar com seu parceiro” e o widget dele mostra sua semana e a foto da barriga desta semana do seu álbum. Uma compra vale para os dois. Seu parceiro precisa ter o Weekly Bump instalado para abrir o link."),
          ("Escolha a cor da flor", "Em Ajustes → Aparência, escolha Rosa ou Peônia. Os widgets seguem a mesma cor."),
          ("Álbum da barriga (Pro)", "Uma foto por semana, as quarenta num só lugar, com apresentação de slides."),
          ("Contagem para marcos (Pro)", "Mostre no widget quantos dias faltam para a licença-maternidade, o chá de bebê ou seus próprios marcos."),
          ("Encerrar acompanhamento", "Ajustes → “Encerrar acompanhamento” apaga a data prevista, as fotos e os marcos e limpa os widgets. Se você compartilhou com seu parceiro, some da tela dele também.")],
    h_price="Preço",
    price=["Grátis: sua semana, os dias que faltam e as pétalas no app, o widget Small e as cores da flor. Sem prazo.",
           "Pro (compra única, não é assinatura): compartilhar com o parceiro, widgets Medium, Large e da Tela Bloqueada, álbum da barriga, marcos, imagem da flor para compartilhar e aviso semanal.",
           "Sem anúncios. Não precisa de conta."],
    h_faq="Perguntas frequentes",
    faq=[("É uma assinatura?", "Não. O Weekly Bump é gratuito para baixar e o Pro é uma única compra. Nada é renovado."),
         ("Meu parceiro também precisa comprar o Pro?", "Não. Se você tem o Pro, quem abrir seu link também usa o Pro."),
         ("Para onde vai minha data prevista quando compartilho?", "Ela fica no seu próprio iCloud e aparece só para quem abrir seu link. Nunca é enviada aos servidores do desenvolvedor, e o desenvolvedor não pode vê-la. Se você não compartilhar, ela não sai do seu aparelho."),
         ("Funciona para gêmeos ou trigêmeos?", "Sim. Escolha o número de bebês e dê um apelido para cada um. Há uma contagem de semanas e uma data prevista."),
         ("Nada acontece quando meu parceiro abre o link.", "Verifique se o Weekly Bump está instalado no iPhone dele e abra o link de novo. É preciso estar conectado ao iCloud."),
         ("É aconselhamento médico?", "Não. O Weekly Bump mostra apenas a semana e os dias que faltam a partir da data prevista."),
         ("Como entro em contato?", "No Weekly Bump, vá em Ajustes → “Contato / relatar um problema” para enviar um e-mail. A versão do app, a do iOS e o modelo do iPhone já vêm preenchidos (nunca sua data prevista, apelidos ou fotos).")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 ou posterior)", "Português (Brasil), inglês, japonês, tailandês, coreano e espanhol"],
    h_privacy="Privacidade",
    privacy="Sua data prevista, apelidos e fotos ficam no seu aparelho. Só quando você escolhe compartilhar eles vão para seu parceiro, pelo seu próprio iCloud. O app envia apenas dados de uso anônimos, que você pode desativar nos Ajustes.",
    privacy_link="Política de privacidade (em inglês)",
),
"es": dict(
    title="Weekly Bump — tu semana de embarazo en la pantalla de inicio, un pétalo al mes (sin suscripción)",
    desc="Weekly Bump muestra tu semana de embarazo y cuántos días faltan para tu fecha probable de parto en un widget de la pantalla de inicio del iPhone. Un pétalo se llena de color cada mes: diez pétalos, cuarenta semanas. Comparte tu semana y la foto de tu barriga con el widget de tu pareja. Compatible con gemelos y trillizos. Sin suscripción, sin anuncios, sin cuenta.",
    tagline="Tu semana de embarazo, un pétalo al mes.",
    lede="Escribe tu fecha probable de parto una vez y tu pantalla de inicio muestra de cuántas semanas estás y cuántos días faltan, actualizado cada medianoche. Un pétalo se llena de color cada mes; diez pétalos son cuarenta semanas.",
    cta="Ver en la App Store",
    h_howto="Cómo usar",
    steps=["Abre Weekly Bump y escribe tu fecha probable de parto (o el primer día de tu última regla). Para gemelos o trillizos, elige el número de bebés y pon un apodo a cada uno.",
           "Mantén pulsado un espacio vacío de la pantalla de inicio, toca Editar → Añadir widget y añade Weekly Bump. El widget Small es gratis.",
           "El widget se actualiza cada medianoche. El pétalo del mes se llena un poco más de color cada semana."],
    h_more="Más para disfrutar",
    more=[("Comparte con tu pareja (Pro)", "Envía un enlace desde “Compartir con tu pareja” y su widget muestra tu semana y la foto de la barriga de esta semana de tu álbum. Una compra sirve para los dos. Tu pareja necesita tener Weekly Bump instalada para abrir el enlace."),
          ("Elige el color de la flor", "En Ajustes → Apariencia, elige Rosa o Peonía. Tus widgets usan el mismo color."),
          ("Álbum de la barriga (Pro)", "Una foto por semana, las cuarenta en un solo lugar, con presentación."),
          ("Cuenta regresiva a tus hitos (Pro)", "Muestra en el widget cuántos días faltan para la baja por maternidad, el baby shower o tus propios hitos."),
          ("Cerrar seguimiento", "Ajustes → “Cerrar seguimiento” borra tu fecha, las fotos y los hitos y vacía los widgets. Si lo compartiste con tu pareja, también desaparece de su pantalla.")],
    h_price="Precio",
    price=["Gratis: tu semana, los días que faltan y los pétalos en la app, el widget Small y los colores de la flor. Sin límite de tiempo.",
           "Pro (pago único, no es una suscripción): compartir con tu pareja, widgets Medium, Large y de pantalla bloqueada, álbum de la barriga, hitos, imagen de tu flor para compartir y aviso semanal.",
           "Sin anuncios. Sin cuenta."],
    h_faq="Preguntas frecuentes",
    faq=[("¿Es una suscripción?", "No. Weekly Bump se descarga gratis y Pro es un único pago. Nada se renueva."),
         ("¿Mi pareja también tiene que comprar Pro?", "No. Si tú tienes Pro, quien abra tu enlace también usa Pro."),
         ("¿A dónde va mi fecha cuando comparto?", "Se guarda en tu propio iCloud y solo la ve quien abre tu enlace. Nunca se envía a los servidores del desarrollador y el desarrollador no puede verla. Si no compartes, no sale de tu dispositivo."),
         ("¿Sirve para gemelos o trillizos?", "Sí. Elige el número de bebés y pon un apodo a cada uno. Hay una sola cuenta de semanas y una sola fecha."),
         ("No pasa nada cuando mi pareja abre el enlace.", "Comprueba que Weekly Bump esté instalada en su iPhone y abre el enlace de nuevo. Debe haber iniciado sesión en iCloud."),
         ("¿Da consejos médicos?", "No. Weekly Bump solo muestra tu semana y los días que faltan a partir de tu fecha probable de parto."),
         ("¿Cómo me pongo en contacto?", "En Weekly Bump, ve a Ajustes → “Contacto / informar de un problema” para enviar un correo. La versión de la app, la de iOS y el modelo de iPhone ya vienen escritos (nunca tu fecha, apodos ni fotos).")],
    h_spec="Requisitos",
    spec=["iPhone (iOS 17 o posterior)", "Español, inglés, japonés, tailandés, coreano y portugués (Brasil)"],
    h_privacy="Privacidad",
    privacy="Tu fecha, apodos y fotos se quedan en tu dispositivo. Solo cuando eliges compartir llegan a tu pareja, a través de tu propio iCloud. La app solo envía datos de uso anónimos, que puedes desactivar en Ajustes.",
    privacy_link="Política de privacidad (en inglés)",
),
}

def page(code, folder, hreflang, label):
    t = T[code]
    e = html.escape
    up = "../" if folder else ""
    root = up + "../../"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "name": "Weekly Bump", "alternateName": ["Weekly Bump – Pregnancy Week"],
         "operatingSystem": "iOS 17 or later", "applicationCategory": "HealthApplication",
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
           "", "<h1>Weekly Bump</h1>", '<p class="tagline">%s</p>' % e(t["tagline"]), '<p class="langs">%s</p>' % langs,
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
            '<p>%s <a href="%sprivacy/weeklybump/%s">%s</a></p>' % (e(t["privacy"]), root, PRIVACY_ANCHOR[code], e(t["privacy_link"])),
            '<p class="dim" style="margin-top:3rem">\n  <a href="%s">minari-app-feeds</a> · Made by Minari Taniguchi\n</p>' % root, ""]
    return "\n".join(out)


# 見た目（style）は 1.0 の手書きページのものをそのまま使う。
_src = open(os.path.join(HERE, "index.html")).read()
STYLE_BLOCK = _src[_src.index("<style>"):_src.index("</style>") + len("</style>")] + "\n<style> ol { padding-left: 1.3rem; } ol li { margin: .45rem 0; } </style>"

if __name__ == "__main__":
    for code, folder, hreflang, label in LANGS:
        d = os.path.join(HERE, folder)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(page(code, folder, hreflang, label))
        print("wrote", folder or "(ja)")
