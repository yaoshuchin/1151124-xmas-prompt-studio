# -*- coding: utf-8 -*-
import json

with open('chapters_data.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Build chapter cards
chapter_cards = []
sidebar_nav_items = []

for idx, ch in enumerate(chapters, 1):
    ch_id = f"ch-{idx:02d}"
    title = ch['title']
    
    sidebar_nav_items.append(f'''
    <a href="#{ch_id}" onclick="jumpToChapter('{ch_id}')" class="flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white hover:bg-slate-800/80 transition-colors">
      <span class="w-5 h-5 flex items-center justify-center rounded bg-slate-800 text-[10px] font-mono font-bold text-amber-400">{idx:02d}</span>
      <span class="truncate">{title}</span>
    </a>
    ''')
    
    body_parts = []
    plain_texts = [f"### {title}"]
    
    for item in ch['items']:
        itype = item['type']
        ihtml = item['html']
        itxt = item['text']
        plain_texts.append(itxt)
        
        if itype == 'sub_sub_header':
            body_parts.append(f'<h4 class="text-base font-bold text-amber-300 mt-4 mb-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-amber-400 inline-block"></span>{ihtml}</h4>')
        elif itype == 'bulleted_list':
            body_parts.append(f'<li class="text-slate-300 text-sm leading-relaxed pl-1 marker:text-emerald-400 list-disc ml-5 mb-1">{ihtml}</li>')
        elif itype == 'numbered_list':
            body_parts.append(f'<li class="text-slate-300 text-sm leading-relaxed pl-1 list-decimal ml-5 marker:text-amber-400 mb-1">{ihtml}</li>')
        elif itype == 'divider':
            body_parts.append('<hr class="border-slate-800/80 my-3" />')
        else:
            if itxt.strip():
                if any(itxt.startswith(p) for p in ['M01｜', 'F0', '01｜', '02｜', '03｜', '04｜', '05｜', '06｜', '07｜', '08｜', '09｜', '10｜', '11｜', '12｜', '專案：', '系統：', '引擎：', '人物：']):
                    body_parts.append(f'<div class="p-2.5 my-1.5 bg-slate-950/70 rounded-lg border border-slate-800 font-mono text-xs text-cyan-200">{ihtml}</div>')
                else:
                    body_parts.append(f'<p class="text-slate-300 text-sm leading-relaxed mb-2.5">{ihtml}</p>')
                    
    card_body_html = '\n'.join(body_parts)
    escaped_plain_text = json.dumps('\n'.join(plain_texts), ensure_ascii=False)
    
    card_html = f'''
    <div class="chapter-card bg-slate-900/75 backdrop-blur-md border border-slate-800 rounded-xl p-5 shadow-lg transition-all hover:border-slate-700 mb-5" id="{ch_id}" data-chapter-index="{idx}" data-chapter-title="{title}">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-3 pb-2.5 border-b border-slate-800/80">
        <div class="flex items-center gap-2.5">
          <span class="px-2.5 py-0.5 rounded-md text-[11px] font-bold bg-gradient-to-r from-red-600 to-amber-600 text-white shadow-sm">第 {idx:02d} 章</span>
          <h3 class="text-base sm:text-lg font-bold text-slate-100 tracking-wide">{title}</h3>
        </div>
        <div class="flex items-center gap-2">
          <button onclick='copyCustomText({escaped_plain_text}, "已複製 第{idx:02d}章 內容")' class="px-2.5 py-1 rounded-md text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 hover:border-slate-500 transition-colors flex items-center gap-1.5 cursor-pointer">
            <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>
            複製此章
          </button>
          <button onclick="toggleChapter('{ch_id}')" class="toggle-btn p-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-slate-200 transition-colors cursor-pointer" title="收合/展開">
            <svg class="w-4 h-4 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
        </div>
      </div>
      <div class="chapter-content text-slate-300">
        {card_body_html}
      </div>
    </div>
    '''
    chapter_cards.append(card_html)

sidebar_nav_html = '\n'.join(sidebar_nav_items)
all_chapters_html = '\n'.join(chapter_cards)

# Read full markdown text
with open('full_content.md', 'r', encoding='utf-8') as f:
    full_markdown_text = f.read()

escaped_full_markdown = json.dumps(full_markdown_text, ensure_ascii=False)

# 30 Effects array definition
effects_list = [
    ("01", "聖誕星光降臨", "金色星光由天空緩緩落下", "緩慢下移俯視 -> 微光粒子特寫", "Slow pan down, shimmering golden starlight descending softly from twilight winter sky, glistening bokeh and magical atmosphere"),
    ("02", "雪花瞬間凝結", "飄落雪花凝結為水晶圖案", "極限特寫微距", "Macro shot, floating snowflakes instantly crystallizing into intricate diamond-like geometric mandalas with ethereal glint"),
    ("03", "魔法禮盒開啟", "聖誕禮盒開啟並釋放魔法光芒", "前推推進特寫", "Slow push-in, ribbon untying automatically, velvet Christmas gift box creaking open to unleash an erupting beam of warm champagne golden light"),
    ("04", "冰晶王冠覺醒", "冰晶組合成皇家王冠", "環繞頭部特寫", "Orbital camera move, swirling azure frost particles floating up and condensing into an ornate royal ice crystal tiara with sparkling facets"),
    ("05", "聖誕樹光芒爆發", "聖誕樹燈飾逐層點亮，形成華麗光波", "由下往上仰拍升降", "Low-angle crane shot ascending, gigantic Christmas pine tree igniting tiers of twinkling lights sequentially, exploding in an ultra-wide shockwave of warm golden and pastel purple radiance"),
    ("06", "極光時空之門", "極光形成夢幻空間入口", "穿越推進鏡頭", "Dolly-in moving through a swirling vortex portal made of emerald and magenta northern lights curtain, glowing particles floating in zero gravity"),
    ("07", "馴鹿雪橇穿越", "馴鹿雪橇穿越夜空，留下金色星光軌跡", "遠景側跟拍", "Side tracking wide shot, majestic glowing reindeer pulling a Santa sleigh across the starry night sky, leaving a glittering luminous trail of golden sparkles"),
    ("08", "雪人魔法甦醒", "雪人由靜止裝飾變成可愛魔法角色", "平視中景", "Eye-level medium shot, static handcrafted snowman suddenly blinking with cute sparkling coal eyes, scarf gently fluttering as it comes alive with joy"),
    ("09", "水晶宮殿變形", "冰晶逐漸展開成皇家宮殿", "宏大鳥瞰俯衝", "Grand aerial panoramic shot, crystalline ice pillars and vaulted Gothic arches erupting from the frozen snowfield, transforming into an opulent royal palace"),
    ("10", "聖誕服裝瞬間變裝", "以雪花及光圈完成華麗換裝", "全身環繞 360 度", "Full-body 360 rotation, shimmering ribbon of frost and golden glitter spiraling around the characters, seamlessly morphing winter outfits into lavish royal Christmas attire"),
    ("11", "飄雪時間暫停", "雪花停留空中，人物自然互動", "子彈時間軌道滑行", "Bullet-time tracking shot, falling snowflakes freezing mid-air like suspended glass beads while characters look around in awe and reach out to touch them"),
    ("12", "魔法列車啟動", "列車燈光亮起，蒸汽及魔法軌道啟動", "低角度前進追焦", "Dynamic low-angle tracking shot, vintage enchanted steam locomotive blowing glowing golden steam, ice tracks illuminating underneath as it roars to life"),
    ("13", "聖誕精靈召喚", "魔法粒子凝聚出精靈", "微距跟隨旋轉", "Micro camera tracking, swirling golden dust particles swirling and manifesting into tiny glowing Christmas pixies leaving trails of fairy glitter"),
    ("14", "金色鈴鐺風暴", "金色鈴鐺及光點環繞", "高速旋轉後定格", "Whirlwind vortex shot, shimmering brass and gold jingle bells floating in a hurricane of festive chime sparks, ringing harmoniously"),
    ("15", "雪地煙火綻放", "魔法煙火在雪夜天空綻放", "廣角仰拍", "Ultra-wide low-angle shot, silent winter night sky erupting into spectacular kaleidoscopic fireworks mirroring upon pristine snowbanks"),
    ("16", "聖誕禮物雨", "精緻禮物由天空緩緩落下", "緩慢推進中遠景", "Gentle forward glide, thousands of beautifully wrapped colorful gift boxes drifting down softly with tiny parachutes made of frost"),
    ("17", "冰雪翅膀展開", "冰晶光翼於指定角色身後展開", "背影轉正面升鏡", "Dramatic camera tilt-up, breathtaking wings made of iridescent ice feathers and radiant aurora energy spreading grandly from character shoulders"),
    ("18", "糖果森林變形", "雪地轉化為夢幻糖果森林", "橫移滑軌全景", "Lateral dolly shot, frozen snow mounds flowering into oversized translucent peppermint canes, gumdrop trees, and sugar-frosted candy wonderland"),
    ("19", "聖誕城市點燈", "聖誕小鎮依序亮起燈飾", "高空大俯瞰推向街道", "High-angle city sweep zooming into cozy cobbled streets as warm amber shop lights and holiday garland lanterns illuminate one by one in succession"),
    ("20", "星河聖誕舞會", "星光形成夢幻舞池", "流暢華爾滋環繞運鏡", "Smooth waltz-style floating glide, reflective ice floor reflecting a celestial river of stars, glittering dust dancing beneath characters steps"),
    ("21", "巨大雪球穿越", "巨大雪球以喜劇方式滾過場景", "快速搖鏡追隨", "Fast pan tracking shot, enormous snowball comically rolling across frame in background, kicking up powdered snow with lighthearted festive charm"),
    ("22", "冰雪鏡面分身幻影", "冰晶鏡面形成反射幻影（不增真實人物）", "對稱構圖推鏡", "Symmetrical composition, pristine crystalline ice mirrors reflecting mystical ethereal light illusions and prism refractions without multiplying actual characters"),
    ("23", "聖誕城堡升空", "魔法城堡緩緩升起", "仰角穩定長鏡頭", "Steadicam low-angle tilt, majestic snow-covered fairy-tale fortress detaching from mountain peaks, floating slowly into glowing twilight clouds"),
    ("24", "極光雪花漩渦", "極光與雪花形成旋轉光流", "第一人稱穿透鏡頭", "Immersive forward rush, spiral vortex of violet aurora ribbons and crystalline snowstorm enveloping the viewer in a dazzling celestial tunnel"),
    ("25", "魔法雪橇競速", "雪橇在冬夜天空快速穿越", "高速跟隨長鏡頭", "High-speed pursuit shot flying alongside ornate golden sled runners carving neon light trails through cloud banks over snowy pine forests"),
    ("26", "聖誕時鐘倒轉", "巨大聖誕時鐘呈現時間倒流", "機械齒輪推拉鏡頭", "Vertigo zoom on monumental antique Christmas clockwork face, glowing golden Roman numerals spinning counter-clockwise with mystical rewind energy"),
    ("27", "水晶雪鹿現身", "水晶雪鹿由冰晶粒子凝聚", "緩步靠近特寫", "Slow creeping forward camera, translucent ethereal stag formed from starlight and ice crystals emerging peacefully through mist"),
    ("28", "聖誕光影傳送", "角色透過魔法光門轉換場景", "光芒閃爍穿梭轉場", "Flash-transition whip pan, characters stepping through an arched ring of festive fairy lights, instant seamless teleportation into a new wonderland"),
    ("29", "皇家聖誕加冕", "魔法王冠及皇家光芒形成加冕儀式", "崇高仰望推鏡", "Solemn low-angle push-in, royal golden halo and crystal scepter levitating gently, cascading regal blessing light over characters"),
    ("30", "終極聖誕魔法大合奏", "整合星光、極光、雪花、聖誕樹與皇家魔法", "史詩級 360 度環繞全景", "Epic grand 360 cinematic crane shot harmonizing starlight, ribbons of aurora, fireworks, glowing giant Christmas tree, and royal snow magic into a climactic symphonic finale")
]

effects_json_str = json.dumps(effects_list, ensure_ascii=False)

# Build effects cards HTML
effect_cards = []
for code, name, desc, camera, prompt_en in effects_list:
    effect_cards.append(f'''
    <div class="effect-item bg-slate-900/80 border border-slate-800 hover:border-amber-400/60 rounded-xl p-4 transition-all hover:-translate-y-1 hover:shadow-lg hover:shadow-amber-500/10 group cursor-pointer" onclick="selectEffect('{code}', '{name}', '{prompt_en}')">
      <div class="flex items-center justify-between mb-2">
        <span class="px-2 py-0.5 rounded text-[11px] font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">特效 #{code}</span>
        <button onclick="event.stopPropagation(); copyCustomText('{prompt_en}', '已複製特效 #{code} 提示詞')" class="text-slate-400 hover:text-amber-300 text-xs flex items-center gap-1 transition-colors">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
          複製
        </button>
      </div>
      <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition-colors mb-1">{name}</h4>
      <p class="text-xs text-slate-400 mb-2 leading-relaxed">{desc}</p>
      <div class="text-[11px] font-mono text-cyan-300/80 bg-slate-950/60 p-1.5 rounded border border-slate-800/80 truncate">
        🎬 運鏡：{camera}
      </div>
    </div>
    ''')
effects_cards_html = '\n'.join(effect_cards)

html_template = f'''<!DOCTYPE html>
<html lang="zh-Hant" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>隨心 AI Studio 🎄 2026 聖誕魔法宇宙 V4.0 Ultimate Commercial Cinema Edition</title>
  <meta name="description" content="2026 聖誕魔法宇宙 V4.0 電影級 AI 提示詞工程旗艦系統・三大引擎・七人一致性・30種電影特效・商業廣告・LINE 貼圖・25大章節完整指令">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            xmas: {{
              red: '#E53E3E',
              gold: '#F59E0B',
              green: '#10B981',
              dark: '#0A0E17',
              purple: '#9333EA',
              ice: '#38BDF8'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', '"Noto Sans TC"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
          }}
        }}
      }}
    }}
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', 'Noto Sans TC', system-ui, sans-serif;
      background-color: #070A12;
      color: #E2E8F0;
      overflow-x: hidden;
    }}
    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0B0F19;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1E293B;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}
    /* Glow Effects */
    .glow-gold {{
      text-shadow: 0 0 16px rgba(245, 158, 11, 0.45);
    }}
    .glow-red {{
      text-shadow: 0 0 16px rgba(239, 68, 68, 0.45);
    }}
    .glow-ice {{
      text-shadow: 0 0 16px rgba(56, 189, 248, 0.45);
    }}
    /* Glassmorphism */
    .glass-panel {{
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(51, 65, 85, 0.6);
    }}
    .nav-tab.active {{
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.9), rgba(217, 119, 6, 0.9));
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.3);
    }}
  </style>
</head>
<body class="min-h-screen relative selection:bg-amber-500 selection:text-slate-950">

  <!-- Snowfall Background Canvas -->
  <canvas id="snowCanvas" class="fixed inset-0 pointer-events-none z-10 opacity-70"></canvas>

  <!-- ==================== SECURITY AUTH GATE MODAL ==================== -->
  <div id="authGateModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/90 backdrop-blur-xl transition-opacity duration-300">
    <div class="relative w-full max-w-md p-6 sm:p-8 rounded-2xl bg-slate-900 border border-slate-700 shadow-2xl text-center">
      <div class="w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-tr from-red-600 via-amber-500 to-emerald-500 flex items-center justify-center shadow-lg shadow-amber-500/20">
        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
      </div>
      <h2 class="text-xl sm:text-2xl font-black text-white mb-2">研習專屬內部資源驗證</h2>
      <p class="text-xs sm:text-sm text-slate-400 mb-6 leading-relaxed">
        隨心 AI Studio 🎄 2026 聖誕魔法宇宙 V4.0<br/>
        請輸入研習通行碼以啟動完整提示詞系統
      </p>
      
      <form id="authForm" onsubmit="handleAuthSubmit(event)" class="space-y-4">
        <div class="relative">
          <input type="password" id="accessPassInput" autocomplete="off" placeholder="請輸入研習通行碼..." required
            class="w-full px-4 py-3 bg-slate-950 border border-slate-700 rounded-xl text-center text-amber-300 placeholder-slate-500 focus:outline-none focus:border-amber-400 focus:ring-2 focus:ring-amber-400/20 font-mono tracking-widest text-lg transition-all" />
        </div>
        <div id="authErrorMsg" class="hidden text-xs text-red-400 font-medium">通行碼比對失敗，請再次確認</div>
        <button type="submit" class="w-full py-3 px-6 rounded-xl font-bold bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-white shadow-lg shadow-red-600/25 active:scale-[0.98] transition-all cursor-pointer">
          確認登入解鎖
        </button>
      </form>
      <div class="mt-6 pt-4 border-t border-slate-800 text-[11px] text-slate-500 flex items-center justify-between">
        <span>© 2026 隨心 AI Studio</span>
        <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-500"></span>SHA-256 安全晶片驗證</span>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 pointer-events-none">
    <div class="px-5 py-3 rounded-xl bg-slate-900/95 border border-amber-400/60 shadow-2xl backdrop-blur-md flex items-center gap-3 text-slate-100 text-sm">
      <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
      <span id="toastMsg" class="font-medium">已完成操作</span>
    </div>
  </div>

  <!-- Main Container -->
  <div id="mainApp" class="relative z-20 min-h-screen flex flex-col">
    
    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-40 bg-slate-950/85 backdrop-blur-xl border-b border-slate-800/80">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
        
        <!-- Brand Title -->
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-red-600 to-amber-500 flex items-center justify-center text-lg shadow-md shadow-amber-500/20">
            🎄
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-black text-sm sm:text-base text-white tracking-wide">隨心 AI Studio</span>
              <span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-red-600/30 text-red-300 border border-red-500/40">V4.0</span>
            </div>
            <div class="text-[11px] text-slate-400 hidden sm:block">2026 聖誕魔法宇宙・商業電影旗艦版</div>
          </div>
        </div>

        <!-- Controls (Snow, Audio, Re-lock) -->
        <div class="flex items-center gap-2 sm:gap-3">
          <!-- Snow Toggle -->
          <button id="toggleSnowBtn" onclick="toggleSnow()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 flex items-center gap-1.5 transition-colors cursor-pointer" title="切換飄雪動畫">
            <span id="snowIcon">❄️</span>
            <span class="hidden md:inline" id="snowLabel">飄雪: 開</span>
          </button>
          
          <!-- Audio Toggle -->
          <button id="toggleSoundBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 flex items-center gap-1.5 transition-colors cursor-pointer" title="切換聖誕互動音效">
            <span id="soundIcon">🔔</span>
            <span class="hidden md:inline" id="soundLabel">音效: 開</span>
          </button>

          <!-- Quick Full Prompt Copy -->
          <button onclick="copyMasterPrompt()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 flex items-center gap-1.5 transition-all shadow-md shadow-amber-500/20 cursor-pointer">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
            <span class="hidden sm:inline">複製全篇提示詞</span>
            <span class="sm:hidden">複製全文</span>
          </button>

          <!-- Relock Button -->
          <button onclick="lockSystem()" class="p-1.5 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-red-950/60 border border-slate-800 hover:border-red-700 text-slate-400 hover:text-red-300 flex items-center gap-1 transition-colors cursor-pointer" title="重新鎖定系統">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
            <span class="hidden lg:inline">鎖定</span>
          </button>
        </div>

      </div>

      <!-- Navigation Tabs Bar -->
      <div class="border-t border-slate-800/60 bg-slate-950/60 overflow-x-auto no-scrollbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 flex gap-1 py-1.5">
          <button onclick="switchTab('studio')" id="tab-studio" class="nav-tab active px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>🎛️</span> 提示詞產生工作室
          </button>
          <button onclick="switchTab('chapters')" id="tab-chapters" class="nav-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>📚</span> 25 章指令總覽庫
          </button>
          <button onclick="switchTab('effects')" id="tab-effects" class="nav-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>🌟</span> 30 種電影特效盒
          </button>
          <button onclick="switchTab('characters')" id="tab-characters" class="nav-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>👥</span> 七人角色一致性
          </button>
          <button onclick="switchTab('commercial')" id="tab-commercial" class="nav-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>💼</span> 商業廣告與貼圖
          </button>
          <button onclick="switchTab('master')" id="tab-master" class="nav-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-all whitespace-nowrap cursor-pointer flex items-center gap-1.5">
            <span>📜</span> 原文指令總覽
          </button>
        </div>
      </div>
    </header>

    <!-- Hero Banner -->
    <div class="relative bg-gradient-to-b from-slate-900 via-slate-950 to-slate-950 border-b border-slate-800/60 py-10 sm:py-14 px-4 sm:px-6">
      <div class="max-w-5xl mx-auto text-center relative z-20">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800/80 border border-slate-700 text-xs font-medium text-amber-300 mb-4 shadow-sm">
          <span>✨ 2026 最新電影級旗艦標準</span>
          <span class="w-1 h-1 rounded-full bg-slate-500"></span>
          <span>隨心 AI Studio 官方授權</span>
        </div>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-emerald-400 tracking-tight mb-4">
          聖誕魔法宇宙 V4.0
        </h1>
        <p class="text-base sm:text-lg text-slate-300 max-w-3xl mx-auto leading-relaxed mb-6 font-normal">
          三大引擎・七人一致性鎖定・30 種聖誕電影特效・商業廣告旗艦・LINE 聖誕貼圖<br class="hidden sm:inline"/>
          提供完整繁體中文 25 大章節正式提示詞與即打即用互動提示詞產生器。
        </p>

        <!-- Metrics Pills -->
        <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-6 text-xs font-mono text-slate-300">
          <div class="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 shadow-sm flex items-center gap-2">
            <span class="text-amber-400 font-bold text-sm">25</span> 章核心規範
          </div>
          <div class="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 shadow-sm flex items-center gap-2">
            <span class="text-red-400 font-bold text-sm">30</span> 種電影特效
          </div>
          <div class="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 shadow-sm flex items-center gap-2">
            <span class="text-emerald-400 font-bold text-sm">12</span> 種視覺畫風
          </div>
          <div class="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 shadow-sm flex items-center gap-2">
            <span class="text-sky-400 font-bold text-sm">7</span> 人角色鎖定
          </div>
          <div class="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 shadow-sm flex items-center gap-2">
            <span class="text-purple-400 font-bold text-sm">3</span> 大旗艦引擎
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-8">
      
      <!-- ==================== TAB 1: PROMPT STUDIO (產生器) ==================== -->
      <section id="view-studio" class="tab-view block space-y-8">
        
        <!-- Preset Quick Loader -->
        <div class="bg-gradient-to-r from-red-950/40 via-slate-900/70 to-amber-950/40 border border-amber-500/30 rounded-2xl p-5 flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-xl">
              🌲
            </div>
            <div>
              <h3 class="text-base font-bold text-amber-300">快速載入預設專案</h3>
              <p class="text-xs text-slate-400">第二十二章官方範例：七人聖誕魔法森林（ABC 引擎・夢幻粉紫童話・10秒爆發光芒）</p>
            </div>
          </div>
          <button onclick="loadDefaultProjectPreset()" class="px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 shadow-md shadow-amber-500/20 transition-all flex items-center gap-1.5 cursor-pointer">
            <span>✨</span> 載入預設專案
          </button>
        </div>

        <!-- Studio 2-Column Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <!-- Left Column: Controls (18 Options) -->
          <div class="lg:col-span-7 bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h2 class="text-lg font-bold text-white flex items-center gap-2">
                <span>🎛️</span> 參數與設定面板（18 項維度）
              </h2>
              <button onclick="resetStudioForm()" class="text-xs text-slate-400 hover:text-amber-400 transition-colors">
                重置預設
              </button>
            </div>

            <form id="studioForm" oninput="updatePromptOutput()" class="space-y-5">
              
              <!-- 01 & 02: Engine & Characters -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">01｜引擎組合</label>
                  <select id="opt_engine" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="ABC" selected>ABC 引擎旗艦全合一 (生圖+短劇+商業廣告)</option>
                    <option value="A">A 引擎｜聖誕 AI 生圖</option>
                    <option value="B">B 引擎｜電影特效與短劇導演</option>
                    <option value="C">C 引擎｜商業廣告與商品展示</option>
                    <option value="AB">AB 引擎｜生圖與電影短劇</option>
                    <option value="AC">AC 引擎｜生圖與商業廣告</option>
                    <option value="BC">BC 引擎｜短劇與商業廣告</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">02｜人物來源與組合</label>
                  <select id="opt_people" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="7P" selected>七人固定模式 (M01 男主 + F01~F06 六女神)</option>
                    <option value="M01_ONLY">單人男主角 (M01 沿用照片鎖定)</option>
                    <option value="F01_ONLY">單人女神代言 (F01 原創角色卡)</option>
                    <option value="M01_F01">雙人搭檔 (M01 男主 + F01 女神)</option>
                    <option value="6F">六位成年女神 (F01～F06 組合)</option>
                    <option value="CUSTOM">自訂人物組合</option>
                  </select>
                </div>
              </div>

              <!-- 03 & 04: Consistency Lock & Style -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">03｜七人角色卡與身份鎖定</label>
                  <select id="opt_lock" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="ON" selected>強制開啟 (鎖定男主五官神韻 + 六女各自辨識)</option>
                    <option value="AI_NEW">AI 原創成年角色 (暫定設定，未鎖定照片)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">04｜12 種視覺畫風</label>
                  <select id="opt_style" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="05_PURPLE" selected>05｜夢幻粉紫童話 (粉紫/冰藍/珍珠白/極光)</option>
                    <option value="01_REALISTIC">01｜電影級真人寫實 (真實肌膚/自然電影光影)</option>
                    <option value="02_Q25">02｜精緻 2.5 頭身 Q 版 (可愛3D比例/特徵清晰)</option>
                    <option value="03_QFUNNY">03｜爆笑誇張 Q 版 (喜劇表情/誇張動態)</option>
                    <option value="04_3DMOVIE">04｜電影級 3D 動畫 (頂級精緻材質/動態光追)</option>
                    <option value="06_BLACKGOLD">06｜黑金皇家聖誕 (黑金/深紅/香檳金/奢華)</option>
                    <option value="07_CYBER">07｜未來科幻聖誕 (全息聖誕樹/科技光效)</option>
                    <option value="08_PLUSH">08｜毛絨療癒 (溫暖柔光/毛絨童話質感)</option>
                    <option value="09_ANIME">09｜日系動畫 (唯美冬日/日式賽璐璐風)</option>
                    <option value="10_SNOWGLOBE">10｜微縮水晶雪球 (透明水晶球微型世界)</option>
                    <option value="11_EPIC">11｜史詩魔法電影 (巨大皇家宮殿/震撼特效)</option>
                    <option value="12_COMMERCIAL">12｜精品商業廣告 (商業棚拍/焦點景深構圖)</option>
                  </select>
                </div>
              </div>

              <!-- 05 & 06: Medium & Scene -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">05｜人物呈現媒材</label>
                  <select id="opt_medium" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="3D_ANIMATION" selected>高品質動畫電影 (Cinematic 3D Animation)</option>
                    <option value="LIVE_ACTION">電影真人寫實攝影 (Cinematic Live-Action)</option>
                    <option value="3D_Q">3D 精緻 Q 版黏土公仔 (3D Stylized Chibi)</option>
                    <option value="ILLUSTRATION">夢幻藝術概念插畫 (Fantasy Concept Art)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">06｜聖誕場景系統</label>
                  <select id="opt_scene" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="MAGIC_FOREST" selected>06 魔法森林 (巨大發光雪松/紫金極光/雪屋)</option>
                    <option value="TRAIN">01 聖誕魔法列車 (復古蒸氣/漂浮冰軌/溫暖車廂)</option>
                    <option value="PLAZA">02 聖誕樹雪地廣場 (燈海/木造市集/飄雪夜空)</option>
                    <option value="PURPLE_CASTLE">03 粉紫水晶城堡 (琉璃尖塔/浮空島/極光光環)</option>
                    <option value="ICE_PALACE">04 冰雪皇家宮殿 (水晶石柱/宏偉大廳/冰雕加冕)</option>
                    <option value="AURORA_MOUNTAIN">05 極光雪山 (雄偉山脊/星夜長河/冰湖倒影)</option>
                    <option value="TOWN">07 夢幻聖誕小鎮 (鵝卵石小徑/暖黃閣樓)</option>
                    <option value="BALLROOM">08 皇家聖誕舞會 (鏡面冰池/奢華吊燈)</option>
                    <option value="STUDIO">11 聖誕商品攝影棚 (無縫背景/柔光箱/精品台)</option>
                  </select>
                </div>
              </div>

              <!-- 07 & 08: Clothing & Positioning -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">07｜聖誕服裝系統</label>
                  <select id="opt_costume" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="ROYAL_ICE" selected>冰雪皇家聖誕禮服 (白絨毛邊/香檳金刺繡/冰晶配件)</option>
                    <option value="CLASSIC_RED">經典紅白金聖誕裝 (天鵝絨紅袍/白絨邊/金色鈴鐺)</option>
                    <option value="PASTEL_PURPLE">粉紫夢幻聖誕裝 (淡粉/丁香紫/珍珠白披肩)</option>
                    <option value="BLACK_GOLD">黑金皇家聖誕裝 (曜石黑/深金刺繡/皇家勳章)</option>
                    <option value="CASUAL_WINTER">聖誕休閒冬裝 (北歐圖騰厚毛衣/暖冬針織帽/圍巾)</option>
                    <option value="BALLROOM_GOWN">聖誕舞會華麗禮服 (星光紗裙/水晶王冠/燕尾服)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">08｜人物站位佈局</label>
                  <select id="opt_position" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="FOUR_BACK_TWO_FRONT" selected>標準四後二前・男主正中 (無遮擋/面部清晰)</option>
                    <option value="SURROUND">半月形環繞站位 (男主居中/女神兩側階梯式環繞)</option>
                    <option value="DYNAMIC_INTERACTION">動態互動聚會 (圍繞發光聖誕樹禮盒交流)</option>
                  </select>
                </div>
              </div>

              <!-- 09: 30 Effects Selector -->
              <div>
                <label class="block text-xs font-bold text-slate-300 mb-1.5 flex items-center justify-between">
                  <span>09｜30 種聖誕電影特效</span>
                  <span class="text-[11px] text-amber-400 font-normal">首幀不提前透支特效</span>
                </label>
                <select id="opt_effect" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-amber-300 font-mono focus:outline-none focus:border-amber-400">
                  <option value="05" selected>05｜聖誕樹光芒爆發 (燈飾逐層亮起，衝擊波光芒擴散)</option>
                  <option value="01">01｜聖誕星光降臨 (金色星光自夜空緩緩落下)</option>
                  <option value="02">02｜雪花瞬間凝結 (落雪凝固為晶瑩幾何曼陀羅)</option>
                  <option value="03">03｜魔法禮盒開啟 (禮盒開啟噴發出暖金光柱)</option>
                  <option value="04">04｜冰晶王冠覺醒 (藍色冰晶浮空凝聚成皇家王冠)</option>
                  <option value="06">06｜極光時空之門 (極光形成穿越異界蟲洞光環)</option>
                  <option value="07">07｜馴鹿雪橇穿越 (夜空掠過留下金粉星光軌跡)</option>
                  <option value="10">10｜聖誕服裝瞬間變裝 (雪花光圈環繞全身華麗換裝)</option>
                  <option value="11">11｜飄雪時間暫停 (雪花定格空中，人物驚奇觸碰)</option>
                  <option value="12">12｜魔法列車啟動 (金光蒸氣噴發，軌道冰晶逐節點亮)</option>
                  <option value="17">17｜冰雪翅膀展開 (角色背後展開極光羽翼)</option>
                  <option value="20">20｜星河聖誕舞會 (冰面化作星河流轉舞池)</option>
                  <option value="29">29｜皇家聖誕加冕 (金色光環與權杖漂浮加冕)</option>
                  <option value="30">30｜終極聖誕魔法大合奏 (星光/極光/煙火/聖誕樹巔峰交響)</option>
                </select>
              </div>

              <!-- 10 & 11: Ratios -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">10｜首幀圖片比例</label>
                  <select id="opt_first_ratio" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="4:5" selected>4:5 (社群直式高畫質推薦)</option>
                    <option value="9:16">9:16 (短影音全螢幕直式)</option>
                    <option value="16:9">16:9 (橫式電影寬螢幕)</option>
                    <option value="1:1">1:1 (正方形社群圖卡)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">11｜影片比例</label>
                  <select id="opt_video_ratio" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="9:16" selected>9:16 (Reels / TikTok / Shorts)</option>
                    <option value="16:9">16:9 (YouTube / 電視電影螢幕)</option>
                    <option value="1:1">1:1 (社群方塊影片)</option>
                  </select>
                </div>
              </div>

              <!-- 12 & 13: Duration & Platform -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">12｜影片長度與結構</label>
                  <select id="opt_duration" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="10s" selected>10 秒單幕標準 (0-2s開場 2-4s互動 4-7s特效 7-9s反應 9-10s收尾)</option>
                    <option value="5s">5 秒極速動態短片</option>
                    <option value="15s">15 秒完整情節單幕</option>
                    <option value="30s_3acts">30 秒經典三幕短劇 (啟承轉合)</option>
                    <option value="60s_6acts">60 秒六幕迷你微電影</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">13｜影片生成平台</label>
                  <select id="opt_platform" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="Grok Imagine" selected>Grok Imagine (專業電影模式推薦)</option>
                    <option value="Google Flow">Google Flow (Veo 3.1 首尾幀強大)</option>
                    <option value="Kling">Kling AI (可靈 1.5/2.0 高一致性)</option>
                    <option value="Runway Gen-3">Runway Gen-3 Alpha</option>
                    <option value="Seedance">Seedance (字節跳動海螺)</option>
                  </select>
                </div>
              </div>

              <!-- 14 & 15: Drama & Commercial -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">14｜短劇導演模式</label>
                  <select id="opt_drama" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="FEATURED" selected>溫馨奇幻合奏 (注重角色微笑驚喜互動)</option>
                    <option value="COMEDY">輕喜劇幽默風格 (逗趣表情與雪人小意外)</option>
                    <option value="ROMANCE">浪漫電影光影 (深情眼神與星光微風)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">15｜商業廣告目標 (選填)</label>
                  <select id="opt_commercial" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="NONE" selected>暫無商業商品 (純電影短片，C 引擎保留)</option>
                    <option value="TECH_3C">3C 科技產品 (手機/耳機懸浮拆解)</option>
                    <option value="HOLIDAY_GIFT">聖誕節禮物主視覺 (精品手錶/珠寶香水)</option>
                    <option value="SHOPEE_AFF">電商導購與蝦皮推廣 (留言區引導)</option>
                  </select>
                </div>
              </div>

              <!-- 17 & 18: Phase & Extra Notes -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">17｜執行階段</label>
                  <select id="opt_phase" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400">
                    <option value="PHASE1" selected>階段一：確認設定摘要與角色鎖定</option>
                    <option value="PHASE2">階段二：首幀生圖提示詞生成</option>
                    <option value="PHASE3">階段三：影片逐秒分鏡與提示詞</option>
                    <option value="PHASE4">階段四：成片驗收與局部修復</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-300 mb-1.5">18｜補充微調要求</label>
                  <input type="text" id="opt_notes" placeholder="例如：強化紫色極光反光、不加字幕..." value="強化極光反光，無字幕無Logo無浮水印"
                    class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-amber-400" />
                </div>
              </div>

            </form>
          </div>

          <!-- Right Column: Live Output & Prompt Blocks -->
          <div class="lg:col-span-5 space-y-4">
            
            <div class="flex items-center justify-between">
              <h3 class="text-base font-bold text-white flex items-center gap-2">
                <span>📋</span> 即時生成的提示詞套件
              </h3>
              <span class="text-xs text-emerald-400 font-mono flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                同步更新中
              </span>
            </div>

            <!-- Block 1: Chinese Setup Summary -->
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md">
              <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
                <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                  <span>📑</span> 中文設定摘要與角色排程
                </span>
                <button onclick="copyElementText('output_summary', '已複製中文設定摘要')" class="text-xs text-slate-400 hover:text-amber-400 flex items-center gap-1 transition-colors cursor-pointer">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                  複製
                </button>
              </div>
              <pre id="output_summary" class="text-xs text-slate-300 font-mono whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto no-scrollbar"></pre>
            </div>

            <!-- Block 2: Positive First Frame Image Prompt -->
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md">
              <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
                <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                  <span>🎨</span> 首幀生圖正面提示詞 (Positive Prompt)
                </span>
                <button onclick="copyElementText('output_positive_img', '已複製首幀正面提示詞')" class="text-xs text-slate-400 hover:text-emerald-400 flex items-center gap-1 transition-colors cursor-pointer">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                  複製
                </button>
              </div>
              <div id="output_positive_img" class="text-xs text-slate-200 font-mono leading-relaxed bg-slate-950 p-2.5 rounded-lg max-h-40 overflow-y-auto"></div>
            </div>

            <!-- Block 3: Video Motion Prompt -->
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md">
              <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
                <span class="text-xs font-bold text-sky-400 flex items-center gap-1.5">
                  <span>🎬</span> 影片動態提示詞 (Video Motion Prompt)
                </span>
                <button onclick="copyElementText('output_positive_video', '已複製影片動態提示詞')" class="text-xs text-slate-400 hover:text-sky-400 flex items-center gap-1 transition-colors cursor-pointer">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                  複製
                </button>
              </div>
              <div id="output_positive_video" class="text-xs text-slate-200 font-mono leading-relaxed bg-slate-950 p-2.5 rounded-lg max-h-40 overflow-y-auto"></div>
            </div>

            <!-- Block 4: Negative Prompt (Independent) -->
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md">
              <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
                <span class="text-xs font-bold text-red-400 flex items-center gap-1.5">
                  <span>🚫</span> 獨立負面提示詞 (Negative Prompt)
                </span>
                <button onclick="copyElementText('output_negative', '已複製獨立負面提示詞')" class="text-xs text-slate-400 hover:text-red-400 flex items-center gap-1 transition-colors cursor-pointer">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                  複製
                </button>
              </div>
              <div id="output_negative" class="text-xs text-red-300/90 font-mono leading-relaxed bg-slate-950 p-2.5 rounded-lg">
                subtitles, text, watermark, signature, logo, UI, extra characters, missing limbs, bad anatomy, deformed fingers, blurry face, face morphing, mismatched face, oversaturated, low quality, pixelated
              </div>
            </div>

            <!-- Block 5: 10s Timeline Breakdown -->
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md">
              <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
                <span class="text-xs font-bold text-purple-400 flex items-center gap-1.5">
                  <span>⏱️</span> 10 秒逐秒導演分鏡規劃表
                </span>
                <button onclick="copyElementText('output_timeline', '已複製分鏡規劃表')" class="text-xs text-slate-400 hover:text-purple-400 flex items-center gap-1 transition-colors cursor-pointer">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                  複製
                </button>
              </div>
              <div id="output_timeline" class="text-xs text-slate-300 font-mono space-y-1.5 leading-relaxed bg-slate-950 p-2.5 rounded-lg"></div>
            </div>

          </div>

        </div>

      </section>

      <!-- ==================== TAB 2: 25 CHAPTERS EXPLORER (章節庫) ==================== -->
      <section id="view-chapters" class="tab-view hidden space-y-6">
        
        <!-- Search & Control Header -->
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg flex flex-wrap items-center justify-between gap-4">
          <div class="relative flex-1 min-w-[240px]">
            <input type="text" id="chapterSearchInput" oninput="filterChapters()" placeholder="搜尋 25 章內容關鍵字（例如：首幀、一致性、貼圖、特效）..."
              class="w-full bg-slate-950 border border-slate-700 rounded-xl pl-10 pr-4 py-2.5 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-400" />
            <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="expandAllChapters()" class="px-3 py-2 rounded-xl text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition-colors cursor-pointer">
              全部展開
            </button>
            <button onclick="collapseAllChapters()" class="px-3 py-2 rounded-xl text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition-colors cursor-pointer">
              全部收合
            </button>
          </div>
        </div>

        <!-- Layout: Sidebar Nav + Chapter Cards -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <!-- Sticky Table of Contents -->
          <div class="hidden lg:block lg:col-span-3 sticky top-36 bg-slate-900/80 border border-slate-800 rounded-2xl p-4 shadow-xl max-h-[calc(100vh-160px)] overflow-y-auto no-scrollbar">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-3 px-2 flex items-center justify-between">
              <span>25 大章節導覽</span>
              <span class="text-[10px] text-slate-500">25 目錄</span>
            </h4>
            <nav class="space-y-0.5">
              {sidebar_nav_html}
            </nav>
          </div>

          <!-- Cards Column -->
          <div class="lg:col-span-9 space-y-5" id="chaptersContainer">
            {all_chapters_html}
          </div>

        </div>

      </section>

      <!-- ==================== TAB 3: 30 EFFECTS GRID (電影特效盒) ==================== -->
      <section id="view-effects" class="tab-view hidden space-y-6">
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl">
          <div class="flex flex-wrap items-center justify-between gap-4 mb-4 pb-4 border-b border-slate-800">
            <div>
              <h2 class="text-xl font-bold text-white flex items-center gap-2">
                <span>🌟</span> 30 種聖誕電影特效矩陣
              </h2>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">
                第九章精選 30 種專業電影動態特效。點擊卡片即可將該特效帶入「提示詞工作室」進行自訂組合！
              </p>
            </div>
            <div class="text-xs font-mono text-amber-400 bg-amber-500/10 border border-amber-500/30 px-3 py-1.5 rounded-lg">
              特效製作鐵律：首幀不提前透支特效・維持角色尾幀連續性
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4" id="effectsGrid">
            {effects_cards_html}
          </div>
        </div>
      </section>

      <!-- ==================== TAB 4: 7-CHARACTER CONSISTENCY (七人一致性) ==================== -->
      <section id="view-characters" class="tab-view hidden space-y-6">
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-6">
          <div>
            <h2 class="text-xl font-bold text-white flex items-center gap-2">
              <span>👥</span> V4.0 七人角色一致性強化系統
            </h2>
            <p class="text-xs sm:text-sm text-slate-400 mt-1">
              遵循第五章鐵律：嚴格執行「一男六女」恰好七人模式，人物身份一致性永遠優先於美化與特效。
            </p>
          </div>

          <!-- 6 Golden Rules of Consistency -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div class="p-4 rounded-xl bg-slate-950/70 border border-red-500/30">
              <span class="text-red-400 font-bold text-xs">鐵律 01</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">恰好一男六女</h4>
              <p class="text-xs text-slate-400 leading-relaxed">使用者指定七人時，總數必須恰好七人。不得多手多指、不得重複人物或擅自增減。</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-950/70 border border-amber-500/30">
              <span class="text-amber-400 font-bold text-xs">鐵律 02</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">M01 男主鎖定照片</h4>
              <p class="text-xs text-slate-400 leading-relaxed">以使用者指定的真實男性照片為身份依據，保留臉型、五官比例、年齡感與神韻，不可變成陌生人。</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-950/70 border border-emerald-500/30">
              <span class="text-emerald-400 font-bold text-xs">鐵律 03</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">六女神獨立辨識</h4>
              <p class="text-xs text-slate-400 leading-relaxed">F01～F06 六位女神必須具備獨立不同的臉型五官、髮型與專屬特徵，嚴禁六人同臉換裝。</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-950/70 border border-sky-500/30">
              <span class="text-sky-400 font-bold text-xs">鐵律 04</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">換裝換景不換臉</h4>
              <p class="text-xs text-slate-400 leading-relaxed">更換聖誕服裝、切換城堡/雪山/列車場景或改變肢體動作時，人物臉型與身份特徵絕對不得改變。</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-950/70 border border-purple-500/30">
              <span class="text-purple-400 font-bold text-xs">鐵律 05</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">四後二前標準站位</h4>
              <p class="text-xs text-slate-400 leading-relaxed">預設站位：M01 男主位於正中央；F01～F04 位於後排；F05、F06 位於前排兩側，所有人臉無遮擋。</p>
            </div>
            <div class="p-4 rounded-xl bg-slate-950/70 border border-slate-700">
              <span class="text-slate-400 font-bold text-xs">鐵律 06</span>
              <h4 class="text-sm font-bold text-white mt-1 mb-1">局部修改保留原貌</h4>
              <p class="text-xs text-slate-400 leading-relaxed">收到局部修改指令時，僅修改使用者明確指定的區塊（如單純修復服裝或道具），其餘畫面百分之百保留。</p>
            </div>
          </div>

          <!-- Character Cards -->
          <h3 class="text-base font-bold text-amber-300 pt-4 border-t border-slate-800">
            七人固定編號與特徵配置表
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-7 gap-3">
            
            <!-- M01 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-amber-500/50 shadow-md">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">M01</span>
              <h4 class="text-sm font-bold text-white mt-1">唯一男主角</h4>
              <p class="text-[11px] text-slate-400 mt-1">身份：沿用真實照片</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：正中央</div>
                <div>聲線：固定男中音</div>
                <div>鎖定：自然年齡神韻</div>
              </div>
            </div>

            <!-- F01 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">F01</span>
              <h4 class="text-sm font-bold text-white mt-1">第一女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">優雅大方・長卷髮</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：後排偏左</div>
                <div>服裝：冰雪長袍</div>
                <div>特徵：杏眼溫和</div>
              </div>
            </div>

            <!-- F02 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">F02</span>
              <h4 class="text-sm font-bold text-white mt-1">第二女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">清麗靈動・波浪捲</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：後排左二</div>
                <div>服裝：星芒雪紗</div>
                <div>特徵：高挺鼻樑</div>
              </div>
            </div>

            <!-- F03 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">F03</span>
              <h4 class="text-sm font-bold text-white mt-1">第三女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">端莊貴氣・盤髮冠</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：後排右二</div>
                <div>服裝：天鵝絨斗篷</div>
                <div>特徵：深邃眼神</div>
              </div>
            </div>

            <!-- F04 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">F04</span>
              <h4 class="text-sm font-bold text-white mt-1">第四女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">甜美活潑・側編髮</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：後排偏右</div>
                <div>服裝：短斗篷毛邊</div>
                <div>特徵：酒窩微笑</div>
              </div>
            </div>

            <!-- F05 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">F05</span>
              <h4 class="text-sm font-bold text-white mt-1">第五女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">自信颯爽・俐落短髮</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：前排左側</div>
                <div>服裝：修身皇家冬裝</div>
                <div>特徵：英挺眉目</div>
              </div>
            </div>

            <!-- F06 -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">F06</span>
              <h4 class="text-sm font-bold text-white mt-1">第六女神</h4>
              <p class="text-[11px] text-slate-400 mt-1">仙氣空靈・雙馬尾</p>
              <div class="text-[10px] font-mono text-cyan-300 mt-2 space-y-0.5">
                <div>站位：前排右側</div>
                <div>服裝：輕盈毛絨冬裙</div>
                <div>特徵：靈秀大眼</div>
              </div>
            </div>

          </div>

        </div>
      </section>

      <!-- ==================== TAB 5: COMMERCIAL & LINE STICKER ==================== -->
      <section id="view-commercial" class="tab-view hidden space-y-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">
          
          <!-- C Engine Commercial Ads -->
          <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
            <div class="flex items-center gap-3 pb-3 border-b border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold">
                C
              </div>
              <div>
                <h3 class="text-base font-bold text-white">C 引擎｜商業廣告旗艦版 SOP</h3>
                <p class="text-xs text-slate-400">第十六章商業規範：外觀100%鎖定、無虛假數據、社群導購文案</p>
              </div>
            </div>

            <!-- 10-Second Commercial Rhythm -->
            <div>
              <h4 class="text-xs font-bold text-amber-300 mb-2">🎬 10 秒黃金廣告節奏軸</h4>
              <div class="space-y-2 text-xs font-mono">
                <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
                  <span class="text-amber-400 font-bold">0～2 秒</span>
                  <span class="text-slate-300">吸睛開場 (強烈視覺懸疑/魔法光芒破題)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
                  <span class="text-emerald-400 font-bold">2～5 秒</span>
                  <span class="text-slate-300">產品特寫展示 (質感光澤/商品懸浮或精緻旋轉)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
                  <span class="text-sky-400 font-bold">5～8 秒</span>
                  <span class="text-slate-300">核心痛點優勢 (具體解決生活難題，真實可信)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between">
                  <span class="text-purple-400 font-bold">8～10 秒</span>
                  <span class="text-slate-300">品牌記憶點與 CTA (限時優惠/引導留言區連結)</span>
                </div>
              </div>
            </div>

            <!-- Social Media Formula -->
            <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800 text-xs text-slate-300 space-y-2">
              <h4 class="font-bold text-white">📱 FB / IG 社群文案發布公式</h4>
              <p>1. 吸睛開場鉤子（生活痛點共鳴）</p>
              <p>2. 核心功能亮點（白話生動描述）</p>
              <p>3. 節慶使用情境（聖誕送禮/年末犒賞）</p>
              <p class="text-amber-400 font-semibold">4. 嚴格遵守：粉專正文不放外部連結，連結一律置於留言區第一則！</p>
            </div>
          </div>

          <!-- LINE Sticker Engine -->
          <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
            <div class="flex items-center gap-3 pb-3 border-b border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 flex items-center justify-center font-bold">
                貼
              </div>
              <div>
                <h3 class="text-base font-bold text-white">LINE 聖誕貼圖引擎規準</h3>
                <p class="text-xs text-slate-400">第十七章貼圖鐵律：先單張後總覽、25%安全留白、真正透明PNG</p>
              </div>
            </div>

            <!-- Sticker Rules -->
            <div class="space-y-3 text-xs leading-relaxed text-slate-300">
              <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/30 space-y-1">
                <span class="font-bold text-emerald-400">01｜先單張，後總覽</span>
                <p class="text-slate-400">嚴禁直接把 4×4 合成圖當成正式貼圖交件。必須逐張產出、逐張檢查無誤後，再做總覽表。</p>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-amber-500/30 space-y-1">
                <span class="font-bold text-amber-400">02｜留白安全規範</span>
                <p class="text-slate-400">人物、字體與配件視為同一群組，總佔比原則上不超過寬高 50%，四周各預留至少 25% 空間防邊界切字。</p>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-red-500/30 space-y-1">
                <span class="font-bold text-red-400">03｜真正透明 PNG</span>
                <p class="text-slate-400">必須具備真 Alpha 透明通道，嚴禁保留灰白棋盤格假透明背景！</p>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-sky-500/30 space-y-1">
                <span class="font-bold text-sky-400">04｜ZIP 交付前物理驗證</span>
                <p class="text-slate-400">未實際驗證檔案數量（8/16/24張）、主圖 main.png、標籤 tab.png 與透明通道前，絕不虛構已完成交付。</p>
              </div>
            </div>

          </div>

        </div>
      </section>

      <!-- ==================== TAB 6: MASTER PROMPT COPY (全文) ==================== -->
      <section id="view-master" class="tab-view hidden space-y-6">
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-4 pb-4 border-b border-slate-800">
            <div>
              <h2 class="text-lg font-bold text-white flex items-center gap-2">
                <span>📜</span> 隨心 AI Studio V4.0 全篇 25 章完整正式提示詞
              </h2>
              <p class="text-xs text-slate-400 mt-1">
                適用於直接整篇複製貼入 ChatGPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro、NotebookLM 或 Grok 建立完整系統身分。
              </p>
            </div>
            <button onclick="copyMasterPrompt()" class="px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-white shadow-lg shadow-amber-500/20 transition-all flex items-center gap-1.5 cursor-pointer">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
              一鍵複製全篇提示詞
            </button>
          </div>

          <pre id="masterPromptText" class="text-xs text-slate-300 font-mono leading-relaxed bg-slate-950 p-4 rounded-xl border border-slate-800 max-h-[600px] overflow-y-auto whitespace-pre-wrap">{full_markdown_text}</pre>
        </div>
      </section>

    </main>

    <!-- Footer -->
    <footer class="mt-16 border-t border-slate-800/80 bg-slate-950/80 py-8 px-4 text-center text-xs text-slate-500">
      <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>隨心 AI Studio 🎄 2026 聖誕魔法宇宙 V4.0 Ultimate Commercial Cinema Edition</div>
        <div class="flex items-center gap-4 text-slate-400">
          <a href="#" onclick="switchTab('studio')" class="hover:text-amber-400">提示詞產生器</a>
          <a href="#" onclick="switchTab('chapters')" class="hover:text-amber-400">25章總覽</a>
          <a href="#" onclick="switchTab('effects')" class="hover:text-amber-400">30種特效</a>
          <a href="#" onclick="copyMasterPrompt()" class="hover:text-amber-400">複製全文</a>
        </div>
      </div>
    </footer>

  </div>

  <!-- Client-side Logic Script -->
  <script>
    // Security Passcode Hash (SHA-256 of passcode)
    const AUTH_HASH = "5cae49b1fea5b5b969cdc931b8338968940c92309aa2339360cdd5c77be4a4ff";
    const AUTH_STORAGE_KEY = "xmas_v4_auth_token";

    // 30 Effects Data
    const EFFECTS_DATA = {effects_json_str};
    const FULL_PROMPT_TEXT = {escaped_full_markdown};

    // Web Audio Sound Engine (pure Web Audio API)
    let audioCtx = null;
    let soundEnabled = true;

    function initAudio() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}
    }}

    function playChime(freq = 880, type = 'sine', duration = 0.4) {{
      if (!soundEnabled) return;
      try {{
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{}}
    }}

    function playChristmasBell() {{
      if (!soundEnabled) return;
      playChime(1046.5, 'triangle', 0.5); // C6
      setTimeout(() => playChime(1318.5, 'sine', 0.6), 80); // E6
      setTimeout(() => playChime(1567.98, 'sine', 0.8), 160); // G6
    }}

    function toggleSound() {{
      soundEnabled = !soundEnabled;
      document.getElementById('soundIcon').innerText = soundEnabled ? '🔔' : '🔕';
      document.getElementById('soundLabel').innerText = soundEnabled ? '音效: 開' : '音效: 關';
      if (soundEnabled) playChristmasBell();
      showToast(soundEnabled ? '聖誕互動音效已開啟' : '互動音效已靜音');
    }}

    // Snowfall Canvas Engine
    let snowRunning = true;
    let snowCanvas, snowCtx, flakes = [];

    function initSnow() {{
      snowCanvas = document.getElementById('snowCanvas');
      snowCtx = snowCanvas.getContext('2d');
      resizeSnow();
      window.addEventListener('resize', resizeSnow);

      flakes = [];
      const count = window.innerWidth < 768 ? 45 : 85;
      for (let i = 0; i < count; i++) {{
        flakes.push({{
          x: Math.random() * snowCanvas.width,
          y: Math.random() * snowCanvas.height,
          r: Math.random() * 3 + 1,
          d: Math.random() * count,
          speed: Math.random() * 0.8 + 0.4,
          drift: Math.random() * 0.5 - 0.25
        }});
      }}
      requestAnimationFrame(renderSnow);
    }}

    function resizeSnow() {{
      if (!snowCanvas) return;
      snowCanvas.width = window.innerWidth;
      snowCanvas.height = window.innerHeight;
    }}

    function renderSnow() {{
      if (!snowRunning) return;
      snowCtx.clearRect(0, 0, snowCanvas.width, snowCanvas.height);
      snowCtx.fillStyle = 'rgba(255, 255, 255, 0.75)';
      snowCtx.beginPath();
      for (let i = 0; i < flakes.length; i++) {{
        const f = flakes[i];
        snowCtx.moveTo(f.x, f.y);
        snowCtx.arc(f.x, f.y, f.r, 0, Math.PI * 2, true);
        
        f.y += f.speed;
        f.x += f.drift;
        if (f.y > snowCanvas.height) {{
          f.y = -5;
          f.x = Math.random() * snowCanvas.width;
        }}
        if (f.x > snowCanvas.width) f.x = 0;
        if (f.x < 0) f.x = snowCanvas.width;
      }}
      snowCtx.fill();
      requestAnimationFrame(renderSnow);
    }}

    function toggleSnow() {{
      snowRunning = !snowRunning;
      document.getElementById('snowIcon').innerText = snowRunning ? '❄️' : '⏹️';
      document.getElementById('snowLabel').innerText = snowRunning ? '飄雪: 開' : '飄雪: 關';
      if (snowRunning) {{
        renderSnow();
        showToast('飄雪動畫已開啟');
      }} else {{
        snowCtx.clearRect(0, 0, snowCanvas.width, snowCanvas.height);
        showToast('飄雪動畫已暫停');
      }}
    }}

    // Security Gate Management
    async function sha256(str) {{
      const buf = new TextEncoder().encode(str);
      const digest = await crypto.subtle.digest('SHA-256', buf);
      return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
    }}

    async function handleAuthSubmit(e) {{
      e.preventDefault();
      const input = document.getElementById('accessPassInput').value.trim();
      const hash = await sha256(input);
      if (hash === AUTH_HASH) {{
        localStorage.setItem(AUTH_STORAGE_KEY, hash);
        document.getElementById('authGateModal').classList.add('opacity-0', 'pointer-events-none');
        setTimeout(() => {{
          document.getElementById('authGateModal').classList.add('hidden');
        }}, 300);
        playChristmasBell();
        showToast('🎉 研習專屬資源驗證成功！');
      }} else {{
        document.getElementById('authErrorMsg').classList.remove('hidden');
        document.getElementById('accessPassInput').classList.add('border-red-500');
        playChime(300, 'sawtooth', 0.2);
      }}
    }}

    function checkAuthOnLoad() {{
      const saved = localStorage.getItem(AUTH_STORAGE_KEY);
      if (saved === AUTH_HASH) {{
        document.getElementById('authGateModal').classList.add('hidden');
      }} else {{
        document.getElementById('authGateModal').classList.remove('hidden');
      }}
    }}

    function lockSystem() {{
      localStorage.removeItem(AUTH_STORAGE_KEY);
      document.getElementById('authErrorMsg').classList.add('hidden');
      document.getElementById('accessPassInput').value = '';
      document.getElementById('accessPassInput').classList.remove('border-red-500');
      document.getElementById('authGateModal').classList.remove('hidden', 'opacity-0', 'pointer-events-none');
      showToast('🔒 系統已安全鎖定');
    }}

    // Tabs Switching
    function switchTab(tabKey) {{
      document.querySelectorAll('.tab-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.nav-tab').forEach(b => {{
        b.classList.remove('active');
        b.classList.add('text-slate-300');
      }});
      
      const targetView = document.getElementById('view-' + tabKey);
      const targetBtn = document.getElementById('tab-' + tabKey);
      if (targetView && targetBtn) {{
        targetView.classList.remove('hidden');
        targetBtn.classList.add('active');
        targetBtn.classList.remove('text-slate-300');
      }}
      playChime(1100, 'sine', 0.15);
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Chapter Card Toggle
    function toggleChapter(chId) {{
      const card = document.getElementById(chId);
      if (!card) return;
      const content = card.querySelector('.chapter-content');
      const arrow = card.querySelector('.toggle-btn svg');
      if (content.classList.contains('hidden')) {{
        content.classList.remove('hidden');
        arrow.classList.remove('rotate-180');
      }} else {{
        content.classList.add('hidden');
        arrow.classList.add('rotate-180');
      }}
      playChime(950, 'sine', 0.1);
    }}

    function expandAllChapters() {{
      document.querySelectorAll('.chapter-card .chapter-content').forEach(c => c.classList.remove('hidden'));
      document.querySelectorAll('.chapter-card .toggle-btn svg').forEach(a => a.classList.remove('rotate-180'));
      playChime(1200, 'sine', 0.2);
      showToast('已全部展開 25 章內容');
    }}

    function collapseAllChapters() {{
      document.querySelectorAll('.chapter-card .chapter-content').forEach(c => c.classList.add('hidden'));
      document.querySelectorAll('.chapter-card .toggle-btn svg').forEach(a => a.classList.add('rotate-180'));
      playChime(800, 'sine', 0.2);
      showToast('已全部收合 25 章內容');
    }}

    function jumpToChapter(chId) {{
      const el = document.getElementById(chId);
      if (!el) return;
      el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      const content = el.querySelector('.chapter-content');
      if (content && content.classList.contains('hidden')) {{
        toggleChapter(chId);
      }}
    }}

    function filterChapters() {{
      const q = document.getElementById('chapterSearchInput').value.trim().toLowerCase();
      document.querySelectorAll('.chapter-card').forEach(card => {{
        const title = card.getAttribute('data-chapter-title').toLowerCase();
        const text = card.innerText.toLowerCase();
        if (!q || title.includes(q) || text.includes(q)) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Toast Function
    let toastTimeout = null;
    function showToast(msg) {{
      const toast = document.getElementById('toast');
      const msgEl = document.getElementById('toastMsg');
      msgEl.innerText = msg;
      toast.classList.remove('translate-y-24', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-24', 'opacity-0');
      }}, 2600);
    }}

    // Copy Utilities
    function copyCustomText(text, successMsg = '已複製到剪貼簿') {{
      navigator.clipboard.writeText(text).then(() => {{
        playChristmasBell();
        showToast(successMsg);
      }}).catch(() => {{
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        playChristmasBell();
        showToast(successMsg);
      }});
    }}

    function copyElementText(elId, successMsg) {{
      const el = document.getElementById(elId);
      if (el) {{
        copyCustomText(el.innerText, successMsg);
      }}
    }}

    function copyMasterPrompt() {{
      copyCustomText(FULL_PROMPT_TEXT, '🎁 已成功複製 25 章完整正式提示詞！');
    }}

    // Studio Prompt Generator Engine
    function updatePromptOutput() {{
      const engine = document.getElementById('opt_engine').value;
      const people = document.getElementById('opt_people').value;
      const lock = document.getElementById('opt_lock').value;
      const style = document.getElementById('opt_style').value;
      const medium = document.getElementById('opt_medium').value;
      const scene = document.getElementById('opt_scene').value;
      const costume = document.getElementById('opt_costume').value;
      const pos = document.getElementById('opt_position').value;
      const effectCode = document.getElementById('opt_effect').value;
      const firstRatio = document.getElementById('opt_first_ratio').value;
      const videoRatio = document.getElementById('opt_video_ratio').value;
      const duration = document.getElementById('opt_duration').value;
      const platform = document.getElementById('opt_platform').value;
      const drama = document.getElementById('opt_drama').value;
      const comm = document.getElementById('opt_commercial').value;
      const phase = document.getElementById('opt_phase').value;
      const notes = document.getElementById('opt_notes').value;

      // Find effect object
      const effectObj = EFFECTS_DATA.find(e => e[0] === effectCode) || EFFECTS_DATA[4];

      // Summary
      const summaryText = `專案：聖誕魔法宇宙 V4.0
系統版本：V4.0 Ultimate Commercial Cinema Edition
引擎模式：${{engine}}
人物設定：${{people}} (鎖定狀態: ${{lock === 'ON' ? '開啟 (男主依照片+六女神獨立卡)' : 'AI 原創角色'}})
視覺畫風：${{style}}
人物媒材：${{medium}}
場景環境：${{scene}}
服裝配置：${{costume}}
站位安排：${{pos}}
核心特效：#${{effectCode}} ${{effectObj[1]}}
首幀比例：${{firstRatio}} ｜ 影片規格：${{videoRatio}} (${{duration}})
目標平台：${{platform}}
商業目標：${{comm}}
執行階段：${{phase}}
補充備註：${{notes}}`;

      document.getElementById('output_summary').innerText = summaryText;

      // Positive Image Prompt (First Frame)
      let promptImg = `Cinematic first frame, masterwork, 8k resolution, ${{medium === '3D_ANIMATION' ? 'high quality 3D animated cinema film style' : medium === 'LIVE_ACTION' ? 'cinematic live-action photography with realistic skin texture' : '3D stylized cute chibi claymation'}}, winter Christmas holiday wonderland. `;
      if (people === '7P') {{
        promptImg += `Seven adult characters in harmonious Christmas setting: one unique handsome adult male protagonist in center (M01), surrounded by six distinct adult female goddesses (F01-F06), each with unique recognizable facial features and graceful hairstyles. Standard composition: four in back row, two in front sides, male protagonist centered, all faces clearly visible without obstruction. `;
      }} else {{
        promptImg += `Main adult characters posing naturally for holiday portrait. `;
      }}

      if (style.includes('PURPLE')) {{
        promptImg += `Color palette of dreamy pastel purple, lilac, soft icy blue, champagne gold and pearl white. `;
      }} else if (style.includes('BLACKGOLD')) {{
        promptImg += `Opulent royal black and gold aesthetic, deep crimson accents, luxurious baroque trim. `;
      }} else {{
        promptImg += `Warm holiday cinematic ambient lighting, festive glowing bokeh. `;
      }}

      promptImg += `Wearing ${{costume === 'ROYAL_ICE' ? 'luxurious royal ice crystal Christmas attire with white fur trim and golden snowflake embroidery' : 'classic crimson velvet and fur-trimmed festive attire'}}. Setting in dreamy magical snow-covered pine forest with a monumental Christmas tree softly glowing in the background, suspended starlight, atmospheric aurora glow. Initial stable state before dynamic magical burst, calm happy expressions, --ar ${{firstRatio}}`;
      
      document.getElementById('output_positive_img').innerText = promptImg;

      // Positive Video Motion Prompt
      let promptVideo = `Continuous cinematic motion, ${{duration}}, starting precisely from the stable first frame. Camera gently tracks forward with subtle ascending tilt. The giant Christmas tree begins sequentially igniting tiers of twinkling lights, leading to: ${{effectObj[4]}}. Characters naturally look up and around with joyful, enchanted smiles and subtle holiday interactions. Zero facial distortion, seamless character identity preservation, no subtitles, no watermark, smooth 60fps cinematic fluidity, resolving into a stable final keyframe.`;
      
      document.getElementById('output_positive_video').innerText = promptVideo;

      // 10s Timeline
      const timelineHtml = `
        <div class="flex items-center gap-2"><span class="text-amber-400 font-bold w-16">0～2 秒</span><span class="text-slate-300">穩定首幀開場：七人站位定格，溫暖微光浮動，確認身份一致</span></div>
        <div class="flex items-center gap-2"><span class="text-emerald-400 font-bold w-16">2～4 秒</span><span class="text-slate-300">角色互動：男主與女神眼神交會微笑，聖誕樹底層燈飾預備</span></div>
        <div class="flex items-center gap-2"><span class="text-sky-400 font-bold w-16">4～7 秒</span><span class="text-amber-300 font-semibold">特效高潮：${{effectObj[1]}}（${{effectObj[2]}}）華麗綻放</span></div>
        <div class="flex items-center gap-2"><span class="text-purple-400 font-bold w-16">7～9 秒</span><span class="text-slate-300">驚喜反饋：微風吹拂髮絲，光塵灑落肩膀，角色自然讚嘆</span></div>
        <div class="flex items-center gap-2"><span class="text-pink-400 font-bold w-16">9～10 秒</span><span class="text-slate-300">穩定尾幀：光芒回歸溫馨常駐，保留供次幕銜接之穩定畫面</span></div>
      `;
      document.getElementById('output_timeline').innerHTML = timelineHtml;
    }}

    function selectEffect(code, name, promptEn) {{
      const select = document.getElementById('opt_effect');
      if (select) {{
        select.value = code;
        updatePromptOutput();
        switchTab('studio');
        showToast(`已載入特效 #${{code}}：${{name}}`);
        playChristmasBell();
      }}
    }}

    function loadDefaultProjectPreset() {{
      document.getElementById('opt_engine').value = 'ABC';
      document.getElementById('opt_people').value = '7P';
      document.getElementById('opt_lock').value = 'ON';
      document.getElementById('opt_style').value = '05_PURPLE';
      document.getElementById('opt_medium').value = '3D_ANIMATION';
      document.getElementById('opt_scene').value = 'MAGIC_FOREST';
      document.getElementById('opt_costume').value = 'ROYAL_ICE';
      document.getElementById('opt_position').value = 'FOUR_BACK_TWO_FRONT';
      document.getElementById('opt_effect').value = '05';
      document.getElementById('opt_first_ratio').value = '4:5';
      document.getElementById('opt_video_ratio').value = '9:16';
      document.getElementById('opt_duration').value = '10s';
      document.getElementById('opt_platform').value = 'Grok Imagine';
      document.getElementById('opt_drama').value = 'FEATURED';
      document.getElementById('opt_commercial').value = 'NONE';
      document.getElementById('opt_phase').value = 'PHASE1';
      document.getElementById('opt_notes').value = '粉紫金色極光反光，無字幕無浮水印';
      
      updatePromptOutput();
      playChristmasBell();
      showToast('✨ 已載入第二十二章官方預設專案：七人聖誕魔法森林！');
    }}

    function resetStudioForm() {{
      loadDefaultProjectPreset();
    }}

    // Init on Page Load
    window.addEventListener('DOMContentLoaded', () => {{
      checkAuthOnLoad();
      initSnow();
      loadDefaultProjectPreset();
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated index.html successfully!")
