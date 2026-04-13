import os
import glob
import re

TARGET_DIR = r"c:\Users\ASUS\OneDrive\Desktop\skilizee\best-delegate"

# Mappings of exact strings / emojis to Font Awesome equivalents
MAPPING = {
    # Fullscreen
    "â›¶": '<i class="fa-solid fa-expand"></i>',
    "⛶": '<i class="fa-solid fa-expand"></i>',
    
    # Back to Top
    "&uarr;": '<i class="fa-solid fa-arrow-up"></i>',
    
    # Notes Toggle 
    "ðŸ“  Notes": '<i class="fa-solid fa-clipboard-list"></i> Notes',
    "📝 Notes": '<i class="fa-solid fa-clipboard-list"></i> Notes',
    
    # 1.1 and general
    "ðŸŒ ": '<i class="fa-solid fa-globe"></i>',
    "🌐": '<i class="fa-solid fa-globe"></i>',
    
    "ðŸª‘": '<i class="fa-solid fa-chair"></i>',
    "🪑": '<i class="fa-solid fa-chair"></i>',
    
    "ðŸ‘‘": '<i class="fa-solid fa-crown"></i>',
    "👑": '<i class="fa-solid fa-crown"></i>',
    
    "ðŸ‡ºðŸ‡³": '<i class="fa-solid fa-flag"></i>',
    "🇺🇳": '<i class="fa-solid fa-flag"></i>',
    
    "ðŸ”„": '<i class="fa-solid fa-rotate"></i>',
    "🔄": '<i class="fa-solid fa-rotate"></i>',
    
    "ðŸ¤ ": '<i class="fa-regular fa-handshake"></i>',
    "🤝": '<i class="fa-regular fa-handshake"></i>',
    
    "âš¡": '<i class="fa-solid fa-bolt"></i>',
    "⚡": '<i class="fa-solid fa-bolt"></i>',
    
    "â˜…": '<i class="fa-solid fa-star"></i>',
    "★": '<i class="fa-solid fa-star"></i>',
    
    "âœ¦": '<i class="fa-solid fa-sparkles"></i>',
    "✦": '<i class="fa-solid fa-sparkles"></i>',
    
    "ðŸ“ ": '<i class="fa-solid fa-clipboard-list"></i>',
    "📝": '<i class="fa-solid fa-clipboard-list"></i>',
    
    # 1.2 and others
    "🔍": '<i class="fa-solid fa-magnifying-glass"></i>',
    "🗣️": '<i class="fa-solid fa-bullhorn"></i>',
    "🎭": '<i class="fa-solid fa-masks-theater"></i>',
    "🛡️": '<i class="fa-solid fa-shield-halved"></i>',
    "📌": '<i class="fa-solid fa-thumbtack"></i>',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Add FontAwesome CDN if not present
    fa_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />'
    if fa_link not in content:
        # Find <script src="https://cdn.tailwindcss.com"></script> and inject it after
        if '<script src="https://cdn.tailwindcss.com"></script>' in content:
            content = content.replace(
                '<script src="https://cdn.tailwindcss.com"></script>',
                f'<script src="https://cdn.tailwindcss.com"></script>\n{fa_link}'
            )
        elif '<title>' in content:
            content = content.replace(
                '<title>',
                f'{fa_link}\n<title>'
            )

    # 2. String replacements
    # Sort mapping by length of key descending so longer strings (like "ðŸ“  Notes") are matched before "ðŸ“ "
    for k in sorted(MAPPING.keys(), key=len, reverse=True):
        content = content.replace(k, MAPPING[k])

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No changes for {os.path.basename(filepath)}")

html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))
for f in html_files:
    process_file(f)
