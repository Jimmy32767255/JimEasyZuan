import webview
import random
import os
import subprocess
import threading
import sys

# 随机小字内容
RANDOM_TEXTS = [
    "感谢Microsoft Edge WebView2让我们能得以避免一台电脑上有好几百个浏览器这种事，是时候停用Electron框架了！",
    "畏惧神是正常的，因为神也会自畏",
    "eyes eyes baby to go ten..."
]

# 随机按钮文本
BUTTON_TEXTS = [
    "开始装B",
    "high翻全场",
    "成为嘉豪",
    "冻结时间",
    "释放洪荒之力"
]

# 当前选定的文本
current_text = random.choice(RANDOM_TEXTS)
current_button_text = random.choice(BUTTON_TEXTS)

class Api:
    def __init__(self):
        self.window = None
        
    def set_window(self, window):
        self.window = window
        
    def start_app(self):
        # 切换到模式选择界面
        self.window.evaluate_js("showModeSelection()")
        
    def hacker_mode(self):
        # 黑客模式：打开10个cmd窗口执行命令
        def open_cmd_windows():
            for _ in range(10):
                subprocess.Popen('cmd.exe /c "color 02&dir C:\\ /C /Q /R /S /W /4&tree C:\\ /f /a"', 
                                creationflags=subprocess.CREATE_NEW_CONSOLE)
        
        # 在新线程中执行，避免阻塞UI
        threading.Thread(target=open_cmd_windows, daemon=True).start()
        
    def dj_mode(self):
        # 切换到DJ界面
        self.window.evaluate_js("showDJMode()")
        
    def play_music(self):
        # 使用系统默认播放器打开音乐文件
        try:
            audio_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Friendships(Plain_Jane).wav")
            if os.path.exists(audio_file):
                os.startfile(audio_file)  # Windows系统打开文件
                print(f"正在使用系统播放器打开: {audio_file}")
            else:
                print(f"音频文件不存在: {audio_file}")
        except Exception as e:
            print(f"播放音乐失败: {e}")
        
    def go_back(self):
        # 返回主界面
        self.window.evaluate_js("showMainScreen()")

def create_html():
    # 创建HTML内容
    # 生成正确的文件URL路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(script_dir, "bg.avif").replace("\\", "/")
    bg_url = f"file:///{bg_path}"
    
    # 生成音频文件路径
    audio_path = os.path.join(script_dir, "Friendships(Plain_Jane).wav").replace("\\", "/")
    audio_url = f"file:///{audio_path}"
    
    return f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JimEasyZuan</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Microsoft YaHei', sans-serif;
            background: url('{bg_url}') no-repeat center center fixed;
            background-size: cover;
            color: white;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }}
        
        body::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            z-index: -1;
        }}
        
        .container {{
            text-align: center;
            z-index: 1;
            width: 80%;
            max-width: 600px;
        }}
        
        h1 {{
            font-size: 3.5em;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
            animation: glow 2s infinite alternate;
        }}
        
        .subtitle {{
            font-size: 1.2em;
            color: #ccc;
            margin-bottom: 30px;
            text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
        }}
        
        .btn {{
            background: linear-gradient(45deg, #ff0080, #ff8c00, #ffed00);
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            color: white;
            border-radius: 50px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        }}
        
        .btn:active {{
            transform: translateY(1px);
        }}
        
        .mode-btn {{
            background: linear-gradient(45deg, #00b4db, #0083b0);
            width: 200px;
        }}
        
        .back-btn {{
            background: linear-gradient(45deg, #8e2de2, #4a00e0);
            position: absolute;
            top: 20px;
            left: 20px;
        }}
        
        .screen {{
            display: none;
        }}
        
        #main-screen {{
            display: flex;
        }}
        
        .volume-slider-container {{
            margin-top: 50px;
            width: 80%;
            max-width: 400px;
        }}
        
        .volume-slider {{
            -webkit-appearance: none;
            width: 100%;
            height: 25px;
            background: linear-gradient(90deg, #00ff00, #ff0000);
            outline: none;
            border-radius: 15px;
        }}
        
        .volume-slider::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #ffffff;
            cursor: pointer;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }}
        
        @keyframes glow {{
            from {{
                text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
            }}
            to {{
                text-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00, 0 0 40px #00ff00, 0 0 50px #00ff00;
            }}
        }}
        
        .particles {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
        
        .particle {{
            position: absolute;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 10s infinite linear;
        }}
        
        @keyframes float {{
            0% {{
                transform: translateY(0) translateX(0);
                opacity: 1;
            }}
            100% {{
                transform: translateY(-100vh) translateX(100vw);
                opacity: 0;
            }}
        }}
        
        .dj-title {{
            font-size: 3em;
            margin-bottom: 50px;
            text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
            animation: dj-glow 2s infinite alternate;
        }}
        
        @keyframes dj-glow {{
            from {{
                text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
            }}
            to {{
                text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff;
            }}
        }}
    </style>
</head>
<body>
    <div id="main-screen" class="screen">
        <h1>JimEasyZuan</h1>
        <div class="subtitle" id="random-text">{current_text}</div>
        <button class="btn" onclick="startApp()" id="start-btn">{current_button_text}</button>
    </div>
    
    <div id="mode-selection" class="screen">
        <h2>选择装B模式</h2>
        <button class="btn mode-btn" onclick="hackerMode()">黑客模式</button>
        <button class="btn mode-btn" onclick="djMode()">DJ模式</button>
        <button class="btn back-btn" onclick="goBack()">返回</button>
    </div>
    
    <div id="dj-mode" class="screen">
        <h2 class="dj-title">DJ模式</h2>

        <button class="btn" onclick="playMusic()">播放音乐</button>
        <button class="btn back-btn" onclick="goBack()">返回</button>
    </div>
    
    <div class="particles" id="particles"></div>

    <script>
        // 创建粒子效果
        function createParticles() {{
            const container = document.getElementById('particles');
            for (let i = 0; i < 50; i++) {{
                const particle = document.createElement('div');
                particle.classList.add('particle');
                const size = Math.random() * 10 + 5;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                particle.style.left = Math.random() * 100 + 'vw';
                particle.style.top = Math.random() * 100 + 'vh';
                particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
                particle.style.animationDelay = Math.random() * 5 + 's';
                container.appendChild(particle);
            }}
        }}
        
        // 显示主界面
        function showMainScreen() {{
            document.querySelectorAll('.screen').forEach(screen => {{
                screen.style.display = 'none';
            }});
            document.getElementById('main-screen').style.display = 'flex';
        }}
        
        // 显示模式选择
        function showModeSelection() {{
            document.querySelectorAll('.screen').forEach(screen => {{
                screen.style.display = 'none';
            }});
            document.getElementById('mode-selection').style.display = 'flex';
        }}
        
        // 显示DJ模式
        function showDJMode() {{
            document.querySelectorAll('.screen').forEach(screen => {{
                screen.style.display = 'none';
            }});
            document.getElementById('dj-mode').style.display = 'flex';
        }}
        
        // 启动应用
        function startApp() {{
            pywebview.api.start_app();
        }}
        
        // 黑客模式
        function hackerMode() {{
            pywebview.api.hacker_mode();
        }}
        
        // DJ模式
        function djMode() {{
            pywebview.api.dj_mode();
        }}
        
        // 播放音乐
        function playMusic() {{
            pywebview.api.play_music();
        }}
        
        // 返回
        function goBack() {{
            pywebview.api.go_back();
        }}
        
        // 初始化
        window.addEventListener('DOMContentLoaded', function() {{
            createParticles();
        }});
    </script>
</body>
</html>
'''

def check_webview2():
    """检查WebView2运行时是否安装"""
    try:
        if sys.platform == 'win32':
            # 检查WebView2运行时是否可用
            try:
                import webview
                webview.initialize()
                return True
            except Exception as e:
                print(f"WebView2初始化失败: {e}")
                print("请安装Microsoft Edge WebView2运行时")
                print("下载地址: https://developer.microsoft.com/en-us/microsoft-edge/webview2/")
                return False
        return True
    except Exception as e:
        print(f"检查WebView2时出错: {e}")
        return True

def main():
    # 检查WebView2运行时
    if not check_webview2():
        input("按回车键退出...")
        return
    
    api = Api()
    window = webview.create_window(
        'JimEasyZuan',
        html=create_html(),
        js_api=api,
        width=1280,
        height=720,
        resizable=False,
        frameless=True,
        text_select=True  # 允许文本选择，有助于音频播放
    )
    api.set_window(window)
    webview.start()

if __name__ == '__main__':
    main()