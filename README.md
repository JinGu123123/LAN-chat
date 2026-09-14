# LAN-chat

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> 一个基于 Python 的局域网聊天系统，支持多客户端实时文本通信。

## ✨ 功能特点

- 服务端 / 客户端架构
- 局域网内多客户端同时在线
- 实时文本消息收发
- 使用多线程处理并发连接
- 纯 Python 标准库实现，无需安装任何第三方依赖

## 🛠️ 技术栈

- **语言**：Python 3.x
- **网络通信**：socket（标准库）
- **并发处理**：threading（标准库）
- **依赖**：无第三方依赖

## 📦 快速开始

### 环境要求

- Python 3.6 或更高版本
- 多台设备处于同一局域网内（或同一台电脑开多个终端测试）

### 运行步骤

1. 启动服务端（在一台电脑上执行）：

   ```bash
   python server.py
   ```

2. 启动客户端（在另一台电脑上执行，或同一台电脑另开终端）：

   ```bash
   python client.py
   ```

3. 开始聊天：在客户端输入文本消息，按回车发送。

### 测试方式

如果没有多台设备，可以在一台电脑上：

- 打开终端 1：运行 python server.py
- 打开终端 2：运行 python client.py
- 打开终端 3：再运行 python client.py（模拟多个用户）

## 📁 项目结构

    LAN-chat/
    ├── client.py       客户端程序
    ├── server.py       服务端程序
    ├── .gitignore      Git 忽略配置
    └── README.md       项目说明

## 🔧 工作原理

- 服务端：监听指定端口，接受客户端连接，使用多线程为每个客户端创建独立线程，接收到消息后广播给所有在线客户端
- 客户端：连接服务端，启动独立线程接收消息，主线程负责发送消息

## 📄 许可证

MIT
