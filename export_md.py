import json

with open('chapters_data.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

with open('full_content.md', 'w', encoding='utf-8') as out:
    for ch in chapters:
        out.write(f"# {ch['title']}\n\n")
        for it in ch['items']:
            t = it['type']
            txt = it['text']
            if t == 'sub_sub_header':
                out.write(f"\n### {txt}\n\n")
            elif t == 'bulleted_list':
                out.write(f"- {txt}\n")
            elif t == 'numbered_list':
                out.write(f"1. {txt}\n")
            elif t == 'divider':
                out.write("\n---\n\n")
            else:
                out.write(f"{txt}\n\n")
        out.write("\n---\n\n")

print("Written full_content.md successfully!")
