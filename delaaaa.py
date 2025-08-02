import re

def has_consecutive_letters(line, min_consecutive=4):
    """检查行中是否有连续 min_consecutive 个及以上字母"""
    pattern = r'[A-Za-z]{' + str(min_consecutive) + r',}'
    return bool(re.search(pattern, line))

def filter_file(input_file, output_file=None):
    """从输入文件读取，过滤后写入输出文件（或打印到控制台）"""
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    filtered_lines = [line.strip() for line in lines if not has_consecutive_letters(line)]
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write('\n'.join(filtered_lines))
        print(f"过滤完成！结果已保存到 {output_file}")
    else:
        print("过滤后的行：")
        for line in filtered_lines:
            print(line)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="过滤文件中包含连续4个及以上字母的行")
    parser.add_argument("input_file", help="输入文件路径")
    parser.add_argument("-o", "--output", help="输出文件路径（可选）")
    args = parser.parse_args()

    filter_file(args.input_file, args.output)