#!/bin/bash

commands=(
    "sleep 1"                   # 示例命令1（实际会被强制运行5秒）
    "yes > /dev/null"           # 示例命令2（CPU占用）
    "dd if=/dev/zero of=/dev/null bs=1M"  # 示例命令3（I/O占用）
    "ping -c 100 google.com"    # 示例命令4（网络请求）
    "tail -f /var/log/syslog"   # 示例命令5（持续读取日志）
)

echo "开始随机执行命令（每条运行5秒），按 Ctrl+C 停止..."

while true; do
    # 随机选择一条命令
    random_cmd="${commands[$RANDOM % ${#commands[@]}]}"

    echo "执行命令: $random_cmd (持续5秒)"
    
    # 启动命令并在后台运行
    eval "$random_cmd" &
    cmd_pid=$!
    
    # 让命令运行5秒后强制停止
    sleep 5
    kill $cmd_pid 2>/dev/null
    wait $cmd_pid 2>/dev/null  # 避免僵尸进程
    
    echo "----------------------------------"
done
