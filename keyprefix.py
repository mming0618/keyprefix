import os
from tqdm import tqdm  # 任务进度条模块

def is_valid_password(password):
    """
    检查密码是否满足以下条件：
    1. 不包含连续3个相同字符。
    2. 不包含两个以上连续相同字符。
    """
    for i in range(len(password) - 2):
        # 检查是否有3个相同字符连续出现
        if password[i] == password[i + 1] == password[i + 2]:
            return False
    for i in range(len(password) - 1):
        # 检查是否有两个以上（大于2）相同字符连续出现
        if password[i] == password[i + 1] and (
            i + 2 < len(password) and password[i] == password[i + 2]
        ):
            return False
    return True

def generate_passwords(start, end):
    """
    生成符合条件的密码列表，并显示任务进度条。
    """
    passwords = []
    for num in tqdm(range(start, end + 1), desc="生成密码进度", unit="密码"):
        hex_password = f"{num:04X}"  # 转为大写的四位十六进制表示
        if is_valid_password(hex_password):
            passwords.append(hex_password)
    return passwords

def save_passwords_to_file(passwords, file_path):
    """
    将密码列表保存为密码字典文件。
    """
    with open(file_path, "w") as file:
        for password in passwords:
            file.write(password + "\n")

# 主程序
if __name__ == "__main__":
    # 指定范围
    start_hex = 0x40000
    end_hex = 0x7ffff

    # 生成符合条件的密码
    print("开始生成密码列表...")
    passwords = generate_passwords(start_hex, end_hex)

    # 文件保存路径
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    save_dir = os.path.join(desktop, "keyprefix")  # 文件夹名称改为“keyprefix”
    os.makedirs(save_dir, exist_ok=True)  # 确保目标文件夹存在
    save_path = os.path.join(save_dir, "passwords.txt")

    # 保存密码到文件
    print("保存密码列表至文件...")
    save_passwords_to_file(passwords, save_path)

    print(f"密码字典已生成并保存至：{save_path}")
