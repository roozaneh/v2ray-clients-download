#!/usr/bin/env python3
import re

HTML_PATH = "/home/hokar/.gemini/antigravity/scratch/v2ray-clients-download/index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Header Button: Replace "۲ تا ۳ گیگ تست رایگان" with "دریافت کلاینت‌ها"
content = re.sub(
    r'<a href="https://t\.me/RoozanehNetBot\?start=gh_download" target="_blank" rel="noopener noreferrer"\s+class="inline-flex items-center gap-2 px-4 sm:px-5 py-2\.5 rounded-full bg-brand-600[^"]*">.*?<span>۲ تا ۳ گیگ تست رایگان</span>\s*</a>',
    '''<a href="#downloads"
           class="inline-flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-brand-600 hover:bg-brand-500 text-white font-semibold text-xs sm:text-sm transition-all shadow-md shadow-brand-600/30 hover:-translate-y-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          <span>دریافت کلاینت‌ها</span>
        </a>''',
    content,
    flags=re.DOTALL
)

# 2. Update Hero Subtitle & Action Buttons
old_hero_sub = r'<!-- Subtitle -->\s*<p class="text-base sm:text-lg md:text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed mb-10">.*?<!-- Primary Action Buttons -->'
new_hero_sub = '''<!-- Subtitle -->
      <p class="text-base sm:text-lg md:text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed mb-10">
        پرتال رسمی و امن دریافت آخرین نسخه‌های نرم‌افزارهای متن‌باز V2Ray، Xray و Sing-box برای اندروید، آیفون، ویندوز و مک. 
        فایل‌های خام باینری مستقیم از مخازن گیت‌هاب رسمی بدون واسطه، بدون بدافزار و همراه با دانشنامه فنی دور زدن DPI.
      </p>

      <!-- Primary Action Buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 max-w-lg mx-auto mb-16">
        <a href="#downloads"
           class="w-full sm:w-auto px-8 py-4 rounded-full bg-brand-600 hover:bg-brand-500 text-white font-bold text-base transition-all shadow-xl shadow-brand-600/30 hover:-translate-y-0.5 flex items-center justify-center gap-2">
          <span>مشاهده و دانلود کلاینت‌ها</span>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
          </svg>
        </a>
        <a href="#whitepaper"
           class="w-full sm:w-auto px-8 py-4 rounded-full bg-slate-800/90 hover:bg-slate-700/90 text-slate-200 border border-slate-700 font-semibold text-base transition-all hover:-translate-y-0.5 flex items-center justify-center gap-2">
          <span>دانشنامه فنی و حل مشکلات</span>
          <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </a>
      </div>'''

content = re.sub(
    r'<!-- Subtitle -->.*?<!-- Trust Pillars Grid -->',
    new_hero_sub + '\n\n      <!-- Trust Pillars Grid -->',
    content,
    flags=re.DOTALL
)

# 3. Trust Pillar 4 update: Replace "تست ۲ تا ۳ گیگابایت" with "۱۰۰٪ حریم خصوصی"
content = re.sub(
    r'<div class="font-bold text-sm text-white">تست ۲ تا ۳ گیگابایت</div>\s*</div>\s*<p class="text-xs text-slate-400 leading-relaxed">تحویل آنی در ربات بدون کارت بانکی قبل از هرگونه خرید\.</p>',
    '''<div class="font-bold text-sm text-white">۱۰۰٪ حریم خصوصی</div>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">کلاینت‌های بدون لاگ و مبتنی بر مجوزهای آزاد بین‌المللی.</p>''',
    content
)

# 4. App Cards update:
# v2rayNG Card
content = re.sub(
    r'<h3 class="text-xl font-bold text-white mb-2">v2rayNG \(نسخه جامع یونیورسال\)</h3>',
    r'<h3 class="text-xl font-bold text-white mb-2">v2rayNG (نسخه رسمی اندروید)</h3>',
    content
)
content = re.sub(
    r'<span>دانلود مستقیم فایل Universal APK</span>\s*</a>\s*<a href="https://t\.me/RoozanehNetBot\?start=gh_download"[^>]*>.*?<span>🎁 دریافت ۲ تا ۳ گیگ کانفیگ تست رایگان</span>\s*</a>',
    '''<span>دانلود مستقیم (سازگار با تمامی گوشی‌ها)</span>
            </a>
            <a href="apps/v2rayng.html"
               class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-brand-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>اطلاعات بیشتر، راهنمای راه‌اندازی و سایر معماری‌ها ←</span>
            </a>''',
    content,
    flags=re.DOTALL
)

# Happ Card
content = re.sub(
    r'<span>دانلود مستقیم فایل Happ\.apk</span>\s*</a>\s*<a href="https://t\.me/RoozanehNetBot\?start=gh_download"[^>]*>.*?<span>دریافت کانفیگ سابسکریپشن Happ</span>\s*</a>',
    '''<span>دانلود مستقیم (سازگار با تمامی گوشی‌ها)</span>
            </a>
            <a href="apps/happ.html"
               class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-teal-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>اطلاعات بیشتر و راهنمای راه‌اندازی ←</span>
            </a>''',
    content,
    flags=re.DOTALL
)

# Streisand Card
content = re.sub(
    r'<a href="#tutorial" class="w-full py-2\.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 font-medium text-xs transition-all flex items-center justify-center">\s*<span>آموزش تصویری راه‌اندازی در ۳۰ ثانیه</span>\s*</a>',
    '''<a href="apps/streisand.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-brand-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>راهنمای راه‌اندازی در آیفون و آیپد ←</span>
            </a>''',
    content,
    flags=re.DOTALL
)

# v2rayN Card
content = re.sub(
    r'<a href="#tutorial" class="w-full py-2\.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 font-medium text-xs transition-all flex items-center justify-center">\s*<span>راهنمای فعال‌سازی Tun Mode</span>\s*</a>',
    '''<a href="apps/v2rayn.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-blue-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>راهنمای فعال‌سازی Tun Mode و سایر معماری‌ها ←</span>
            </a>''',
    content,
    flags=re.DOTALL
)

# NekoBox Card
content = re.sub(
    r'(<a href="https://github\.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1\.4\.2/NekoBox-1\.4\.2-arm64-v8a\.apk"[^>]*>.*?<span>دانلود مستقیم فایل APK از گیت‌هاب</span>\s*</a>)(\s*</div>\s*</div>\s*<!-- Card 6)',
    r'''\1
            <a href="apps/nekobox.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-purple-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>اطلاعات بیشتر و نسخه‌های ۳۲ بیت و شبیه‌ساز ←</span>
            </a>\2''',
    content,
    flags=re.DOTALL
)

# V2Box Card
content = re.sub(
    r'(<a href="https://apps\.apple\.com/app/v2box-v2ray-client/id6446814690"[^>]*>.*?<span>دریافت رایگان از App Store</span>\s*</a>)(\s*</div>\s*</div>\s*<!-- Card 7)',
    r'''\1
            <a href="apps/v2box.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-brand-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>راهنمای تصویری راه‌اندازی در آیفون و مک ←</span>
            </a>\2''',
    content,
    flags=re.DOTALL
)

# Hiddify Card
content = re.sub(
    r'<span>دانلود مستقیم APK اندروید \(Universal\)</span>',
    r'<span>دانلود APK اندروید (سازگار با همه گوشی‌ها)</span>',
    content
)
content = re.sub(
    r'(<a href="https://github\.com/hiddify/hiddify-app/releases/download/v5\.9\.15/Hiddify-Windows-Setup-x64\.exe"[^>]*>.*?<span>دانلود مستقیم نسخه Setup ویندوز \(x64\)</span>\s*</a>)(\s*</div>\s*</div>\s*<!-- Card 8)',
    r'''\1
            <a href="apps/hiddify.html" class="w-full py-2 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-cyan-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>نسخه پرتابل، مک، لینوکس و راهنمای راه‌اندازی ←</span>
            </a>\2''',
    content,
    flags=re.DOTALL
)

# NekoRay Card
content = re.sub(
    r'(<a href="https://github\.com/MatsuriDayo/nekoray/releases/download/4\.0\.1/nekoray-4\.0\.1-2024-12-12-windows64\.zip"[^>]*>.*?<span>دانلود مستقیم فایل Zip ویندوز ۶۴ بیت</span>\s*</a>)(\s*</div>\s*</div>\s*<!-- Card 9)',
    r'''\1
            <a href="apps/nekoray.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-indigo-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>راهنمای تنظیم Tun Mode و نسخه لینوکس ←</span>
            </a>\2''',
    content,
    flags=re.DOTALL
)

# Sing-box Card
content = re.sub(
    r'<span>دانلود مستقیم فایل Universal APK</span>',
    r'<span>دانلود مستقیم (سازگار با تمامی گوشی‌ها)</span>',
    content
)
content = re.sub(
    r'(<a href="https://github\.com/SagerNet/sing-box/releases/download/v1\.14\.4/SFA-1\.14\.4-universal\.apk"[^>]*>.*?<span>دانلود مستقیم \(سازگار با تمامی گوشی‌ها\)</span>\s*</a>)(\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>\s*<!-- CTA Trial Intermission -->)',
    r'''\1
            <a href="apps/singbox.html" class="w-full py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-amber-400 font-semibold text-xs transition-all flex items-center justify-center gap-1.5">
              <span>اطلاعات بیشتر و نسخه‌های ۳۲ و ۶۴ بیت ←</span>
            </a>\2''',
    content,
    flags=re.DOTALL
)

# 5. Tone down CTA Trial Intermission
content = re.sub(
    r'<!-- CTA Trial Intermission -->.*?<!-- Step-by-Step Setup Tutorial -->',
    '''<!-- Testing Utility Intermission -->
  <section class="py-12 relative z-10">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="glass-card rounded-3xl p-8 sm:p-10 border border-slate-800 relative overflow-hidden bg-slate-900/60">
        <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="max-w-2xl text-center md:text-right">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 text-slate-300 text-xs font-semibold mb-3 border border-slate-700">
              ⚡ اعتبارسنجی اتصال
            </div>
            <h3 class="text-xl sm:text-2xl font-black text-white mb-2">
              پس از نصب کلاینت، به سرور برای تست اتصال نیاز دارید؟
            </h3>
            <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
              جهت ارزیابی پایداری و سرعت، می‌توانید کانفیگ تست VLESS Reality شبکه روزنه نت را به صورت خودکار از ربات تلگرامی دریافت کرده و در نرم‌افزار خود فعال نمایید.
            </p>
          </div>
          <div class="shrink-0">
            <a href="https://t.me/RoozanehNetBot?start=gh_download" target="_blank" rel="noopener noreferrer"
               class="px-6 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-brand-400 font-bold text-sm transition-all border border-slate-700 inline-flex items-center gap-2">
              <span>دریافت کانفیگ تست در تلگرام</span>
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.121l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.197 1.006.128.832.946z"/></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Step-by-Step Setup Tutorial -->''',
    content,
    flags=re.DOTALL
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html cleanly!")
