from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Load TELEGRAM_API_TOKEN from token.txt
with open("token.txt", "r") as file:
    TELEGRAM_API_TOKEN = file.read().strip()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    keyboard = [[InlineKeyboardButton("🌐 Sayt", callback_data='site'),
                 InlineKeyboardButton("📞 Əlaqə", callback_data='elaqe')],
                 [InlineKeyboardButton("🔧 Xidmət", callback_data='xidmet'),
                 InlineKeyboardButton("📍  Ünvan", callback_data='unvan')],
                 [InlineKeyboardButton("🚗 Avtopark", callback_data='avtopark'),
                 InlineKeyboardButton("🏢 Şirkətimiz", callback_data='sirket')],
                 [InlineKeyboardButton("💼 Karyera", callback_data='karyera')
                 ,InlineKeyboardButton("🌟 Rəylər", callback_data='reyler')]
            ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("😇 Salam, 🚍 166 Yükdaşıma Xidmətinə Xoş gəldiniz. Zəhmət olmasa seçim edin:",
                              reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    choice = query.data
    if choice == 'site':
        query.answer()
        query.message.reply_text("<b>166 Yükdaşıma Xidmətinin</b> Web Sayt: https://166.az/az", parse_mode=ParseMode.HTML)
    elif choice == 'elaqe':
        keyboard = [[
            InlineKeyboardButton("✍️ Bizə mesaj göndərin", url='https://166.az/az/contact')
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.answer()
        query.message.reply_text("""Ofislə əlaqə 🏢

· Poçt indeksi: AZ1138 📬

· Korporativ əlaqə: +994502311621 ☎️

· Əlaqə nömrəsi: +994502534616 ☎️

· Qaynar xətt: Bütün mobil operatorlardan 166 -a zəng 📞

· Elektron poçt: info@166.az 📧"""  , reply_markup=reply_markup)
    elif choice == 'xidmet':
        xidmet_menu(query, context)
    elif choice == 'unvan':
        query.answer()
        query.message.reply_text("• Ünvan: Yeni Həyat Plaza, mərtəbə 7 ( Zərifə Əliyeva 55): \n• Map: https://2gis.az/baku/firm/70000001037351974?m=49.851418%2C40.377576%2F18.03 ", parse_mode=ParseMode.HTML)
        
    elif choice == 'reyler':
        keyboard = [[
            InlineKeyboardButton("👀 Rəylərə bax", url='https://166.az/az/comments#main-send'),
            InlineKeyboardButton("✍️ Rəy göndər", url='https://166.az/az/comments#main-send')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.answer()
        query.message.reply_text("""
        **Müştəri rəyləri** 🌟

        Biz sifarişlərinizin sağlam və vaxtında çatdırılmasını təmin edirik. Saytımız vasitəsilə ödənişləri onlayn formada həyata keçirə bilərsiniz. 💳💻

        Müştərilərimizin rəyləri bizim üçün çox dəyərlidir. Təklif olunan tövsiyələr nəzərə alınır və əksər tövsiyələr artıq tətbiq olunur. 🤝✨

        Xidmətimizdən istifadə və rəyinizə görə təşəkkür edirik. Qeyd etmək istərdik ki, saytımızda vulqar sözlərin istifadəsi qadağandır. Qaydalara riayət olunmadığı halda yazdığınız şərh silinir və müştəri bazamızdan çıxarılır. Ümid edirik ki, göstərdiyimiz xidmətlər sizdə xoş təəssürat buraxacaq. 🙌🌈
        """, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
    elif choice == 'karyera':
        keyboard = [
    [
        InlineKeyboardButton("📝 Qeydiyyat", url='https://hr.eflow.az/register'),
        InlineKeyboardButton("🔑 Daxil ol", url='https://hr.eflow.az/login')
    ],
    [
        InlineKeyboardButton("💼 Vakansiyalar", url='https://hr.eflow.az/vakansiyalar'),
        InlineKeyboardButton("🌐 Ümumi məlumat", callback_data= 'umum_melumat')
    ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.answer()
        query.message.reply_text("""
        **Müştəri rəyləri** 🌟

        Biz sifarişlərinizin sağlam və vaxtında çatdırılmasını təmin edirik. Saytımız vasitəsilə ödənişləri onlayn formada həyata keçirə bilərsiniz. 💳💻

        Müştərilərimizin rəyləri bizim üçün çox dəyərlidir. Təklif olunan tövsiyələr nəzərə alınır və əksər tövsiyələr artıq tətbiq olunur. 🤝✨

        Xidmətimizdən istifadə və rəyinizə görə təşəkkür edirik. Qeyd etmək istərdik ki, saytımızda vulqar sözlərin istifadəsi qadağandır. Qaydalara riayət olunmadığı halda yazdığınız şərh silinir və müştəri bazamızdan çıxarılır. Ümid edirik ki, göstərdiyimiz xidmətlər sizdə xoş təəssürat buraxacaq. 🙌🌈
            
        """, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

    elif choice == 'avtopark':
        keyboard = [
        [
         InlineKeyboardButton("Hamısı", url='https://166.az/az/cars')   
        ],
        [InlineKeyboardButton("Soyuduculu (5m/5t)", url='https://166.az/az/car/1'),
        InlineKeyboardButton("Soyuduculu (6m/5t)", url='https://166.az/az/car/6')],
        [InlineKeyboardButton("Liftli Soyuduculu (5m/5t)", url='https://166.az/az/car/15'),
        InlineKeyboardButton("Liftli Soyuduculu (7m/8t)", url='https://166.az/az/car/17')],
        [InlineKeyboardButton("Liftli Soyuduculu (8m/10t)", url='https://166.az/az/car/19'),
        InlineKeyboardButton("Liftli Soyuduculu (9m/16t)", url='https://166.az/az/car/21')],
        [InlineKeyboardButton("Yük maşını (3m/2t)", url='https://166.az/az/car/7'),
         InlineKeyboardButton("Yük maşını (4m/3t)", url='https://166.az/az/car/8')],
        [InlineKeyboardButton("Yük maşını (5m/5t)", url='https://166.az/az/car/9'),
        InlineKeyboardButton("Yük maşını (6m/7t)", url='https://166.az/az/car/10')],
        [InlineKeyboardButton("Yük maşını (7m/16t)", url='https://166.az/az/car/11'),
        InlineKeyboardButton("Yük maşını (8m/15t)", url='https://166.az/az/car/12')],
        [InlineKeyboardButton("TIR (14m/ 30t)", url='https://166.az/az/car/13'),
        InlineKeyboardButton("Liftli Soyuduculu (5m/5t)", url='https://166.az/az/car/14')],
        [InlineKeyboardButton("Liftli Soyuduculu (7m/8t)", url='https://166.az/az/car/16'),
         InlineKeyboardButton("Liftli Soyuduculu (8m/10t)", url='https://166.az/az/car/18')],
        [InlineKeyboardButton("Liftli Soyuduculu (9m/16t)", url='https://166.az/az/car/20'),
        InlineKeyboardButton("Liftli (4m/2t)", url='https://166.az/az/car/22')],
        [InlineKeyboardButton("Liftli (5m/5t)", url='https://166.az/az/car/23'),
        InlineKeyboardButton("Liftli (6m/6t)", url='https://166.az/az/car/24')],
        [InlineKeyboardButton("Liftli (7m/8t)", url='https://166.az/az/car/25'),
        InlineKeyboardButton("Liftli (8m/15t)", url='https://166.az/az/car/26')],
        [InlineKeyboardButton("Üstü yanı açılan liftli (6m/13t)", url='https://166.az/az/car/29'),
         InlineKeyboardButton("Üstü yanı açılan liftli (7m/10t)", url='https://166.az/az/car/32')],
        [InlineKeyboardButton("Üstü yanı açılan liftli (8m/13t)", url='https://166.az/az/car/35'),
        InlineKeyboardButton("Üstü yanı açılan liftli (6m/13t)", url='https://166.az/az/car/30')],
        [InlineKeyboardButton("Üstü yanı açılan liftli (7m/10t)", url='https://166.az/az/car/33'),
        InlineKeyboardButton("Üstü yanı açılan liftli (8m/13t)", url='https://166.az/az/car/36')],
        [InlineKeyboardButton("Üstü açılan (5m/5t)", url='https://166.az/az/car/40'),
        InlineKeyboardButton("Üstü yana açılan (7m/15t)", url='https://166.az/az/car/41')],
        [InlineKeyboardButton("Yana açılan liftli (7m/8t)", url='https://166.az/az/car/27'),
         InlineKeyboardButton("Üstü yanı açılan liftli (6m/13t)", url='https://166.az/az/car/31')],
        [InlineKeyboardButton("Üstü yanı açılan liftli (7m/10t)", url='https://166.az/az/car/34'),
        InlineKeyboardButton("Üstü yanı açılan liftli (8m/13t)", url='https://166.az/az/car/37')],
        [InlineKeyboardButton("Üstü yana açılan (7m/15t)", url='https://166.az/az/car/42'),
        InlineKeyboardButton("Özüboşaldan (4m/4t)", url='https://166.az/az/car/28')],
        [InlineKeyboardButton("Evakuator (6m/7t)", url='https://166.az/az/car/43'),
        InlineKeyboardButton("Evakuator (7m/16t)", url='https://166.az/az/car/44')],
        [InlineKeyboardButton("Evakuator (8m/18t)", url='https://166.az/az/car/45'),
         InlineKeyboardButton("Manipulyator (6m/12t)", url='https://166.az/az/car/46')],
        [InlineKeyboardButton("Manipulyator (7m/20t)", url='https://166.az/az/car/47'),
        InlineKeyboardButton("Manipulyator (8m/20t)", url='https://166.az/az/car/48')],
        [InlineKeyboardButton("Manipulyator (10m/30t)", url='https://166.az/az/car/49'),
        InlineKeyboardButton("Dayman (9m/40t)", url='https://166.az/az/car/50')],
        [InlineKeyboardButton("Dayman (10m/50t)", url='https://166.az/az/car/51'),
        InlineKeyboardButton("Dayman (11m/80t)", url='https://166.az/az/car/52')],
        [InlineKeyboardButton("Dayman (12m/80t)", url='https://166.az/az/car/53'),
         InlineKeyboardButton("Dayman (14m/40t)", url='https://166.az/az/car/54')]
         
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.answer()
        query.message.reply_text("""
            ℹ Daha ətraflı məlumat və sifariş üçün uyğun kateqoriyanı seçin:
   """, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
    elif choice == 'sirket':
        keyboard = [
        [
            InlineKeyboardButton("🌟 Missiyamız", url='https://hr.eflow.az/register'),
            InlineKeyboardButton("🔔 Abunə ol", url='https://166.az/az/about')
        ],
        [
            InlineKeyboardButton("👥 Bizim komanda", url='https://166.az/az/team'),
            InlineKeyboardButton("📰 Mediada biz", url='https://166.az/az/media'),
        ],
        [
            InlineKeyboardButton("✒️ Bloq", url='https://166.az/az/blog'),
            InlineKeyboardButton("❓ Tez-tez verilən suallar", url='https://166.az/az/faq')
        ],
        [
            InlineKeyboardButton("🎨 Qalareya", callback_data = "pictures")
        ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.answer()
        query.message.reply_text("""
        🚚 166 - Yükdaşıma və Logistika 🌐
2012-ci ildə fəaliyyətinə bir neçə yük maşını ilə başlayan “Yüktaksisi.az MMC” brendi hazırda yükdaşıma və logistika sahəsi üzrə ölkənin qabaqcıl şirkətlərindən biridir. Yüklərin daşınması yalnız ölkədaxili sərhədlərlə məhdudlaşmır, həmçinin beynəlxalq arenada da həyata keçirilir. Daim müştərilərimizin xidmətində olmaq və operativ xidmət göstərmək məqsədilə 166 qaynar xəttimiz 7/24 ölkənin istənilən nöqtəsindən zəngləri qəbul edir.

Göstərdiyimiz xidmətin müştərilərimizə rahat və əlçatan olması məqsədilə xidmət sahələrimiz genişlənməyə davam edir. Şirkətimiz yükdaşıma sahəsi ilə fəaliyyətə başlasa da, hazırda müxtəlif kompleks xidmətləri – yükdaşıma və logistika, evakuasiya, işçi qüvvəsi, usta xidməti, anbar xidməti, təmizlik xidməti və xalça yuma xidmətlərini müştərilərinə təqdim edib. Xidmətlərimizin daha əlçatan olması üçün sərfəli qiymət və hər bir bölgəyə xidmət anlayışları ilə çalışırıq.

🌟 166 brendi altında fəaliyyət göstərən hər bir xidmətin keyfiyyətinin ölçülməsi bizim üçün olduqca vacibdir. Bu məqsədlə, mütəmadi olaraq müştərilərimizin göstərilən xidmətlər üzrə fikirlərini öyrənir, təklif və iradlarına əsasən xidmət keyfiyyətini daim təkmilləşdiririk. (ISO 9001:2015 - Keyfiyyət İdarəetmə Sistemi, ISO 45001:2018 - Peşə Sağlamlığı və Əməyin Təhlükəsizliyi İdarəetmə Sistemi və ISO 14001:2015 - Ətraf Mühitin İdarəetmə sistemi üzrə beynəlxalq sertifikatları)

“166 Yükdaşıma və Logistika – Yükünüzü daşıyırıq” 🌍

        """, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)


def pictures(update, context):
    query = update.callback_query
    choice = query.data
    keyboard = [
        [
             InlineKeyboardButton("🚚 Yükdaşıma", callback_data= 'yuk'),
             InlineKeyboardButton("🧹 Təmizlik Xidməti", callback_data= 'tem')
        ],
        [
             InlineKeyboardButton("🏡 Ev təmizliyi", callback_data= 'ev'),
             InlineKeyboardButton("🛋️ Xalça yuma", callback_data= 'xal')
        ],
        [
             InlineKeyboardButton("📦 Anbar Xidməti", callback_data= 'an'),
             InlineKeyboardButton("👷 İşçi qüvvəsi xidməti", callback_data= 'isci')
        ],
        [
             InlineKeyboardButton("🔧 Karqo xidməti", callback_data= 'kar'),
             InlineKeyboardButton("💻 Texnoloji həllər", callback_data= 'tex')
        ],
        [
             InlineKeyboardButton("🐾 Ev heyvanlarının və digər qoxuların aradan qaldırılması", callback_data= 'heyv')
        ]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.answer()
    query.message.reply_text("✅Qalereyasını görmək istədiyiniz xidməti seçin 🎨", reply_markup=reply_markup)

def pictures1(update, context):
    query = update.callback_query
    choice = query.data
    if choice == "yuk":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal1.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
   
    elif choice == "tem":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal2.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

    elif choice == "ev":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal3.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
     
    elif choice == "xal":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal4.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
   
    elif choice == "an":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal5.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
   
    elif choice == "isci":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal6.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

    elif choice == "kar":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal7.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

    elif choice == "tex":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal8.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
            
    elif choice == "heyv":
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\qal9.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)











def umum_melumat(update, context):
    query = update.callback_query
    choice = query.data
    keyboard = [
        [
            InlineKeyboardButton("🔑 166-a daxil ol", url='https://hr.eflow.az/login')
        ],
        [
            InlineKeyboardButton("📝 166-dan qeydiyyatdan keç", url='https://hr.eflow.az/register')
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)  
    if choice == 'umum_melumat':
        query.answer()
        query.message.reply_text("""Ümumi məlumat
Portalın məqsədi namizədlər və şirkət arasında rahat şəkildə əlaqənin qurulmasıdır. Siz portal vasitəsilə şirkətimizdə olan aktiv vakansiyaları izləyə, uyğun olan vakansiyalara müraciət edə və statusunuza nəzarət edə bilərsiniz. İşə qəbul şansınızı artırmaq üçün mütəmadi yeni məlumatları profilinizdə qeyd edin.

Qeyd: Şirkətimizə işə qəbulla bağlı müraciət sayının çoxluğunu nəzərə alaraq xahiş edirik, daima öz profilinizin statusunu izləyəsiniz. İşə qəbul komandası tərəfindən yalnız vakansiya tələblərinə uyğun gələn namizədlərlə əlaqə saxlanılacaqdır. Digər profillər portalın namizəd bazasına əlavə ediləcək və münasib vakansiyalar üzrə yenidən dəyərləndiriləcəkdir.

Müraciətiniz üçün təşəkkürlər!
🤝 Komandamıza qoşulun""" , reply_markup = reply_markup)

        
    
def xidmet_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🚚 Transport", callback_data='ferdi_transport'),
         InlineKeyboardButton("📦 Yükdaşıma", callback_data='ferdi_yukdasma')],
        [InlineKeyboardButton("🧣 Xalça Yuma", callback_data='ferdi_xalca'),
         InlineKeyboardButton("🧹 Təmizlik Xidməti", callback_data='ferdi_temizlik')],
        [InlineKeyboardButton("🚑 Evakuasiya", callback_data='ferdi_evakuasiya'),
         InlineKeyboardButton("📦 Anbar Xidməti", callback_data='ferdi_anbar')],
        [InlineKeyboardButton("👷 İşçi qüvvəsi xidməti", callback_data='ferdi_isci_quvvesi'),
         InlineKeyboardButton("🔧 Usta Xidməti", callback_data='ferdi_usta')],
        [InlineKeyboardButton("🔌 Texnoloji Həllər", callback_data='ferdi_texnoloji_heller'),
         InlineKeyboardButton("🛠️ Texnoservis", callback_data='ferdi_texnoservis')],
        [InlineKeyboardButton("🚽 Sanitariya Xidməti", callback_data='ferdi_sanitariya'),
         InlineKeyboardButton("🚗 Karqo Xidməti", callback_data='ferdi_karqo')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("😊Siz 166 Yükdaşıma Xidmətinin Fərdi müştərilər üçün xidmətlər bölməsindəsiz. Aşağıda mövcud xidmətlərin siyahısı verilmişdir. Zəhmət olmasa seçim edin:" 
                              ,reply_markup=reply_markup)

def ferdi_button_click(update, context):
    query = update.callback_query
    choice = query.data
    # Transport
    if choice == 'ferdi_transport':
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/transport#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/transport#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\TRANSPORT.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

        query.answer()
        query.message.reply_text("""·Turizm, iş və digər sahələrdə ən rahat, müasir standartlara uyğun və operativ sərnişin daşınma xidmətini 166 Transport təklif edir.
                                 
Sprinterlərimizin üstünlük və özəllikləri:
- Wi-Fi sistemi
- Powerbanklar
- Sürət həddinə xüsusi nəzarət (GPS)
- 18-20 nəfərlik
- Yumşaq və komfortlu oturacaqlar
- Kondisioner və monitor
- Masa və işıqlı salon
- Mütəmadi təmizlənən salon
- Baqaj
- Peşəkar sürücü heyəti.

Sprinterlərdən nə üçün istifadə edilə bilər?
- Şəhərdaxili sərnişin daşınması
- Ailəvi, dostlarla və ya iş yoldaşlarınızla birgə istirahət üçün
- Toy, yas və digər mərasimlər üçün
- Ölkədaxili işgüzar səfərlər məqsədi ilə (işçi heyətinin daşınması)
- Hava limanından turistlərin istənilən ünvana çatdırılması
- Həftəiçi şirkət işçilərinin daşınması
- Məktəblilərin və universitet tələbələrinin daşınması
- Müalicə məqsədilə bölgələrimizə səyahət edən şəxslər
- Ölkənin dörd bir yanına səfər təşkil edən tur agentləri
- Zavod, fabrik, bank işçilərinin istirahət və ya iş məqsədilə daşınması
- Özəl səfərlər üçün sürücü və nəqliyyat vasitəsinin icarəsi

Bron etmək üçün əlaqə nömrəsi: 050-224-73-24\nGediləcək istiqamət\nTarix""",reply_markup=reply_markup,  parse_mode=ParseMode.HTML)
    #Ferdi Yukdasima 
    elif choice == 'ferdi_yukdasma':
        query.answer()
        
        # Create inline keyboard with service buttons
        keyboard = [
        [InlineKeyboardButton("🌍 Beynəlxalq Yükdaşıma", callback_data='beynelxalq_yukdasma')],
        [InlineKeyboardButton("🚚 Yük Daşıma Xidməti", callback_data='yuk_xidməti')],
        [InlineKeyboardButton("🇦🇿 Ölkədaxili Yükdaşıma", callback_data='olke_yükdaşıma')],
        [InlineKeyboardButton("📦 Yüngül Yükdaşıma", callback_data='yun_yükdaşıma')],
        [InlineKeyboardButton("🚖 Yük Taksisi", callback_data='yuk_taksisi')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Message to be sent to the user
        message = """🚚 166 Yük daşıma və Logistika şirkəti olaraq 10 ildən artıqdır ki, böyük səy və sədaqətlə göstərdiyimiz beynəlxalq logistika və yükdaşıma xidməti ilə qabaqcıl şirkətlərdən biriyik. Geniş avtoparkımız və peşəkar heyətimizlə müştərilərimizə təhlükəsiz, vaxtında və ən ucuz yük daşıma xidmətləri təklif edirik. 2012-ci ildə fəaliyyətinə çox az sayda yük maşını ilə başlayan “166 yükdaşıma və logistika” şirkəti hazırda yükdaşıma və logistika sahəsi üzrə ölkənin qabaqcıl şirkətlərindən biridir. Yüklərin daşınması yalnız ölkədaxili sərhədlərlə məhdudlaşmır, həmçinin beynəlxalq arenada da həyata keçirilir. \n\n✅ Zəhmət olmasa, aşağıdakı xidmətlərdən birini seçin:"""
        query.message.reply_text(message, reply_markup=reply_markup)
    
    #Xalça Yuma
    elif choice == 'ferdi_xalca':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/xalca-yuma#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/xalca-yuma#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)
        keyboard = [
            [InlineKeyboardButton("🐾 Ev heyvanlarının və digər qoxuların aradan qaldırılması", callback_data='ev')],
            [InlineKeyboardButton("🏢 Korporativ Xidmət", callback_data='kor')],
            [InlineKeyboardButton("🛁 Sintefon yorğan, yastıq və örtüklərin yuyulması", callback_data='sint')],
            [InlineKeyboardButton("🧼 Xüsusi Ləkə Çıxarma", callback_data='xus')],
            [InlineKeyboardButton("🛋️ Ədyal, Pled, və Örtüklərin yuyulması", callback_data='edy')],
            [InlineKeyboardButton("💠 Xalçaların bərpası-Overlok", callback_data='xalc')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Message to be sent to the user
        message = """Xalça Yuma xidməti cəmi 3 AZN! 🧺💰

166 Xalça yuma xidmətimizdən yararlanaraq xalçalarınızı peşəkar komandamıza həvalə edə bilərsiniz. Xalca yuma xidmətimiz ən müasir avadanlıqlar, keyfiyyətli yuyucular və peşəkar komanda ilə mövsümündən asılı olmayaraq il boyu xidmətə hazırdır. Pak xalcalara sahib olmaq istəyirsinizsə bizə rahatlıqla müraciət edə bilərsiniz. Xüsusi maddələr ilə xalçalarınız paklanır və xoş ətir verir. Pak xalca ilə evinizdə gözəl aura yarada bilərsiniz. 🌟

Xalçalarınızın təmiz və etibarlı bir şəkildə çatdırılması üçün Yükdaşıma xidmətindən istifadə edə bilərsiniz. 🚚💫

Xalça yuma xidmətlərimiz:
· Əl toxuma floş və ipək xalçaların yuyulması
· Ofis xalçalarının yuyulması
· Yun və ipək Nepal xalçalarının yuyulması
· Yun və ipək kilimlərin yuyulması
· Təbii lifli xalcaların yuyulması

Xalça yuma sifarişi zamanı:
· Əməkdaşlarımız tərəfindən xalçalarınız evinizdən təhvil alınır.
· Xalça yuma üçün xüsusi mərkəzlərimizə çatdırılan xalçalarınız ilk növbədə çırpma maşınında toz-torpaqdan təmizlənir.
· Daha sonrasında müasir xalça yuma avadanlıqları ilə xalçanızın bütün qatları təmizlənir və bol su ilə durulanır. Təmizlik bitdikdən sonra xalçalar qurutma otaqlarında quruyana qədər havalandırılır.
· Xalçaların qurudulması başa çatdıqdan sonra xalçalarınız ətirlənərək pak xalca halına gətirilir.
· Paketlənən xalçalar ünvana çatdırılma xidmətimizlə birbaşa evinizə çatdırılır. Xalçaların ünvana çatdırılması 3-4 iş günü ərzində həyata keçirilir.

Çatdırılma xidmətimizə daxildir:
· Antibakterial yuyulma
· Ətirləmə və paketləmə
· Ödənişsiz çatdırılma
· Qəza zamanı evakuator xidməti sizin köməyinizə gələcəkdir. 🚑

166 Xalça yuma olaraq xalçaların təhvil-təslimini barkod sistemi ilə həyata keçiririk. Əlavə olaraq xalçaların ünvandan götürülməsi və ünvana çatdırılması ödənişsizdir. Həmçinin Abşeron yarımadası, Sumqayıt, Bakı və Xırdalan ərazisində xidmət göstəririk.

Mövsümdən asılı olmadan istənilən zaman xalçalarınızın yuyulması üçün elə indi bizə zəng edin. 166 Xalça Yuma! 📞✨"""
        query.message.reply_text(message, reply_markup=reply_markup2)
        query.message.reply_text("📚 Ətraflı məlumat əldə etmək üçün uyğun kateqoriyanı seçin:", reply_markup=reply_markup)

    #Təmizlik Xidməti
    elif choice == 'ferdi_temizlik':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\TEMIZLIKXIDMETI.png'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

        keyboard = [
            [InlineKeyboardButton("🏠 Ev təmizliyi", callback_data='evt')],
            [InlineKeyboardButton("🧹 Təmizlik paketləri", callback_data='pak')],
            [InlineKeyboardButton("💼 Ofis təmizliyi", callback_data='ofis')],
            [InlineKeyboardButton("🛋️ Yumşaq mebellərin kimyəvi təmizliyi", callback_data='mebel')],
            [InlineKeyboardButton("🌳 Ərazi təmizliyi", callback_data='erazi')],
            [InlineKeyboardButton("🔨 Təmir sonrası təmizlik", callback_data='temir')],
            [InlineKeyboardButton("🏡 Bağ evlərinin təmizliyi", callback_data='bag')],
            [InlineKeyboardButton("🎭 Pərdə və Jaluz yuma", callback_data='perde')],
            [InlineKeyboardButton("🏢 Fasad təmizliyi", callback_data='fasad')],
            [InlineKeyboardButton("🧽 Kovrolit təmizliyi", callback_data='kovrolit')],
            [InlineKeyboardButton("🎴 Pəncərə təmizliyi", callback_data='pencere')],
            [InlineKeyboardButton("💡 Çilçıraq təmizliyi", callback_data='cil')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Message to be sent to the user
        message = """166 Təmizlik Xidməti 🧹

Müasir avadanlıq və təmizlik vasitələri ilə istənilən təmizlik problemini həll edirik. Əgər təmizlik şirkəti axtarırsınızsa, doğru ünvandasınız. Yükdaşıma sahəsində olduğu kimi həmçinin təmizlik sahəsində də sizlərə ən yaxşı xidmətlər təqdim edirik. 💫

Təmizlik Xidməti Qiymətləri 💰

Şirkətimiz sizində büdcənizi nəzərə alaraq daha ucuz qiymətə təmizlik xidmətləri təklif edir. Qiymətlər sifarişinizə uyğun olaraq müəyyən edilir. Müvafiq sahə və görülən xidmətin həcmindən asılı olaraq qiymət aşağı-yuxarı dəyişir. 🌟

Peşəkar İşçi Heyəti 💼

Böyük və peşəkar işçi heyəti qısa zamanda maksimum təmizliyi sizin üçün təmin edəcək. Xidmətlərin qiyməti təmizlik paketlərində olduğu kimi hesablanır. Lakin qeyd etmək lazımdır ki, bəzi hallarda təmizlik dərəcəsindən asılı olaraq qiymətlər aşağı və ya yüksək ola bilər. 🌍

Ən Son Təmizlik Cihazları ilə 🌿

Təmizlik xidməti deyildikdə peşəkarlar tərəfindən ən son təmizlik cihazları ilə yaşayış sahələrinin, iş yerlərinin təmizlənməsi nəzərdə tutulur. Bu xidməti həyata keçirən şirkətlərdə çalışan şəxslər kifayət qədər təcrübəyə sahib peşə sahibləridir. Bunu nəzərə alaraq bir çox insan məhz təmizlik xidməti təklif edən şirkətlərin köməyindən faydalanır. 

Əgər siz də təmizliyə önəm verir və peşəkar təmizlik şirkəti axtarışındasınızsa, bütün bu sadalanan xüsusiyyətlərə malik olan personalımızla işləmək istəyirsinizsə, bizimlə əlaqə saxlayıb vaxt təyin edə bilərsiniz. 🕒

"""
        query.message.reply_text(message, reply_markup=reply_markup2)
        query.message.reply_text("📚 Ətraflı məlumat əldə etmək üçün uyğun kateqoriyanı seçin:", reply_markup=reply_markup)

      
    #Evakuasiya
    elif choice == 'ferdi_evakuasiya':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/evakuasiya-evakuator-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/evakuasiya-evakuator-xidmeti#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)         
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\EVAKUASIYA.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        
        # Message to be sent to the user
        message = """
🚗 166 EVAKUASİYA XİDMƏTİ 🚗

Sürücülük zamanı təhlükəli və çətin hallarla üzləşmək bəzən xilasxan olur. İşte burada 166 Evakuasiya xidməti sizə köməklik edir! Bizim evakuator xidməti sizi yolda qoymayacaq və ən çətin hallarda yanınızda olacaq.

Nəyə xidmət göstəriri
✅ Nəqliyyat vasitələrinin daşınması
✅ Konteynerlərin daşınması
✅ Uzun müddətli dayanacaq xidməti

Niyə 166 Evakuasiya seçməlisiniz?
✅ Bütün ölkə üzrə 24/7 operativ xidmət
✅ Ən aşağı qiymətlər
✅ Daşınan avtomobillərə korporativ zəmanət
✅ Keyfiyyətə nəzarət sistemi

Evakuator xidməti məsələlərini unudun və sürücülük təcrübənizi rahat şəkildə davam etdirin. 166 Evakuasiya – təhlükəsizlik və etibarlılığın simvoludur! 🚦🔧

"""
        query.message.reply_text(message, reply_markup=reply_markup2)


      
    #Fərdi Anbar
    elif choice == 'ferdi_anbar':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/anbar-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/anbar-xidmeti#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)         
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\ANBARXIDMETI.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        # Message to be sent to the user
        message = """
📦 166 ANBAR XİDMƏTİ 📦

Əşyalarınız bizim üçün dəyərlidir və onları təhlükəsiz saxlamaq bizim əsas vəzifəmizdir! 166 Anbar xidməti ilə əşyalarınız təhlükəsiz və keyfiyyətli şəkildə saxlanılacaq. Xüsusi havalandırma sistemi ilə təchiz olunmuş anbar və depolarımız Bakı və Gəncə şəhərlərində ən müxtəlif həcmli yüklərin saxlanması üçün təhlükəsiz yer təmin edir.

Anbar xidmətindən nə gözləyə bilərsiniz?
✅ Müxtəlif həcmli yüklərin saxlanması
✅ Mebel və digər əşyaların saxlanılması
✅ Sığorta təminatı ilə təhlükəsizlik
✅ Əşyalarınıza 24/7 şəxsi giriş

Fərdi və hüquqi şəxslər üçün nələri saxlaya bilərsiniz?
🏠 Böyük həcmli, mövsümə görə istifadə olunan əşyalar
🏢 Ofisdə çox yer tutan vacib sənəd və arxiv materiallar
🛋️ Evin böyük hissəsini tutan əşyalar
🖥️ Laboratoriya və ofis avadanlıqları
🛒 Satış məqsədilə alınan mallar

Əşyalarınızı bizimlə təhlükəsiz saxlayın və hər an ehtiyacınız olduğunda onlara çatmaq imkanı qazanın! 🗄️🔐

"""
        query.message.reply_text(message, reply_markup=reply_markup2)

    #Fərdi Anbar
    elif choice == 'ferdi_isci_quvvesi':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/isci-quvvesi-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/isci-quvvesi-xidmeti#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)         
       
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\ISCIQUVVESI.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
       
        # Message to be sent to the user
        message = """
👨‍🔧 İşçi qüvvəsi xidməti 👩‍🔧

Yükləriniz etibarlı əllərdədir!

Ev və ofislərin köçürülməsi, yüklərin daşınması zamanı ağır əşyaları yükləyib boşaltmaq daşınma prosesini bir xeyli çətinləşdirir. Yükü düzgün götürmədikdə bu sizin sağlamlığınıza, düzgün yüklənmə olmadıqda isə əşyalarınızın ziyan görməsinə gətirib çıxarır.

🛡 İşçi qüvvəsi xidməti təhlükəsizdir

Təhlükəsizliyi maxsimum dərəcədə təmin edərək yüklərinizin düzgün qablaşdırılması və yüklənib boşaldılması üçün İşçi qüvvəsi xidmətimiz fəaliyyət göstərir. İş qüvvəsi yükləri qısa bir müddət ərzində yükləyir və əşyalarınızın zədələnməsi kimi xoşagəlməz hallar baş vermir. Mövcud proses üzrə mütəmadi olaraq təlim keçirilmiş işçi heyətimizlə daşıyacağınız bütün əşyalarınız etibarlı əllərdə olacaqdır.

💵 Fəhlə Xidmətinin Qiyməti

Bu qiymət sizin sifarişinizə əsasən müəyyən edilir. Belə ki, fəhlə xidmətinin qiyməti sərf olunan zaman və daşınan yükün ağırlığına görə təyin edilir. Siz sadəcə görülən iş haqqında məlumat verirsiniz, ən uyğun qiymət sizə təklif edilir və fəhlə heyətimiz lazım olan tapşırıqları təyin olunan zaman ərzində tam dəqiqliklə icra edir.

📞 İşçi qüvvəsi xidmətindən istifadə

Bizimlə istənilən vaxt əlaqə saxlaya bilərsiniz, bunun üçün aşağıdakı əlaqə vasitələrindən istifadə edə bilərsiniz. Ofis və evlərin köçürülməsi zamanı işçi qüvvəmiz tam zamanında sifariş olunan məkana çatır və lazım olan işləri görür.

"""
        query.message.reply_text(message, reply_markup=reply_markup2)


    #Texnoloji Həllər
    elif choice == 'ferdi_texnoloji_heller':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/texnologiya#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/texnologiya#'),
                    InlineKeyboardButton("🌐 Veb sayt", url='https://166tech.az/#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)         

        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\TEXNOLOJIHELLER.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

        # Message to be sent to the user
        message = """
🚀 Texnoloji həllər 166 Tech ilə!

Rəqəmsal Gələcəyinizi 166 Tech ilə formalaşdırın!
166 Tech olaraq biz təkcə ən müasir və lisenziyalı proqram təminatından istifadə etmirik, həm də biznesinizi qurmaq, inkişaf etdirmək və optimallaşdırmaq üçün sizə fərdiləşdirilmiş həllər təklif edirik.

Xidmətlərimiz:
🌐 Veb saytların hazırlanması və Dizaynı: Hər bir müştərinin tələblərinə uyğunlaşdırılmış ən müasir veb-saytların hazırlanması,
📱 Mobil Tətbiq hazırlanması: İstifadəsi rahat və tələbatınıza uyğun olan mobil tətbiq hazırlanması,
💼 Saytlara Texniki Dəstək: Biz həmişə sizin üçün buradayıq - problemlərinizin tez və effektiv şəkildə həll edilməsi,
📧 Korporativ Email: Peşəkar ünsiyyət və biznesinizin ciddiyətini vurğulamaq üçün xüsusi e-poçt sistemlərinin qurulması,
💳 Ödəniş Sistemlərinin İnteqrasiyası: Biznesinizin ödəniş proseslərini sadə və təhlükəsiz şəkildə inteqrasiyası,
📊 ERP Sistemləri: Səmərəliliyi artırmaq və biznes proseslərinizi idarə etmək üçün fərdiləşdirilmiş ERP həlləri.

🤝 Biznesinizi böyütmək, rəqabətdə öndə olmaq və müştəri məmnuniyyətini artırmaq istəyirsinizsə, 166 Tech ilə işləyin.

Bizə qoşulmağınız üçün səbəblər:
✅ Təcrübəli Komandamız: Siz təcrübəli və ekspert komanda tərəfindən dəstəklənirsiniz.
✅ Fərdi Həllər: Biznesinizin ehtiyaclarına uyğun olaraq fərdiləşdirilmiş həllər təklif edirik.
✅ Təhlükəsizlik: Məlumatlarınız bizim üçün vacibdir, ona görə də təhlükəsizliyinizi maksimum dərəcədə artırırıq.

Rəqəmsal transformasiyaya başlayın və biznesinizi gələcəyə aparın. Bizimlə əlaqə saxlayın və necə kömək edə biləcəyimizi öyrənin. 💬🌐

"""
        query.message.reply_text(message, reply_markup=reply_markup2)


    #TexnoServis
    elif choice == 'ferdi_texnoservis':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/az#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/az#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)         
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\TEXNOSERVIS.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)

        # Message to be sent to the user
        message = """
Texnoservis 🛠️

166 Texnoservis məişət avadanlıqlarının təmiri və servisi xidmətini təqdim edir. Biz problemli məişət əşyasına gəlib baxış keçirir, problemini dəqiqləşdirir və ən qısa zamanda təmirini həyata keçiririk. Sıradan çıxmış avadanlığınız texnoservis üzrə ixtisaslaşmış peşəkar ustalarımız tərəfindən işlək vəziyyətə gətirilir və işimizin keyfiyyətinə zəmanət verilir.

Texnoservis xidmətləri 🏠

1. Böyük məişət avadanlıqlarının təmiri:
Soyuducu, paltaryuyan kimi iri məişət əşyalarını mümkün olsa, evinizdə, olmadığı təqdirdə bizim ünvanımızda təmir edilir.

2. Kiçik məişət avadanlıqlarının təmiri:
Ütü, fen, tozsoran kimi kiçik məişət əşyalarını yenidən işlək vəziyyətə gətirib sizə təhvil veririk.

3. İsitmə/soyutma avadanlıqlarının təmiri:
Hava şəraitinə uyğun kombi və ya kondisioner kimi avadanlıqlar böyük önəm daşıyır. Operativ xidmətdən yararlanaraq qısa zamanda arzuladığınız temperaturu əldə edəcəksiniz.

4. Mətbəx əşyalarının təmiri:
Evimizdə ən çox işlənən əşyalar məhz mətbəxdədir. Elektrik çaydanı, mikrodalğalı soba, blender kimi daim əlinizdən tutan əşyaların təmirini rahatlıqla bizə etibar edə bilərsiniz.

Texnoservis qiymətləri 💰
Təmir xidmətimiz avadanlığa görə fərqlənsə də texniki baxış qiymətlərimiz bəllidir. Bakı şəhəri daxilində 20, şəhərkənarı zonalarda isə 30 AZN-dən başlayan qiymətlərlə xidmətinizdəyik.

"""
        query.message.reply_text(message, reply_markup=reply_markup2)

    #Kargo
    elif choice == 'ferdi_karqo':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/karqo#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/karqo#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)         
        
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\KARQOXIDMETI.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        
        # Message to be sent to the user
        message = """
Karqo xidməti 🚚

166 Cargo - Alıcıların xarici ölkələrdən etdiyi sifarişlərə daha tez qovuşması üçün təchizatçılarla əməkdaşlıq edən karqo şirkətidir. Ucuz qiymətə kargo xidmətləri, sizin üçün etibarlı və daha sərfli şərrtlərlə təqdim edilir.

Tükiyədən Azərbaycana kargo xidmeti 🌍
Şirkət 2020-ci ildən etibarən Azərbaycan Respublikasının qanunvericiliyinə uyğun olaraq alınmış lisenziya əsasında beynəlxalq hava daşımalarını həyata keçirərək alış-veriş prosesini asanlaşdırır. 166 Cargo hazırda Türkiyədən sifarişləri həftədə 4 dəfə, Amerikadan sifarişləri isə həftədə 1 dəfə çatdırır. Bütün bunlar ucuz qiymətə edilir, müştərilərin razı qalması üçün operativ xidmət göstərilir.

Kargo xidmətimiz bölgələrdə 🏢
Kargo xidmətlərimiz təkcə Bakıda yox həmçinin bölgələrimizdə də fəaliyyət göstərir. Hazırda Gəncə, Şəki, Balakən, Lənkəran, Bərdə və Sumqayıt filiallarında yerində xidmət göstərilir, Azərpoçt sayəsində isə Azərbaycanın bütün bölgələrinə çatdırılma həyata keçirilir.

Ucuz qiymətə kargo xidməti 💰
Hər zaman qiymətlərin aşağı olması, aşağı keyfiyyət kimi düşünülür, ancaq 166 ucuz kargo xidməti ilə bu düşüncələri arxada qoydu. Həm münasib qiymət həm də üstün xidmət keydiyyəti ilə. Müştərilər məhsulların gecikməsi və ya hər hansısa problemlə bağlı qəti narahat deyillər. Buda bizim məsuliyyətli və məqsədyönlü fəaliyyətimizin nəticəsidir. 🌟

"""
        query.message.reply_text(message, reply_markup=reply_markup)

    #Usta
    elif choice == 'ferdi_usta':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti#')]]
        reply_markup2 = InlineKeyboardMarkup(keyboard)
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\USTAXIDMETI.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        keyboard = [
            [InlineKeyboardButton("🔧 Mebel usta", callback_data='mebel_usta')],
            [InlineKeyboardButton("⚡ Elektrik usta", callback_data='elektrik_usta')],
            [InlineKeyboardButton("🚿 Santexnik usta", callback_data='santexnik_usta')],
            [InlineKeyboardButton("❄️ Kondisioner usta", callback_data='kondisioner_usta')],
            [InlineKeyboardButton("🔩 Digər xidmətlər", callback_data='diger_xidmetler')],
            [InlineKeyboardButton("📦 Paketləmə xidməti", callback_data='paketleme_xidmeti')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Message to be sent to the user
        message = """

Usta xidməti 🛠️

İşinizi ustasına tapşırın!

Ətrafınızda “usta” çox olsa da işindən razı qalacağınız usta tapmaq çətindir. Təmir-bərpa işləri uzun və məsuliyyətli prosesdir. Bir çox hallarda müştərilər xoşagəlməz hallarla qarşılaşırlar, ya gözlənilən işlər görülmür ya da keyfiyyət çox aşağı olur. Bəzən insanları məlumatsızlığından suistifadə halları müşahidə edilmişdir.

Etibarlı usta xidməti 💼
166 Usta xidməti sizə, tam etibar edəcəyiniz bir xidmət təklif edir. Bizim əməkdaşlarımız  təcrübəli, vicdanlı və dürüst insanlardan ibarətdir, işlərində səliqəlidir və öz üzərilərinə görtürdükləri işi tam zamanında təhvil verirlər. İstənilən bir xoşagəlməz hadisələrə qarşı şirkət sizi təmin edir.

Usta xidmətimizə daxildir:

Santexnika xidməti 🚿
Elektrik xidməti ⚡
Mebel təmiri və quraşdırılması 🪑
Mərkəzləşdirilmiş hava sistemlərinin sökülməsi 🌬️
Çöl reklam löhvələrinin və LED monitorların sökülməsi 🖥️
Digər nasazlıqların aradan qaldırılması 🛠️

Usta xidməti qiymətləri 💲
Usta xidməti müqabilində təklif olunan qiymətlərdə çox münasibdir. Burada görüləcək işlərin həcmi və ustalarımızın işləyəcəyi müddət önəmlidir. İşlərin ağırlığından və zamanından asılı olaraq ortalama qiymət müəyyən edilir. Sadəcə görülən işlər haqqında məlumat və zamanı qeyd etməklə sizə daha aydın və dəqiq qiyməti demək olar. Siz müraciət edirsiniz, ustalarımız baxış keçirir və sizə məlumat verir. 

Usta xidmətimizə müraciət üçün ☎️
166 Usta xidmətinə müraciət edərək həm peşəkar usta, həm də təmir işlərinizi bir zənglə aradan qaldıra bilərsiniz. Müxtəlif sahələr üzrə peşəkar ustalarımızın işindən bütün xidmətlərimizdə olduğu kimi istifadə etdikdən sonra razı qalacağınızdan heç şübhəniz olmasın. 

Bundan əlavə siz etibarlı “İşçi qüvvəmizdən” də istifadə edə bilərsiniz. 🤝

"""
        query.message.reply_text(message, reply_markup=reply_markup2)
        query.message.reply_text("📚 Ətraflı məlumat əldə etmək üçün uyğun kateqoriyanı seçin:", reply_markup=reply_markup)


    #Sanitariya
    elif choice == 'ferdi_sanitariya':
         query.answer()
         keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/sanitariya-xidmeti#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/sanitariya-xidmeti#')]]
         reply_markup2 = InlineKeyboardMarkup(keyboard)
         
         photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\SANITARIYA.jpeg'  
         with open(photo_path, 'rb') as photo:
             context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
         
         keyboard = [
         [InlineKeyboardButton("🌱 Bağban xidməti", callback_data='bagban_xidmeti')],
         [InlineKeyboardButton("🦠 Dezinfeksiya", callback_data='dezinfeksiya')],
         [InlineKeyboardButton("🚫 Dezinseksiya", callback_data='dezinseksiya')],
         [InlineKeyboardButton("🐀 Deratizasiya", callback_data='deratizasiya')],
         [InlineKeyboardButton("🐍 İlanlara qarşı dərmanlama", callback_data='dermanlama')],
         [InlineKeyboardButton("💨 Fumiqasiya", callback_data='fumiqasiya')]
         ]
         reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Message to be sent to the user
         message = """
Sanitariya xidməti 🧼
Zərərvericilərin evdə, ofisdə, bağda, həyətdə istirahətinizə mane olmasına imkan verməyin. Bunun üçün təmizliyi qorumağınız və onu yüksək səviyyədə təmin etməyiniz çox zəruridir. 💪

Sanitariya nədir? 
Sanitariya sözünü anlamadan bu xidmət haqqında danışmaq doğru olmaz. Sanitariya sözünün mənası “sağlamlıq haqqında sənət” deməkdir. Yəni sizin sağlamlığınızı təmin edən bir sənət növüdür. Sanitariya xidməti insanların gigiyenik təmizliyin qorunması və ətraf mühitin onların yaşayışına uyğun bir şəkilə salınması üçün fəaliyyəti təmin edilən xidmət növüdür. Bura ətrafda olan zibilliklərin təmizlənməsi, sanitar qovşaqların yaradılması və zəhərli həşaratların müxtəlif üsullarla zərərsizləşdirilməsi kimi bir çox xidmətlər daxildir. 🧽

Sanitariya xidmətləri
"166 Sanitariya Xidməti"nin peşəkar əməkdaşları tərəfindən yerinə yetirilir. Sanitariya xidmətlərimiz mövsümü və daim olaraq tələb olunan sanitar-gigiyenik xidmətləri əhatə edir və aşağıdakılardan ibarətdir: 🛡️

- Dezinfeksiya 🦠
- Dezinseksiya 🧴
- Deratizasiya 🐀
- Bağban xidməti 🌿
- Fumiqasiya 💨
- İlanlara qarşı dərmanlama 💊
- Sanitar-epidemioloji qaydalar 📜

Bu qaydalar hər bir sahə üçün nəzərdə tutulmuşdur. Xidmət sahəsindən qida sahəsinə qədər ölkədə mövcud olan bütün sahələr müəyyən sanitar-epidemoloji qaydalara uyğun bir şəkildə olmalıdır. Bunu həmçinin təmizlik xidmətlərində və ətraf mühitin mühafizəsi zamanı da təmin etmək çox önəmlidir. 🌍

166 Sanitariya xidməti sizə sanitar-epidemioloji qaydalar əsasında müxtəlif xidmətlər təklif edir. Sanitariya xidmətindən istifadə etmək üçün 166-ya zəng edə və ya onlayn qaydada: “SİFARİŞ VER” və “Geri zəng” bölmələrindən istifadə edə bilərsiniz. 📞🔄

"""
         query.message.reply_text(message, reply_markup=reply_markup2)
         query.message.reply_text("📚 Ətraflı məlumat əldə etmək üçün uyğun kateqoriyanı seçin:", reply_markup=reply_markup)




#-----------------------------------------------Usta
# Usta:
def usta(update, context):
    query = update.callback_query
    choice = query.data

    if choice == 'mebel_usta':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/mebel-ustasi#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/mebel-ustasi#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Usta xidməti 🛠️
İşinizi ustasına tapşırın! 👨‍🔧

Ətrafınızda “usta” çox olsa da işindən razı qalacağınız usta tapmaq çətindir. Təmir-bərpa işləri uzun və məsuliyyətli prosesdir. Bir çox hallarda müştərilər xoşagəlməz hallarla qarşılaşırlar, ya gözlənilən işlər görülmür ya da keyfiyyət çox aşağı olur. Bəzən insanları məlumatsızlığından suistifadə halları müşahidə edilmişdir.

Etibarlı usta xidməti 🌟
166 Usta xidməti sizə, tam etibar edəcəyiniz bir xidmət təklif edir. Bizim əməkdaşlarımız təcrübəli, vicdanlı və dürüst insanlardan ibarətdir, işlərində səliqəlidir və öz üzərilərinə görtürdükləri işi tam zamanında təhvil verirlər. İstənilən bir xoşagəlməz hadisələrə qarşı şirkət sizi təmin edir.

Usta xidmətimizə daxildir:
- Santexnika xidməti 🚿
- Elektrik xidməti ⚡
- Mebel təmiri və quraşdırılması 🪑
- Mərkəzləşdirilmiş hava sistemlərinin sökülməsi ❄️
- Çöl reklam löhvələrinin və LED monitorların sökülməsi 🖥️
- Digər nasazlıqların aradan qaldırılması 🔧

Usta xidməti qiymətləri 💰
Usta xidməti müqabilində təklif olunan qiymətlərdə çox münasibdir. Burada görüləcək işlərin həcmi və ustalarımızın işləyəcəyi müddət önəmlidir. İşlərin ağırlığından və zamanından asılı olaraq ortalama qiymət müəyyən edilir. Sadəcə görülən işlər haqqında məlumat və zamanı qeyd etməklə sizə daha aydın və dəqiq qiyməti demək olar. Siz müraciət edirsiniz, ustalarımız baxış keçirir və sizə məlumat verir.

Usta xidmətimizə müraciət üçün ☎️
166 Usta xidmətinə müraciət edərək həm peşəkar usta, həm də təmir işlərinizi bir zənglə aradan qaldıra bilərsiniz. Müxtəlif sahələr üzrə peşəkar ustalarımızın işindən bütün xidmətlərimizdə olduğu kimi istifadə etdikdən sonra razı qalacağınızdan heç şübhəniz olmasın. 🌟


""",reply_markup=reply_markup) 


    elif choice == 'elektrik_usta':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/elektrik-ustasi#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/elektrik-ustasi#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""

Elektrik ustası ⚡
166 Qaynar xəttinə zəng etməklə elektrik nasazılıqları haqqında məlumat verərək, elektrik ustası xidməti sifariş edə bilərsiniz.

Elektrik işi vacib məsələ olduğu üçün onu peşəkar ustalara həvalə etmək lazımdır.

166 Qaynar xəttinə zəng etməklə elektrik nasazılıqları haqqında məlumat verərək, elektrik ustası xidməti sifariş edə bilərsiniz. ☎️

Elektrikə aid xidmətlərimiz:

- Hər növ və hər ölçüdə çilçıraqların sökülməsi və qurulması 💡
- Hər ölçüdə plafonların qurulması 🕯️
- Elektrik şitlərinin yığılması 🔌

Qeyd: 166 Usta Xidmətimiz Abşeron yarımadasında 24/7 fəaliyyətinizdədir. 🕒

""",reply_markup=reply_markup) 
        


    elif choice == 'santexnik_usta':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/santexnik-ustasi#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/santexnik-ustasi#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
                                 
Santexnik ustası 🚿
Santexnik ustası, içməli su, kanalizasiya və kanalizasiya sistemlərində istifadə olunan avadanlıqların quraşdırılması və tənzimlənməsi üzrə ixtisaslaşan şəxsdir. Müasir dövrdə santexnik ustası kimi tanınan bu şəxslər insanların məişət problemlərinin bir çox hissəsini həll edir. Santexnik işləri görən bir çox peşəkar ustalar ilə buradan əlaqə yarada bilərsiniz.

Santexnika problemlərini aradan qaldırmaq üçün həftənin 7 günü 24 saat fəaliyyət göstərən 166 Usta Xidmətinə müraciət edə bilərsiniz. ☎️

Santexnikə aid xidmətlərimiz:

- Simsitellərin təmiri, sökülməsi və qurulması 🚽
- «ARCO» krantların təmiri, sökülməsi və qurulması 🚰
- Unitazların təmiri, sökülməsi və qurulması 🚽
- Moykaların təmiri, sökülməsi və qurulması 🚰
- Duşların təmiri, sökülməsi və qurulması 🚿
- Duş kabinalarının sökülməsi və qurulması 🚿

Qeyd: 166 Usta Xidmətimiz Abşeron yarımadasında 24/7 fəaliyyətinizdədir. 🕒
                                 
""",reply_markup=reply_markup) 




    elif choice == 'kondisioner_usta':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/kondisioner-ustasi#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/kondisioner-ustasi#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""

Kondisioner ustası ❄️
Evinizin mövsümdən asılı olaraq, yayda sərinləşdirilməsi, qışda isə istiləşdirilməsi üçün kondisionerlərin vacib rolu var.

Daim istifadə olunan kondisionerlərin ilk gündəki kimi işləməsini istəyirsinizsə, onu ildə iki dəfə texniki baxışdan keçirməlisiniz.

166 Usta Xidməti markasından və modelindən asılı olmayaraq hər növ kondisionerlərin texniki baxış və təmir xidmətlərini həyata keçirir. 🔧

Nəzərinizə çatdıraq ki, kondisonerlərin sökülmə prosesi qazın saxlanması ilə həyata keçirilir. ❄️

Kondisioner quraşdırılması zamanı əlavə qazın vurulması xidmətimizdə mövcuddur. 🔥

Xidmətlərimiz:

- Kondisionerin qurulması və sökülməsi 🛠️
- Kondisionerə qaz vurulması 🔥
- Kondisionerin təmiri 🔩
- Kondisionerin yuyulması 🚿

""",reply_markup=reply_markup) 


    elif choice == 'diger_xidmetler':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/diger-xidmetler#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/diger-xidmetler#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""

Digər xidmətlər 🛠️
Reklamların sökülməsi 📢

Bankomatların sökülüb və quraşdırılması 💳

Royal pianino sökülüb qurulması 🎹

Arakəsmə şüşələrin, alçipanın, lambirin sökülməsi 🪞

Obyektlərin və mənzillərin, taxta, plastik və dəmir qapıların sökülməsi 🚪

""",reply_markup=reply_markup) 


    elif choice == 'paketleme_xidmeti':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/usta-xidmeti/paketleme-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/usta-xidmeti/paketleme-xidmeti#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
                                 
Paketləmə xidməti 📦
166 Usta Xidməti olaraq, yüklərinizin daha təhlükəsiz daşınma üçün paketlənmə xidmətini təklif edirik.

Yükdaşıma zamanı diqqət yetirilməsi lazım olan ən mühüm məqam yüklərin təhlükəsiz vəziyyətdə daşınmasıdır. 🛡️

166 Usta Xidməti olaraq, yüklərinizin daha təhlükəsiz daşınma üçün paketlənmə xidmətini təklif edirik.

Qeyd edək ki, paketlənən yükün daşınması zamanı yaranacaq ən xırda cızıqda belə məsuliyyət daşıyırıq. 🔍

Paketləmə xidmətinin yükdaşımanın növündən və müştərinin istəyindən asılı olaraq, aşağıda qeyd olunmuş növləri var.

Paketləmə növləri:

- Strec 🔄  
- Polietilen 🌐
- Polietilen strec 🌀
- Polietilen kardon 🛡️
- Polietilen kardon strec 🌈
- Polietilen bükülmüş, penaplas ilə qablanmış taxta yeşikdə 📏

Xidmətlərimiz:

- Hər növ klassik, avangard mebellerin tək-tək və toplu paketlənməsi 🪑
- Şüşəli əşyalar, çilçıraq, suvenir, televizor, soyuducu, paltaryuyan, şüşə qapıların paketlənməsi 📺
- Hər ölçüdə büstlərin, sadə və xüsusi avadanlıqların və hər bir detallarının - taxta yeşiklərə yığılıb xarici ölkələrə göndərmək 🌍
- Sənət əsərləri, lövhələr, printerlər, paltarlar və bir çox əşyaların qablaşdırılması 🎨

""",reply_markup=reply_markup) 
#-----------------------------------------------Usta


#-----------------------------------------------Sanitariya
# Sanitariya:
def sanitariya(update, context):
    query = update.callback_query
    choice = query.data

    if choice == 'bagban_xidmeti':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/bagban-xidmeti#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/bagban-xidmeti#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Bağban xidməti 🌿
Bağınızın səliqəli olması üçün ağaclara və bitkilərə mütəmadi olaraq qulluq edilməlidir. 🌱

"166 Sanitariya Xidməti"nin bağban xidmətindən bütün bölgələrimiz asanlıqla yararlana bilərsiniz. Sizin üçün aşağıdakı xidmətləri təklif edirik! 🌼

- Ağac, kol və çiçəklərə qulluq 🍃
- Qazona qulluq 🌱
- Ziyanvericilərə qarşı dərmanlama 💊
- Dekorasiya və landşaft dizaynı 🏡
- Suvarma sistemlərinin qurulması 💧

Sifariş üçün: 166 ☎️
                                 
""",reply_markup=reply_markup) 


    elif choice == 'dezinfeksiya':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/dezinfeksiya#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/dezinfeksiya#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
                                 
Dezinfeksiya 🧼
Dezinfeksiya prosesi xəstəlik mənbəyi ola biləcək virus və bakteriyaların məhv edilməsini özündə birləşdirir. 🦠🧽

166 Dezinfeksiya Xidməti olaraq, sifariş zamanı məkanın hərtərəfli dezinfeksiyasını həyata keçiririk. Dezinfeksiya prosesi zamanı məkanınız peşəkar dezinfektorlarımız tərəfindən virus, mikrob, bakteriyalar əleyhinə maddələrlə dərmanlanır və ətirlənərək sizə təhvil edilir. 🧪🔬

Nəzərinizə çatdıraq ki, dezinfeksiya zamanı şirkətimiz tərəfindən sertifikat verilir. 📜✅

Sifariş üçün: 166 📞
Whatsapp/ zəng: +994 50 231 17 80 ☎️

""",reply_markup=reply_markup) 
        


    elif choice == 'dezinseksiya':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/dezinseksiya#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/dezinseksiya#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
                                 
Dezinseksiya 🔍
Dezinseksiya prosesinə tarakan, ilbiz, taxtabiti, milçək, ağcaqanad, gənə, birə, qurdlar və digər həşəratların məhv edilməsi daxildir. 🐜🕷️

166 Sanitariya Xidmətində ziyanverici həşaratlara qarşı dərmanlama zamanı eviniz ən gizli nöqtələrdə nəzərə alınmaqla hərtərəfli dezinseksiya edilir. 🔒🏠

Sifariş üçün: 166 📞
Whatsapp/ zəng: +994 50 231 17 80 ☎️

""",reply_markup=reply_markup) 


    elif choice == 'deratizasiya':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/deratizasiya#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/deratizasiya#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Deratizasiya 🐀
Deratizasiya bağ evlərinin, əkin və istehsalat sahlərinin, kafe və restoranların siçan, siçovul, ilan, kərtənkələ və digər gəmirici və sürünənlərdən müdafiə etmək üçün istifadə edilən üsuldur. 🚫

Deratizasiya sifarişi zamanı dərmanlama prosesi 166 Dezinfeksiya Xidmətinin peşəkar əməkdaşları tərəfindən keyfiyyətlə və xüsusi diqqətlə yerinə yetirilir. 🧤🛡️

Gəmiricilər üçün yeni ev sahibi olmaq istəmirsinizsə, bizə müraciət edin. 🏡

Sifariş üçün: 166 📞
Whatsapp/ zəng: +994 50 231 17 80 ☎️

""",reply_markup=reply_markup) 


    elif choice == 'dermanlama':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/ilanlara-qarsi-dermanlama#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/ilanlara-qarsi-dermanlama#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
İlanlara qarşı dərmanlama 🦟
İlanlara qarşı dərmanlama zamanı xüsusi qoxulu maddələrdən istifadə edilərək, ilanların əraziyə gəlməsinin qarşı alınır. 💪

Dərmanlama üsulunda daimi olaraq, eyni tərkibli dərmandan istifadə etmək məsləhət görülmür. 🚫

Eyni zamanda evinizə və iş yerinizə girmiş ilanların canlı şəkildə tutulması və ərazidən uzaqlaşdırılması işini də həyata keçiririk. 🏠✨

Sifariş üçün: 166 📞
Whatsapp/ zəng: +994 50 231 17 80 ☎️

""",reply_markup=reply_markup) 
        

    elif choice == 'fumiqasiya':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/sanitariya-xidmeti/fumiqasiya#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/sanitariya-xidmeti/fumiqasiya#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Fumiqasiya 🔥
Fumiqasiya – Böcək və digər ziyanvericilərə (göbələk, bakteriya və s.) qarşı mübarizə aparmaq məqsədi ilə istifadə edilən dezinfeksiya üsuludur. 💥

Proses zamanı qaz halında olan kimyəvi maddə (fumiqant) vasitəsilə ziyanvericilər məhv edilir. 🔬

Bu üsul bitki və heyvan mənşəli məhsullar və digər materialları ziyanvericilərdən qorumaq üçün digər tədbirlər imkansız olduğu hallarda tətbiq edilir. 🌿

Digər dərmanlama üsullarından aşağıdakı üstünlükləri var:

- Çirklənmiş məhsula birbaşa tətbiq edilir,
- Diffuziyası yüksək olduğundan məhsulun dərinliklərinə qədər nüfuz edir,
- Qısa müddətdə, böyük miqdardakı məhsullara tətbiq olunur,
- Ziyanvericilərin bütün bioloji dövrlərində (yumurta, sürfə, nimfa, pup və yetişkin mərhələlərində) təsirlidir. 🐜🐞

Sifariş üçün: 166 📞
Whatsapp/ zəng: +994 50 231 17 80 ☎️

""",reply_markup=reply_markup) 
#-----------------------------------------------Sanitariya





# #-----------------------------------------------Evakuasiya
# # Evakuasiya:
# def temizlik(update, context):
#     query = update.callback_query
#     choice = query.data

#     if choice == 'evt':
#         query.answer()
#         keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/evakuasiya-evakuator-xidmeti#'), 
#                     InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/evakuasiya-evakuator-xidmeti#')]]
#         reply_markup = InlineKeyboardMarkup(keyboard)

#         # Send detailed information about Beynəlxalq Yükdaşıma service
#         query.message.reply_text("""
# """,reply_markup=reply_markup) 

# #-----------------------------------------------Evakuasiya



#-----------------------------------------------Təmizlik Xidməti
# Təmizlik Xidməti:
def temizlik(update, context):
    query = update.callback_query
    choice = query.data

    if choice == 'evt':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/evlerin-temizlenmesi#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/evlerin-temizlenmesi#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Ev Təmizliyi 🏡

Təmizliyi 166 Təmizlik Xidmətinin peşəkar təmizlik komandasına həvalə etməklə vaxtınıza qənaət edin! 🧼💫

Ev Təmizlənməsi Xidmətləri 🧹

İş və ailə həyatının bu qədər stresli olduğu bir vaxtda ev təmizliyinə saatlarınızı sərf etmək böyük enerji tələb edir. 166-ya bir zənglə və ya saytımızdan sifariş verməklə istəyinizə uyğun “gündəlik” və “əsasl”ı təmizlik xidməti sifariş edərək, evinizdəki bütün təmizlik işlərini yoluna qoya bilərsiniz. 🌟

Ev Təmizliyi Qiymətləri 💰

Sizin üçün daha doğru qiymət təklifimizi formalaşdırmaq üçün ilkin mərhələdə evinizə baxış keçirilir və təmizlik paketlərimiz müştərilərimizin istəklərinə uyğun olaraq optimallaşdırılır. Beləcə təmizlik paketinə istədiyiniz təmizliyi əlavə edə və ya çıxara bilərsiniz. Xidmət zamanı təmizlik işçilərinin sayı, təmizlik olunacaq saat və müddət müştərilərimizin istəyinə uyğun təyin olunur. ✨

Əsaslı Ev Təmizliyi Xidmətlərimiz:
- Otaq, dəhliz və zal təmizliyi;
- Mətbəxin təmizliyi;
- Tavan və divarların təmizliyi;
- Mebellərin tozunun alınması;
- Kafel və metlaxların təmizliyi;
- Sanitar qovşaqlarının təmizlənməsi.

Təmizlik qayğısından azad olun, indi sevdiklərinizə zaman ayırmaq və sevdiyiniz işlə məşğul olmaq vaxtıdır. Vaxt itirmədən 166 ev təmizliyi xidmətinə müraciət edin, təmizliyinizi bizə etibar edin. 🕒✨

""",reply_markup=reply_markup) 


        
    elif choice == 'pak':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/temizlik-paketleri#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/temizlik-paketleri#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Təmizlik Paketləri 🧹

166 Temizlik xidməti sizin büdcənizə uyğun müxtəlif təmizlik paketlərini təqdim edir. Temizlik paketləri qiymətini və ona daxil olan xidmətlərdən asılı olaraq bir neçə kateqoriyaya ayrılmışdır. Burada siz təmizlik paketlərimi gözdən keçirərək, uyğun olanı seçə bilərsiniz. Temizlik paketlərini seçdikdən sonra əməkdaşlarımızın işə cəlb olunması üçün bizə müraciət edə bilərsiniz. Hər hansısa bir sualınız yaranarsa, bir başa bizimlə əlaqə saxlayaraq istənilən sualınıza cavab tapa bilərsiniz.

Büdcənizə uyğun Təmizlik Paketləri:
- Ekspress
- Ekonom
- Standart
- Premium
- Saatlıq təmizlik paketləri: 4 saat və 8 saatlıq təmizlik

Temizlik xidməti sizin seçiminiz əsasında olur. Belə ki, daha mükəmməl təmizlik üçün premium paketləri seçə bilərsiniz. Bundan əlavə saatlıq paketlər də sizin üçün münasib hesab edilir. Sadəcə bizimlə əlaqə saxalayaraq uyğun temizlik paketini seçə bilərsiniz. Temizlik paketleri seçərkən bizim temizlik şirkəti əməkdaşlarımız da sizə uyğun tövsiyələr verəcək. Temizlik firması olaraq sizə ən təmiz xidməti göstərməyə çalışırıq. 🌟✨

""",reply_markup=reply_markup) 




    elif choice == 'ofis':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/ofis-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/ofis-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
Ofis Təmizliyi 🏢

Təmizlik sadəcə rahatlıq üçün deyil, eyni zamanda səmərəli iş üçün də vacibdir. Təmiz olmayan ofis, toz və mikrobun ofis əməkdaşlarının sağlamlığına təsir etdiyi üçün onların əmək məhsuldarlığını azaldır. Təmizlik xərcləri, şirkət büdcəsinə təsir etdiyi kimi, təmizlik əməkdaşlarının tapılmasına sərf olunan zamanda da nəzərə alınmalı əsas məqamlardan biridir.

Ofis təmizliyi xidməti sərfəlidir. Təmizlik məsələləri həll olunmadığı müddətcə iş üçün tamamilə uyğun olmayan mühit yaranmağa başlayır. 166 Təmizlik Xidməti ofis büdcənizə təsir etmədən, müxtəlif xidmət paketləri ilə sizə uyğun ofis təmizliyi xidmətini təklif edir. Təmizləmə işi ofisin xüsusiyyətləri və müştərinin istəkləri nəzərə alınaraq həyata keçirilir. Peşəkar işçi heyətimiz müəyyənləşdirdiyiniz zaman kəsiyində ofisinizdə təmizliyi bərpa edəcək.

Ofis Təmizliyi Xidmətinə Daxildir:
- Döşəmə örtüyünün müvafiq üsul ilə təmizlənməsi
- Əşyaların tozunun alınması
- Ofis mebelləri və avadanlıqlarının təmizlənməsi, dezinfeksiya olunması
- Qapı-pəncərələrin, güzgülərin və əlavə aksesuarların təmizlənməsi
- Mətbəxin təmizlənməsi
- Sanitar qovşaqlarının təmizlənməsi və dezinfeksiya olunması

Siz öz işinizlə uğur qazanın, ofisinizi biz təmizləyərik! 💼🧹

""",reply_markup=reply_markup) 


    elif choice == 'mebel':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/kimyevi-temizleme#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/kimyevi-temizleme#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""
Yumşaq Mebellərin Kimyəvi Təmizliyi 🛋️🧽

Gündəlik istifadə olunan divan, kreslo və stul kimi mebellər çox tez kirə bürünür. Hər bir əşyanın kimi, yumşaq mebelləri də müvafiq təmizlikə ehtiyacı var. Mebellər təmizlənmədikdə, əsl bakteriya yuvası olur və ləkələr rəngini soldurur, görünüşünü itirir. 166 Təmizlik Xidməti ilə artıq yumşaq mebellərinizi yenisi ilə əvəz etməyə ehtiyac qalmayacaq.

Xüsusi avadanlıqlar və yumşaq mebelə qulluq etmək üçün tətbiq edilən peşəkar təmizləyici vasitələr ilə təmizlənən yumşaq mebelləriniz təzə kimi təmiz olacaq. Sifariş zamanı mebel üzərindəki ləkələr xüsusi ləkəçıxarıcı maddələrlə təmizlənir, fırça vasitəsilə şampunlu su ilə fırçalanır. Ləkələrdən tam azad olmuş mebel su vaakum aparatı ilə çəkilir. Təmizlənəcək mebellərinizi təhvil aldıqdan bir neçə saat sonra, "yeni mebelləriniz" sizə təhvil verilir.

Mebel Təmizliyi Xidmətinə Daxil Olan Qiymətlər:
- 1 Kreslo Kimyəvi Təmizliyi – 10 AZN
- 1 Stul Kimyəvi Təmizliyi – 8 AZN
- 1 Nəfərlik Matrasın Kimyəvi Təmizliyi – 30 AZN

Təmizlik xidməti ilə əlaqə saxlayın və yumşaq mebellərinizi bərpa edin! 🌟🪣

""",reply_markup=reply_markup) 



    elif choice == 'erazi':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/erazi-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/erazi-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
Yumşaq Mebellərin Kimyəvi Təmizliyi 🛋️🧽

Gündəlik istifadə olunan divan, kreslo və stul kimi mebellər çox tez kirə bürünür. Hər bir əşyanın kimi, yumşaq mebelləri də müvafiq təmizlikə ehtiyacı var. Mebellər təmizlənmədikdə, əsl bakteriya yuvası olur və ləkələr rəngini soldurur, görünüşünü itirir. 166 Təmizlik Xidməti ilə artıq yumşaq mebellərinizi yenisi ilə əvəz etməyə ehtiyac qalmayacaq.

Xüsusi avadanlıqlar və yumşaq mebelə qulluq etmək üçün tətbiq edilən peşəkar təmizləyici vasitələr ilə təmizlənən yumşaq mebelləriniz təzə kimi təmiz olacaq. Sifariş zamanı mebel üzərindəki ləkələr xüsusi ləkəçıxarıcı maddələrlə təmizlənir, fırça vasitəsilə şampunlu su ilə fırçalanır. Ləkələrdən tam azad olmuş mebel su vaakum aparatı ilə çəkilir. Təmizlənəcək mebellərinizi təhvil aldıqdan bir neçə saat sonra, "yeni mebelləriniz" sizə təhvil verilir.

Mebel Təmizliyi Xidmətinə Daxil Olan Qiymətlər:
- 1 Kreslo Kimyəvi Təmizliyi – 10 AZN
- 1 Stul Kimyəvi Təmizliyi – 8 AZN
- 1 Nəfərlik Matrasın Kimyəvi Təmizliyi – 30 AZN

Təmizlik xidməti ilə əlaqə saxlayın və yumşaq mebellərinizi bərpa edin! 🌟🪣

""",reply_markup=reply_markup) 



    elif choice == 'temir':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/temirden-sonra-temizlik#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/temirden-sonra-temizlik#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
Təmir Sonrası Təmizlik 🧹🔨

Təmir sonrası təmizlik zamanı qapıları və pəncələri zədələmədən qoruyucu üzlükləri çıxartmaq, döşəməni cızmadan boya və yapışdırıcı ləkələrindən təmizləmək lazımdır. Bu işlər sizə yeni evinizdən zövq almağa imkan vermir. 166 Təmizlik Xidməti sizi belə çətin vəziyyətdən qurtaracaq! Peşəkar təmizlik komandası xüsusi təmizlik vasitələri ilə istənilən ölçüdə mənzil və obyektlərin təmir sonrası təmizlik işlərini həyata keçiririk.

Təmizlik prosesinə tikinti materialları, qarışıqlar, ləkələr, yapışqan, qoruyucu lent, sement tozu, boya qalıqları və başqa çirklənmələrin aradan qaldırılması daxildir. Tullantıların atılmasından ən kiçik sənaye ləkələrinin təmizlənməsinə qədər hər bir detal təmizlənərək mənzil və obyektləriniz qısa zamanda istifadəyə verilir. Biz sizə evinizi və iş yerinizi tam təmiz şəkildə təhvil verəcəyik.

Təmizlikdə Peşəkarlığımıza Güvənin! 🌟🏠
                                     
""",reply_markup=reply_markup) 



    elif choice == 'bag':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/bag-evi-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/bag-evi-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
Bağ Evinizin Təmizliyi 🌿🏡

Təbiətdən zövq almaq üçün bağ evi əla bir seçimdir, lakin baxımsız vəziyyətdəki bağ və hovuz çox da ürəkaçan bir mənzərə təşkil etməyə bilər. Təmizləmə işinə başlasanız, bağ mövsümünün sonuna qədər çətinlik çəkə bilərsiniz.

166 Təmizlik Xidməti ilin bütün fəsilləri üçün bağ evinizi təzə vəziyyətə salmaq üçün təmizlik və bağa qulluq üzərinə görür. Sürətli iş rejimi ilə qısa zamanda bağ eviniz təmizlənərək istifadəyə verilir. Bağların təmizliyinə zibillərin yığılması, payız mövsümündə xəzəllərin təmizlənməsi, ağartma və boyama işlərinin görülməsi və istəyinizə uyğun digər xidmətlərin təminatı daxildir.

Bağ evlərinin təmizliyi xidmətinə daxildir:

- Evin təmizlənməsi
- Həyətin təmizlənməsi
- Tametin aparatla yuyulması
- Hovuzun təmizlənməsi
- Zibillərin yığılması və atılması (10 kq qədər)

1 kvadrat metr tametin aparatla yuyulması - 3.5 AZN

Təmizlikdə Peşəkar Yardım! 🌟🌳
                                     
""",reply_markup=reply_markup) 



    elif choice == 'perde':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/perde-yuma#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/perde-yuma#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
Evinizdəki Pərdə və Jaluz Yuma Xidməti 🏡✨

Evin dəkorasyasında əhəmiyyətli bir rol oynayan pərdələrin təmizliyi çox vacibdir. Peşəkar pərdə yuma komandamız ipək, tül, kətan və digər növ pərdələrinizi və jalüzlərinizi itirir, xüsusi metoddan istifadə edərək yuyur, havalandırma otağında tamamilə qurudur, ütüləyir və sizin üçün təyin etdiyiniz tarixdə təslim edir. Pərdələrin sökülməsi və yuyulduqdan sonra təkrar quraşdırılması ödənişsizdir.

Nəzərinizə çatdırırıq ki, pərdələrin asılması üçün istifadə olunan asılqanlar tərəfindən təmin edilir.

Pərdə Yuma Xidməti Abşeron yarımadasının istənilən nöqtəsində mövcuddur.

Qiymətlər:

- 1 metr tül pərdə yuma - 2.40 AZN
- 1 kq dekor pərdə yuma – 3 AZN

Peşəkar və Keyfiyyətli Xidmət üçün Bizə Əlaqə Saxlayın! 🌟

""",reply_markup=reply_markup) 
            


    elif choice == 'fasad':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/fasad-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/fasad-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""

Fasad Təmizliyi Xidməti 🏢✨

Binaların xaricinin təmiz olması, şirkətin imicini və tərəqqisini əks etdirir. Bu səbəbdən 166 Təmizlik Xidməti kimi peşəkar komandamızın fasad təmizliyi xidmətinə etibar etmək ən doğru qərardır. Bakı şəhəri çoxmərtəbəli binalarla bezənmiş olduğu üçün, fasad təmizliyi yüksək riskli zonalar arasında yer alır. Biz təmizlik prosesində əmək təhlükəsizliyinə böyük əhəmiyyət veririk və təhlükəsizlik prinsiplərindən asla kənarda qalmayaraq işləyirik.

166 Təmizlik Xidməti kimi biz, xüsusi təchizatla təchiz olunmuş qaldırıcı sistemlər istifadə edərək binaların ən hündür yerlərinin də təmizliyini həyata keçiririk. Əlavə olaraq, istifadə etdiyimiz təmizləyici maddələr şüşə və metal səthələrə heç bir ziyan vurmayacaq şəkildə formulalaşdırılmışdır.

Sizi təhlükəsiz, peşəkar və təmiz bir fasadla bəzədilmiş binaya sahib olmağa dəvət edirik. Bizimlə əlaqə saxlayın və binanızın yeni görkəmini bizimlə birgə yaradın!

""",reply_markup=reply_markup) 
            

    elif choice == 'kovrolit':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/kovrolit-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/kovrolit-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""

Kovrolit Təmizliyi Xidməti 🧹🏢

Kovrolitləriniz çirk və ləkələrdən təmizlənməli və yenidən parlaq görünməli? Bizim kovrolit təmizliyi xidməti ilə məşğul olmağınız tələb etmir! Siz yalnızca sifariş verin və gerisini bizə təhvil verin. Kovrolitləriniz sökülmədən əməkdaşlarımız tərəfindən yerində təmizlənir, bütün çirk və ləkələrdən azad şəkildə sizə təhvil verilir.

Yerində yuma zamanı ilkin olaraq, kovrolit nəmləndirilir. Fırçalama zamanı kovrolit çirk və ləkələrdən təmizlənir. Xalçada qalan nəm normal vaakum aparatı ilə tam çəkilir. Təmizlikdən sonra 4 saat havalandırılan kovrolitləriniz istifadəyə hazır olacaqdır.

Təmizlik işləri başa çatdıqdan sonra ofisinizdə təravətli bir abu-hava yaranır. Bizə əlaqə saxlayın və kovrolitlərinizin bərpa olunmuş təzə görkəmini təcrübə edin!


""",reply_markup=reply_markup) 
            

    elif choice == 'pencere':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/pencere-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/pencere-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""

🎴 Pəncərə Təmizliyi Xidməti 🎴

Yüksək mərtəbəli binalarda pəncərə təmizliyi çətin və təhlükəli ola bilər, amma artıq sizin üçün bu proses asan və sürətli olacaq! 166 Təmizlik Xidməti ilə pəncərələrinizin gündəlik və təmir sonrası təmizliyini etmək daha çox problem olmayacaq. Təmir sonrası təmizlikdə isə ən çətin məsələ pəncərələrdən montaj lentlərinin təmizlənməsidir, amma siz bu işi bizə etimadla həvalə edə bilərsiniz.

Peşəkar təmizlik komandamız hər zaman xidmətinizdədir. 1 standart ölçülü pəncərə təmizlənməsi üçün yalnız 10 azn! Bizə əlaqə saxlayın və parlaq pəncərələrin keyfini çıxarın!

""",reply_markup=reply_markup)
            

    elif choice == 'cil':
            query.answer()
            keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/temizlik-xidmeti/cilciraq-temizliyi#'), 
                        InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/temizlik-xidmeti/cilciraq-temizliyi#')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send detailed information about Beynəlxalq Yükdaşıma service
            query.message.reply_text("""
💡 Çilçıraq Təmizliyi Xidməti 💡

Çilçıraqlarınızın bəziləri elektriklə işləyir və vaxtaşırı sönməsə də, onların təmiz olması və parlaq görünməsi vacibdir. Bizim platformalarımız vasitəsilə təmin edilən çilçıraq təmizliyi xidməti ilə bu proses daha asan və sürətli olacaq.

Təmizləmə prosesi belə həyata keçirilir:
1. Çilçıraq elektrikdən söndürülür.
2. Platonlar özel yuyucu maddələrlə isladılır.
3. Su ləkələrindən təmizlənmək və parlaqlıq vermək üçün təmamilə qurudulur.

Qiymətlərimiz çox mülayimdir:
1 çilçıraq üçün yalnız 10 azn!
5 çilçıraq üçün sadəcə 20 azn!

Bizimlə əlaqə saxlayın və parlaq çilçıraqlarınızın keyfini çıxarın!

""",reply_markup=reply_markup)


#-----------------------------------------------Təmizlik Xidməti








#-----------------------------------------------Xalca Yuma
# Xalça Yuma:
def xalca(update, context):
    query = update.callback_query
    choice = query.data

    if choice == 'ev':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/ev-heyvani-qoxu#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/ev-heyvani-qoxu#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""Bir çox ev heyvanı sahibləri üçün onların tüklü dostları ailə hesab olunur. Bununla belə, ev heyvanlarına sahib olmağın sevinci ilə birlikdə bəzi çətinliklər də gəlir ki, bunlardan biri də xalçaları təmiz və qoxusuz saxlamaqdır. Palçıqlı pəncələrdən tutmuş digər qəzalara qədər sevimli ev heyvanlarımız xalçalarımızı çirkləndirə və pis qoxuya səbəb ola bilər. Xoşbəxtlikdən, xalça təmizləmə xidmətlərimiz evinizin təmiz, gigiyenik və qoxusuz qalmasını təmin edərək bu problemlərin həllində ixtisaslaşmışdır. 🐾

Ev heyvanlarının çirkləndirdiyi xalçalara niyə xüsusi diqqət lazımdır?

Gecikmiş qoxular: Tipik xalça ləkələrindən fərqli olaraq, ev heyvanları qəzaları aradan qaldırılması çətin olan qoxuları geridə qoya bilər. Bu, xalça liflərinə dərindən nüfuz edə bilən ləkələrin üzvi təbiəti ilə bağlıdır.

Potensial sağlamlıq riskləri: Sidik və nəcis bakteriyaları saxlaya bilər. Düzgün təmizlənməsələr, evdəki həm insanlar, həm də ev heyvanları üçün sağlamlıq riski yarada bilərlər.

Uzunmüddətli zərər: Heyvan sidiyin turşulu təbiəti, vaxtında müalicə edilmədikdə, xalça liflərinə və hətta altındakı yastıqlara zərər verə bilər. 🏠

Professioanal Heyvan Xalçası Təmizləmə Prosesimiz

Dərin Təmizləmə: Hər hansı boş zibilləri təmizləmək üçün ərazini hərtərəfli tozsoranla təmizləməyə başlayırıq. Sonra güclü təmizləyici maddələrin və isti su ekstraksiyasının birləşməsindən istifadə edərək, biz xalça liflərinə dərindən nüfuz edir, inadkar ləkələri və qoxuları parçalayır və aradan qaldırırıq.

Qoxunun zərərsizləşdirilməsi: Ləkəni sadəcə çıxarmaq kifayət deyil. İxtisaslaşdırılmış həllərimiz ev heyvanlarının qoxularını zərərsizləşdirir, onların geri qayıtmamasını təmin edir.

Qoruyucu müalicə: Gələcək ləkələrin qarşısını almaq və təmizlənməsini asanlaşdırmaq üçün xalçanıza kir, ləkə və qoxulara qarşı maneə yaradan qoruyucu müalicə tətbiq edə bilərik. 🧼

Niyə Xidmətlərimizi Seçməlisiniz?

Biz ev heyvanları ilə əlaqədar xalçanın çirklənməsinin yaratdığı unikal problemləri başa düşürük. Ən müasir avadanlıqlarımız, təcrübəli texniklərimiz və effektiv təmizləmə həllərimizlə xalçalarınızı cavanlaşdırmağa və sizin və ev heyvanlarınız üçün daha sağlam yaşayış mühiti təmin etməyə söz veririk.

Nəticə olaraq, ev heyvanları böyük sevinc gətirsə də, qarışıqlıq da gətirə bilər. Heyvan ləkələri və qoxularının ev heyvanına sahib olmaq sevincini azaltmasına imkan verməyin. Xüsusi xalça təmizləmə xidmətlərimizlə eviniz yenidən təravətli, təmiz və qonaqpərvər hiss edəcək. Bu gün bizimlə görüş təyin edin! 🐶

Təmizləmələr Arasında Heyvan Sahibləri üçün Məsləhətlər

Sürətlə hərəkət edin: Təzə ləkəni nə qədər tez silə bilsəniz (ovuşdurmayın), onu çıxarmaq bir o qədər asan olacaq.
Enzimatik Təmizləyicilərdən istifadə edin: Bunlar heyvan ləkələrindəki üzvi maddələri parçalamaq üçün nəzərdə tutulmuşdur.
Müntəzəm olaraq tozsoran: Bu, ev heyvanlarının tüklərini, tüklərini və digər zibilləri təmizləməyə kömək edir.
Müntəzəm Təmizliklər Planlayın: Təmizlik mövzusunda çalışqan olsanız belə, xalçanın sağlamlığını və uzunömürlülüyünü qorumaq üçün vaxtaşırı peşəkar təmizliklər etmək tövsiyə olunur. 🧹

Sevimli ev heyvanları bəzən xoşagəlməz hallara da səbəb olur. Bu zaman xalçanızdan pis qoxular gəlir və qalıcı ola bilir. Peşəkar komandamız bu halların qarşısının alınması üçün sizə dəstək olacaq. Sifariş üçün 166 qısa nömrəsinə zəng edin! 📞"
""",reply_markup=reply_markup) 
        

    elif choice == 'kor':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/korporativ-xalca#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/korporativ-xalca#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
       
        query.message.reply_text("""Ofislərinizin, otel, bağça, məktəb və digər ictimai və iaşə obyektlərində olan xalçaların yuyulmasını peşəkar xidmətə -166 Xalça Yuma xidmətinə həvalə edin! Zəmanətli və peşəkar xalça təmizliyi bir ünvanda. 🧼🏢

İş dünyasında mövzuşan şirkətlər, müştərilərinin gözləntilərinə uyğun təmiz və təzə mühit yaratmaq üçün hər tərəfdə geniş imkanlar axtarır. Mükəmməl xidmət və iş yeri estetikası, korporativ mükafat və tanınmışlığın əsas amillərindəndir. Şirkətimiz, korporativ şirkətlərlə əməkdaşlıq edərək onlara profesionallaşdırılmış xalça yuma xidməti təklif edir. 💼🌟

Həssas Təmizlik Prosedurları və Məhsul Seçimi
Xalçalarınızın uyğun təmizlənməsi, ləkələrin və qırışların tamamilə aradan qaldırılması üçün həssas prosedurlar tələb edir. Biz, korporativ şirkətlərin xalçalarında mövcud olan müxtəlif ləkələri və çirkləri dəyərləndirərək, uyğun təmizlik prosedurları və məhsullarını seçirik. Hər bir xalçanın xüsusiyyətləri, materialı və rəngi gözləntilərə uyğun olaraq əsas alınır. 🌈✨

Bərpa Edilmiş Xalçalar, Şirkətimizin İmzası
Bizim xalça yuma xidmətimiz, şirkətinizin iş yeri görünüşünü bərpa edərək imzasını yaratmağa kömək edir. Biz, xalçalarınızın təmiz, təzə və sağlam olmasını təmin etmək üçün ən son texnologiyalardan və təcrübəli komandamızdan istifadə edirik. Xalçalarınızın bərpa edilmiş görünüşü, şirkətinizin üstünlüyünü, mükəmməlliyyətini və peşəkarlığını vurğulayaraq korporativ kimliyinizi gücləndirir. 🎩🏆
""",reply_markup=reply_markup)



    elif choice == 'sint':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/sintifon-yorgan#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/sintifon-yorgan#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        #------------Photo
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\yorgan_1.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\edyal_1.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        #------------
        query.message.reply_text("""

Sintefon yastıq, yorğan və örtüklərin yuyulması
Yorğan, yastıq və örtüklərin düzgün yuyulması təmiz və sağlamlıq üçün vacibdir. 🛏️🧼

Sintefon yorğan və döşək

Əgər yorğan, yastıq və örtüklər düzgün yuyulmazsa, onlarda mikrob və bakteriyaların çoxalması mümkündür. Bu maddələr insan sağlamlığına ziyanlı olaraq xəstəliklərin və allergiyaların səbəbi ola bilər. Bu səbəblərə görə, yorğan, yastıq və örtüklərin təmiz və təmizliyinə fikir vermək vacibdir. 🦠🚫

Yorğan, yastıq və örtüklər insanların günlük həyatlarında ən çox istifadə etdikləri əşyalardandır və onların səhərə hazırlaşmaq, günlük fəaliyyətlərindən sonra rahatlamaları üçün tərəfdaşlarıdır. Amma bu məhsulların təmizliyi və həmişə təzə və təmiz olması çox vacibdir. Yorğan, yastıq və örtüklərin düzgün yuyulması təmiz və sağlamlıq üçün vacibdir. 🛌💤

Yorğan, yastıq və örtüklərin düzgün yuyulması həm də bu məhsulların ömrünü artırır. Yastıqlar və örtüklər düzgün yuyulduqda onların məhsulun istifadə ömrü uzadır. Bəzən, insanlar yorğan, yastıq və örtüklərlə məhsul qaynaqları üzərindən baxırlar, amma bununla yorğan, yastıq və örtüklərin təmizliyi təmin edilə bilməz. Yorğan, yastıq və örtüklərin yuyulması bu məhsulların təmizliyinə və sağlamlığına diqqət çəkərək onların istifadə müddətini uzadır. 🔄🕒

Bizə müraciət edərək sizin üçün yüksək keyfiyyətli işlər görə bilərik. Bir zənglə yanınızdayıq! 📞

Yorğan, yastıq və örtüklərin yuyulması ilə bağlı təcrübələr və müştəri təcrübələri
Yorgan döşək və matras

Ümumi olaraq, müştəri təcrübələri və rəylərə görə, yorğan, yastıq və örtüklərin təmizliyi insan sağlamlığı və önəmli bir təsirdə sahibdir və müştərilər bu məhsulların təmizliyinə ciddi diqqət yetirirlər. Yorğan, yastıq və örtüklərin təmizliyinə diqqət etməklə insanlar, yuxudan sonra daha təzə və yüksək keyfiyyətli bir hiss alırlar. Həmçinin, yorğan, yastıq və örtüklərin təmizliyi ağrıların azalmasına, alerji və astma kimi problemlərə mane olmağa, və hətta depresiya və anksiyetəyə qarşı qoruyucu təsir göstərə bilər. Ona görə də xüsusi və peşəkar komanda olaraq daim sizin xidmətinizdəyik! 💪🌟

Müştərilər yorğan, yastıq və örtükləri yuyarkən, geniş vahidlərdə qulluq etmək, istilikli su və doğru kimyəvi məhsulların istifadəsi, və məhsulların düzgün saxlanılması kimi amillərə diqqət edirlər. Bəzi müştərilər tərəfindən də dəstəklənir ki, təmizliyin vacibliyi ilə bağlı olaraq yorğan, yastıq və örtüklərini daha sıx yuymanın əvəzində, qayğıları və yastıqları təmizləmək üçün əlavə məhsullar, məsələn, qayğı təmizləyici spreyləri, istifadə edə bilərlər. 🧽🌊


""",reply_markup=reply_markup)



    elif choice == 'xus':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/xususi-xalca#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/xususi-xalca#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        #---------Photo
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\serab_2.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        #---------       
       
        query.message.reply_text("""
             Ləkə Çıxarma: Praktik Məsləhətlər və Texniki Bilik 💡

Xalçalar, evimizin səsiz qəhrəmanlarıdır. Zərif görünümləri və konfortlu hissi ilə daxil olan xalçalar zamanla istifadə səbəbiylə ləkələrə məruz qala bilər. Şirkətimiz, xalçalardan ləkə çıxarma prosesində praktik məsləhətlər və texniki bilik təklif etməklə yanaşı yüksək keyfiyyətdə xidmət təklif edir. 🧼🧹

Doğru Texnologiya və Tətbiqat 🛠️
Xalçaların fərqli növləri və materialları olduğundan, doğru texnologiya və tətbiqat, ləkə çıxarma prosesinin ən effektiv şəkildə həyata keçirilməsi üçün əhəmiyyətlidir. Bizim texniki komandamız, xalça materialını və ləkənin cürünü dəyərləndirərək, uyğun təmizləmə mənbəyini və prosedurlarını seçir. Xalçalarınızdakı ləkələri təhlil edərək, onlara uyğun məsləhətlər və texniki bilik təqdim edirik. Bu, ləkələri mümkün ən yüksək səviyyədə və effektiv şəkildə çıxarmağa kömək edir. 🌟

Praktik Məsləhətlər 🌿
Xalçalardan ləkə çıxarma prosesində əlavədən praktik məsləhətlər də istifadə edirik. Müştərilərimizə, xalçalarında müstəsna vəziyyətdə olan ləkələr üçün təcrübəli və məsləhətli həllər təklif edirik. Xalçalarınızın rənginə, materialına və ləkənin xüsusiyyətlərinə uyğun olaraq, doğru məsləhətlər veririk. Bu, ləkələrin tamamını və mümkün qədər minimal zədəni çıxarmağa imkan verir. 🎨

Müştəri Memnuniyyəti və Xidmət Sonrası Dəstək 🤝
Bizim üçün müştəri məmnuniyyəti ən çox qiymət verdiyimiz məsələlərdən biridir. Xalçalardan ləkə çıxarma xidmətimizdə daima müştəri tələbləri və gözləntiləri əsasında hərəkət edirik. Müştərimiz olaraq sizin məmnuniyyətinizi təmin etmək üçün səmərəli və keyfiyyətli bir xidmət sunmağa özümüzü həsr edirik.

Bizimlə işləməklə, sizi sərfəli və effektiv xidmətlərlə tanış edirik. Təmizləmə prosesində, ləkə çıxarma maddələri, texnologiyalar və təcrübəli komandamızla mükəmməl nəticələr əldə edirik. Xalçalarınızın təmiz və təzə görünməsini təmin etməklə yanaşı, biz müştəri memnuniyyətini təmin etmək üçün xidmət sonrası dəstək də təklif edirik. Sizə məsləhətlər, istifadə qaydaları və ləkələrin yenidən formalaşdırılması üçün təlimatlar veririk. Bizimlə əlaqə saxladığınız müddətdə, hər bir məsələyə diqqət yetirir və ən yaxşı çözümü təmin etmək üçün sizi yanınızda oluruq. 🌟👍


""",reply_markup=reply_markup)
    
    elif choice == 'edy':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/adyal-yuma#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/adyal-yuma#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        #---------Photo
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\pled_3.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        #---------
        query.message.reply_text("""

Ədyal və Örtüklərin Yuyulması 🧺

Ədyal, pled və örtüklərin ev şəraitində, xüsüsən də bina evlərində bu təmizliyi həyata keçirtmək qeyri-mümkündür. Havanın isti və ya soyuq olmasından asılı olmayaraq, istənilən fəsildə yun yorğan və döşəklərinizin tam gigiyenik bir ortamda yuyulub, qurudulub, çırpılıb, didilib və peşəkar xanımlar tərəfindən sırınması xidmətini sizə təklif edirik. Gecələriniz daha rahat, yuxularınız daha şirin olacaq. 💤🌟

Ədyal, Pled və Örtüklərinizi Parlaq və Təmiz Tutmağa Yardım Edirik ✨

Ədyallar, pledlər və örtüklər, evimizdə rahatlıq, gözəllik və istirahət hissi yaratmağın ən əhəmiyyətli hissələrindəndir. Bu məhsulların sağlamlığını və təmizliyini qorumaq, onların uzun müddət parlaq və təmiz görünməsini təmin etmək üçün vacibdir. Bizim şirkət, ədyal, pledlər və örtüklərinizi bərabərlik və səmərəlilik ilə yumaq və saxlamaq üçün birinci seçimdir. 💫

Texniki Bilik və Təcrübə 🛠️

Ədyal, pledlər və örtüklərin materialı, hər birinin texniki xüsusiyyətlərini və təmizlənmə prosedurlarını göz önündən keçirməni tələb edir. Bizim texniki komandamız, bu sahədə çoxlu illik təcrübəyə malikdir və məhsullarınızın materialına və rənginə uyğun olaraq optimal təmizləmə prosedurlarını seçir. Ədyallarınız, pledləriniz və örtükləriniz müxtəlif növ qirlərlə mübarizə edə biləcək və təmiz, bərpa olunmuş bir görkəm əldə edəcək. 🌈

Təhlükəsizlik və Keyfiyyət Təminatı 🌿

Müştəri memnuniyyəti bizim üçün ən böyük prioritetdir. Biz müştərilərimizə şəxsi xidmət təklif edir və ədyal, pledlər və örtüklərinizə uyğun optimal təmizləmə təcrübəsi yaşatmağa çalışırıq. Sizə önəm verərək, sizin istəklərinizi və xüsusi tələblərinizi başa düşmək üçün dinləyirik. Məqsədimiz, sizə məhsullarınızı təmiz, parlaq və bərpa olunmuş şəkildə geri verərkən tam memnuniyyət təmin etməkdir. 🌟

Müştəri memnuniyyəti üzrə təhlükəsizlik və keyfiyyətə verdiyimiz diqqət, bizə güvənən müştərilərimizin bizimlə uzunmüddətli əlaqə qurmağa əlavə imkan verir. Biz, ədyallarınızın, pledlərinizin və örtüklərinizin yuyulması və saxlanması prosesində sizi məmnun etmək üçün çox çalışırıq. İnsi Sifariş Edin və Bir Zəngdə Qapıda Olaq! 📞🌟


""",reply_markup=reply_markup)
        

    elif choice == 'xalc':
        query.answer()

        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/service/xalca-yuma/overlok#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/service/xalca-yuma/overlok#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        #---------Photo
        photo_path = 'C:\\Users\\HP\\OneDrive\\İş masası\\hacathon\\xalca_4.jpg'  
        with open(photo_path, 'rb') as photo:
            context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
        #---------
        query.message.reply_text("""

Xalçaların Bərpası-Overlok 🪡

Evin interyerində xüsusi rola malik olan xalçalar zaman keçdikcə deformasiyaya uğrayır. Məsələn, kənar hissələri sökülərək yararsız vəziyyətə düşə bilirlər. Belə halda isə ağla ilk gələn köhnənin yenisi ilə əvəz olunmasıdır. Amma buna gərək yoxdur. Çünki 166 Xalça Yuma-da overlok xidməti var. Belə ki, mütəxəssislərimiz köhnəlmiş və yararsız halda olan xalçalarınızı bərpa edərək onu əvvəlki vəziyyətinə qaytaracaqlar. ✨

Overlok: Xalçalarınızın Bərpası Üçün Birinci Seçim 💫

Evimizdəki xalçalar, konfort və gözəllik hissini yaratmaqda ən əhəmiyyətli aksesuarlardır. Ancaq zamanla, onlar kirlər, ləkələr və yırtılmalar səbəbiylə zədə görə bilər. Bax tam bu anda şirkətimiz, xalçalarınızı yenidən rəngli və gözəl görünməsi üçün birinci seçim olaraq qarşınıza çıxır. 🌟

Texniki Mənbələr və Materiallar 🛠️

Overlok, xalçalarınızın bərpası üçün ən yüksək keyfiyyətli materiallar və texniki mənbələr istifadə edir. Xalçalarınızın materialına uyğun olan təhlükəsiz və effektiv məhsulları seçirik. Bu, xalçalarınızın çıxışının orijinal struktur və rənginə sədaqətli qalmasını təmin edir. Məhsullarımızın keyfiyyəti və dayanıqlılığı sayəsində, xalçalarınız bərpa olunduqdan sonra uzun ömürlü olacaq və sizə uzunmüddətli bir zövq təmin edəcəkdir. 🌈

Profesional Təmir və Bərpalar 🧵

166 Xalça kimi mütəxəssis şirkət olaraq, xalçalarınızın bərpası üçün ən inkişaf etmiş təcrübə və texniki biliklərə malik olduğumuzu iddia edirik. Təmir və bərpalarımız, xalçalarınızın orijinal görünüşünü bərpa etmək üçün müvafiq və effektiv prosedurlarla həyata keçirilir. Ləkələri, yırtıqları və digər deformasiyaları profesionallıqla aradan qaldırır, xalçalarınızın ilk günkü kimi parlaq və təmiz görünməsini təmin edirik. 🪣

Şəxsi Xidmət və Müştəri Məmnuniyyəti 💖

Bizim üçün müştəri məmnuniyyəti ən böyük prioritetdir. Xidmətlərimizə əsaslanan şəxsi xidmət anlayış və müştəri məmnuniyyəti, Overlok'un əsas prinsiplərindən biridir. Bizimlə əlaqə saxladığınızda, sizə qarşı hörmət və diqqətə əsaslanan bir xidmət təmin edirik. Xalçalarınızın xüsusi tələblərini başa düşmək üçün sizinlə əlaqə saxlayır və ən yaxşı həlli tapmaq üçün sizi dinləyirik. Hər bir müştəriyə şəxsi məsləhətlər verir və x



""",reply_markup=reply_markup)
#-----------------------------------------------Xalça Yuma






#-----------------------------------------------Yukdasima
# Yukdasima:
def service_details(update, context):
    query = update.callback_query
    choice = query.data
    
    if choice == 'beynelxalq_yukdasma':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/yukdasima#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/yukdasima#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Send detailed information about Beynəlxalq Yükdaşıma service
        query.message.reply_text("""·Dünyanın bir sıra nöqtələrinə sürətli və münasib qiymətlərə daşınmaların təmin edilməsini, daşınma prosesinin başdan sonra əməkdaşlarımız tərəfindən nəzarətdə saxlanmasını, müştərilərimizin operativ məlumatlandırılmasını və daşınmalarda təhlükəsizlik prinsiplərinə xüsusi diqqət ayrılmasını özümüzə prioritet seçmişik. O cümlədən son texnoloji yeniliklərin və tələb olunan beynəlxalq standartların işimizin hər sahəsinə tətbiq edilməsi sizin istəklərə layiqincə cavab vərməyə bizə imkan verəcəkdir. Uzaq məsafələri bizə və sizə yaxın edən əməkdaşlıqdan məmnun qalacağınıza ümid edirik.

Xidmətlərimizə aşağıdakılar daxildir:
·Dəmiryolu yükdaşimaları 🚂
·Hava yükdaşimaları ✈️
·Dəniz yolu ilə yükdaşima ⛴️
·Avtomobil yükdaşimaları 🚚""",reply_markup=reply_markup)

    elif choice == 'olke_yükdaşıma':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/yukdasima#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/yukdasima#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("""·1200-dən çox maşınla 500 kq-dan başlayaraq 26 tona qədər yüklərin müxtəlif təyinatlı maşınlarla (soyuduculu, evakuator, lapalı, tentli) siğortalı daşınmasını təmin edirik. Uzunluq olaraq isə minimum 2 metr uzunluqda Fiat Doblo maşınlarımızdan başlayaraq 13.6 metr uzunluğuna qədər tırlarımızla yükün uzunluğuna görə də seçim imkanları təqdim edirik. Əlbəttə ki, həftənin hər günü 24 saat operativ olaraq xidmətinizdəyik. 🕒🚚

Məhsullarınızın yüklənməsi üçün peşəkar fəhlə xidmətimiz, təhlükələrdən qorunması üçün bir neçə növdə (kardon, polietilen, penoplast, laminat) paketləmə xidmətimiz, saxlanması üçün davamlı nəzarət altında olan anbar xidmətimiz mövcuddur. 📦🛡️

Yalnız paytaxt və şəhərlərdə deyil, Azərbaycanda istənilən ünvanda xidmət göstəririk.""",reply_markup=reply_markup)
    elif choice == 'yuk_xidməti':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/yukdasima#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/yukdasima#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("""·166 Yükdaşıma şirkəti istənilən növ yüklərin bir nöqtədən, bir neçə nöqtəyə daşınmasını həyata keçirir. Yükdaşıma xidməti yükün həcmindən asılı olaraq olaraq bir neçə qrupa bölünür. Bunlara: yüngül yükdaşıma, ölkədaxili yükdaşıma və beynəlxalq yükdaşıma xidmətləri daxildir. Bundan başqa eyni region daxilində xidmət göstərən yük taksisi xidməti də mövcuddur. Ən ucuz yük daşıma xidməti olaraq sizlərə 7/24 xidmət edirik. Yüklərinizi bizə etibar edə biləriniz. 🚛💼

166 Yükdaşıma və Logistika şirkətinin təqdim etdiyi yükdaşıma xidmətlərindən sizdə yaralana bilərsiniz, ətraflı məlumat ilə tanış ola bilərsiniz. 🌐📦""",reply_markup=reply_markup)
    elif choice == 'yun_yükdaşıma':
        query.answer()
        keyboard = [[InlineKeyboardButton("😇 Sifariş Ver", url='https://166.az/az/yukdasima#'), 
                    InlineKeyboardButton("📞 Geri zəng", url='https://166.az/az/yukdasima#')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("""·Yüngül yükdaşıma xidmətimizə daha çox kiçik ölçülü və zəruri hesab edilən əşyaların daşınması nəzərdə tutulur. Bunun üçün ayrılmış xüsusi nəqliyyat vasitələri mövcuddur. Yüngül hesab etdiyiniz yükləri daşımaq üçün asan və sərfəli xidmətimizdən yararlana bilərsiniz. 📦💡
Qəza zamanı evakuator xidmətimiz sizi yolda qoymaz. 🚑🔧""",reply_markup=reply_markup)
    
    elif choice == 'yuk_taksisi':
        query.answer()
        query.message.reply_text("""·Yük taksisi xidməti daha çox yüngül və az yüklərin daşınması zamanı istifadə edilir. Evlərin daşınması zamanı, ağır yüklər  olmadıqda yük taksisi xidməti sizin üçün çox münasib olacaqdır. Daha iri həcimli nəqliyyat vasitələri əvəzinə yük taksilərini ucuz qiymətə sifariş edə bilərsiniz.

Xalca yuma xidməti cəmi 3 Azn!

Yükdaşıma xidmətini sifariş vermək üçün 166-ya zəng edə və ya onlayn qaydada: “SİFARİŞ VER”, “Geri zəng” və “Bizdən soruşun” bölmələrindən istifadə edə bilərsiniz.

""",reply_markup=reply_markup)
#---------------------------------------Yukdasima
    



updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button_click, pattern='^(site|elaqe|xidmet|unvan|reyler|karyera|avtopark|sirket)$'))
dispatcher.add_handler(CallbackQueryHandler(ferdi_button_click, pattern='^ferdi_'))
dispatcher.add_handler(CallbackQueryHandler(ferdi_button_click, pattern='^ferdi_services$'))
dispatcher.add_handler(CallbackQueryHandler(service_details, pattern='^(beynelxalq_yukdasma|yuk_taksisi|yun_yükdaşıma|olke_yükdaşıma|yuk_xidməti)$'))
dispatcher.add_handler(CallbackQueryHandler(xalca, pattern='^(edy|xalc|kor|sint|xus|ev)$'))
dispatcher.add_handler(CallbackQueryHandler(temizlik, pattern='^(pencere|kovrolit|fasad|perde|bag|temir|erazi|mebel|ofis|pak|evt|cil)$'))
dispatcher.add_handler(CallbackQueryHandler(usta, pattern='^(paketleme_xidmeti|diger_xidmetler|santexnik_usta|kondisioner_usta|elektrik_usta|mebel_usta)$'))
dispatcher.add_handler(CallbackQueryHandler(umum_melumat, pattern='^(umum_melumat)$'))
dispatcher.add_handler(CallbackQueryHandler(sanitariya, pattern='^(fumiqasiya|dermanlama|deratizasiya|dezinseksiya|dezinfeksiya|bagban_xidmeti)$'))
dispatcher.add_handler(CallbackQueryHandler(xidmet_menu, pattern='^(ferdi_karqo|ferdi_sanitariya|ferdi_texnoloji_heller|ferdi_usta|ferdi_isci_quvvesi|ferdi_anbar|ferdi_evakuasiya|ferdi_temizlik|ferdi_xalca|ferdi_yukdasma|ferdi_transport)$'))
dispatcher.add_handler(CallbackQueryHandler(pictures, pattern='^(pictures)$'))
dispatcher.add_handler(CallbackQueryHandler(pictures1, pattern='^(yuk|tem|ev|xal|an|isci|kar|tex|heyv)$'))

updater.start_polling()
updater.idle()
