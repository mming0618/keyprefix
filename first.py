def process_line(line):
    # 去除行尾的换行符
    line = line.strip()
    # 添加13个0和13个f，格式为原始内容+13个0:原始内容+13个f
    processed_line = f"{line}0000000000000:{line}fffffffffffff"
    return processed_line

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # 跳过空行
            if line.strip():
                processed_line = process_line(line)
                outfile.write(processed_line + '\n')

# 使用示例
input_filename = 'passwords.txt'  # 输入文件名
output_filename = 'output.txt'  # 输出文件名

process_file(input_filename, output_filename)
print(f"处理完成，结果已保存到 {output_filename}")
