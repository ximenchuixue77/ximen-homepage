#!/usr/bin/env python3
import re

# 添加闪光效果的 CSS
shine_css = '''
        @keyframes shine {
            0% {
                background-position: -200% center;
            }
            100% {
                background-position: 200% center;
            }
        }
        
        .header h1 span {
            margin-left: 15px;
            font-size: 0.5em;
            background: linear-gradient(90deg, 
                rgba(255,255,255,0.3) 0%, 
                rgba(255,255,255,0.8) 50%, 
                rgba(255,255,255,0.3) 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shine 3s linear infinite;
            font-weight: bold;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
        }'''

files = ['lesson1-1.html', 'lesson1-2.html', 'lesson1-3.html', 'tutorial.html', 'index.html']

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换原有的 .header h1 span 样式
        content = re.sub(
            r'\.header h1 span \{[^}]+\}',
            shine_css.strip(),
            content,
            flags=re.DOTALL
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ 更新完成：{filename}')
    except FileNotFoundError:
        print(f'⚠️  文件不存在：{filename}')

print('\n闪光效果添加完成！')
