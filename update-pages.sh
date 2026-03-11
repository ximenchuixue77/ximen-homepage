#!/bin/bash
# 批量更新页面，添加折叠菜单

PAGES=("lesson1-2.html" "lesson1-3.html" "tutorial.html")

for page in "${PAGES[@]}"; do
    # 读取原文件内容（主体部分）
    content=$(sed -n '/<main class="content">/,/<\/main>/p' "$page")
    
    # 使用 lesson1-1.html 作为模板
    cp lesson1-1.html "$page"
    
    # 根据不同页面修改 active 状态
    case "$page" in
        "lesson1-2.html")
            sed -i 's/lesson1-1.html" class="active"/lesson1-2.html" class="active"/g' "$page"
            ;;
        "lesson1-3.html")
            sed -i 's/lesson1-1.html" class="active"/lesson1-3.html" class="active"/g' "$page"
            ;;
        "tutorial.html")
            sed -i 's/lesson1-1.html" class="active"//g' "$page"
            ;;
    esac
done

echo "更新完成"
