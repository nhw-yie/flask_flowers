# Flower Classification Web App using Flask & CNN

Đây là một ứng dụng web đơn giản dùng Flask kết hợp mô hình học sâu (CNN) để **phân loại các loài hoa** (tulip, dandelion, rose, sunflower, daisy) từ ảnh người dùng tải lên.

---

## Demo
Người dùng có thể tải lên hình ảnh hoa, và ứng dụng sẽ dự đoán tên loài hoa cùng độ tin cậy.
<img src="https://github.com/user-attachments/assets/84e3a98d-44c4-4125-9899-310185561678" width="400"/>

---

## Mô hình
Ứng dụng sử dụng mô hình CNN được huấn luyện bằng TensorFlow và lưu trữ trên Google Drive. Mô hình sẽ được **tự động tải về** nếu chưa có.

## RUN
git clone https://github.com/nhw-yie/flask_flowers.git
cd flower-flask-cnn
pip install -r requirements.txt
python app.py


