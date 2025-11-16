# 🤖 Web Automation Bot with FastAPI & Playwright

A robust Python-based web automation service that performs browser tasks automatically through a clean API interface. Built with FastAPI and Playwright for reliable, scalable web automation.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green?logo=fastapi)
![Playwright](https://img.shields.io/badge/Playwright-Automation-orange?logo=playwright)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🚀 Overview

This project provides a sophisticated web automation framework that can perform complex browser tasks like form filling, order tracking, and data extraction through a simple REST API. The system handles errors gracefully and provides detailed feedback about automation results.

## ✨ Features

### 🔧 Core Automation Engine
- **Browser Control**: Full web browser automation using Playwright
- **Multi-Action Support**: Navigate, click, type, and extract data from web pages
- **Error Resilience**: Robust error handling for slow pages and missing elements
- **Task Reliability**: Automatic retries and timeout management

### 🌐 API Interface
- **RESTful Endpoints**: Clean API design with FastAPI
- **Async Operations**: Non-blocking automation tasks
- **Real-time Status**: Progress tracking and result reporting
- **Swagger Documentation**: Auto-generated API docs with interactive testing

### 🛡️ Production Ready
- **Comprehensive Error Handling**: Graceful degradation and informative error messages
- **Logging & Monitoring**: Detailed execution logs and performance metrics
- **Configurable Timeouts**: Adaptive waiting strategies for dynamic content
- **Cross-browser Support**: Chrome, Firefox, and WebKit automation

## 🏗️ Architecture

```
web-automation-bot/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py        # API route handlers
│   ├── core/
│   │   ├── __init__.py
│   │   ├── automation.py       # Playwright automation engine
│   │   ├── app2.py           # Predefined automation tasks
│   ├── routes/
│       ├── __init__.py
│       └── router.py         # Pydantic models for API
├── requirements.txt
└── README.md
```

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Node.js (for Playwright browsers)

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/web-automation-bot.git
cd web-automation-bot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install
```

5. **Run the application**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🚀 Quick Start

### Using the API

1. **Start the server**:
```bash
uvicorn app.main:app --reload
```

2. **Access the API documentation**:
   Open http://localhost:8000/docs in your browser for interactive Swagger UI.
```

## 🎯 Predefined Tasks

### 1. **Login and Search**
- Logs into a website and searches for specific products
- Returns product information and prices

### 2. **Form Filling**
- Automatically fills complex multi-step forms
- Handles validation and submission

### 3. **Order Tracking**
- Tracks package status across multiple carriers
- Extracts delivery estimates and status updates

### 4. **Data Extraction**
- Scrapes structured data from websites
- Exports data in JSON format

## ⚙️ Configuration

### Environment Variables
Create a `.env` file:
```env
```

### Custom Task Configuration
Add custom tasks in `app/core/tasks.py`:
```python
CUSTOM_TASKS = {
    "my_custom_task": {
        "description": "My custom automation workflow",
        "steps": [
            {"action": "navigate", "url": "https://example.com"},
            {"action": "click", "selector": "#start-button"},
            {"action": "extract", "selector": ".result", "output_key": "final_result"}
        ]
    }
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Playwright](https://playwright.dev/) for robust browser automation
- [FastAPI](https://fastapi.tiangolo.com/) for high-performance API framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

---

**Start automating your web tasks with a single API call!** 🚀

*Built with ❤️ using Python, FastAPI, and Playwright*
