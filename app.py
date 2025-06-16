from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import gdown


def download_model():
    url = "https://drive.google.com/file/d/1PplrzOd1p2Ck5DBxqeWtEozYQRczlSYA/view?usp=sharing"  
    output = "model/best_cnn_model.h5"
    if not os.path.exists(output):
        print("Downloading model...")
        gdown.download(url, output, quiet=False)
    else:
        print("Model already exists.")

download_model()


app = Flask(__name__)
model = load_model('model/best_cnn_model.h5')
class_names = ['tulip', 'dandelion', 'rose', 'sunflower', 'daisy']
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tạo thư mục uploads nếu chưa có
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict_flower(img_path):
    # Load và tiền xử lý ảnh
    img = image.load_img(img_path, target_size=(224, 224))  # Kích thước giống trong huấn luyện
    img_tensor = image.img_to_array(img)
    img_tensor = img_tensor / 255.0  # Chuẩn hóa giống trong ImageDataGenerator
    img_tensor = np.expand_dims(img_tensor, axis=0)  # Thêm batch dimension

    # Dự đoán
    prediction = model.predict(img_tensor)[0]

    # In xác suất cho từng lớp
    for i, prob in enumerate(prediction):
        print(f"{class_names[i]}: {prob:.2%}")

    # Lấy lớp có xác suất cao nhất
    class_idx = np.argmax(prediction)
    predicted_class = class_names[class_idx]
    confidence = prediction[class_idx] * 100  # Chuyển thành phần trăm

    return f"{predicted_class} ({confidence:.2f}%)"

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    file_path = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            prediction = predict_flower(file_path)
    return render_template('index.html', prediction=prediction, image_path=file_path)

if __name__ == '__main__': 
    app.run(debug=True)