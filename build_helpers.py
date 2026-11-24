# -*- coding: utf-8 -*-
import json
import os

with open('chapters_data.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Format the 25 chapters into HTML cards
chapter_cards_html = []
for idx, ch in enumerate(chapters, 1):
    ch_id = f"ch-{idx:02d}"
    title = ch['title']
    
    body_parts = []
    plain_texts = [f"### {title}"]
    
    for item in ch['items']:
        itype = item['type']
        ihtml = item['html']
        itxt = item['text']
        
        plain_texts.append(itxt)
        
        if itype == 'sub_sub_header':
            body_parts.append(f'<h4 class="text-lg font-bold text-amber-300 mt-5 mb-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-amber-400 inline-block"></span>{ihtml}</h4>')
        elif itype == 'bulleted_list':
            body_parts.append(f'<li class="text-slate-300 leading-relaxed pl-1 marker:text-emerald-400">{ihtml}</li>')
        elif itype == 'numbered_list':
            body_parts.append(f'<li class="text-slate-300 leading-relaxed pl-1 list-decimal ml-5 marker:text-amber-400">{ihtml}</li>')
        elif itype == 'divider':
            body_parts.append('<hr class="border-slate-800 my-4" />')
        else:
            if itxt.strip():
                # check if it looks like an alert or quote
                if itxt.startswith('M01｜') or itxt.startswith('F0') or itxt.startswith('01｜') or itxt.startswith('02｜') or itxt.startswith('03｜') or itxt.startswith('04｜') or itxt.startswith('05｜') or itxt.startswith('06｜') or itxt.startswith('07｜') or itxt.startswith('08｜') or itxt.startswith('09｜') or itxt.startswith('10｜') or itxt.startswith('11｜') or itxt.startswith('12｜'):
                    body_parts.append(f'<div class="p-3 my-2 bg-slate-900/60 rounded-xl border border-slate-700/60 font-mono text-sm text-cyan-200">{ihtml}</div>')
                else:
                    body_parts.append(f'<p class="text-slate-300 leading-relaxed mb-3">{ihtml}</p>')
                    
    card_body_html = '\n'.join(body_parts)
    escaped_plain_text = json.dumps('\n'.join(plain_texts), ensure_ascii=False)
    
    card_html = f'''
    <div class="chapter-card bg-slate-900/80 backdrop-blur-md border border-slate-700/60 rounded-2xl p-6 shadow-xl transition-all hover:border-amber-400/50 hover:shadow-amber-500/10 mb-6" id="{ch_id}" data-chapter-index="{idx}">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-gradient-to-r from-red-600 to-amber-600 text-white shadow-sm">第 {idx:02d} 章</span>
          <h3 class="text-xl font-bold text-slate-100 tracking-wide">{title}</h3>
        </div>
        <div class="flex items-center gap-2">
          <button onclick='copyCustomText({escaped_plain_text}, "已複製 第{idx:02d}章 內容")' class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 hover:border-slate-500 transition-colors flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>
            複製此章
          </button>
          <button onclick="toggleChapter('{ch_id}')" class="toggle-btn p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-slate-200 transition-colors" title="收合/展開">
            <svg class="w-4 h-4 transform transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
        </div>
      </div>
      <div class="chapter-content text-slate-300">
        {card_body_html}
      </div>
    </div>
    '''
    chapter_cards_html.append(card_html)

all_chapters_html_str = '\n'.join(chapter_cards_html)

# Read full content markdown
with open('full_content.md', 'r', encoding='utf-8') as f:
    full_markdown_text = f.read()

escaped_full_markdown = json.dumps(full_markdown_text, ensure_ascii=False)

print(f"Generated HTML for {len(chapter_cards_html)} chapters.")
