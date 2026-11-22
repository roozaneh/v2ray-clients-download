#!/usr/bin/env python3
import os

APPS_DIR = "/home/hokar/.gemini/antigravity/scratch/v2ray-clients-download/apps"
os.makedirs(APPS_DIR, exist_ok=True)

apps_data = [
    {
        "id": "v2rayng",
        "name": "v2rayNG",
        "title": "دانلود کلاینت رسمی v2rayNG برای اندروید | نسخه کامل بدون دستکاری",
        "desc": "دانلود مستقیم آخرین نسخه پایدار v2rayNG با لینک مستقیم از گیت‌هاب رسمی سازنده (2dust). راهنمای راه‌اندازی، حل مشکل پینگ منفی یک، و جدول تمامی معماری‌های پردازنده.",
        "icon": "v2rayng.png",
        "version": "۲.۳.۱۵ (2.3.15)",
        "os": "اندروید (Android 5.0+)",
        "developer": "2dust (توسعه‌دهنده رسمی گیت‌هاب)",
        "license": "GPL v3.0 (متن‌باز و رایگان)",
        "core": "Xray-core / V2Ray-core",
        "size": "۶۸.۵ مگابایت",
        "primary_url": "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_universal.apk",
        "primary_text": "دانلود مستقیم (مناسب تمامی مدل‌های گوشی)",
        "tagline": "استانداردترین، باثبات‌ترین و محبوب‌ترین نرم‌افزار اتصال V2Ray برای گوشی‌های سامسونگ، شیائومی، هواوی و تمامی مدل‌های اندروید در ایران.",
        "security_note": "به دلیل قوانین مربوط به VpnService در گوگل‌پلی، نسخه رسمی صرفاً در گیت‌هاب منتشر می‌شود. برنامه‌های موجود در گوگل‌پلی تقلبی و غیررسمی هستند.",
        "builds": [
            ("نسخه جامع یونیورسال (پیشنهادی برای همه)", "v2rayNG_2.3.15_universal.apk", "۶۸.۵ MB", "سازگار با تمامی مدل‌ها بدون نیاز به شناخت نوع پردازنده", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_universal.apk"),
            ("معماری ۶۴ بیت جدید (arm64-v8a)", "v2rayNG_2.3.15_arm64-v8a.apk", "۳۰.۹ MB", "گوشی‌های مدرن تولید ۲۰۱۸ به بعد (سامسونگ، شیائومی)", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_arm64-v8a.apk"),
            ("معماری ۳۲ بیت قدیمی (armeabi-v7a)", "v2rayNG_2.3.15_armeabi-v7a.apk", "۳۱.۴ MB", "گوشی‌ها و تبلت‌های قدیمی‌تر اندرویدی", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_armeabi-v7a.apk"),
            ("شبیه‌سازها و کامپیوتر (x86_64)", "v2rayNG_2.3.15_x86_64.apk", "۳۱.۹ MB", "شبیه‌سازهای اندروید روی ویندوز نظیر LDPlayer و Nox", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_x86_64.apk"),
        ],
        "tutorial_steps": [
            ("نصب فایل", "فایل نصبی دانلود شده را لمس کرده و گزینه Install را بزنید. در صورت نمایش اخطار Play Protect، گزینه جزئیات بیشتر (More Details) و سپس نصب در هر شرایطی (Install Anyway) را انتخاب فرمایید."),
            ("دریافت کانفیگ", "کد کانفیگ یا لینک اشتراک خود را کپی کنید (می‌توانید از ربات @RoozanehNetBot کانفیگ تست رایگان تحویل بگیرید)."),
            ("افزودن به برنامه", "برنامه v2rayNG را باز کنید، آیکون + در بالای صفحه را بزنید و گزینه Import config from Clipboard را لمس نمایید."),
            ("اتصال پایدار", "کانفیگ افزوده شده را لمس کرده و دکمه دایره‌ای V در پایین صفحه را فشار دهید تا اتصال سبز شود.")
        ],
        "faqs": [
            ("چرا v2rayNG از گوگل پلی حذف شده است؟", "توسعه‌دهنده رسمی اپلیکیشن به دلیل سیاست‌های اختصاصی گوگل‌پلی درباره برنامه‌های فیلترشکن، از انتشار نسخه‌های جدید در این مارکت خودداری کرده است. تمامی فایل‌های این صفحه باینری خام و دست‌نخورده از گیت‌هاب رسمی ۲dust هستند."),
            ("پینگ منفی یک (-1 ms) در v2rayNG به چه معناست؟", "این پینگ به دلیل مسدود بودن بسته‌های تست ICMP توسط اپراتور سیم‌کارت است. در تنظیمات برنامه تست تاخیر را روی Real Delay بگذارید تا پینگ واقعی وب نمایش داده شود."),
            ("چگونه تنظیمات فرگمنت را در v2rayNG فعال کنیم؟", "در منوی تنظیمات v2rayNG، بخش Fragment را باز کرده و پارامتر Packets را روی tlshello، طول را برای همراه اول روی 10-20 و بازه تاخیر را روی 10-20ms قرار دهید.")
        ]
    },
    {
        "id": "happ",
        "name": "Happ",
        "title": "دانلود کلاینت مدرن Happ برای اندروید | سبک‌ترین فیلترشکن Xray",
        "desc": "دانلود مستقیم نرم‌افزار جدید و فوق‌العاده شیک Happ برای اندروید با اتصال هوشمند تک‌کلیک، مصرف باتری ناچیز و بدون تبلیغات.",
        "icon": "happ.png",
        "version": "۴.۱۱.۲ (4.11.2)",
        "os": "اندروید (Android 6.0+)",
        "developer": "Happ-proxy Team",
        "license": "Open Source",
        "core": "Xray-core / Sing-box",
        "size": "۶۶.۱ مگابایت",
        "primary_url": "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ.apk",
        "primary_text": "دانلود مستقیم (مناسب تمامی مدل‌های گوشی)",
        "tagline": "کلاینت نسل جدید با طراحی فوق‌العاده مدرن، روان و بدون کوچک‌ترین پیچیدگی. انتخابی بی‌نظیر برای کاربرانی که به دنبال سادگی مطلق و اتصال خودکار هستند.",
        "security_note": "نرم‌افزار Happ صددرصد متن‌باز و بدون هیچ‌گونه تبلیغات درون‌برنامه‌ای است.",
        "builds": [
            ("نسخه رسمی پایدار (پیشنهادی)", "Happ.apk", "۶۶.۱ MB", "فایل نصبی استاندارد برای تمام دستگاه‌ها", "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ.apk"),
            ("نسخه آزمایشی بتا", "Happ_beta.apk", "۶۶.۱ MB", "حاوی جدیدترین بهینه‌سازی‌های آزمایشی هسته", "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ_beta.apk")
        ],
        "tutorial_steps": [
            ("دانلود و نصب", "فایل Happ.apk را دانلود کرده و روی گوشی خود نصب نمایید."),
            ("کپی لینک سابسکریپشن", "لینک سابسکریپشن هوشمند روزنه نت را کپی کنید."),
            ("افزودن و بروزرسانی", "برنامه Happ را باز کنید، لینک را در بخش سابسکریپشن وارد کنید تا لیست سرورهای بهینه بارگذاری شود."),
            ("اتصال فوری", "دکمه اتصال بزرگ وسط صفحه را لمس کنید تا در کمتر از ۲ ثانیه متصل شوید.")
        ],
        "faqs": [
            ("مزیت Happ نسبت به v2rayNG چیست؟", "رابط کاربری بسیار مدرن‌تر، بازیابی خودکار اینترنت بعد از جابجایی بین وای‌فای و اینترنت سیم‌کارت، و تنظیمات خودکار هوشمند."),
            ("آیا روی گوشی‌های شیائومی و سامسونگ به خوبی کار می‌کند؟", "بله، Happ با رابط کاربری One UI سامسونگ و HyperOS شیائومی به طور کامل سازگار است.")
        ]
    },
    {
        "id": "streisand",
        "name": "Streisand",
        "title": "دانلود کلاینت رایگان Streisand برای آیفون و آیپد (iOS) | اپ استور رسمی",
        "desc": "بهترین کلاینت رایگان V2Ray و VLESS Reality برای سیستم‌عامل iOS بدون تبلیغات، مصرف باتری حداقل و هماهنگ با پردازنده‌های اپل.",
        "icon": "streisand.png",
        "version": "رسمی App Store",
        "os": "iOS 14.0 یا بالاتر (iPhone & iPad)",
        "developer": "Streisand App Team",
        "license": "Freeware (رایگان رسمی)",
        "core": "Sing-box Core",
        "size": "بر اساس نسخه اپ استور",
        "primary_url": "https://apps.apple.com/app/streisand/id6450534064",
        "primary_text": "دریافت رایگان از App Store اپل",
        "tagline": "کلاینت شماره ۱ پیشنهادی برای کاربران آیفون و آیپد. سازگاری کامل با هسته فوق‌پایدار Sing-box، بدون تبلیغات مزاحم و اتصال با یک لمس.",
        "security_note": "تایید شده توسط بخش بررسی امنیتی شرکت اپل و منتشر شده در اپ‌استور رسمی.",
        "builds": [
            ("نسخه رسمی اپ‌استور (iOS / iPadOS)", "Streisand on App Store", "رایگان", "قابل نصب روی آیفون، آیپد و مک‌های مجهز به اپل سیلیکون (M1/M2/M3)", "https://apps.apple.com/app/streisand/id6450534064")
        ],
        "tutorial_steps": [
            ("دانلود از App Store", "بر روی دکمه دریافت از اپ‌استور کلیک کنید و برنامه را با Apple ID خود به رایگان دانلود نمایید."),
            ("کپی کانفیگ", "کانفیگ اختصاصی یا لینک سابسکریپشن روزنه نت را کپی فرمایید."),
            ("ایمپورت در برنامه", "وارد برنامه Streisand شوید، علامت + در بالای صفحه را لمس کرده و Import from Clipboard را بزنید."),
            ("روشن کردن اتصال", "سوئیچ اتصال در بالای صفحه را روشن کنید و در صورت درخواست سیستم، اجازه ساخت پروفایل VPN را تایید فرمایید.")
        ],
        "faqs": [
            ("آیا برنامه Streisand رایگان است؟", "بله، این نرم‌افزار به صورت کاملاً رایگان و بدون هیچ‌گونه تبلیغ یا نیاز به خرید اشتراک درون‌برنامه‌ای عرضه می‌شود."),
            ("آیا از پروتکل‌های Reality و سابسکریپشن پشتیبانی می‌کند؟", "بله، Streisand از پروتکل‌های VLESS Reality و آپدیت خودکار لیست کانفیگ‌ها به طور کامل پشتیبانی می‌کند.")
        ]
    },
    {
        "id": "v2rayn",
        "name": "v2rayN",
        "title": "دانلود نرم‌افزار v2rayN برای ویندوز | نسخه رسمی ۶۴ بیت با هسته کامل Xray",
        "desc": "دانلود مستقیم نسخه کامل v2rayN ویندوز مجهز به هسته Xray، قابلیت System Proxy و حالت TUN Mode برای اجرای بازی‌ها و نرم‌افزارهای دسکتاپ.",
        "icon": "v2rayn.png",
        "version": "۷.۲۵.۶ (7.25.6)",
        "os": "ویندوز ۱۰ و ۱۱ (64-bit)",
        "developer": "2dust (توسعه‌دهنده رسمی گیت‌هاب)",
        "license": "GPL v3.0 (متن‌باز و رایگان)",
        "core": "Xray-core / Sing-box Core",
        "size": "۱۶۰.۹ مگابایت (With Core)",
        "primary_url": "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64.zip",
        "primary_text": "دانلود مستقیم نسخه کامل ویندوز ۶۴ بیت (Zip)",
        "tagline": "قدرتمندترین و پرامکانات‌ترین کلاینت ویندوز برای کامپیوتر و لپ‌تاپ. مناسب وب‌گردی، دانلود پرسرعت، تریدینگ و بازی‌های آنلاین بدون افت پینگ.",
        "security_note": "بسته رسمی ارائه‌شده همراه با تمامی هسته‌های رسمی است و نیازی به دانلود جداگانه Xray Core ندارد.",
        "builds": [
            ("نسخه کامل ویندوز ۶۴ بیت با هسته (پیشنهادی)", "v2rayN-windows-64.zip", "۱۶۰.۹ MB", "کامل‌ترین بسته بدون نیاز به نصب، آماده اجرا در ویندوز ۱۰ و ۱۱", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64.zip"),
            ("نسخه ویندوز ۶۴ بیت Desktop Runtime", "v2rayN-windows-64-desktop.zip", "۱۳۸.۰ MB", "مخصوص سیستم‌هایی که دات‌نت ران‌تایم دارند", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64-desktop.zip"),
            ("نسخه سبک ویندوز ۳۲ بیت", "v2rayN-windows-86.zip", "۱۳۴.۵ MB", "برای سیستم‌های قدیمی‌تر ۳۲ بیتی", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-86.zip"),
            ("نسخه مک او اس (macOS)", "v2rayN-macos-arm64.dmg", "۱۲۹.۲ MB", "نسخه مخصوص مک‌های Apple Silicon (M1/M2/M3)", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-macos-arm64.dmg")
        ],
        "tutorial_steps": [
            ("اکسترکت کردن فایل Zip", "فایل فشرده دانلود شده را با کلیک راست و گزینه Extract All در یک پوشه (مثلاً در درایو C یا دسکتاپ) باز کنید."),
            ("اجرای برنامه", "روی فایل v2rayN.exe دابل‌کلیک کنید تا برنامه در کنار ساعت ویندوز باز شود."),
            ("افزودن کانفیگ", "کانفیگ کپی‌شده را با فشردن کلیدهای میانبر Ctrl + V در محیط برنامه پیست کنید."),
            ("فعال‌سازی پراکسی", "در نوار پایین برنامه، گزینه System Proxy را روی Set System Proxy بگذارید. برای بازی‌ها می‌توانید گزینه Enable Tun را تیک بزنید.")
        ],
        "faqs": [
            ("آیا v2rayN نیاز به نصب دارد؟", "خیر، این نرم‌افزار پرتابل است و فقط با اکسترکت کردن فایل فشرده قابل اجراست."),
            ("حالت Tun Mode در ویندوز چه کاربردی دارد؟", "حالت TUN تمام ترافیک سیستم‌عامل (از جمله بازی‌های آنلاین نظیر وارزون، کلاینت‌های صرافی و تلگرام دسکتاپ) را بدون نیاز به تنظیم جداگانه وارد تونل امن می‌کند.")
        ]
    },
    {
        "id": "nekobox",
        "name": "NekoBox",
        "title": "دانلود کلاینت گیمینگ NekoBox برای اندروید | کمترین تاخیر و پینگ",
        "desc": "دانلود مستقیم کلاینت تخصصی NekoBox بر پایه هسته Sing-box برای گیمرهای اندروید، کاهش تاخیر و پینگ در بازی‌های آنلاین.",
        "icon": "nekobox.png",
        "version": "۱.۴.۲ (1.4.2)",
        "os": "اندروید (Android 6.0+)",
        "developer": "MatsuriDayo",
        "license": "GPL v3.0",
        "core": "Sing-box Core",
        "size": "۱۴.۵ مگابایت",
        "primary_url": "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-arm64-v8a.apk",
        "primary_text": "دانلود مستقیم نسخه ۶۴ بیت (arm64-v8a)",
        "tagline": "کلاینت تخصصی و مهندسی‌شده برای گیمرها و کاربران حرفه‌ای. بهینه‌سازی شده برای حداقل مصرف پهنای باند و کاهش پینگ بسته‌های UDP.",
        "security_note": "متن‌باز و پاک، استخراج مستقیم از گیت‌هاب MatsuriDayo.",
        "builds": [
            ("پردازنده‌های جدید ۶۴ بیتی (پیشنهادی)", "NekoBox-1.4.2-arm64-v8a.apk", "۱۴.۵ MB", "تقریباً ۱۰۰٪ گوشی‌های سامسونگ و شیائومی مدرن", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-arm64-v8a.apk"),
            ("پردازنده‌های قدیمی ۳۲ بیتی", "NekoBox-1.4.2-armeabi-v7a.apk", "۱۴.۷ MB", "گوشی‌های قدیمی با اندروید ۵ و ۶", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-armeabi-v7a.apk"),
            ("شبیه‌سازهای کامپیوتر (x86_64)", "NekoBox-1.4.2-x86_64.apk", "۱۵.۲ MB", "شبیه‌سازهای اندروید پی‌سی", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-x86_64.apk")
        ],
        "tutorial_steps": [
            ("نصب نسخه arm64", "فایل نصبی مناسب گوشی‌های امروزی (arm64-v8a) را دانلود و نصب کنید."),
            ("افزودن کانفیگ", "کانفیگ روزنه نت را کپی کرده و از منوی بالای برنامه علامت افزودن را بزنید."),
            ("اتصال به سرور کم‌پینگ", "تست پینگ URL Test را اجرا کرده و سرور با کمترین تاخیر میلی‌ثانیه‌ای را انتخاب نمایید.")
        ],
        "faqs": [
            ("چرا نسخه یونیورسال ندارد؟", "توسعه‌دهنده NekoBox برای کاهش حجم فایل نصبی، بسته‌ها را به تفکیک معماری منتشر کرده است که نسخه arm64 برای ۹۵٪ گوشی‌های امروزی مناسب است.")
        ]
    },
    {
        "id": "singbox",
        "name": "Sing-box",
        "title": "دانلود کلاینت رسمی Sing-box برای اندروید | سریع‌ترین معماری Go",
        "desc": "دانلود مستقیم نسخه رسمی کلاینت SagerNet Sing-box برای اندروید با هسته نسل جدید، کمترین مصرف رم و بالاترین پایداری در شبکه.",
        "icon": "singbox.png",
        "version": "۱.۱۴.۴ (1.14.4)",
        "os": "اندروید (Android 7.0+)",
        "developer": "SagerNet Team",
        "license": "GPL v3.0",
        "core": "Sing-box Native Go",
        "size": "۱۲۱.۴ مگابایت (Universal)",
        "primary_url": "https://github.com/SagerNet/sing-box/releases/download/v1.14.4/SFA-1.14.4-universal.apk",
        "primary_text": "دانلود مستقیم نسخه جامع یونیورسال (APK)",
        "tagline": "کلاینت مرجع و انقلابی توسعه‌یافته توسط تیم اصلی SagerNet. پرچمدار فناوری‌های ضدسانسور با سبک‌ترین معماری نرم‌افزاری در سال ۲۰۲۶.",
        "security_note": "سورس کاملاً باز با قابلیت ممیزی کد در مخزن SagerNet/sing-box.",
        "builds": [
            ("نسخه استاندارد یونیورسال (پیشنهادی)", "SFA-1.14.4-universal.apk", "۱۲۱.۴ MB", "سازگار با تمامی پردازنده‌ها و مدل‌های اندروید", "https://github.com/SagerNet/sing-box/releases/download/v1.14.4/SFA-1.14.4-universal.apk"),
            ("معماری ۶۴ بیت اختصاصی", "SFA-1.14.4-arm64-v8a.apk", "۳۴.۹ MB", "حجم کم، ویژه گوشی‌های مدرن ۶۴ بیت", "https://github.com/SagerNet/sing-box/releases/download/v1.14.4/SFA-1.14.4-arm64-v8a.apk"),
            ("معماری ۳۲ بیت اختصاصی", "SFA-1.14.4-armeabi-v7a.apk", "۳۴.۸ MB", "ویژه گوشی‌های ۳۲ بیت", "https://github.com/SagerNet/sing-box/releases/download/v1.14.4/SFA-1.14.4-armeabi-v7a.apk")
        ],
        "tutorial_steps": [
            ("نصب فایل یونیورسال", "فایل نصبی را اجرا و نصب فرمایید."),
            ("افزودن پروفایل", "از بخش Profiles گزینه New Profile را بزنید و لینک سابسکریپشن خود را وارد کنید."),
            ("اتصال به سرور", "پروفایل را فعال کرده و کلید اتصال در صفحه اصلی را روشن کنید.")
        ],
        "faqs": [
            ("چرا Sing-box را نسل آینده فیلترشکن‌ها می‌دانند؟", "به دلیل بازنویسی ماژولار در زبان Go، حذف وابستگی‌های سنگین و پشتیبانی بومی از Reality، ShadowTLS و TUIC v5 با کمترین مصرف باتری.")
        ]
    },
    {
        "id": "v2box",
        "name": "V2Box",
        "title": "دانلود کلاینت V2Box برای آیفون، آیپد و مک | رابط کاربری ساده",
        "desc": "دانلود مستقیم V2Box کلاینت رایگان و ساده اکوسیستم اپل با اسکنر کیو‌آرکد لحظه‌ای، پشتیبانی از Reality و پایداری بالا.",
        "icon": "v2box.png",
        "version": "رسمی App Store",
        "os": "iOS 14.0+ و macOS",
        "developer": "V2Box Dev Team",
        "license": "Freeware (رایگان)",
        "core": "V2Box Engine",
        "size": "بر اساس نسخه اپ استور",
        "primary_url": "https://apps.apple.com/app/v2box-v2ray-client/id6446814690",
        "primary_text": "دریافت رایگان از App Store اپل",
        "tagline": "کلاینت بسیار آسان و روان برای کاربران آیفون و مک بوک با امکان آپدیت خودکار لیست کانفیگ‌ها و اسکن سریع کدهای QR.",
        "security_note": "موجود در اپ‌استور رسمی اپل و فاقد هرگونه لاگ یا ترافیک غیرمجاز.",
        "builds": [
            ("نسخه رسمی اپ‌استور برای iOS و macOS", "V2Box on App Store", "رایگان", "آیفون، آیپد و مک‌های مجهز به تراشه‌های اپل سیلیکون", "https://apps.apple.com/app/v2box-v2ray-client/id6446814690")
        ],
        "tutorial_steps": [
            ("نصب از اپ استور", "برنامه را از اپ‌استور دانلود فرمایید."),
            ("اسکن یا پیست کانفیگ", "کانفیگ کپی شده را با لمس گزینه Add Config پیست کنید یا کد QR را اسکن نمایید."),
            ("اتصال", "اسلایدر اتصال را بکشید تا اینترنت آزاد و پرسرعت متصل گردد.")
        ],
        "faqs": [
            ("آیا V2Box روی مک بوک هم کار می‌کند؟", "بله، نسخه مک بوک این نرم‌افزار در اپ‌استور مک در دسترس است و عملکرد پایداری دارد.")
        ]
    },
    {
        "id": "hiddify",
        "name": "Hiddify",
        "title": "دانلود نرم‌افزار جامع Hiddify برای اندروید و ویندوز | رابط کاملاً فارسی",
        "desc": "دانلود مستقیم کلاینت کراس‌پلتفرم Hiddify با رابط کاربری فارسی و مدرن، پشتیبانی خودکار از پروتکل‌های امن و هسته Sing-box.",
        "icon": "hiddify.png",
        "version": "۵.۹.۱۵ (5.9.15)",
        "os": "اندروید، ویندوز، مک و لینوکس",
        "developer": "Hiddify Community",
        "license": "GPL v3.0 (متن‌باز)",
        "core": "Sing-box Core",
        "size": "اندروید: ۱۷۹.۲ MB | ویندوز: ۴۸.۸ MB",
        "primary_url": "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Android-universal.apk",
        "primary_text": "دانلود مستقیم APK اندروید (مناسب همه گوشی‌ها)",
        "tagline": "نرم‌افزار جامع، مدرن و چندسکویی با زبان شیرین فارسی، مسیریابی هوشمند برای وب‌سایت‌های ایرانی و اتصال تک‌لمسی بدون سردرگمی.",
        "security_note": "متن‌باز و شفاف با پشتیبانی فعال از تمامی پروتکل‌های ضد فیلترینگ.",
        "builds": [
            ("اندروید نسخه جامع یونیورسال (پیشنهادی)", "Hiddify-Android-universal.apk", "۱۷۹.۲ MB", "سازگار با تمامی گوشی‌ها و تبلت‌های اندروید", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Android-universal.apk"),
            ("ویندوز نسخه Setup نصبی ۶۴ بیت", "Hiddify-Windows-Setup-x64.exe", "۴۸.۸ MB", "نصب آسان در ویندوز ۱۰ و ۱۱", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Windows-Setup-x64.exe"),
            ("ویندوز نسخه پرتابل (بدون نیاز به نصب)", "Hiddify-Windows-Portable-x64.zip", "۵۷.۱ MB", "اجرای سریع و بدون ردپا در ویندوز", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Windows-Portable-x64.zip"),
            ("مک او اس (macOS)", "Hiddify-MacOS.pkg", "۴۸.۰ MB", "فایل نصبی پکیج مک بوک", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-MacOS.pkg"),
            ("لینوکس (Linux AppImage)", "Hiddify-Linux-x64.AppImage", "۶۹.۸ MB", "اجرای مستقیم در اوبونتو و لینوکس ۶۴ بیت", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Linux-x64.AppImage")
        ],
        "tutorial_steps": [
            ("نصب برنامه", "نسخه متناسب با سیستم‌عامل خود (اندروید یا ویندوز) را نصب کنید."),
            ("افزودن پروفایل", "لینک سابسکریپشن اختصاصی خود را در بخش Profile اضافه فرمایید."),
            ("اتصال هوشمند", "روی دکمه اتصال بزنید تا بهترین و سریع‌ترین سرور به شکل خودکار انتخاب شود.")
        ],
        "faqs": [
            ("مزیت منوی فارسی Hiddify چیست؟", "تمام گزینه‌های فنی و تنظیمات روتینگ به زبان فارسی روان ترجمه شده‌اند و هر کاربری بدون دانش تخصصی می‌تواند از آن استفاده کند.")
        ]
    },
    {
        "id": "nekoray",
        "name": "NekoRay",
        "title": "دانلود نرم‌افزار NekoRay برای ویندوز | کلاینت تخصصی Tun Mode بدون نصب",
        "desc": "دانلود مستقیم نسخه پرتابل NekoRay ویندوز ۶۴ بیت با هسته Sing-box و Xray، مناسب برای بازی‌های آنلاین و عبور کامل ترافیک سیستم.",
        "icon": "nekoray.png",
        "version": "۴.۰.۱ (4.0.1)",
        "os": "ویندوز ۱۰ و ۱۱ (64-bit) و لینوکس",
        "developer": "MatsuriDayo",
        "license": "GPL v3.0",
        "core": "Sing-box / Xray",
        "size": "۳۹.۷ مگابایت (Portable)",
        "primary_url": "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-windows64.zip",
        "primary_text": "دانلود مستقیم فایل Zip پرتابل ویندوز",
        "tagline": "کلاینت مهندسی و سبک کامپیوتر بدون نیاز به نصب، مجهز به درایور قدرتمند Tun Mode برای عبور بدون وقفه ترافیک بازی‌ها و نرم‌افزارها.",
        "security_note": "متن‌باز و قابل بازرسی با حجم کم و مصرف ناچیز پردازنده.",
        "builds": [
            ("ویندوز ۶۴ بیت پرتابل (پیشنهادی)", "nekoray-4.0.1-2024-12-12-windows64.zip", "۳۹.۷ MB", "ویندوز ۱۰ و ۱۱ بدون نیاز به نصب", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-windows64.zip"),
            ("لینوکس دبیان و اوبونتو (.deb)", "nekoray-4.0.1-2024-12-12-debian-x64.deb", "۳۳.۰ MB", "نصب آسان در Ubuntu/Debian", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-debian-x64.deb"),
            ("لینوکس پرتابل (.zip)", "nekoray-4.0.1-2024-12-12-linux64.zip", "۳۶.۱ MB", "اجرا در تمامی توزیع‌های لینوکس ۶۴ بیت", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-linux64.zip")
        ],
        "tutorial_steps": [
            ("اکسترکت کردن فایل", "فایل فشرده را اکسترکت کنید و nekoray.exe را اجرا نمایید."),
            ("انتخاب هسته Sing-box", "در اولین اجرا، هسته پیشنهادی Sing-box را تایید فرمایید."),
            ("افزودن کانفیگ", "کانفیگ کپی‌شده را پیست کرده و تیک گزینه Tun Mode را برای فعال‌سازی کامل بزنید.")
        ],
        "faqs": [
            ("تفاوت NekoRay با v2rayN چیست؟", "نکورای حجم بسیار کمتری دارد (حدود ۴۰ مگابایت در مقابل ۱۶۰ مگابایت)، سبک‌تر است و تمرکز اصلی آن بر پیاده‌سازی سریع حالت TUN است.")
        ]
    }
]

from build_app_pages import SHARED_HEAD_TEMPLATE

for app in apps_data:
    # Build content body
    builds_html = ""
    for b_name, b_file, b_size, b_desc, b_url in app["builds"]:
        builds_html += f"""
        <div class="glass-card rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border border-slate-800">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="font-bold text-sm text-white">{b_name}</span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-slate-800 text-slate-300 font-mono">{b_size}</span>
            </div>
            <div class="text-xs text-slate-400 mb-1">{b_desc}</div>
            <div class="text-[11px] font-mono text-slate-500">{b_file}</div>
          </div>
          <div class="shrink-0 w-full sm:w-auto">
            <a href="{b_url}" target="_blank" rel="noopener noreferrer"
               class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-brand-400 hover:text-white border border-slate-700 text-xs font-semibold transition-all inline-flex items-center justify-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
              <span>دانلود مستقیم فایل</span>
            </a>
          </div>
        </div>
        """

    steps_html = ""
    for idx, (s_title, s_desc) in enumerate(app["tutorial_steps"], 1):
        steps_html += f"""
        <div class="glass-card rounded-2xl p-5 border border-slate-800 flex items-start gap-4">
          <div class="w-8 h-8 rounded-xl bg-brand-500/20 text-brand-400 font-bold flex items-center justify-center shrink-0 text-sm">
            {idx}
          </div>
          <div>
            <h4 class="font-bold text-sm text-white mb-1">{s_title}</h4>
            <p class="text-xs text-slate-300 leading-relaxed">{s_desc}</p>
          </div>
        </div>
        """

    faqs_html = ""
    for q, a in app["faqs"]:
        faqs_html += f"""
        <details class="group glass-card rounded-2xl p-5 border border-slate-800 transition-all [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between cursor-pointer font-bold text-xs sm:text-sm text-white">
            <span>{q}</span>
            <span class="text-slate-400 group-open:rotate-180 transition-transform">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </span>
          </summary>
          <div class="mt-3 text-slate-300 text-xs leading-relaxed border-t border-slate-800/80 pt-3">
            {a}
          </div>
        </details>
        """

    content_body = f"""
    <!-- Advanced Builds Table -->
    <section class="mb-14">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h2 class="text-lg sm:text-xl font-black text-white">جدول تمامی نسخه‌ها و معماری‌های رسمی ({app['name']})</h2>
          <p class="text-xs text-slate-400">برای کاربران حرفه‌ای: دسترسی مستقیم به بسته‌های تفکیک‌شده پردازنده و پلتفرم</p>
        </div>
      </div>
      <div class="space-y-3">
        {builds_html}
      </div>
    </section>

    <!-- Security & Trust Callout -->
    <section class="mb-14">
      <div class="glass-card rounded-3xl p-6 border border-emerald-500/30 bg-emerald-950/15">
        <div class="flex items-start gap-4">
          <div class="text-2xl shrink-0">🛡️</div>
          <div>
            <h3 class="text-base font-bold text-emerald-400 mb-1">تضمین اصالت کد منبع و سلامت فایل‌های رسمی</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-3">
              {app['security_note']} تمامی بسته‌های دانلودی بالا مستقیماً از وب‌هوک و سرورهای رسمی گیت‌هاب استخراج شده‌اند و هیچ‌گونه تغییر، تبلیغات یا دستکاری در ساختار باینری آنها اعمال نگردیده است.
            </p>
            <div class="flex flex-wrap gap-2 text-[11px] text-emerald-300">
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">تایید اصالت SHA-256</span>
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">بدون بدافزار و کریپتوماینر</span>
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">حفظ ۱۰۰٪ حریم خصوصی</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Setup Guide -->
    <section class="mb-14">
      <h2 class="text-lg sm:text-xl font-black text-white mb-2">راهنمای گام‌به‌گام راه‌اندازی {app['name']}</h2>
      <p class="text-xs text-slate-400 mb-6">مراحل ساده اتصال در کمتر از یک دقیقه بدون نیاز به پیکربندی دستی:</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {steps_html}
      </div>
    </section>

    <!-- Dedicated FAQ -->
    <section class="mb-14">
      <h2 class="text-lg sm:text-xl font-black text-white mb-4">سوالات متداول کلاینت {app['name']}</h2>
      <div class="space-y-3">
        {faqs_html}
      </div>
    </section>

    <!-- Testing CTA Banner (Calm & Subtle) -->
    <section>
      <div class="glass-card rounded-3xl p-6 border border-slate-800 bg-slate-900/60 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div>
          <h4 class="text-sm sm:text-base font-bold text-white mb-1">نیاز به سرور پرسرعت و تست شده دارید؟</h4>
          <p class="text-xs text-slate-400">می‌توانید کانفیگ تست هدیه VLESS Reality را از ربات تلگرامی روزنه نت دریافت فرمایید.</p>
        </div>
        <a href="https://t.me/RoozanehNetBot?start=gh_download" target="_blank" rel="noopener noreferrer"
           class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-brand-400 text-xs font-semibold border border-slate-700 transition-colors shrink-0">
          ورود به ربات و دریافت کانفیگ تست ←
        </a>
      </div>
    </section>
    """

    download_target = 'target="_blank" rel="noopener noreferrer"' if 'apple.com' in app["primary_url"] else ''

    full_html = SHARED_HEAD_TEMPLATE.format(
        title=app["title"],
        description=app["desc"],
        filename=f"{app['id']}.html",
        app_name=app["name"],
        icon=app["icon"],
        version_badge=app["version"],
        os_badge=app["os"],
        tagline=app["tagline"],
        developer=app["developer"],
        license=app["license"],
        core=app["core"],
        primary_download_url=app["primary_url"],
        primary_button_text=app["primary_text"],
        file_size_text=app["size"],
        download_target=download_target,
        content_body=content_body
    )

    out_file = os.path.join(APPS_DIR, f"{app['id']}.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated {out_file}")

print("All dedicated app pages generated successfully.")
