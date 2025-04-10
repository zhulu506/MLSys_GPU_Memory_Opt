import os

# 目标文件
output_file = "bib.txt"

# 获取当前文件夹内的所有 txt 文件
files = [f for f in os.listdir() if f.endswith(".txt") and f != output_file]

# 合并文件内容
with open(output_file, "w", encoding="utf-8") as outfile:
    for file in files:
        with open(file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n")

print(f"合并完成，所有 txt 内容已保存到 {output_file}")
