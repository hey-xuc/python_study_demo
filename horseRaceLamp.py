import os
import time

def main():
    content = '北京欢迎你。。。'
    while True:
        # 清理屏幕输出
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
    
if __name__ == '__main__':
    main()