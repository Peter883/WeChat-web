# 微信直接打开静态页面

当前目录已经生成了一个可显示“蓓妮生日快乐🎂”的静态页面：`index.html`。

## 为什么微信不能直接打开

微信只能打开公网可访问的 `http://` 或 `https://` 链接，不能直接打开电脑里的本地文件。

## 最快的部署方案

### 方案一：GitHub Pages

1. 在 GitHub 上创建一个仓库，例如 `birthday-wish`。
2. 将当前目录的 `index.html` 上传到仓库根目录。
3. 在仓库设置里启用 GitHub Pages，选择 `main` 分支的根目录。
4. 等几分钟，访问 `https://<你的GitHub用户名>.github.io/birthday-wish/`。
5. 在微信中打开这个链接。

### 方案二：Netlify

1. 访问 https://app.netlify.com/drop
2. 将当前目录中的 `index.html` 拖到页面上。
3. 等待部署完成，Netlify 会生成一个 HTTPS 链接。
4. 在微信中打开该链接。

### 方案三：Vercel

1. 登录 https://vercel.com
2. 创建一个新项目并导入 GitHub 仓库，或直接上传 `index.html`。
3. 发布后获取 HTTPS 链接。
4. 在微信中打开该链接。

## 现在你已经准备好

- `index.html` 已经是一个微信友好的移动页面
- 只需将它部署到一个线上静态站点
- 之后复制链接到微信里打开即可

---

如果你没有安装 Git，可以直接使用 Netlify 或 Vercel 上传 `index.html`，这两个服务都支持直接部署静态文件。