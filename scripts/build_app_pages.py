#!/usr/bin/env python3
"""
Dedicated App Page Generator for Roozaneh Net Client Portal
Generates standalone, Apple Light corporate detail pages in apps/<app>.html
using ../assets/css/apple-ui.css and ../assets/brand/* (zero external CDN).
"""
import html
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, "apps")
BASE_URL = "https://roozaneh.github.io/v2ray-clients-download"
OG_IMAGE_URL = "https://roozaneh.github.io/og.png"

PAGE_STYLES = """  <style>
    .app-hero-card {
      display: flex;
      flex-direction: column;
      gap: 24px;
      padding: 28px;
      margin-bottom: 40px;
    }
    @media (min-width: 768px) {
      .app-hero-card {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        padding: 36px;
      }
    }
    .app-hero-main {
      display: flex;
      align-items: flex-start;
      gap: 20px;
    }
    .app-icon-box {
      width: 76px;
      height: 76px;
      border-radius: 20px;
      border: 1px solid var(--border-hairline);
      background: var(--bg-secondary);
      padding: 4px;
      flex-shrink: 0;
      overflow: hidden;
    }
    .app-icon-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 14px;
    }
    .app-title-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }
    .app-title {
      margin: 0;
      font-size: clamp(24px, 3vw, 32px);
      font-weight: 900;
      color: var(--ink-primary);
      line-height: 1.25;
    }
    .app-chip {
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      font-size: 12px;
      font-weight: 600;
      background: var(--bg-secondary);
      border: 1px solid var(--border-hairline);
      color: var(--ink-secondary);
    }
    .app-chip--accent {
      background: var(--accent-tint);
      border-color: rgba(0, 113, 227, 0.18);
      color: var(--accent);
    }
    .app-meta-list {
      display: flex;
      flex-wrap: wrap;
      gap: 10px 16px;
      font-size: 12.5px;
      color: var(--ink-secondary);
      margin-top: 12px;
    }
    .app-meta-list strong {
      color: var(--ink-primary);
    }
    .app-hero-cta {
      display: flex;
      flex-direction: column;
      align-items: stretch;
      gap: 10px;
      flex-shrink: 0;
    }
    @media (min-width: 768px) {
      .app-hero-cta {
        min-width: 270px;
      }
    }
    .app-verify-note {
      font-size: 12px;
      color: var(--ink-secondary);
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .app-section {
      margin-bottom: 48px;
    }
    .app-section-head {
      margin-bottom: 18px;
    }
    .app-section-title {
      margin: 0 0 6px;
      font-size: clamp(19px, 2.4vw, 24px);
      font-weight: 800;
      color: var(--ink-primary);
    }
    .app-section-sub {
      margin: 0;
      font-size: 14px;
      color: var(--ink-secondary);
    }
    .build-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .build-row {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    @media (min-width: 640px) {
      .build-row {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }
    }
    .build-name-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }
    .build-name {
      font-size: 15px;
      font-weight: 700;
      color: var(--ink-primary);
    }
    .build-file {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--ink-muted);
      direction: ltr;
      text-align: right;
      margin-top: 4px;
    }
    .trust-banner {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      background: var(--status-ok-bg);
      border-color: rgba(22, 163, 74, 0.22);
    }
    .trust-banner-icon {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: #FFFFFF;
      color: var(--status-ok);
      border: 1px solid rgba(22, 163, 74, 0.2);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .step-card {
      display: flex;
      align-items: flex-start;
      gap: 14px;
    }
    .step-num {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      background: var(--accent-tint);
      color: var(--accent);
      font-weight: 800;
      font-size: 14px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .step-title {
      margin: 0 0 6px;
      font-size: 15.5px;
      font-weight: 700;
      color: var(--ink-primary);
    }
    .cta-banner {
      display: flex;
      flex-direction: column;
      gap: 16px;
      background: var(--accent-tint);
      border-color: rgba(0, 113, 227, 0.18);
    }
    @media (min-width: 640px) {
      .cta-banner {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }
    }
  </style>"""


def build_json_ld(app):
    page_url = f"{BASE_URL}/apps/{app['id']}.html"
    graph = [
        {
            "@type": "SoftwareApplication",
            "name": app["name"],
            "operatingSystem": app["schema_os"],
            "applicationCategory": "UtilitiesApplication",
            "softwareVersion": app["schema_version"],
            "downloadUrl": app["primary_url"],
            "url": page_url,
            "description": app["desc"],
            "offers": {
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "USD"
            }
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "خانه",
                    "item": f"{BASE_URL}/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "کلاینت‌ها",
                    "item": f"{BASE_URL}/#downloads"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": app["name"],
                    "item": page_url
                }
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": a
                    }
                }
                for q, a in app["faqs"]
            ]
        }
    ]
    payload = {
        "@context": "https://schema.org",
        "@graph": graph
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_app_page(app):
    bot_url = f"https://t.me/RoozanehNetBot?start={app['bot_payload']}"
    page_url = f"{BASE_URL}/apps/{app['id']}.html"
    escaped_title = html.escape(app["title"], quote=True)
    escaped_desc = html.escape(app["desc"], quote=True)
    json_ld = build_json_ld(app)

    builds_html = []
    for b_name, b_file, b_size, b_desc, b_url in app["builds"]:
        builds_html.append(f"""          <div class="apple-card build-row">
            <div>
              <div class="build-name-row">
                <span class="build-name">{b_name}</span>
                <span class="app-chip"><bdi>{b_size}</bdi></span>
              </div>
              <p class="apple-card-desc">{b_desc}</p>
              <div class="build-file"><bdi>{b_file}</bdi></div>
            </div>
            <div>
              <a href="{b_url}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                <span>دانلود مستقیم فایل</span>
              </a>
            </div>
          </div>""")

    steps_html = []
    persian_digits = ["۱", "۲", "۳", "۴", "۵", "۶"]
    for idx, (s_title, s_desc) in enumerate(app["tutorial_steps"]):
        step_num = persian_digits[idx] if idx < len(persian_digits) else str(idx + 1)
        steps_html.append(f"""          <div class="apple-card step-card">
            <span class="step-num">{step_num}</span>
            <div>
              <h3 class="step-title">{s_title}</h3>
              <p class="apple-card-desc">{s_desc}</p>
            </div>
          </div>""")

    faqs_html = []
    for idx, (q, a) in enumerate(app["faqs"]):
        open_attr = " open" if idx == 0 else ""
        faqs_html.append(f"""          <details class="faq-item"{open_attr}>
            <summary class="faq-trigger">
              <span>{q}</span>
              <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
            </summary>
            <div class="faq-panel">{a}</div>
          </details>""")

    download_target = ' target="_blank" rel="noopener noreferrer"' if "apple.com" in app["primary_url"] else ""

    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escaped_title}</title>
  <meta name="description" content="{escaped_desc}">
  <link rel="canonical" href="{page_url}">

  <link rel="icon" href="../assets/brand/favicon.ico" sizes="any">
  <link rel="icon" href="../assets/brand/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="../assets/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../assets/brand/favicon-16.png">
  <link rel="apple-touch-icon" href="../assets/brand/apple-touch-icon.png">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{escaped_title}">
  <meta property="og:description" content="{escaped_desc}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:image" content="{OG_IMAGE_URL}">
  <meta property="og:locale" content="fa_IR">
  <meta property="og:site_name" content="روزنه نت | Roozaneh Net">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escaped_title}">
  <meta name="twitter:description" content="{escaped_desc}">
  <meta name="twitter:image" content="{OG_IMAGE_URL}">

  <script type="application/ld+json">
{json_ld}
  </script>

  <link rel="stylesheet" href="../assets/css/apple-ui.css">
{PAGE_STYLES}

  <!-- GoatCounter Analytics -->
  <script data-goatcounter="https://roozaneh.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
  <!-- Microsoft Clarity Tracking -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "zip7qlr39v");
  </script>
</head>
<body>

  <!-- Sticky Frosted Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="brand-link">
        <img src="../assets/brand/logo-rail.svg" alt="لوگوی روزنه نت" class="brand-logo" width="32" height="32">
        <span class="brand-meta">
          <span class="brand-name">روزنه نت</span>
          <span class="brand-sub"><bdi>Roozaneh Net</bdi></span>
        </span>
      </a>
      <nav class="nav-links" aria-label="منوی اصلی">
        <a href="../index.html#downloads" class="nav-link is-active">همه کلاینت‌ها</a>
        <a href="../index.html#whitepaper" class="nav-link">دانشنامه فنی</a>
        <a href="../index.html#pricing" class="nav-link">تعرفه‌ها</a>
        <a href="../privacy.html" class="nav-link">حریم خصوصی</a>
      </nav>
      <div class="header-actions">
        <a href="{bot_url}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">دریافت تست رایگان</a>
        <button type="button" class="mobile-menu-btn" aria-label="باز کردن منو" aria-expanded="false" onclick="document.getElementById('mobile-nav').classList.toggle('is-open')">☰</button>
      </div>
    </div>
    <div id="mobile-nav" class="mobile-nav">
      <div class="mobile-nav-list">
        <a href="../index.html#downloads" class="mobile-nav-link">همه کلاینت‌ها</a>
        <a href="../index.html#whitepaper" class="mobile-nav-link">دانشنامه فنی</a>
        <a href="../index.html#pricing" class="mobile-nav-link">تعرفه‌ها</a>
        <a href="../privacy.html" class="mobile-nav-link">حریم خصوصی</a>
      </div>
    </div>
  </header>

  <main class="section section-sm">
    <div class="container">

      <!-- Breadcrumb -->
      <nav class="breadcrumb" aria-label="مسیر صفحه">
        <a href="../index.html">خانه</a>
        <span>/</span>
        <a href="../index.html#downloads">کلاینت‌ها</a>
        <span>/</span>
        <span><bdi>{app['name']}</bdi></span>
      </nav>

      <!-- Hero Card -->
      <section class="apple-card app-hero-card">
        <div class="app-hero-main">
          <div class="app-icon-box">
            <img src="../assets/icons/{app['icon']}" alt="لوگوی {app['name']}" width="68" height="68">
          </div>
          <div>
            <div class="app-title-row">
              <h1 class="app-title"><bdi>{app['name']}</bdi></h1>
              <span class="app-chip app-chip--accent">{app['version']}</span>
              <span class="app-chip">{app['os']}</span>
            </div>
            <p class="apple-card-desc" style="max-width: 620px;">{app['tagline']}</p>
            <div class="app-meta-list">
              <span>توسعه‌دهنده: <strong>{app['developer']}</strong></span>
              <span>لایسنس: <strong>{app['license']}</strong></span>
              <span>هسته: <strong>{app['core']}</strong></span>
            </div>
          </div>
        </div>
        <div class="app-hero-cta">
          <a href="{app['primary_url']}"{download_target} class="btn btn-primary btn-lg">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>{app['primary_text']}</span>
          </a>
          <div class="app-verify-note">
            <svg width="15" height="15" fill="none" stroke="#16A34A" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            <span>تایید اصالت باینری رسمی بدون دستکاری ({app['size']})</span>
          </div>
        </div>
      </section>

      <!-- Builds Section -->
      <section class="app-section">
        <div class="app-section-head">
          <h2 class="app-section-title">جدول تمامی نسخه‌ها و معماری‌های رسمی (<bdi>{app['name']}</bdi>)</h2>
          <p class="app-section-sub">دسترسی مستقیم به بسته‌های تفکیک‌شده پردازنده و پلتفرم از منبع رسمی توسعه‌دهنده</p>
        </div>
        <div class="build-list">
{chr(10).join(builds_html)}
        </div>
      </section>

      <!-- Security & Trust Callout -->
      <section class="app-section">
        <div class="apple-card trust-banner">
          <div class="trust-banner-icon" aria-hidden="true">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
          </div>
          <div>
            <h2 class="apple-card-title">تضمین اصالت کد منبع و سلامت فایل‌های رسمی</h2>
            <p class="apple-card-desc mb-4">
              {app['security_note']} تمامی بسته‌های دانلودی این صفحه مستقیم از انتشار رسمی گیت‌هاب یا اپ‌استور لینک‌دهی شده‌اند و هیچ تغییری در ساختار باینری آن‌ها اعمال نگردیده است.
            </p>
            <div class="flex flex-wrap gap-2">
              <span class="status-pill status-pill--ok">تایید اصالت <bdi>SHA-256</bdi></span>
              <span class="status-pill status-pill--ok">بدون بدافزار و تبلیغات</span>
              <span class="status-pill status-pill--ok">کلاینت متن‌باز و شفاف</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Setup Guide -->
      <section class="app-section">
        <div class="app-section-head">
          <h2 class="app-section-title">راهنمای گام‌به‌گام راه‌اندازی <bdi>{app['name']}</bdi></h2>
          <p class="app-section-sub">مراحل ساده اتصال در کمتر از یک دقیقه بدون نیاز به پیکربندی دستی پیچیده</p>
        </div>
        <div class="bento-grid bento-grid--2">
{chr(10).join(steps_html)}
        </div>
      </section>

      <!-- Dedicated FAQ -->
      <section class="app-section">
        <div class="app-section-head">
          <h2 class="app-section-title">سوالات متداول کلاینت <bdi>{app['name']}</bdi></h2>
          <p class="app-section-sub">پاسخ دقیق به پرسش‌های پرتکرار نصب، پینگ و اتصال پایدار</p>
        </div>
        <div class="faq-list" style="max-width: 100%;">
{chr(10).join(faqs_html)}
        </div>
      </section>

      <!-- Testing CTA Banner -->
      <section>
        <div class="apple-card cta-banner">
          <div>
            <h3 class="apple-card-title">نیاز به کانفیگ تست رایگان ۳ روزه دارید؟</h3>
            <p class="apple-card-desc">دریافت آنی ۲ تا ۳ گیگابایت اشتراک تست <bdi>VLESS Reality</bdi> روی ۵ لوکیشن فعال (آلمان، هلند، انگلیس، آمریکا، ترکیه) از ربات تلگرام روزنه نت.</p>
          </div>
          <a href="{bot_url}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            ورود به ربات و دریافت تست رایگان
          </a>
        </div>
      </section>

    </div>
  </main>

  <!-- Unified 4-Column Apple Light Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a href="../index.html" class="brand-link mb-4">
            <img src="../assets/brand/logo-rail.svg" alt="لوگوی روزنه نت" class="brand-logo" width="32" height="32">
            <span class="brand-meta">
              <span class="brand-name">روزنه نت</span>
              <span class="brand-sub"><bdi>Roozaneh Net</bdi></span>
            </span>
          </a>
          <p class="apple-card-desc mb-4">مرجع دانلود مستقیم باینری‌های رسمی گیت‌هاب و اپ‌استور برای کلاینت‌های <bdi>V2Ray</bdi>، <bdi>Xray</bdi> و <bdi>Sing-box</bdi>.</p>
          <span class="status-pill status-pill--ok">همگام‌سازی خودکار با گیت‌هاب فعال</span>
        </div>
        <div>
          <h3 class="footer-col-title">سرویس‌ها</h3>
          <ul class="footer-links">
            <li><a href="https://roozaneh.github.io/" target="_blank" rel="noopener noreferrer">هاب مرکزی روزنه نت</a></li>
            <li><a href="https://roozaneh.github.io/kharid-vpn-filter-shekan/" target="_blank" rel="noopener noreferrer">خرید <bdi>VPN</bdi> پرسرعت</a></li>
            <li><a href="https://roozaneh.github.io/v2ray-configs-iran/" target="_blank" rel="noopener noreferrer">کانفیگ‌های <bdi>V2Ray</bdi> ایران</a></li>
            <li><a href="https://roozaneh.github.io/iran-tunnel-v2ray-netmeli/" target="_blank" rel="noopener noreferrer">تانل اینترنت ملی</a></li>
            <li><a href="../index.html">پرتال دانلود کلاینت‌ها</a></li>
          </ul>
        </div>
        <div>
          <h3 class="footer-col-title">اپلیکیشن‌ها</h3>
          <ul class="footer-links">
            <li><a href="v2rayng.html">دانلود <bdi>v2rayNG</bdi> اندروید</a></li>
            <li><a href="happ.html">دانلود <bdi>Happ</bdi> اندروید</a></li>
            <li><a href="streisand.html">دانلود <bdi>Streisand</bdi> آیفون</a></li>
            <li><a href="v2box.html">دانلود <bdi>V2Box</bdi> آیفون و مک</a></li>
            <li><a href="v2rayn.html">دانلود <bdi>v2rayN</bdi> ویندوز</a></li>
            <li><a href="hiddify.html">دانلود <bdi>Hiddify</bdi> چندسکویی</a></li>
          </ul>
        </div>
        <div>
          <h3 class="footer-col-title">قوانین و پشتیبانی</h3>
          <ul class="footer-links">
            <li><a href="../privacy.html">شفافیت فنی و حریم خصوصی</a></li>
            <li><a href="../terms.html">قرارداد سطح خدمات (<bdi>SLA</bdi>)</a></li>
            <li><a href="{bot_url}" target="_blank" rel="noopener noreferrer">ربات تست رایگان (<bdi>@RoozanehNetBot</bdi>)</a></li>
            <li><a href="https://t.me/RoozanehHelp" target="_blank" rel="noopener noreferrer">پشتیبانی ۲۴ ساعته (<bdi>@RoozanehHelp</bdi>)</a></li>
            <li><a href="https://t.me/RoozanehNet" target="_blank" rel="noopener noreferrer">کانال اطلاع‌رسانی (<bdi>@RoozanehNet</bdi>)</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© ۱۴۰۵ روزنه نت (<bdi>Roozaneh Net</bdi>) — کلاینت‌های معرفی‌شده پروژه‌های مستقل متن‌باز هستند.</span>
        <span>تحلیل ترافیک با <bdi>GoatCounter</bdi> و <bdi>Microsoft Clarity</bdi> بدون ذخیره داده شخصی</span>
      </div>
    </div>
  </footer>

</body>
</html>
"""


def get_apps_data():
    return [
        {
            "id": "v2rayng",
            "name": "v2rayNG",
            "bot_payload": "app_v2rayng",
            "title": "دانلود مستقیم v2rayNG برای اندروید | نسخه رسمی یونیورسال گیت‌هاب | روزنه نت",
            "desc": "دانلود مستقیم v2rayNG آخرین نسخه پایدار از گیت‌هاب رسمی سازنده (2dust) بدون دستکاری. راهنمای راه‌اندازی، حل مشکل پینگ منفی یک، تنظیمات فرگمنت و جدول معماری‌های پردازنده.",
            "icon": "v2rayng.png",
            "version": "۲.۳.۱۵ (<bdi>2.3.15</bdi>)",
            "schema_version": "2.3.15",
            "os": "اندروید (<bdi>Android 5.0+</bdi>)",
            "schema_os": "Android",
            "developer": "<bdi>2dust</bdi> (گیت‌هاب رسمی)",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Xray-core / V2Ray-core</bdi>",
            "size": "۶۸.۵ مگابایت",
            "primary_url": "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_universal.apk",
            "primary_text": "دانلود مستقیم v2rayNG یونیورسال",
            "tagline": "استانداردترین و باثبات‌ترین کلاینت برای دانلود مستقیم v2rayng روی گوشی‌های سامسونگ، شیائومی، هواوی و تمامی مدل‌های اندروید با پشتیبانی کامل از VLESS Reality و فرگمنت.",
            "security_note": "به دلیل قوانین مربوط به VpnService در گوگل‌پلی، نسخه رسمی صرفاً در گیت‌هاب منتشر می‌شود. برنامه‌های مشابه در گوگل‌پلی غیررسمی هستند.",
            "builds": [
                ("نسخه جامع یونیورسال (پیشنهادی برای همه)", "v2rayNG_2.3.15_universal.apk", "۶۸.۵ MB", "سازگار با تمامی مدل‌ها بدون نیاز به شناخت نوع پردازنده", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_universal.apk"),
                ("معماری ۶۴ بیت جدید (arm64-v8a)", "v2rayNG_2.3.15_arm64-v8a.apk", "۳۰.۹ MB", "گوشی‌های مدرن تولید ۲۰۱۸ به بعد (سامسونگ، شیائومی)", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_arm64-v8a.apk"),
                ("معماری ۳۲ بیت قدیمی (armeabi-v7a)", "v2rayNG_2.3.15_armeabi-v7a.apk", "۳۱.۴ MB", "گوشی‌ها و تبلت‌های قدیمی‌تر اندرویدی", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_armeabi-v7a.apk"),
                ("شبیه‌سازها و کامپیوتر (x86_64)", "v2rayNG_2.3.15_x86_64.apk", "۳۱.۹ MB", "شبیه‌سازهای اندروید روی ویندوز نظیر LDPlayer و Nox", "https://github.com/2dust/v2rayNG/releases/download/2.3.15/v2rayNG_2.3.15_x86_64.apk"),
            ],
            "tutorial_steps": [
                ("نصب فایل یونیورسال", "فایل نصبی دانلود شده را لمس کرده و گزینه Install را بزنید. در صورت نمایش اخطار Play Protect، گزینه جزئیات بیشتر (More Details) و سپس Install Anyway را انتخاب فرمایید."),
                ("دریافت کانفیگ تست", "کد کانفیگ یا لینک اشتراک خود را کپی کنید (می‌توانید از ربات <a href=\"https://t.me/RoozanehNetBot?start=app_v2rayng\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"text-accent\">@RoozanehNetBot</a> کانفیگ تست ۳ روزه ۲ تا ۳ گیگابایت دریافت کنید)."),
                ("افزودن به برنامه", "برنامه v2rayNG را باز کنید، آیکون + در بالای صفحه را بزنید و گزینه Import config from Clipboard را لمس نمایید."),
                ("اتصال پایدار", "کانفیگ افزوده‌شده را لمس کرده و دکمه دایره‌ای V در پایین صفحه را فشار دهید تا اتصال برقرار شود.")
            ],
            "faqs": [
                ("چرا v2rayNG از گوگل‌پلی حذف شده و دانلود مستقیم v2rayng امن است؟", "توسعه‌دهنده رسمی اپلیکیشن به دلیل سیاست‌های گوگل‌پلی درباره برنامه‌های VpnService، از انتشار نسخه‌های جدید در این مارکت خودداری کرده است. تمامی فایل‌های این صفحه باینری خام و دست‌نخورده از مخزن رسمی 2dust/v2rayNG در گیت‌هاب هستند."),
                ("پینگ منفی یک (-1 ms) در v2rayNG به چه معناست؟", "این پینگ معمولاً به دلیل مسدود بودن بسته‌های تست ICMP توسط اپراتور است. در تنظیمات برنامه روش تست تاخیر را روی Real Delay بگذارید تا پینگ واقعی وب نمایش داده شود."),
                ("چگونه تنظیمات فرگمنت را در v2rayNG فعال کنیم؟", "در منوی تنظیمات v2rayNG، بخش Fragment را باز کرده و پارامتر Packets را روی tlshello، طول را برای همراه اول روی 10-20 و بازه تاخیر را روی 10-20ms قرار دهید.")
            ]
        },
        {
            "id": "happ",
            "name": "Happ",
            "bot_payload": "dl_clients",
            "title": "دانلود کلاینت مدرن Happ برای اندروید | سبک و خودکار | روزنه نت",
            "desc": "دانلود مستقیم نرم‌افزار جدید و سبک Happ برای اندروید با اتصال هوشمند تک‌کلیک، مصرف باتری ناچیز و بدون تبلیغات از گیت‌هاب رسمی.",
            "icon": "happ.png",
            "version": "۴.۱۱.۲ (<bdi>4.11.2</bdi>)",
            "schema_version": "4.11.2",
            "os": "اندروید (<bdi>Android 6.0+</bdi>)",
            "schema_os": "Android",
            "developer": "<bdi>Happ-proxy Team</bdi>",
            "license": "متن‌باز (<bdi>Open Source</bdi>)",
            "core": "<bdi>Xray-core / Sing-box</bdi>",
            "size": "۶۶.۱ مگابایت",
            "primary_url": "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ.apk",
            "primary_text": "دانلود مستقیم Happ.apk",
            "tagline": "کلاینت نسل جدید با طراحی مدرن، روان و بدون پیچیدگی. انتخابی ایده‌آل برای کاربرانی که به دنبال سادگی و بازیابی خودکار اتصال بین وای‌فای و اینترنت همراه هستند.",
            "security_note": "نرم‌افزار Happ بدون تبلیغات درون‌برنامه‌ای است و فایل نصبی آن مستقیم از مخزن گیت‌هاب Happ-proxy دریافت می‌شود.",
            "builds": [
                ("نسخه رسمی پایدار (پیشنهادی)", "Happ.apk", "۶۶.۱ MB", "فایل نصبی استاندارد برای تمام دستگاه‌ها", "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ.apk"),
                ("نسخه آزمایشی بتا", "Happ_beta.apk", "۶۶.۱ MB", "حاوی جدیدترین بهینه‌سازی‌های آزمایشی هسته", "https://github.com/Happ-proxy/happ-android/releases/download/4.11.2/Happ_beta.apk")
            ],
            "tutorial_steps": [
                ("دانلود و نصب", "فایل Happ.apk را دانلود کرده و روی گوشی خود نصب نمایید."),
                ("کپی لینک سابسکریپشن", "لینک سابسکریپشن هوشمند روزنه نت را از ربات <a href=\"https://t.me/RoozanehNetBot?start=dl_clients\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"text-accent\">@RoozanehNetBot</a> کپی کنید."),
                ("افزودن و بروزرسانی", "برنامه Happ را باز کنید، لینک را در بخش سابسکریپشن وارد کنید تا لیست سرورهای ۵ لوکیشن بارگذاری شود."),
                ("اتصال فوری", "دکمه اتصال بزرگ وسط صفحه را لمس کنید تا اتصال برقرار شود.")
            ],
            "faqs": [
                ("مزیت Happ نسبت به v2rayNG چیست؟", "رابط کاربری ساده‌تر، بازیابی سریع‌تر اتصال بعد از جابجایی بین وای‌فای و اینترنت سیم‌کارت و پیکربندی خودکار سابسکریپشن."),
                ("آیا روی گوشی‌های شیائومی و سامسونگ به خوبی کار می‌کند؟", "بله، Happ با رابط کاربری One UI سامسونگ و HyperOS شیائومی سازگاری کامل دارد.")
            ]
        },
        {
            "id": "streisand",
            "name": "Streisand",
            "bot_payload": "app_streisand",
            "title": "دانلود Streisand برای آیفون و آیپد (iOS) | فیلتر شکن برای ایفون | روزنه نت",
            "desc": "دانلود کلاینت رایگان Streisand از اپ‌استور رسمی اپل؛ بهترین فیلتر شکن برای ایفون و آیپد با هسته Sing-box، پشتیبانی از VLESS Reality و بدون تبلیغات.",
            "icon": "streisand.png",
            "version": "رسمی <bdi>App Store</bdi>",
            "schema_version": "App Store",
            "os": "<bdi>iOS 14.0+</bdi> (آیفون و آیپد)",
            "schema_os": "iOS",
            "developer": "<bdi>Streisand App Team</bdi>",
            "license": "رایگان رسمی (<bdi>Freeware</bdi>)",
            "core": "<bdi>Sing-box Core</bdi>",
            "size": "نسخه رسمی اپ‌استور",
            "primary_url": "https://apps.apple.com/app/streisand/id6450534064",
            "primary_text": "دریافت رایگان از App Store اپل",
            "tagline": "کلاینت شماره ۱ پیشنهادی به عنوان فیلتر شکن برای ایفون و آیپد. سازگاری کامل با هسته فوق‌پایدار Sing-box، مصرف باتری ناچیز، بدون تبلیغات و اتصال با یک لمس.",
            "security_note": "تایید شده توسط بررسی امنیتی شرکت اپل و منتشرشده مستقیم در App Store رسمی.",
            "builds": [
                ("نسخه رسمی اپ‌استور (iOS / iPadOS)", "Streisand on App Store", "رایگان", "قابل نصب روی آیفون، آیپد و مک‌های مجهز به اپل سیلیکون (M1/M2/M3)", "https://apps.apple.com/app/streisand/id6450534064")
            ],
            "tutorial_steps": [
                ("دانلود از App Store", "بر روی دکمه دریافت از اپ‌استور کلیک کنید و برنامه را با Apple ID خود به رایگان دانلود نمایید."),
                ("دریافت کانفیگ یا ساب", "کانفیگ اختصاصی یا لینک سابسکریپشن روزنه نت را از ربات <a href=\"https://t.me/RoozanehNetBot?start=app_streisand\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"text-accent\">@RoozanehNetBot</a> کپی فرمایید."),
                ("ایمپورت در برنامه", "وارد برنامه Streisand شوید، علامت + در بالای صفحه را لمس کرده و Import from Clipboard را بزنید."),
                ("روشن کردن اتصال", "سوئیچ اتصال در بالای صفحه را روشن کنید و در صورت درخواست سیستم، اجازه ساخت پروفایل VPN را تایید (Allow) فرمایید.")
            ],
            "faqs": [
                ("آیا Streisand بهترین فیلتر شکن برای ایفون بدون تبلیغات است؟", "بله، این نرم‌افزار کاملاً رایگان، بدون تبلیغات مزاحم و مجهز به هسته مدرن Sing-box است و از VLESS Reality و آپدیت خودکار سابسکریپشن پشتیبانی کامل دارد."),
                ("آیا از پروتکل‌های Reality و فرگمنت پشتیبانی می‌کند؟", "بله، Streisand از VLESS Reality، تغییر خودکار لوکیشن و تنظیمات ضد DPI روی اینترنت همراه اول و ایرانسل پشتیبانی می‌کند.")
            ]
        },
        {
            "id": "v2rayn",
            "name": "v2rayN",
            "bot_payload": "dl_clients",
            "title": "دانلود نرم‌افزار v2rayN برای ویندوز و مک | نسخه کامل با هسته Xray | روزنه نت",
            "desc": "دانلود مستقیم نسخه کامل v2rayN ویندوز و مک مجهز به هسته Xray و Sing-box، قابلیت System Proxy و حالت TUN Mode برای بازی‌ها و نرم‌افزارهای دسکتاپ.",
            "icon": "v2rayn.png",
            "version": "۷.۲۵.۶ (<bdi>7.25.6</bdi>)",
            "schema_version": "7.25.6",
            "os": "ویندوز ۱۰ و ۱۱ و <bdi>macOS</bdi>",
            "schema_os": "Windows",
            "developer": "<bdi>2dust</bdi> (گیت‌هاب رسمی)",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Xray-core / Sing-box Core</bdi>",
            "size": "۱۶۰.۹ مگابایت (With Core)",
            "primary_url": "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64.zip",
            "primary_text": "دانلود مستقیم نسخه کامل ویندوز ۶۴ بیت",
            "tagline": "قدرتمندترین و پرامکانات‌ترین کلاینت دسکتاپ برای کامپیوتر و لپ‌تاپ. مناسب وب‌گردی، دانلود پرسرعت، تریدینگ و بازی‌های آنلاین با پشتیبانی کامل از TUN Mode.",
            "security_note": "بسته رسمی ارائه‌شده همراه با تمامی هسته‌های رسمی است و نیازی به دانلود جداگانه Xray Core ندارد.",
            "builds": [
                ("نسخه کامل ویندوز ۶۴ بیت با هسته (پیشنهادی)", "v2rayN-windows-64.zip", "۱۶۰.۹ MB", "کامل‌ترین بسته بدون نیاز به نصب، آماده اجرا در ویندوز ۱۰ و ۱۱", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64.zip"),
                ("نسخه ویندوز ۶۴ بیت Desktop Runtime", "v2rayN-windows-64-desktop.zip", "۱۳۸.۰ MB", "مخصوص سیستم‌هایی که دات‌نت ران‌تایم دارند", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-64-desktop.zip"),
                ("نسخه سبک ویندوز ۳۲ بیت", "v2rayN-windows-86.zip", "۱۳۴.۵ MB", "برای سیستم‌های قدیمی‌تر ۳۲ بیتی", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-windows-86.zip"),
                ("نسخه مک‌بوک (<bdi>macOS Apple Silicon</bdi>)", "v2rayN-macos-arm64.dmg", "۱۲۹.۲ MB", "نسخه مخصوص مک‌بوک‌های Apple Silicon (M1/M2/M3)", "https://github.com/2dust/v2rayN/releases/download/7.25.6/v2rayN-macos-arm64.dmg")
            ],
            "tutorial_steps": [
                ("اکسترکت کردن فایل Zip", "فایل فشرده دانلودشده را با کلیک راست و گزینه Extract All در یک پوشه (مثلاً در درایو C یا دسکتاپ) باز کنید."),
                ("اجرای برنامه", "روی فایل v2rayN.exe دابل‌کلیک کنید تا برنامه در نوار کنار ساعت ویندوز باز شود."),
                ("افزودن کانفیگ", "کانفیگ کپی‌شده را با فشردن کلیدهای میانبر Ctrl + V در محیط برنامه پیست کنید."),
                ("فعال‌سازی پراکسی یا TUN", "در نوار پایین برنامه، گزینه System Proxy را روی Set System Proxy بگذارید. برای بازی‌ها می‌توانید گزینه Enable Tun را تیک بزنید.")
            ],
            "faqs": [
                ("آیا v2rayN نیاز به نصب دارد؟", "خیر، این نرم‌افزار پرتابل است و فقط با اکسترکت کردن فایل فشرده قابل اجراست."),
                ("حالت Tun Mode در ویندوز چه کاربردی دارد؟", "حالت TUN تمام ترافیک سیستم‌عامل (از جمله بازی‌های آنلاین، کلاینت‌های صرافی و تلگرام دسکتاپ) را بدون نیاز به تنظیم جداگانه وارد تونل امن می‌کند.")
            ]
        },
        {
            "id": "nekobox",
            "name": "NekoBox",
            "bot_payload": "dl_clients",
            "title": "دانلود کلاینت گیمینگ NekoBox برای اندروید | کمترین تاخیر و پینگ | روزنه نت",
            "desc": "دانلود مستقیم کلاینت تخصصی NekoBox بر پایه هسته Sing-box برای گیمرهای اندروید، کاهش تاخیر UDP و پینگ پایین در بازی‌های آنلاین.",
            "icon": "nekobox.png",
            "version": "۱.۴.۲ (<bdi>1.4.2</bdi>)",
            "schema_version": "1.4.2",
            "os": "اندروید (<bdi>Android 6.0+</bdi>)",
            "schema_os": "Android",
            "developer": "<bdi>MatsuriDayo</bdi>",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Sing-box Core</bdi>",
            "size": "۱۴.۵ مگابایت",
            "primary_url": "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-arm64-v8a.apk",
            "primary_text": "دانلود مستقیم نسخه ۶۴ بیت (arm64-v8a)",
            "tagline": "کلاینت تخصصی و سبک برای گیمرها و کاربران حرفه‌ای اندروید. بهینه‌سازی شده برای حداقل مصرف رم و کاهش تاخیر بسته‌های UDP.",
            "security_note": "متن‌باز و پاک، استخراج مستقیم از گیت‌هاب رسمی MatsuriDayo.",
            "builds": [
                ("پردازنده‌های جدید ۶۴ بیتی (پیشنهادی)", "NekoBox-1.4.2-arm64-v8a.apk", "۱۴.۵ MB", "سازگار با گوشی‌های سامسونگ و شیائومی مدرن", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-arm64-v8a.apk"),
                ("پردازنده‌های قدیمی ۳۲ بیتی", "NekoBox-1.4.2-armeabi-v7a.apk", "۱۴.۷ MB", "گوشی‌های قدیمی با اندروید ۵ و ۶", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-armeabi-v7a.apk"),
                ("شبیه‌سازهای کامپیوتر (x86_64)", "NekoBox-1.4.2-x86_64.apk", "۱۵.۲ MB", "شبیه‌سازهای اندروید پی‌سی", "https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/download/1.4.2/NekoBox-1.4.2-x86_64.apk")
            ],
            "tutorial_steps": [
                ("نصب نسخه arm64", "فایل نصبی مناسب گوشی‌های امروزی (arm64-v8a) را دانلود و نصب کنید."),
                ("افزودن کانفیگ", "کانفیگ روزنه نت را کپی کرده و از منوی بالای برنامه علامت افزودن را بزنید."),
                ("اتصال به سرور کم‌پینگ", "تست پینگ URL Test را اجرا کرده و سرور با کمترین تاخیر میلی‌ثانیه‌ای را انتخاب نمایید.")
            ],
            "faqs": [
                ("چرا NekoBox نسخه یونیورسال ندارد؟", "توسعه‌دهنده NekoBox برای کاهش حجم فایل نصبی، بسته‌ها را به تفکیک معماری منتشر کرده است که نسخه arm64 برای اغلب گوشی‌های امروزی مناسب است.")
            ]
        },
        {
            "id": "singbox",
            "name": "Sing-box",
            "bot_payload": "dl_clients",
            "title": "دانلود کلاینت رسمی Sing-box برای اندروید | معماری سریع Go | روزنه نت",
            "desc": "دانلود مستقیم نسخه رسمی کلاینت SagerNet Sing-box برای اندروید با هسته نسل جدید، کمترین مصرف رم و بالاترین پایداری در شبکه.",
            "icon": "singbox.png",
            "version": "۱.۱۴.۴ (<bdi>1.14.4</bdi>)",
            "schema_version": "1.14.4",
            "os": "اندروید (<bdi>Android 7.0+</bdi>)",
            "schema_os": "Android",
            "developer": "<bdi>SagerNet Team</bdi>",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Sing-box Native Go</bdi>",
            "size": "۱۲۱.۴ مگابایت (Universal)",
            "primary_url": "https://github.com/SagerNet/sing-box/releases/download/v1.14.4/SFA-1.14.4-universal.apk",
            "primary_text": "دانلود مستقیم نسخه یونیورسال (APK)",
            "tagline": "کلاینت مرجع توسعه‌یافته توسط تیم اصلی SagerNet با سبک‌ترین معماری Go، مصرف بهینه باتری و پشتیبانی بومی از پروتکل‌های جدید.",
            "security_note": "سورس کاملاً باز با قابلیت ممیزی کد در مخزن رسمی SagerNet/sing-box.",
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
                ("چرا Sing-box را نسل آینده کلاینت‌ها می‌دانند؟", "به دلیل بازنویسی ماژولار در زبان Go، حذف وابستگی‌های سنگین و پشتیبانی بومی از Reality، ShadowTLS و TUIC v5 با کمترین مصرف باتری.")
            ]
        },
        {
            "id": "v2box",
            "name": "V2Box",
            "bot_payload": "app_streisand",
            "title": "دانلود V2Box برای آیفون، آیپد و مک | فیلتر شکن برای ایفون با رابط ساده | روزنه نت",
            "desc": "دانلود مستقیم V2Box از اپ‌استور اپل؛ فیلتر شکن برای ایفون، آیپد و مک‌بوک با اسکنر QR لحظه‌ای، پشتیبانی از VLESS Reality و آپدیت خودکار سابسکریپشن.",
            "icon": "v2box.png",
            "version": "رسمی <bdi>App Store</bdi>",
            "schema_version": "App Store",
            "os": "<bdi>iOS 14.0+</bdi> و <bdi>macOS</bdi>",
            "schema_os": "iOS, macOS",
            "developer": "<bdi>V2Box Dev Team</bdi>",
            "license": "رایگان (<bdi>Freeware</bdi>)",
            "core": "<bdi>V2Box Engine</bdi>",
            "size": "نسخه رسمی اپ‌استور",
            "primary_url": "https://apps.apple.com/app/v2box-v2ray-client/id6446814690",
            "primary_text": "دریافت رایگان از App Store اپل",
            "tagline": "فیلتر شکن برای ایفون و مک‌بوک با رابط کاربری بسیار آسان و روان، امکان آپدیت خودکار لیست کانفیگ‌ها و اسکن سریع کدهای QR.",
            "security_note": "موجود در اپ‌استور رسمی اپل و تاییدشده توسط فرآیند بررسی App Store.",
            "builds": [
                ("نسخه رسمی اپ‌استور برای iOS و macOS", "V2Box on App Store", "رایگان", "آیفون، آیپد و مک‌بوک‌های مجهز به تراشه‌های اپل سیلیکون", "https://apps.apple.com/app/v2box-v2ray-client/id6446814690")
            ],
            "tutorial_steps": [
                ("نصب از اپ‌استور", "برنامه را مستقیم از اپ‌استور اپل دانلود فرمایید."),
                ("اسکن یا پیست کانفیگ", "کانفیگ کپی‌شده از ربات <a href=\"https://t.me/RoozanehNetBot?start=app_streisand\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"text-accent\">@RoozanehNetBot</a> را با لمس Add Config پیست کنید یا کد QR را اسکن نمایید."),
                ("اتصال فوری", "اسلایدر اتصال را بکشید تا تونل امن برقرار گردد.")
            ],
            "faqs": [
                ("آیا V2Box روی مک‌بوک هم کار می‌کند؟", "بله، نسخه مک‌بوک این نرم‌افزار در اپ‌استور مک در دسترس است و با کانفیگ‌های VLESS Reality روزنه نت عملکرد پایداری دارد."),
                ("تفاوت V2Box با Streisand برای آیفون چیست؟", "هر دو رایگان هستند؛ Streisand بر پایه هسته متن‌باز Sing-box سبک‌تر است و V2Box برای کاربرانی که اسکنر QR سریع و محیط ساده‌تر می‌خواهند انتخاب عالی است.")
            ]
        },
        {
            "id": "hiddify",
            "name": "Hiddify",
            "bot_payload": "dl_clients",
            "title": "دانلود نرم‌افزار Hiddify برای اندروید، ویندوز و مک | رابط فارسی | روزنه نت",
            "desc": "دانلود مستقیم کلاینت کراس‌پلتفرم Hiddify با رابط کاربری فارسی، مسیریابی هوشمند سایت‌های ایرانی و پشتیبانی از تمامی سیستم‌عامل‌ها.",
            "icon": "hiddify.png",
            "version": "۵.۹.۱۵ (<bdi>v5.9.15</bdi>)",
            "schema_version": "5.9.15",
            "os": "اندروید، ویندوز، مک و لینوکس",
            "schema_os": "Android, Windows, macOS, Linux",
            "developer": "<bdi>Hiddify Community</bdi>",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Sing-box Core</bdi>",
            "size": "اندروید: ۱۷۹.۳ MB | ویندوز: ۴۸.۸ MB",
            "primary_url": "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Android-universal.apk",
            "primary_text": "دانلود مستقیم APK اندروید یونیورسال",
            "tagline": "نرم‌افزار جامع و چندسکویی با زبان فارسی کامل، مسیریابی هوشمند برای وب‌سایت‌های داخلی و اتصال تک‌لمسی بدون نیاز به تنظیم دستی.",
            "security_note": "متن‌باز و شفاف با پشتیبانی فعال از تمامی پروتکل‌های مدرن ضد فیلترینگ.",
            "builds": [
                ("اندروید نسخه جامع یونیورسال (پیشنهادی)", "Hiddify-Android-universal.apk", "۱۷۹.۳ MB", "سازگار با تمامی گوشی‌ها و تبلت‌های اندروید", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Android-universal.apk"),
                ("ویندوز نسخه Setup نصبی ۶۴ بیت", "Hiddify-Windows-Setup-x64.exe", "۴۸.۸ MB", "نصب آسان در ویندوز ۱۰ و ۱۱", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Windows-Setup-x64.exe"),
                ("ویندوز نسخه پرتابل (بدون نیاز به نصب)", "Hiddify-Windows-Portable-x64.zip", "۵۷.۱ MB", "اجرای سریع و پرتابل در ویندوز", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Windows-Portable-x64.zip"),
                ("مک‌او‌اس (<bdi>macOS Installer</bdi>)", "Hiddify-MacOS-Installer.pkg", "۴۸.۰ MB", "فایل نصبی پکیج مک‌بوک و آی‌مک", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-MacOS-Installer.pkg"),
                ("لینوکس (<bdi>Linux AppImage</bdi>)", "Hiddify-Linux-x64.AppImage", "۶۹.۸ MB", "اجرای مستقیم در اوبونتو و لینوکس ۶۴ بیت", "https://github.com/hiddify/hiddify-app/releases/download/v5.9.15/Hiddify-Linux-x64.AppImage")
            ],
            "tutorial_steps": [
                ("نصب برنامه", "نسخه متناسب با سیستم‌عامل خود (اندروید، ویندوز، مک‌بوک یا لینوکس) را دانلود و نصب کنید."),
                ("افزودن پروفایل", "لینک سابسکریپشن اختصاصی خود را در بخش Profile اضافه فرمایید."),
                ("اتصال هوشمند", "روی دکمه اتصال بزنید تا بهترین سرور به شکل خودکار انتخاب شود.")
            ],
            "faqs": [
                ("مزیت منوی فارسی Hiddify چیست؟", "تمام گزینه‌های فنی و تنظیمات روتینگ به زبان فارسی روان ترجمه شده‌اند و هر کاربری بدون دانش تخصصی می‌تواند از آن استفاده کند.")
            ]
        },
        {
            "id": "nekoray",
            "name": "NekoRay",
            "bot_payload": "dl_clients",
            "title": "دانلود نرم‌افزار NekoRay برای ویندوز و لینوکس | کلاینت TUN Mode | روزنه نت",
            "desc": "دانلود مستقیم نسخه پرتابل NekoRay ویندوز ۶۴ بیت و لینوکس با هسته Sing-box و Xray، مناسب بازی‌های آنلاین و عبور کامل ترافیک سیستم.",
            "icon": "nekoray.png",
            "version": "۴.۰.۱ (<bdi>4.0.1</bdi>)",
            "schema_version": "4.0.1",
            "os": "ویندوز ۱۰ و ۱۱ و لینوکس (<bdi>64-bit</bdi>)",
            "schema_os": "Windows, Linux",
            "developer": "<bdi>MatsuriDayo</bdi>",
            "license": "<bdi>GPL v3.0</bdi> (متن‌باز)",
            "core": "<bdi>Sing-box / Xray</bdi>",
            "size": "۳۹.۸ مگابایت (Portable)",
            "primary_url": "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-windows64.zip",
            "primary_text": "دانلود مستقیم Zip پرتابل ویندوز",
            "tagline": "کلاینت مهندسی و سبک کامپیوتر بدون نیاز به نصب، مجهز به درایور قدرتمند TUN Mode برای عبور بدون وقفه ترافیک بازی‌ها و نرم‌افزارهای دسکتاپ.",
            "security_note": "متن‌باز و قابل بازرسی با حجم کم و مصرف ناچیز پردازنده.",
            "builds": [
                ("ویندوز ۶۴ بیت پرتابل (پیشنهادی)", "nekoray-4.0.1-2024-12-12-windows64.zip", "۳۹.۸ MB", "ویندوز ۱۰ و ۱۱ بدون نیاز به نصب", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-windows64.zip"),
                ("لینوکس دبیان و اوبونتو (.deb)", "nekoray-4.0.1-2024-12-12-debian-x64.deb", "۳۳.۰ MB", "نصب آسان در Ubuntu/Debian", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-debian-x64.deb"),
                ("لینوکس پرتابل (.zip)", "nekoray-4.0.1-2024-12-12-linux64.zip", "۳۶.۱ MB", "اجرا در تمامی توزیع‌های لینوکس ۶۴ بیت", "https://github.com/MatsuriDayo/nekoray/releases/download/4.0.1/nekoray-4.0.1-2024-12-12-linux64.zip")
            ],
            "tutorial_steps": [
                ("اکسترکت کردن فایل", "فایل فشرده را اکسترکت کنید و nekoray.exe را اجرا نمایید."),
                ("انتخاب هسته Sing-box", "در اولین اجرا، هسته پیشنهادی Sing-box را تایید فرمایید."),
                ("افزودن کانفیگ و فعال‌سازی TUN", "کانفیگ کپی‌شده را پیست کرده و تیک گزینه Tun Mode را برای عبور کل ترافیک سیستم بزنید.")
            ],
            "faqs": [
                ("تفاوت NekoRay با v2rayN چیست؟", "نکورای حجم بسیار کمتری دارد (حدود ۴۰ مگابایت در مقابل ۱۶۰ مگابایت)، سبک‌تر است و تمرکز اصلی آن بر پیاده‌سازی سریع حالت TUN و لینوکس است.")
            ]
        }
    ]


def main():
    os.makedirs(APPS_DIR, exist_ok=True)
    for app in get_apps_data():
        out_file = os.path.join(APPS_DIR, f"{app['id']}.html")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(render_app_page(app))
        print(f"Generated {out_file}")
    print("All 9 Apple Light dedicated app pages generated successfully.")


if __name__ == "__main__":
    main()
