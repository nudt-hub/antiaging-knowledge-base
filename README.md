# 抗衰老科学前沿知识库

> AI 驱动的静态网站，每日自动更新抗衰老研究最新进展

## 🚀 部署步骤

### 1. 安装 Hugo

```bash
# macOS
brew install hugo

# Linux
sudo apt-get install hugo
```

### 2. 初始化主题

```bash
cd /home/admin/openclaw/workspace/antiaging-site
git submodule add https://github.com/HugoBlox/kit.git themes/hugo-blox
```

### 3. 创建 GitHub 仓库

1. 访问 https://github.com
2. 创建新仓库：`antiaging-knowledge-base`
3. 选择 Public

### 4. 推送

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/antiaging-knowledge-base.git
git push -u origin main
```

### 5. 等待部署

GitHub Actions 会自动构建并部署，约 2-5 分钟。

访问：`https://YOUR_USERNAME.github.io/antiaging-knowledge-base/`

---

## 📁 项目结构

```
antiaging-site/
├── content/           # 网站内容
│   ├── index.md
│   ├── basics.md
│   ├── interventions.md
│   ├── research.md
│   └── about.md
├── config/            # Hugo 配置
├── .github/workflows/ # GitHub Actions
└── themes/            # HugoBlox 主题
```

---

*由 JVS Claw AI 创建*
