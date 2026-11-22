#!/usr/bin/env python3
"""
Dedicated App Page Generator for Roozaneh Net Client Portal
Generates standalone, authoritative, corporate detail pages in apps/<app>.html
"""
import os

APPS_DIR = "/home/hokar/.gemini/antigravity/scratch/v2ray-clients-download/apps"
os.makedirs(APPS_DIR, exist_ok=True)

SHARED_HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="fa" dir="rtl" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://roozaneh.github.io/v2ray-clients-download/apps/{filename}">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://roozaneh.github.io/v2ray-clients-download/apps/{filename}">
  <meta property="og:locale" content="fa_IR">
  <meta property="og:site_name" content="روزنه نت | Roozaneh Net">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#ecfdf5',
              100: '#d1fae5',
              400: '#34d399',
              500: '#10b981',
              600: '#059669',
              700: '#047857',
              800: '#065f46',
              900: '#064e3b',
            }},
            slate: {{
              850: '#131b2e',
              900: '#0b1120',
              950: '#060913',
            }}
          }},
          fontFamily: {{
            sans: ['Vazirmatn', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      font-family: 'Vazirmatn', sans-serif;
      background-color: #080d1a;
      color: #f1f5f9;
      line-height: 1.7;
    }}
    .glass-card {{
      background: rgba(13, 20, 36, 0.75);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(51, 65, 85, 0.45);
    }}
    .ambient-radial {{
      background: radial-gradient(circle at 50% 0%, rgba(5, 150, 105, 0.12) 0%, rgba(8, 13, 26, 0) 70%);
    }}
  </style>
  <script data-goatcounter="https://roozaneh.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</head>
<body class="min-h-screen text-slate-100 selection:bg-brand-500 selection:text-white">
  <div class="fixed inset-0 pointer-events-none z-0 ambient-radial"></div>

  <!-- Header -->
  <header class="sticky top-0 z-50 backdrop-blur-xl bg-slate-950/85 border-b border-slate-800/80">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-18 flex items-center justify-between">
      <a href="../index.html" class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 to-teal-400 flex items-center justify-center shadow-md shadow-brand-500/20">
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
        </div>
        <div>
          <span class="text-lg font-black text-white">روزنه نت</span>
          <span class="text-[11px] text-slate-400 block -mt-1">پرتال جامع کلاینت‌های امن</span>
        </div>
      </a>
      <div class="flex items-center gap-4 text-xs font-medium">
        <a href="../index.html#downloads" class="text-slate-300 hover:text-brand-400 transition-colors">لیست همه کلاینت‌ها</a>
        <a href="../index.html#whitepaper" class="hidden sm:inline-block text-slate-300 hover:text-brand-400 transition-colors">دانشنامه فنی</a>
        <a href="https://t.me/RoozanehNetBot?start=gh_download" target="_blank" rel="noopener" class="px-3.5 py-1.5 rounded-full bg-slate-800 hover:bg-slate-700 text-brand-400 border border-slate-700 transition-colors">دریافت کانفیگ تست</a>
      </div>
    </div>
  </header>

  <!-- Breadcrumb -->
  <div class="max-w-6xl mx-auto px-4 sm:px-6 pt-6 pb-2 relative z-10 text-xs text-slate-400 flex items-center gap-2">
    <a href="../index.html" class="hover:text-white transition-colors">خانه</a>
    <span>/</span>
    <a href="../index.html#downloads" class="hover:text-white transition-colors">کلاینت‌ها</a>
    <span>/</span>
    <span class="text-slate-200 font-semibold">{app_name}</span>
  </div>

  <main class="max-w-6xl mx-auto px-4 sm:px-6 py-8 relative z-10">
    <!-- Hero Box -->
    <div class="glass-card rounded-3xl p-6 sm:p-10 mb-10 border border-slate-700/60 relative overflow-hidden">
      <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
        <div class="flex items-start gap-5">
          <div class="w-20 h-20 rounded-2xl overflow-hidden shadow-xl border border-slate-700 bg-slate-800 shrink-0 p-1 flex items-center justify-center">
            <img src="../assets/icons/{icon}" alt="لوگوی {app_name}" class="w-full h-full object-cover rounded-xl">
          </div>
          <div>
            <div class="flex flex-wrap items-center gap-2 mb-2">
              <h1 class="text-2xl sm:text-3xl font-black text-white">{app_name}</h1>
              <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/10 text-brand-400 border border-brand-500/25">{version_badge}</span>
              <span class="px-2.5 py-0.5 rounded-full text-xs bg-slate-800 text-slate-300 border border-slate-700">{os_badge}</span>
            </div>
            <p class="text-slate-300 text-xs sm:text-sm max-w-2xl leading-relaxed mb-4">
              {tagline}
            </p>
            <div class="flex flex-wrap gap-2 text-[11px] text-slate-400">
              <span>توسعه‌دهنده رسمی: <strong class="text-slate-200">{developer}</strong></span>
              <span>•</span>
              <span>لایسنس: <strong class="text-slate-200">{license}</strong></span>
              <span>•</span>
              <span>هسته: <strong class="text-slate-200">{core}</strong></span>
            </div>
          </div>
        </div>
        <div class="w-full md:w-auto shrink-0 flex flex-col gap-2.5">
          <a href="{primary_download_url}" {download_target}
             class="w-full md:w-auto px-8 py-4 rounded-2xl bg-brand-600 hover:bg-brand-500 text-white font-bold text-sm text-center shadow-lg shadow-brand-600/25 transition-all flex items-center justify-center gap-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>{primary_button_text}</span>
          </a>
          <div class="text-center text-[11px] text-slate-400 flex items-center justify-center gap-1.5">
            <span class="text-emerald-400 font-bold">✓</span>
            <span>تایید اصالت باینری رسمی بدون دستکاری ({file_size_text})</span>
          </div>
        </div>
      </div>
    </div>

    {content_body}

  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 bg-slate-950 py-10 relative z-10 text-slate-400 text-xs mt-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <a href="../index.html" class="text-white font-bold hover:text-brand-400 transition-colors">پرتال دانلود روزنه نت</a>
        <span>| کلاینت‌های رسمی و امن V2Ray و Xray</span>
      </div>
      <div>
        <a href="../index.html#downloads" class="text-slate-400 hover:text-white transition-colors">مشاهده فهرست کامل همه کلاینت‌ها ←</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""
