# 定义输入和输出文件
input_file = "output.sh"
output_file = "output71cmd.sh" 
# 读取命令列表文件，将每一行存入 commands 列表  
with open(input_file, "r") as f:
	commands = [line.strip() for line in f if line.strip()]
# 创建新的脚本文件并写入代码
with open(output_file, "w") as f:
	f.write("#!/bin/bash\n\n")
	# 写入命令列表
	f.write("commands=(\n") 
	for cmd in commands:   
		f.write(f"  {cmd}\n")  # 不使用双引号 
	f.write(")\n\n")            
echo 开始随机执行命令（每条运行5秒），按 Ctrl+C 停止...                                                                 
while true; do                                                                                                              
	#随机选择一条命令                                                                                                      
 	random_cmd="${commands[$RANDIM % ${#commands[@]}]}"                                                                    
 	echo "执行命令: $random_cmd (持续5秒)"                                                                                
  #启动命令并在后台运行                                                                                                  
 	eval "$random_cmd" &                                                                                                   
 	cmd_pid=$!                                                                                                             
 	#让命令运行5秒后强制停止                                                                                                
	sleep 5                                                                                                                 
	kill $cmd_pid 2>/dev/null                                                                                               
	wait $cmd_pid 2>/dev/null #避免僵尸进程                                                                                
	echo "-----------------"                                                                                            
done
