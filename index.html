<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CoffeeSwap - Login</title>
    <style>
        /* Reset básico para garantir que o estilo seja consistente */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body, html {
            height: 100%;
            margin: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }

        /* Contêiner principal */
        .container {
            display: flex;
            justify-content: flex-start;
            height: 100%;
        }

        /* Lado Esquerdo */
        .content-left {
            width: 420px; /* Lado esquerdo com 420px */
            background-color: #D86B16; /* Laranja escuro */
            color: #4C2A1F; /* Marrom escuro para as letras */
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }

        .logo {
            margin-bottom: 30px;
            text-align: center;
        }

        .logo-image {
            width: 150px;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        ul li {
            margin: 15px 0;
        }

        ul li a {
            text-decoration: none;
            color: #4C2A1F;
            font-weight: bold;
            font-size: 16px;
            display: block;
        }

        ul li a:hover {
            color: #3E1F1B;
        }

        /* Formulário de Login */
        .login-form {
            margin-top: 30px;
        }

        .login-form input {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .login-form button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }

        .login-form button:hover {
            background-color: #218838;
        }

        .forgot-password a {
            text-decoration: none;
            color: #fff;
        }

        /* Links do rodapé */
        .footer-links a {
            text-decoration: none;
            color: #4C2A1F;
            margin-right: 10px;
        }

        .footer {
            margin-top: 20px;
            font-size: 12px;
        }

        /* Lado Direito */
        .content-right {
            flex: 1;
            background-color: #3E1F1B; /* Cor café escura */
            padding: 20px;
            color: #fff;
        }

        /* Estilo do chatbot */
        .floating-chatbot {
            position: fixed;
            bottom: 6rem;
            right: 1rem;
            width: 300px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            display: none; /* Começa invisível */
            flex-direction: column;
            padding: 1rem;
            z-index: 1000;
        }

        .floating-chatbot.active {
            display: flex; /* Quando a classe "active" é adicionada, o chatbot aparece */
        }

        .chat-header {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .chat-messages {
            overflow-y: auto;
            max-height: 200px;
            margin-bottom: 1rem;
        }

        .chat-messages div {
            margin-bottom: 0.5rem;
            padding: 0.5rem;
            border-radius: 8px;
        }

        .chat-messages .bot {
            background-color: #f1f1f1;
            text-align: left;
        }

        .chat-messages .user {
            background-color: #007bff;
            color: white;
            text-align: right;
        }

        .chat-input {
            display: flex;
            margin-top: 1rem;
        }

        .chat-input input {
            flex-grow: 1;
            padding: 0.5rem;
            border-radius: 8px;
            border: 1px solid #ddd;
        }

        .chat-input button {
            padding: 0.5rem;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            margin-left: 0.5rem;
        }

        /* Botão para ativar o chatbot */
        .chat-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
        }

        .chat-button button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }

        .chat-button button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Lado Esquerdo -->
        <div class="content-left">
            <div class="logo">
                <img src="logo.png" alt="Logo CoffeeSwap" class="logo-image">
            </div>
            <ul>
                <li><a href="#">QUEM SOMOS</a></li>
                <li><a href="#">Perguntas Frequentes</a></li>
            </ul>

            <div class="login-form">
                <input type="text" id="login" placeholder="Login (ex: Rbitcoin)">
                <input type="password" id="senha" placeholder="Senha">
                <button type="button">Entrar</button>
                <div class="forgot-password">
                    <a href="#">Esqueceu a senha?</a>
                </div>
            </div>

            <ul>
                <li><a href="#">Não tem uma conta? Registro</a></li>
            </ul>
        </div>

        <!-- Lado Direito -->
        <div class="content-right">
            <!-- O conteúdo à direita pode ser uma imagem, por exemplo -->
            <img src="coffee-image.jpg" alt="Imagem de café" class="imagem-animada">
        </div>
    </div>

    <!-- Botão para ativar o chatbot -->
    <div class="chat-button">
        <button>Iniciar Chat</button>
    </div>

    <!-- Chatbot -->
    <div class="floating-chatbot">
        <div class="chat-header">Chatbot</div>
        <div class="chat-messages">
            <!-- Mensagens do chatbot -->
        </div>
        <div class="chat-input">
            <input type="text" placeholder="Digite uma mensagem">
            <button>Enviar</button>
        </div>
    </div>

    <script>
        // Função para mostrar o chatbot
        function showChatbot() {
            document.querySelector('.floating-chatbot').classList.add('active');
        }

        // Adiciona o evento de clique para ativar o chatbot
        document.querySelector('.chat-button button').addEventListener('click', showChatbot);
    </script>
</body>
</html>
