import json

with open('notion_raw_dump.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

root_id = '40be0d81-e9ca-818d-acaa-fd9df4eca4b3'

def get_val(bid):
    b = blocks.get(bid, {})
    v = b.get('value', {})
    if 'value' in v: v = v['value']
    return v

def format_title_html(title):
    if not title: return ''
    res = []
    for chunk in title:
        if isinstance(chunk, list):
            text = chunk[0]
            if len(chunk) > 1 and isinstance(chunk[1], list):
                for decor in chunk[1]:
                    if decor[0] == 'b':
                        text = f'<strong>{text}</strong>'
                    elif decor[0] == 'i':
                        text = f'<em>{text}</em>'
                    elif decor[0] == 'c':
                        text = f'<code>{text}</code>'
                    elif decor[0] == 'a':
                        text = f'<a href="{decor[1]}" target="_blank" rel="noopener">{text}</a>'
                    elif decor[0] == 'h':
                        text = f'<span class="highlight-{decor[1]}">{text}</span>'
            res.append(text)
    return ''.join(res)

def format_title_text(title):
    if not title: return ''
    res = []
    for chunk in title:
        if isinstance(chunk, list):
            res.append(chunk[0])
    return ''.join(res)

root_val = get_val(root_id)
content_ids = root_val.get('content', [])

chapters = []
cur_chapter = None

for cid in content_ids:
    val = get_val(cid)
    btype = val.get('type')
    title_html = format_title_html(val.get('properties', {}).get('title'))
    title_text = format_title_text(val.get('properties', {}).get('title'))
    
    if btype == 'sub_header':
        cur_chapter = {
            'id': cid,
            'title': title_text,
            'title_html': title_html,
            'items': []
        }
        chapters.append(cur_chapter)
    elif cur_chapter is not None:
        if btype == 'divider':
            cur_chapter['items'].append({'id': cid, 'type': 'divider', 'html': '<hr/>', 'text': '---'})
            continue
        cur_chapter['items'].append({
            'id': cid,
            'type': btype,
            'html': title_html,
            'text': title_text
        })

print(f'Extracted {len(chapters)} chapters.')
with open('chapters_data.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

for ch in chapters[:3]:
    print(f"=== {ch['title']} ===")
    for it in ch['items'][:4]:
        print(f"  [{it['type']}] {it['text'][:60]}...")
