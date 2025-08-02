import re
import os

def should_filter_line(line):
    """检查行中是否有'两个数字+三个字母'的连续模式"""
    # 匹配：任意位置出现两个数字紧接着三个字母（不区分大小写）
    pattern = r'\d{2}[A-Za-z]{3}'
    return bool(re.search(pattern, line))

def process_file(file_path, in_place=False, backup_ext='.bak'):
    """处理单个文件，可选择原地修改或创建新文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 过滤并保留行末换行符
    filtered_lines = [line for line in lines if not should_filter_line(line)]
    
    if in_place:
        # 原地修改：先备份原文件
        backup_path = file_path + backup_ext
        os.rename(file_path, backup_path)
        print(f"已备份原文件到: {backup_path}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(filtered_lines)
        print(f"已完成原地修改: {file_path}")
    else:
        # 创建新文件（原文件名_new.txt）
        new_path = os.path.splitext(file_path)[0] + '_filtered.txt'
        with open(new_path, 'w', encoding='utf-8') as f:
            f.writelines(filtered_lines)
        print(f"已生成新文件: {new_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='删除文件中"两个数字+三个字母"的行')
    parser.add_argument('filename', help='要处理的文件名（需在当前目录）')
    parser.add_argument('--in-place', action='store_true', 
                       help='直接修改原文件（默认生成新文件）')
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print(f"错误：文件 {args.filename} 不存在于当前目录")
        exit(1)

    process_file(args.filename, args.in_place)