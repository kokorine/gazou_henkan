from PIL import Image
import os

# 対応する拡張子
formats = ['.jpeg', '.png', '.bmp', '.gif', '.webp']
formats_string = ' '.join(formats)
print('\n\n対応する拡張子 {}\n\n'.format(formats_string.replace('.','')))
convf = input('変換したい形式を入力してください(例 jpeg, png): ').upper()
inputf = input('入力フォルダを指定してください: ') 
outputf = input('出力フォルダを指定してください: ')

# 変換したい画像があるフォルダ
input_folder = inputf
# 変換後の画像を保存するフォルダ
output_folder = outputf

# 拡張子を作成
extension = '.' + convf.lower()
#変換枚数カウント
x = 0

if extension in formats:
 
 if not os.path.exists(output_folder):
     os.makedirs(output_folder)

 for filename in os.listdir(input_folder):
     if any(filename.lower().endswith(fmt) for fmt in formats):
         image = Image.open(os.path.join(input_folder, filename))
         #JPEGの場合はRGB形式に変換
         if convf == 'JPEG' and image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
         #拡張子を設定
         new_filename = os.path.splitext(filename)[0] + extension
         #画像を保存
         image.save(os.path.join(output_folder, new_filename), convf)
         x = x + 1
         print('{}枚変換しました'.format(x))

else:
 print('対応していない拡張子です')
        
