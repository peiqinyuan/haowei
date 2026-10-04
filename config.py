import os
import sys

# ===== 邮件服务（QQ邮箱 SMTP），通过环境变量注入，未配置则邮箱功能自动禁用 =====
SMTP_HOST = os.environ.get('SMTP_HOST', 'smtp.qq.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))     # 587+STARTTLS（465被部分云防火墙拦截）
SMTP_USER = os.environ.get('SMTP_USER', '')          # 发件邮箱地址，如 123456@qq.com
SMTP_AUTH_CODE = os.environ.get('SMTP_AUTH_CODE', '')  # 邮箱授权码
EMAIL_CODE_TTL = int(os.environ.get('EMAIL_CODE_TTL', '600'))          # 验证码有效期(秒)
EMAIL_CODE_RATE_SECONDS = int(os.environ.get('EMAIL_CODE_RATE_SECONDS', '60'))  # 发送间隔(秒)

# 打包成 exe 后：
#   BASE_DIR    = exe 所在目录   （数据库/上传数据存放在这里，可读写、持久）
#   BUNDLE_DIR  = PyInstaller 解压出的只读资源目录（templates/static 等）
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
    BUNDLE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    BUNDLE_DIR = BASE_DIR

if getattr(sys, 'frozen', False):
    DATA_DIR = os.path.join(BASE_DIR, 'data_runtime')
    UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
else:
    DATA_DIR = BASE_DIR
    UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'haowei-secret-key-2024')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(DATA_DIR, "haowei.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_DIR
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    TEMP_DIR = UPLOAD_DIR