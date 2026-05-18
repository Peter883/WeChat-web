import os
import webbrowser

html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>祝福</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            color: #333333;
            font-size: 3rem;
            text-align: center;
            padding: 1rem;
            font-family: 'Arial', sans-serif;
        }
        .emoji {
            font-size: 4rem;
        }
    </style>
</head>
<body>
    <div>
        天天开心吖<span class="emoji">🥰</span>
    </div>
</body>
</html>
'''

output_path = os.path.join(os.path.dirname(__file__), 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'✅ 已生成 HTML 文件：{output_path}')
print('✅ 页面已优化为微信友好版本。')
print('请将生成的 index.html 上传到可访问的 HTTPS 静态网站，再在微信中打开该链接。')
webbrowser.open_new_tab(output_path)
