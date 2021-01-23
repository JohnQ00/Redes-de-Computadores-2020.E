<h2 align = center> Redes de Computadores </h2>
<h3 align = center> Protocolo de aplicação cliente-servidor para distância e localização </h3>
<p align = center> Repositório destinado ao projeto de criação de socket e protocolo de aplicação para a disciplina de Redes de Computadores. </p>
<hr>
<p align = center>
  <a href = 'https://ufal.br/' target = "_blank">
    <img src = '/img/ufal.png' width = '300'>
  </a>
</p>

Professor: Leandro Melo de Sales

Alunos:

- Hiago Lopes Cavalcante
- John Davi Dutra Canuto Pires

### 1. Execução

Para executar o servidor basta rodar o comando:
```
python ServerMultiThread.py
```
e para executar o cliente basta rodar este comando:
```
python ClienteMultiThread.py
```

### 2. Introdução

Este documento especifica um protocolo da camada de aplicação com arquitetura
*Cliente-Servidor* para entrega de localização e cálculo de distância. A aplicação
roda sobre o protocolo TCP, que foi escolhido em virtude de oferecer transferência de dados
de forma confiável. A porta utilizada pelo protocolo é a 15000.

- Porta padrão: 15000
- Arquitetura: Cliente-Servidor
- Protocolo na camada de transporte: TCP
- Padrão de caracteres: ASCII


### 3. Cliente e Servidor

A arquitetura utilizada neste protocolo é a *Cliente-Servidor*. Desse modo, para
o cliente conseguir enviar um comando ao servidor, será necessário que uma conexão TCP
já tenha sido estabelecida entre os dois hospedeiros. Após isso, o cliente terá a possibilidade
de enviar comandos deste protocolo para o servidor.

#### 3.1 O cliente

A função básica do cliente é enviar comandos com as coordenadas para o servidor. Os comandos serão
dotados de seu nome de identificação, seguidos ou não de uma série de informações que caracterizam o ponto e suas marcações
(que serão explicadas na seção 4). Após enviar o comando e seus dados, o servidor retornará um código que representará o êxito
ou a falha do comando, seguidos ou não da ação que o comando realizaria.

#### 3.2 O servidor

As funções básicas do servidor são a de aceitar conexões de múltiplos clientes,
aceitar os comandos e armazenar os dados enviados pelos clientes. Ele também irá guardar
toda informação de pontos enviadas pelo cliente em um arquivo na pasta do servidor.

### 4. Definição de comandos

Dado que a conexão entre o cliente e servidor já estará estabelecida, a comunicação entre
os dois hospedeiros será através de comandos e retornos descritos a seguir.

Os comandos descritos nessa seção, são exclusivamente enviados pelo cliente ao
servidor. Os retornos descritos nessa seção são retornos enviados exclusivamente
do servidor para o cliente.

- **REGISTER** - Comando para registrar o nome do usuário, as coordenadas dele, o nome desejado para o ponto e as coordenadas deste ponto.
- **DISTANCE** - Comando para calcular a distância entre dois pontos que entregues neste comando
- **READ** - Comando utilizado para executar a leitura do arquivo de armazenamento, exibindo os pontos salvos
- **DISCONNECT** - Comando utilizado para encerrar a conexão


### 4.1 - REGISTER

Este comando é utilizado para que o usuário registre um ponto na aplicação, ou seja,
deve carregar os nomes do usuário e o nome do ponto, seguidos de suas coordenadas. Os
nomes podem conter qualquer caractere alfanúmerico, enquanto as coordenadas deverão ser preenchidas
apenas com números, dentro de um parêntese, dividindo por vírgula a latitude e longitude presentes na
coordenada.

#### 4.1.1 - Formato

```
REGISTER#<Nome do usuário>|(<x.xx>,<y.yy>)|<Nome do ponto>|(<x.xx>,<y.yy>)
```
Exemplo:
```
REGISTER#Fulano|(<1.00>,<2.00>)|Casa|(<3.00>,<4.00>)
```

#### 4.1.2 - Retornos

- #150 - Registro foi concluído;  
- #300 - O arquivo de armazenamento está aberto, deve ser mantido fechado para executar o comando

#### 4.1.3 - Formato da mensagem

```
Server returned as response: #<numero_do_retorno> The distance between the two points is <distância> in a straight line.
```
ou

```
Server returned as response: #<numero_do_retorno>
```

Exemplo:
```
Server returned as response: #150 The distance between the two points is 872.26 km in a straight line
```

### 4.2 - DISTANCE

Comando utilizado para calcular diretamente dois pontos dados. O cliente enviará apenas duas coordenadas, sendo retornado
apenas o cálculo de distância entre os dois pontos. Este comando não armazena os pontos dados no arquivo de armazenamento.

#### 4.2.1 - Formato

```
DISTANCE#(<x.xx>,<y.yy>)|(<x.xx>,<y.yy>)
```

Exemplo:
```
DISTANCE#(<1.00>,<2.00>)|(<3.00>,<4.00>)
```

#### 4.2.2 - Retornos

- #165 - Distância calculada e entregue em km
- #170 - Distância calculada e entregue em m
- #320 - Não foi possível calcular a distância

#### 4.2.3 - Formato de mensagem

```
Server returned as response: #<numero_do_retorno>
```

Exemplo:
```
Server returned as response: #<numero_do_retorno> The distance between the two points is 526 m in a straight line
```

### 4.3 - READ

Comando utilizado para executar a leitura do arquivo onde estão guardados os pontos armazenados pelo comando
**REGISTER**.

#### 4.3.1 - Formato

```
READ
```

#### 4.3.2 - Retornos

- #155 - Leitura concluída
- #310 - O arquivo de armazenamento está vazio

#### 4.3.3 - Formato da mensagem

```
Server returned as response: #<numero_do_retorno> <Lista de pontos>
```

Exemplo:

```
Server returned as response: #155
'Username', 'User location', 'Point name', 'Point location'
 'Fulano', '1.00', '2.00', 'Casa', '3.00', '4.00'
```

### 4.4 - DISCONNECT

Comando utilizado para encerrar a conexão entre servidor e o cliente.

#### 4.4.1 - Formato

```
DISCONNECT
```
#### 4.4.2 - Retornos

- #100 - A conexão entre cliente e servidor foi desfeita

### 5. Descrição dos retornos

- #100 - A conexão entre cliente e servidor foi desfeita
- #125 - O comando foi escrito errado
- #150 - Registro foi concluído
- #155 - Leitura concluída
- #165 - Distância calculada e entregue em km
- #170 - Distância calculada e entregue em m
- #300 - O arquivo de armazenamento está aberto, deve ser mantido fechado para executar o comando
- #310 - O arquivo de armazenamento está vazio
- #320 - Não foi possível calcular a distância

### 6. Observações

- Se o arquivo de armazenamento não existir, a aplicação criará um arquivo 'Storage.csv' na pasta local do servidor
- O número máximo de clientes conectados ao servidor é 15
- Caso a conexão entre cliente-servidor seja perdida, todo o processo deverá ser
reiniciado.
- Para fechar o servidor, basta fechar o terminal
