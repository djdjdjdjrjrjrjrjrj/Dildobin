<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Angelbin</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: black;
            color: white;
            overflow: hidden;
            position: relative;
            transition: background-image 0.5s ease;
        }
        
        #initial-message {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 100;
        }
        
        #initial-message h1 {
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        #content {
            display: none;
            text-align: center;
            z-index: 10;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
        }
        
        .telegram-link {
            margin-top: 20px;
            color: white;
            text-decoration: underline;
            font-size: 18px;
        }
        
        .search-container {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }
        
        #search-input {
            padding: 10px;
            width: 300px;
            border: none;
            border-radius: 5px 0 0 5px;
        }
        
        #search-button {
            padding: 10px 20px;
            background-color: #000;
            color: white;
            border: none;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
        }
        
        #result {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div id="initial-message">
        <h1>Все действия произведенные на этом сайте - шутка</h1>
        <h1>Сделано в развлекательных целях</h1>
    </div>
    
    <div id="content">
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Search For Pasta...">
            <button id="search-button">Search</button>
        </div>
        <div id="result"></div>
        <a href="https://t.me/AngelbinOffical" class="telegram-link" target="_blank">Offical Angelbin Telegram</a>
    </div>

    <script>
        // Скрываем начальное сообщение через 3 секунды и показываем контент
        setTimeout(function() {
            document.getElementById('initial-message').style.display = 'none';
            document.getElementById('content').style.display = 'block';
            
            // Устанавливаем фоновое изображение
            document.body.style.backgroundImage = "url('https://wallpapercave.com/wp/wp2735091.jpg')";
            document.body.style.backgroundSize = "cover";
            document.body.style.backgroundPosition = "center";
            document.body.style.backgroundAttachment = "fixed";
        }, 3000);
        
        // Обработчик поиска
        document.getElementById('search-button').addEventListener('click', function() {
            const searchTerm = document.getElementById('search-input').value.toLowerCase();
            const resultDiv = document.getElementById('result');
            
            // Здесь можно добавить список "паст", которые есть на сайте
            const availablePastas = [
                "пример", 
                "тест", 
                "паста",
                "шутка",
                "развлечение"
            ];
            
            if (availablePastas.includes(searchTerm)) {
                resultDiv.textContent = `Найдено: ${searchTerm}`;
            } else {
                resultDiv.textContent = "Ничего не найдено";
            }
        });
        
        // Также можно обрабатывать нажатие Enter в поле ввода
        document.getElementById('search-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                document.getElementById('search-button').click();
            }
        });
    </script>
</body>
</html>
