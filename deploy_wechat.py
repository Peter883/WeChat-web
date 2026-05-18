#!/usr/bin/env python3
"""
微信直接打开部署脚本

此脚本会：
1. 生成微信友好的 HTML 页面
2. 初始化 Git 仓库
3. 提供 GitHub Pages 部署步骤

使用方法：
python deploy_wechat.py
"""

import os
import subprocess
import webbrowser
import shutil

def generate_html():
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
            color: #333;
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
        天天开心吖<span class="emoji">[坏笑]</span>
    </div>
</body>
</html>
'''

    output_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'✅ 已生成微信友好 HTML 文件：{output_path}')
    return output_path

def has_git():
    return shutil.which('git') is not None


def init_git_repo():
    if not has_git():
        print('⚠️ 未检测到 Git，已跳过自动初始化。请安装 Git 后再运行此脚本，或使用 README 中的 Netlify/Vercel 方案。')
        return False
    try:
        if not os.path.exists('.git'):
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            subprocess.run(['git', 'add', 'index.html'], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', 'Add birthday page for WeChat'], check=True, capture_output=True)
            print('✅ Git 仓库已初始化，文件已提交')
            return True
        else:
            print('ℹ️ Git 仓库已存在')
            return False
    except subprocess.CalledProcessError as e:
        print(f'❌ Git 操作失败：{e}')
        return False

def print_deployment_instructions():
    print('\n🚀 部署到 GitHub Pages 步骤：')
    print('1. 在 GitHub 上创建新仓库（例如：birthday-wish）')
    print('2. 复制以下命令并执行：')
    print('   git remote add origin https://github.com/<你的用户名>/birthday-wish.git')
    print('   git push -u origin main')
    print('3. 在 GitHub 仓库设置中：')
    print('   - 找到 "Pages" 部分')
    print('   - Source 选择 "Deploy from a branch"')
    print('   - Branch 选择 "main"，文件夹选择 "/"')
    print('   - 保存设置')
    print('4. 等待几分钟，访问 https://<你的用户名>.github.io/birthday-wish/')
    print('5. 在微信中打开该链接即可！')

def main():
    print('🎉 开始生成微信可直接打开的生日祝福页面...\n')

    # 生成 HTML
    html_path = generate_html()

    # 初始化 Git
    git_initialized = init_git_repo()

    # 打开本地预览
    webbrowser.open_new_tab(html_path)

    # 打印部署说明
    print_deployment_instructions()

    print('\n✨ 完成！按照上述步骤部署后，即可在微信中直接打开。')

if __name__ == '__main__':
    main()
