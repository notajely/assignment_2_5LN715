import os
from pydub import AudioSegment

# 定义输入和输出目录
input_dir = "/Users/jessie/Desktop/speech"
output_dir = "/Users/jessie/Desktop/speech_data"

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 支持的音频格式
audio_formats = ['.m4a', '.mp3', '.aac', '.wav', '.flac']

# 遍历输入目录中的所有文件
for filename in os.listdir(input_dir):
    # 获取文件扩展名
    file_ext = os.path.splitext(filename)[1].lower()
    
    # 检查是否为支持的音频格式
    if file_ext in audio_formats:
        # 构建完整的输入输出路径
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.wav'
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            # 加载音频文件
            audio = AudioSegment.from_file(input_path, format=file_ext[1:])
            
            # 导出为 WAV 格式
            print(f"Converting {filename} to WAV...")
            audio.export(output_path, format='wav')
            print(f"Converted {filename} -> {output_filename}")
            
        except Exception as e:
            print(f"Error converting {filename}: {str(e)}")

print("Conversion complete!")