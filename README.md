# Importador de Credenciais .env para Azure Key Vault

Este é um projeto Python que simplifica a tarefa de importar credenciais armazenadas em um arquivo .env para o Azure Key Vault. Essa integração é útil para manter suas credenciais em um local seguro, o Azure Key Vault, em vez de mantê-las em um arquivo local.

## Pré-requisitos

Antes de utilizar este projeto, certifique-se de que você tenha os seguintes pré-requisitos instalados:

- Python 3.x instalado na sua máquina.
- A CLI da Azure instalada na sua máquina e devidamente configurada com suas credenciais. Você pode instalá-la seguindo as instruções oficiais da Microsoft.

## Instalação

Clone este repositório para a sua máquina:

1. Clone este repositório para a sua máquina:

```bash
git clone https://github.com/rscholant/azure-kv-importer.git
```

2. Navegue até o diretório do projeto:

```bash
cd azure-kv-importer
```

3. Instale as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

## Configuração

Antes de executar o projeto, é necessário configurar algumas informações:

1. Configurar o Azure Key Vault:

- Certifique-se de que você já tenha criado um Azure Key Vault e saiba a URL do seu vault.

2. Configurar as variáveis de ambiente no arquivo .env:

- Crie um arquivo .env na raiz do projeto e inclua as credenciais que deseja importar para o Azure Key Vault. Por exemplo:

```env
CLIENT_ID=seu-client-id
CLIENT_SECRET=sua-client-secret
TENANT_ID=seu-tenant-id
```

- O arquivo poderá conter variáveis que já exixtem no cofre só que com outro nome, assim importando para o nome que é necessário para o projeto. Por exemplo:

```env
VARIAVEL-EXISTENTE-NO-COFRE~>NOVA-VARIAVEL
```

4. Instalação da CLI da azure:

- Para instalação da CLI, pode ser acessado através deste [link](https://learn.microsoft.com/pt-br/cli/azure/install-azure-cli)

3. Configurar a autenticação da CLI da Azure:

- Você deve ter a CLI da Azure devidamente configurada com as suas credenciais. Caso não tenha feito isso, execute o seguinte comando e siga as instruções:

```bash
az login
```

## Uso

Execute o script main.py para importar as credenciais do arquivo .env para o Azure Key Vault:

```bash
python3 -Bu main.py <KV-NAME> <PATH-TO-ENV>
```

Siga as instruções na linha de comando para autenticar-se na Azure, e as credenciais do arquivo .env serão importadas com segurança para o Azure Key Vault.

## Contribuição

Este é um projeto de código aberto, e as contribuições são bem-vindas. Sinta-se à vontade para abrir problemas, propor melhorias ou enviar solicitações de pull.

## Licença

Este projeto é distribuído sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir conforme necessário.

---

<p align="center">Feito com ❤️ e ☕ por Rafael Scholant 👋</p>
