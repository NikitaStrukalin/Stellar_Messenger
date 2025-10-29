from flask import Flask

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой сайт со звуком</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
            background-color: #f0f0f0;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Добро пожаловать!</h1>
        <p>Нажмите на кнопку ниже, чтобы воспроизвести звук:</p>
        
        <iframe 
            width="110" 
            height="200" 
            src="https://www.myinstants.com/instant/vizg-svini-91156/embed/" 
            frameborder="0" 
            scrolling="no">
        </iframe>
        
        <p style="margin-top: 20px; color: #666;">
            Используйте встроенный плеер для воспроизведения звука
        </p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return HTML

if __name__ == '__main__':
    app.run(debug=True)