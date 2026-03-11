#!/usr/bin/env python3
import re

# 定义每个页面的内容
pages_content = {
    'lesson1-5.html': {
        'title': '1.5 连接软件',
        'subtitle': '连接 Telegram、飞书、QQ、WhatsApp',
        'active': 'lesson1-5.html',
        'content': '''
            <div class="card">
                <h3>📱 支持的通讯软件</h3>
                <p>OpenClaw 支持多种通讯软件，选择你常用的平台连接：</p>
                <ul style="margin: 15px 0 15px 30px;">
                    <li><strong>Telegram</strong> - 最推荐，功能最完整</li>
                    <li><strong>飞书</strong> - 企业办公首选</li>
                    <li><strong>QQ</strong> - 国内用户友好</li>
                    <li><strong>WhatsApp</strong> - 国际用户常用</li>
                </ul>
            </div>
            
            <div class="card">
                <h3>🤖 连接 Telegram</h3>
                
                <p><strong>步骤 1：创建 Bot</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li>在 Telegram 搜索 <code>@BotFather</code></li>
                    <li>发送 <code>/newbot</code></li>
                    <li>按提示设置 Bot 名称和用户名</li>
                    <li>保存 Bot Token（格式：<code>123456:ABC-DEF...</code>）</li>
                </ol>
                
                <p style="margin-top: 20px;"><strong>步骤 2：获取 User ID</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li>在 Telegram 搜索 <code>@userinfobot</code></li>
                    <li>发送任意消息</li>
                    <li>保存你的 User ID（纯数字）</li>
                </ol>
                
                <p style="margin-top: 20px;"><strong>步骤 3：配置 OpenClaw</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 编辑配置文件
nano ~/.openclaw/config.json

# 添加 Telegram 配置：
{
  "telegram": {
    "token": "123456:ABC-DEF-your-bot-token",
    "allowedUsers": [123456789]
  }
}

# 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>🚀 连接飞书</h3>
                
                <p><strong>步骤 1：创建飞书应用</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li>访问 <a href="https://open.feishu.cn/" target="_blank" style="color: #667eea;">飞书开放平台</a></li>
                    <li>创建企业自建应用</li>
                    <li>获取 App ID 和 App Secret</li>
                    <li>配置机器人权限和回调地址</li>
                </ol>
                
                <p style="margin-top: 20px;"><strong>步骤 2：配置 OpenClaw</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 编辑配置文件
nano ~/.openclaw/config.json

# 添加飞书配置：
{
  "feishu": {
    "appId": "your-app-id",
    "appSecret": "your-app-secret"
  }
}

# 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>💬 连接 QQ</h3>
                
                <p><strong>步骤 1：安装 go-cqhttp</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 下载 go-cqhttp
wget https://github.com/Mrs4s/go-cqhttp/releases/latest/download/go-cqhttp_linux_amd64.tar.gz
tar -xzf go-cqhttp_linux_amd64.tar.gz

# 运行并配置
./go-cqhttp</code></pre>
                
                <p style="margin-top: 20px;"><strong>步骤 2：配置 OpenClaw</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 编辑配置文件
nano ~/.openclaw/config.json

# 添加 QQ 配置：
{
  "qq": {
    "host": "127.0.0.1",
    "port": 5700,
    "allowedUsers": [123456789]
  }
}

# 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>📞 连接 WhatsApp</h3>
                
                <p><strong>步骤 1：扫码登录</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 启动 WhatsApp 连接
openclaw whatsapp connect

# 会显示二维码，用 WhatsApp 扫码登录</code></pre>
                
                <p style="margin-top: 20px;"><strong>步骤 2：验证连接</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 查看连接状态
openclaw whatsapp status

# 发送测试消息
openclaw whatsapp send "Hello from OpenClaw!"</code></pre>
            </div>
            
            <div style="background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); border-left: 5px solid #28a745; padding: 20px; border-radius: 8px;">
                <strong>✅ 连接完成！</strong><br>
                选择你常用的平台连接，就可以随时随地和 AI 助手对话了。
            </div>
        '''
    },
    
    'lesson2-1.html': {
        'title': '2.1 权限问题',
        'subtitle': 'OpenClaw 常见权限问题及解决方案',
        'active': 'lesson2-1.html',
        'content': '''
            <div class="card">
                <h3>❌ 问题 1：npm 安装权限错误</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: EACCES: permission denied, access '/usr/local/lib/node_modules'</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案 1：修改 npm 全局目录（推荐）</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g openclaw</code></pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案 2：使用 sudo（不推荐）</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>sudo npm install -g openclaw</code></pre>
            </div>
            
            <div class="card">
                <h3>❌ 问题 2：工作空间权限错误</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: EACCES: permission denied, mkdir '~/.openclaw/workspace'</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：修复目录权限</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 修复 OpenClaw 目录权限
sudo chown -R $USER:$USER ~/.openclaw
chmod -R 755 ~/.openclaw

# 重新初始化
openclaw init</code></pre>
            </div>
            
            <div class="card">
                <h3>❌ 问题 3：配置文件无法写入</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: EACCES: permission denied, open '~/.openclaw/config.json'</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：修复文件权限</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 修复配置文件权限
chmod 600 ~/.openclaw/config.json
chmod 600 ~/.openclaw/gateway.json

# 如果文件不存在，重新创建
openclaw init</code></pre>
            </div>
            
            <div class="card">
                <h3>❌ 问题 4：Gateway 启动权限错误</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: listen EACCES: permission denied 0.0.0.0:80</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：使用非特权端口</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 编辑 Gateway 配置
nano ~/.openclaw/gateway.json

# 修改端口为 1024 以上（如 18789）
{
  "port": 18789
}

# 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>❌ 问题 5：技能安装权限错误</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: EACCES: permission denied, mkdir '~/.openclaw/workspace/skills'</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：创建技能目录</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 创建技能目录
mkdir -p ~/.openclaw/workspace/skills
chmod 755 ~/.openclaw/workspace/skills

# 重新安装技能
clawhub install memory-master</code></pre>
            </div>
            
            <div style="background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%); border-left: 5px solid #17a2b8; padding: 20px; border-radius: 8px;">
                <strong>💡 预防权限问题：</strong>
                <ul style="margin-top: 10px;">
                    <li>始终使用普通用户运行 OpenClaw，避免 root</li>
                    <li>定期检查目录权限：<code>ls -la ~/.openclaw</code></li>
                    <li>使用 npm 全局目录而不是 sudo</li>
                </ul>
            </div>
        '''
    },
    
    'lesson2-2.html': {
        'title': '2.2 端口占用',
        'subtitle': 'OpenClaw 常用端口及占用解决方案',
        'active': 'lesson2-2.html',
        'content': '''
            <div class="card">
                <h3>🚪 OpenClaw 常用端口</h3>
                <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                    <thead>
                        <tr style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                            <th style="padding: 15px; text-align: left;">端口</th>
                            <th style="padding: 15px; text-align: left;">用途</th>
                            <th style="padding: 15px; text-align: left;">说明</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e0e0e0;">
                            <td style="padding: 15px;"><code>18789</code></td>
                            <td style="padding: 15px;">Gateway 主端口</td>
                            <td style="padding: 15px;">默认 HTTP 服务端口</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e0e0e0;">
                            <td style="padding: 15px;"><code>18790</code></td>
                            <td style="padding: 15px;">WebSocket 端口</td>
                            <td style="padding: 15px;">实时通信</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e0e0e0;">
                            <td style="padding: 15px;"><code>5700</code></td>
                            <td style="padding: 15px;">QQ Bot 端口</td>
                            <td style="padding: 15px;">go-cqhttp 默认端口</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e0e0e0;">
                            <td style="padding: 15px;"><code>3000</code></td>
                            <td style="padding: 15px;">Web UI 端口</td>
                            <td style="padding: 15px;">可选的 Web 界面</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="card">
                <h3>❌ 问题：端口被占用</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: listen EADDRINUSE: address already in use :::18789</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案 1：查找并关闭占用进程</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 查看端口占用
lsof -i :18789

# 或使用 netstat
netstat -tulpn | grep 18789

# 杀死占用进程（替换 PID）
kill -9 [PID]

# 重启 Gateway
openclaw gateway restart</code></pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案 2：修改端口</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 编辑 Gateway 配置
nano ~/.openclaw/gateway.json

# 修改端口
{
  "port": 18791,
  "host": "127.0.0.1"
}

# 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>🔍 检查端口状态</h3>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># 查看所有监听端口
netstat -tulpn | grep LISTEN

# 查看 OpenClaw 相关端口
lsof -i -P | grep openclaw

# 测试端口是否可用
nc -zv 127.0.0.1 18789</code></pre>
            </div>
            
            <div class="card">
                <h3>🛡️ 防火墙配置</h3>
                <p>如果需要外部访问 OpenClaw，需要开放端口：</p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 15px 0;"><code># Ubuntu/Debian (ufw)
sudo ufw allow 18789/tcp
sudo ufw reload

# CentOS/RHEL (firewalld)
sudo firewall-cmd --add-port=18789/tcp --permanent
sudo firewall-cmd --reload</code></pre>
                
                <p style="margin-top: 20px;"><strong>⚠️ 安全提醒：</strong>不建议将 Gateway 暴露到公网，建议只绑定 127.0.0.1</p>
            </div>
            
            <div style="background: linear-gradient(135deg, #fff3cd 0%, #ffe69c 100%); border-left: 5px solid #ffc107; padding: 20px; border-radius: 8px;">
                <strong>💡 最佳实践：</strong>
                <ul style="margin-top: 10px;">
                    <li>使用默认端口 18789，避免冲突</li>
                    <li>只绑定 127.0.0.1，不暴露到公网</li>
                    <li>定期检查端口占用情况</li>
                    <li>使用反向代理（Nginx）处理外部访问</li>
                </ul>
            </div>
        '''
    },
    
    'lesson2-4.html': {
        'title': '2.4 Telegram 问题',
        'subtitle': 'Telegram Bot 连接常见问题',
        'active': 'lesson2-4.html',
        'content': '''
            <div class="card">
                <h3>❌ 问题 1：Bot 无响应</h3>
                <p><strong>症状：</strong>发送消息后 Bot 没有任何回复</p>
                
                <p style="margin-top: 20px;"><strong>✅ 排查步骤：</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li><strong>检查 Gateway 状态</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>openclaw gateway status</code></pre>
                    </li>
                    <li><strong>查看日志</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>openclaw gateway logs -f</code></pre>
                    </li>
                    <li><strong>验证 Bot Token</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 测试 Token 是否有效
curl https://api.telegram.org/bot[YOUR_TOKEN]/getMe</code></pre>
                    </li>
                    <li><strong>检查 User ID</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 在 Telegram 搜索 @userinfobot 获取正确的 User ID</code></pre>
                    </li>
                </ol>
            </div>
            
            <div class="card">
                <h3>❌ 问题 2：Bot Token 无效</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: 401 Unauthorized</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li>确认 Token 格式正确（<code>123456:ABC-DEF...</code>）</li>
                    <li>检查 Token 是否过期或被撤销</li>
                    <li>重新生成 Token：
                        <ul style="margin: 10px 0 10px 20px;">
                            <li>找 @BotFather</li>
                            <li>发送 <code>/mybots</code></li>
                            <li>选择你的 Bot</li>
                            <li>点击 "API Token" → "Regenerate"</li>
                        </ul>
                    </li>
                    <li>更新配置文件并重启 Gateway</li>
                </ol>
            </div>
            
            <div class="card">
                <h3>❌ 问题 3：User ID 不匹配</h3>
                <p><strong>症状：</strong>Bot 收到消息但不回复，日志显示 "User not allowed"</p>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：</strong></p>
                <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 1. 获取正确的 User ID
# 在 Telegram 搜索 @userinfobot，发送任意消息

# 2. 更新配置文件
nano ~/.openclaw/config.json

# 3. 确保 User ID 是数字，不是字符串
{
  "telegram": {
    "token": "your-token",
    "allowedUsers": [123456789]  # 注意：是数字，不是 "123456789"
  }
}

# 4. 重启 Gateway
openclaw gateway restart</code></pre>
            </div>
            
            <div class="card">
                <h3>❌ 问题 4：网络连接失败</h3>
                <p><strong>错误信息：</strong></p>
                <pre style="background: #1e1e1e; color: #ff6b6b; padding: 15px; border-radius: 8px;">Error: connect ETIMEDOUT api.telegram.org:443</pre>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li><strong>检查网络连接</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>ping api.telegram.org
curl https://api.telegram.org</code></pre>
                    </li>
                    <li><strong>配置代理（如果需要）</strong>
                        <pre style="background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code># 编辑配置文件
nano ~/.openclaw/config.json

# 添加代理配置
{
  "telegram": {
    "token": "your-token",
    "allowedUsers": [123456789],
    "proxy": {
      "host": "127.0.0.1",
      "port": 1080,
      "type": "socks5"
    }
  }
}</code></pre>
                    </li>
                </ol>
            </div>
            
            <div class="card">
                <h3>❌ 问题 5：消息延迟</h3>
                <p><strong>症状：</strong>发送消息后，Bot 过很久才回复</p>
                
                <p style="margin-top: 20px;"><strong>✅ 解决方案：</strong></p>
                <ol style="margin: 15px 0 15px 30px;">
                    <li>检查服务器负载：<code>top</code> 或 <code>htop</code></li>
                    <li>检查网络延迟：<code>ping api.telegram.org</code></li>
                    <li>增加 Gateway 资源限制</li>
                    <li>优化 API Key 配额（如果使用付费 API）</li>
                </ol>
            </div>
            
            <div style="background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%); border-left: 5px solid #17a2b8; padding: 20px; border-radius: 8px;">
                <strong>💡 调试技巧：</strong>
                <ul style="margin-top: 10px;">
                    <li>始终先查看日志：<code>openclaw gateway logs -f</code></li>
                    <li>使用 @BotFather 的 <code>/mybots</code> 检查 Bot 状态</li>
                    <li>测试 Token：<code>curl https://api.telegram.org/bot[TOKEN]/getMe</code></li>
                    <li>确认 User ID 是数字类型，不是字符串</li>
                </ul>
            </div>
        '''
    }
}

# 读取模板
with open('lesson1-4.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 为每个页面生成内容
for filename, data in pages_content.items():
    content = template
    
    # 替换标题
    content = re.sub(r'<title>[^<]+</title>', f'<title>{data["title"]} | OpenClaw 教程</title>', content)
    content = re.sub(r'<h2>[^<]+</h2>', f'<h2>{data["title"]}</h2>', content, count=1)
    content = re.sub(r'<p>([^<]*)</p>', f'<p>{data["subtitle"]}</p>', content, count=1)
    
    # 替换 active 状态
    content = re.sub(r'lesson1-4\.html" class="active"', f'{data["active"]}" class="active"', content)
    
    # 替换主要内容
    content = re.sub(
        r'<div class="card">.*?<div class="nav-buttons">',
        data["content"] + '\n            <div class="nav-buttons">',
        content,
        flags=re.DOTALL
    )
    
    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 生成完成：{filename}')

print('\n所有页面生成完成！')
