#!/usr/bin/env python3
import re

# 新的侧边栏 HTML（带折叠功能）
sidebar_html = '''        <nav class="sidebar">
            <div class="sidebar-section">
                <div class="sidebar-title {lesson1_expanded}" onclick="toggleMenu('lesson1')">
                    <span>📚 第一课：安装</span>
                    <span class="arrow">▶</span>
                </div>
                <ul class="sidebar-menu {lesson1_show}" id="lesson1">
                    <li><a href="lesson1-1.html" {active_1_1}><span class="icon">📦</span>1.1 环境准备</a></li>
                    <li><a href="lesson1-2.html" {active_1_2}><span class="icon">🔧</span>1.2 安装 OpenClaw</a></li>
                    <li><a href="lesson1-3.html" {active_1_3}><span class="icon">⚙️</span>1.3 初始化配置</a></li>
                    <li><a href="#"><span class="icon">🎯</span>1.4 安装技能（待添加）</a></li>
                    <li><a href="#"><span class="icon">📱</span>1.5 连接 Telegram（待添加）</a></li>
                </ul>
            </div>
            
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleMenu('lesson2')">
                    <span>🐛 第二课：问题</span>
                    <span class="arrow">▶</span>
                </div>
                <ul class="sidebar-menu" id="lesson2">
                    <li><a href="#"><span class="icon">🔑</span>2.1 权限问题（待添加）</a></li>
                    <li><a href="#"><span class="icon">🚪</span>2.2 端口占用（待添加）</a></li>
                    <li><a href="#"><span class="icon">🔐</span>2.3 API Key 问题（待添加）</a></li>
                    <li><a href="#"><span class="icon">🤖</span>2.4 Telegram 问题（待添加）</a></li>
                    <li><a href="#"><span class="icon">💾</span>2.5 其他问题（待添加）</a></li>
                </ul>
            </div>
            
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleMenu('lesson3')">
                    <span>💡 第三课：实践</span>
                    <span class="arrow">▶</span>
                </div>
                <ul class="sidebar-menu" id="lesson3">
                    <li><a href="#"><span class="icon">💡</span>3.1 使用心得（待添加）</a></li>
                    <li><a href="#"><span class="icon">🎨</span>3.2 创意玩法（待添加）</a></li>
                    <li><a href="#"><span class="icon">🔧</span>3.3 进阶技巧（待添加）</a></li>
                </ul>
            </div>
            
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleMenu('advanced')">
                    <span>🚀 进阶内容</span>
                    <span class="arrow">▶</span>
                </div>
                <ul class="sidebar-menu" id="advanced">
                    <li><a href="#"><span class="icon">🛠️</span>技能开发（敬请期待）</a></li>
                    <li><a href="#"><span class="icon">🤖</span>自动化实战（敬请期待）</a></li>
                    <li><a href="#"><span class="icon">🔐</span>安全加固（敬请期待）</a></li>
                </ul>
            </div>
            
            <div class="sidebar-other">
                <a href="tutorial.html"><span class="icon">📚</span>教程首页</a>
                <a href="index.html"><span class="icon">🏠</span>返回首页</a>
            </div>
        </nav>'''

# JavaScript 代码
js_code = '''    <script>
        function toggleMenu(id) {
            const menu = document.getElementById(id);
            const title = event.currentTarget;
            
            if (menu.classList.contains('show')) {
                menu.classList.remove('show');
                title.classList.remove('expanded');
            } else {
                menu.classList.add('show');
                title.classList.add('expanded');
            }
        }
    </script>'''

pages = {
    'lesson1-2.html': {'active_1_2': 'class="active"', 'lesson1_expanded': 'expanded', 'lesson1_show': 'show'},
    'lesson1-3.html': {'active_1_3': 'class="active"', 'lesson1_expanded': 'expanded', 'lesson1_show': 'show'},
    'tutorial.html': {'lesson1_expanded': '', 'lesson1_show': ''}
}

for filename, replacements in pages.items():
    # 设置默认值
    rep = {
        'active_1_1': '',
        'active_1_2': '',
        'active_1_3': '',
        'lesson1_expanded': '',
        'lesson1_show': ''
    }
    rep.update(replacements)
    
    # 读取文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换侧边栏
    new_sidebar = sidebar_html.format(**rep)
    content = re.sub(r'<nav class="sidebar">.*?</nav>', new_sidebar, content, flags=re.DOTALL)
    
    # 添加 JavaScript（如果没有）
    if 'function toggleMenu' not in content:
        content = content.replace('</body>', js_code + '\n</body>')
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 更新完成：{filename}')

print('\n所有页面更新完成！')
