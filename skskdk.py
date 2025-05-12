<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Angelbin Site</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #000;
            transition: background-image 1s ease;
        }
        #splash {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            background-color: black;
        }
        #splash h1 {
            color: white;
            font-weight: bold;
            font-size: 24px;
            text-align: center;
            padding: 20px;
        }
        #content {
            display: none;
            width: 100%;
            height: 100%;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 20px;
            box-sizing: border-box;
        }
        /* Подчеркнутая ссылка */
        #telegram-link {
            text-decoration: underline;
            color: white;
            margin-bottom: 20px;
            font-size: 18px;
            cursor: pointer;
        }
        /* Поле поиска и кнопка */
        #search-container {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        #search-input {
            padding: 8px 12px;
            font-size: 16px;
            width: 250px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        #search-button {
            padding: 8px 16px;
            background-color: black;
            color: white;
            border: none;
            margin-left: 10px;
            cursor: pointer;
            border-radius: 4px;
        }
        #search-button:hover {
            background-color: #333;
        }
        /* Результат поиска */
        #result {
            font-size: 18px;
            color: white;
        }
    </style>
</head>
<body>
    <!-- Начальный экран с картинкой и текстом -->
    <div id="splash">
        <h1>Все действия Произведенные на Этом Сайте Шутка Зделанно В Развлекательных Целях</h1>
    </div>

    <!-- Основной контент сайта -->
    <div id="content">
        <div id="background"></div>
        <!-- Ссылка на Telegram -->
        <div id="telegram-link" onclick="window.location.href='https://t.me/AngelbinOffical'">Official Angelbin Telegram</div>

        <!-- Поле поиска -->
        <div id="search-container">
            <input type="text" id="search-input" placeholder="Search For Pasta" />
            <button id="search-button" onclick="searchPasta()">Search</button>
        </div>
        <div id="result"></div>
    </div>

    <script>
        // Задаем список "Паста" для поиска
        const pastaList = ['spaghetti', 'penne', 'fettuccine', 'farfalle', 'lasagna', 'penne rigate'];

        // Когда страница загружается
        window.onload = () => {
            // Через 3 секунды скрываем splash и показываем контент
            setTimeout(() => {
                document.getElementById('splash').style.display = 'none';
                document.getElementById('content').style.display = 'flex';

                // меняем фон на изображение
                document.body.style.backgroundImage = "url('https://wallpapercave.com/wp/wp2735091.jpg')";
                document.body.style.backgroundSize = "cover";
                document.body.style.backgroundPosition = "center";
            }, 3000);
        };

        // Функция поиска
        function searchPasta() {
            const input = document.getElementById('search-input').value.trim().toLowerCase();
            const resultDiv = document.getElementById('result');

            if (pastaList.includes(input)) {
                resultDiv.textContent = 'Паста найдена!';
            } else {
                resultDiv.textContent = 'Ничего не найдено.';
            }
        }
    </script>
</body>
</html>
