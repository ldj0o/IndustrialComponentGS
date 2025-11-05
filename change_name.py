import os

def rename_files(directory):
    # 获取目录中的所有文件
    for filename in os.listdir(directory):
        # 确保处理的文件是jpg文件
        if filename.endswith(".jpg"):
            # 分割出数字部分，例如：input_0001.jpg -> 0001
            num_part = filename.split('_')[-1].split('.')[0]
            
            # 使用 zfill(5) 将数字部分格式化为5位数，例如：0001 -> 00001
            new_filename = num_part.zfill(5) + ".jpg"
            
            # 构建完整的旧路径和新路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    # 替换为你的图片文件夹路径
    directory = "/home/yxiong/PGSR/PGSR-main/output_new/output_1/test/ours_30000/renders"
    rename_files(directory)
