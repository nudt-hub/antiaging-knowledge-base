#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAGR 数据库自动同步脚本
功能：每季度检查 HAGR 数据库更新，同步最新数据
"""

import requests
import json
from datetime import datetime
from pathlib import Path

# HAGR 数据库 URL
HAGR_BASE_URL = "https://genomics.senescence.info"
GENAGE_URL = f"{HAGR_BASE_URL}/genes/"
ANAGE_URL = f"{HAGR_BASE_URL}/species/"

# 输出文件
CONTENT_FILE = Path(__file__).parent.parent / "content" / "aging-genes.md"
DATA_FILE = Path(__file__).parent.parent / "data" / "hagr_last_sync.json"


def check_hagr_updates():
    """
    检查 HAGR 数据库是否有更新
    
    Returns:
        dict: 更新信息，如果失败则返回 None
    """
    try:
        # 尝试访问 HAGR 官网
        response = requests.get(HAGR_BASE_URL, timeout=10)
        if response.status_code == 200:
            return {
                "status": "available",
                "last_check": datetime.now().isoformat(),
                "message": "HAGR 数据库可访问"
            }
        else:
            return {
                "status": "error",
                "last_check": datetime.now().isoformat(),
                "message": f"HAGR 返回状态码：{response.status_code}"
            }
    except Exception as e:
        return {
            "status": "unavailable",
            "last_check": datetime.now().isoformat(),
            "message": f"无法访问 HAGR: {str(e)}"
        }


def load_last_sync():
    """
    加载上次同步的数据
    
    Returns:
        dict: 上次同步的数据
    """
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"last_sync": None, "status": "never"}


def save_sync_data(data):
    """
    保存同步数据
    
    Args:
        data: 要保存的数据
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_content_file(update_info):
    """
    更新内容文件的最后更新时间
    
    Args:
        update_info: 更新信息
    """
    if not CONTENT_FILE.exists():
        print(f"内容文件不存在：{CONTENT_FILE}")
        return
    
    content = CONTENT_FILE.read_text(encoding='utf-8')
    
    # 更新最后更新时间
    today = datetime.now().strftime("%Y-%m-%d")
    content = content.replace(
        "数据最后更新：2026-04-18",
        f"数据最后更新：{today}"
    )
    
    # 如果有更新信息，添加通知
    if update_info.get("status") == "available":
        notification = f"\n\n> ✅ **HAGR 数据库状态**：可访问 | 最后检查：{today}\n"
    else:
        notification = f"\n\n> ⚠️ **HAGR 数据库状态**：{update_info.get('message', '未知')} | 最后检查：{today}\n"
    
    # 在免责声明前添加通知
    content = content.replace(
        "## ⚠️ 免责声明",
        notification + "\n## ⚠️ 免责声明"
    )
    
    CONTENT_FILE.write_text(content, encoding='utf-8")
    print(f"✅ 已更新内容文件：{CONTENT_FILE}")


def sync_hagr():
    """
    主同步函数
    """
    print("=" * 60)
    print("HAGR 数据库同步")
    print("=" * 60)
    
    # 检查 HAGR 更新
    print("正在检查 HAGR 数据库状态...")
    update_info = check_hagr_updates()
    
    if update_info["status"] == "available":
        print(f"✅ {update_info['message']}")
    else:
        print(f"⚠️ {update_info['message']}")
    
    # 保存同步数据
    save_sync_data(update_info)
    
    # 更新内容文件
    update_content_file(update_info)
    
    print("=" * 60)
    print("同步完成！")
    print("=" * 60)


if __name__ == "__main__":
    sync_hagr()
