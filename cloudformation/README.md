# Como fazer o Deploy dos recursos de Analytics na AWS ?

- [Aprenda como utilizar o Amazon Cloud Formation](https://aws.amazon.com/pt/quickstart)

# Templates Disponiveis

Os recursos são disponiveis para provisionamento utilizando Cloud Formation, esses templates são previamente configurados para provisionar os recursos em sua conta AWS de forma mais simples.

- **VPC:** Provisiona uma VPC seguindo as boas práticas da AWS

- **Joker:** Esse template provisiona uma instância EC2 com 8vPCU e 4GB de Ram

- **Thanos:** Esse template provisiona uma instância EC2 com 16vPCU e 64GB de Ram

- **Bucket:** Cria um bucket no AWS S3

- **EMR:** Provisiona um cluster de EMR com suporte a Spark ou Hbase

- **SageMaker Notebook:** Esse template provisiona um Notebook para ser utilizado na AWS.

> Jupyter Notebook é uma aplicação web que permite a você criar e compartilhar documentos que contem ao mesmo tempo código interativo e textos explicativos.

# Realizando o deploy da VPC utilizando Boto3

A Amazon Virtual Private Cloud (Amazon VPC) permite executar recursos da AWS em uma rede virtual definida por você. Essa rede virtual se assemelha a uma rede tradicional que você operaria no seu datacenter, com os benefícios de usar a infraestrutura dimensionável da AWS.

Para facilitar a criação da VPC foi desenvolvido um script em python para provisionar a stack utilizando o CloudFormation, além de mostrar como utilizar o SDK da AWS em python para interagir com a API.

- Primeiro passo é instalar e configurar o [aws-cli](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-welcome.html)

- Após isso é necessário exportar as variavéis de ambiente no seu terminal.
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION

- Instale as dependência necessárias para executar o script em python.

```shell
pip install -r requirements.txt
```

- Execute o script de criação da VPC.

```shell
python deploy-infra.py
```

- O output será parecido com o seguinte.

```
Creating batalha-de-dados-vpc
...waiting for stack to be ready...
This IDS will be used in almost all CFS: ('subnet-xxxxxxx', 'vpc-xxxxxx')
```
> Você utilizará o VPC ID e o Subnet ID em quase todos os outros templates do CloudFormation que você for utilizar.

# Como provisionar as stacks do CloudFormation via console