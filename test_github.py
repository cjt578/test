"""测试 GitHub 上传的简单程序"""

import platform
import sys
from datetime import datetime


def get_system_info():
    """获取当前系统信息"""
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": sys.version,
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def main():
    print("=" * 50)
    print("  GitHub 上传测试程序")
    print("=" * 50)
    print(f"运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    info = get_system_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

    print()
    print("如果这段文字出现在 GitHub 上，说明上传成功!")


if __name__ == "__main__":
    main()
