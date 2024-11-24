import os
import subprocess
import glob

# 要壓縮的資料夾列表
FOLDER_LIST = ["*"]

def run(folder):
    os.chdir(folder)
    
    # 定義 zip 檔案名稱
    zip_filename = f"../{folder}.zip"
    
    # 使用 glob 獲取資料夾內的所有檔案與資料夾
    files_to_zip = glob.glob("*")
    
    if files_to_zip:
        # 執行 zip 壓縮指令
        subprocess.run(["zip", "-r", zip_filename] + files_to_zip, check=True)
    else:
        print(f"警告：'{folder}' 資料夾內沒有檔案可壓縮。")
    
    os.chdir('..')

if FOLDER_LIST == ["*"]:
    for folder in os.listdir():
        if os.path.isdir(folder):
            run(folder)
else:
    # 遍歷每個資料夾
    for folder in FOLDER_LIST:
        # 進入指定的資料夾
        run(folder)
