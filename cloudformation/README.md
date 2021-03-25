# Como fazer o Deploy dos recursos de Analytics na AWS ?

- [Aprenda como utilizar o Amazon Cloud Formation](https://aws.amazon.com/pt/quickstart)

# Templates Disponiveis

Os recursos são disponiveis para provisionamento utilizando Cloud Formation, esses templates são previamente configurados para provisionar os recursos em sua conta AWS de forma mais simples.

- **VPC**

- **Joker:** Esse template provisiona uma instância EC2 com 8vPCU e 4GB de Ram

- **Thanos:** Esse template provisiona uma instância EC2 com 16vPCU e 64GB de Ram

- **Jupyter Notebook:** Esse template provisiona um Notebook para ser utilizado na AWS.

> Jupyter Notebook é uma aplicação web que permite a você criar e compartilhar documentos que contem ao mesmo tempo código interativo e textos explicativos.

# Realizando o deploy da VPC

A Amazon Virtual Private Cloud (Amazon VPC) permite executar recursos da AWS em uma rede virtual definida por você. Essa rede virtual se assemelha a uma rede tradicional que você operaria no seu datacenter, com os benefícios de usar a infraestrutura dimensionável da AWS.