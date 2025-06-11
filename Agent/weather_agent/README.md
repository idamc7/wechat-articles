# Weather-Agent 🌦️

一个智能、可定制的天气预报通知 Agent，使用 LangChain, DeepSeek, 和风天气和 Bark 为你和你关心的人提供每日天气提醒。

## ✨ 特性

-   **个性化**: 支持多用户、多城市配置。
-   **智能化**: 集成 LLM (DeepSeek) 生成自然语言建议。
-   **配置驱动**: 所有敏感信息和参数都在 `config.yaml` 中管理。
-   **定时推送**: 每天早上定时发送天气预报到你的手机。
-   **代码健壮**: 遵循最佳实践，包含单元测试。

## 🚀 快速开始

### 1. 环境准备

-   Python 3.10+
-   一个可用的 Bark App 实例，[bark](https://github.com/Finb/Bark/blob/master/README.zh.md)
-   [和风天气 Web API Key](https://dev.qweather.com/docs/configuration/project-and-key/)
-   [DeepSeek API Key](https://platform.deepseek.com/docs/getting-started/api-key/)

### 2. 安装

```bash
# 构建虚拟环境
python -m venv myenv

# 激活虚拟环境
# windows:
myenv/Scripts/activate
# linux:
source myenv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 更改配置文件，配置自己的key，和想要通知的人
# config/config.yaml

# 测试天气查询
python app/services/weather_service.py

# 启动，默认自动会发起一次
python -m app.main
