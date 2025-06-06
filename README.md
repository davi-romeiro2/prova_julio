# prova_julio

1. Criar e Configurar a Instância EC2
Primeiro, entre na sua conta da AWS e vá para o serviço EC2.

Crie uma nova instância EC2, escolhendo a imagem do sistema operacional que você preferir, como o Ubuntu ou Amazon Linux 2.

Na configuração da instância, escolha o tipo de instância, por exemplo, t2.micro, que pode ser elegível para o uso gratuito.

Durante a criação, crie um novo par de chaves ou use um já existente para poder acessar sua instância via SSH.

Certifique-se de que o grupo de segurança tenha a porta 22 (para SSH) aberta, para que você consiga se conectar à instância.

2. Acessar a Instância EC2 via SSH
Após a criação da instância, vá para a página de detalhes da instância e copie o endereço IP público dela.

Abra seu terminal e acesse a instância com o SSH, utilizando a chave privada que você gerou ao criar a instância. Você fará isso com um comando no terminal (caso use Linux ou Mac) ou por meio de um cliente SSH, como o PuTTY (no caso de Windows).

3. Instalar o Python e as Dependências
Verifique se o Python já está instalado na instância. Caso contrário, instale a versão mais recente do Python.

Para rodar o seu projeto, instale também o pip para gerenciar as bibliotecas do Python.

Se seu projeto tiver um arquivo requirements.txt, use o pip para instalar todas as dependências do seu projeto.

4. Transferir Seu Projeto para a EC2
No seu computador local, você precisará transferir os arquivos do seu projeto para a instância EC2. Isso pode ser feito com o SCP (secure copy protocol) ou uma ferramenta similar.

No terminal, você usará o SCP para transferir o diretório do seu projeto local para a instância EC2.

5. Configurar e Executar o Projeto
Depois de transferir os arquivos para a instância EC2, acesse o diretório onde você colocou os arquivos do projeto.

Caso seu projeto tenha um ambiente virtual configurado, ative-o. Caso contrário, você pode rodar diretamente o script Python.

Execute o script Python que você deseja rodar, verificando se tudo está funcionando corretamente.
