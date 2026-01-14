# **RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS**

**Data:** 15 de Janeiro de 2026 

**Empresa:** Abstergo Industries 

**Responsável:** Pedro Canuto

## **Introdução**

Este relatório apresenta o processo de implementação de ferramentas na empresa **Abstergo Industries**, realizado por Pedro Canuto. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar a diminuição de custos imediatos.

## **Descrição do Projeto**

O projeto de implementação de ferramentas foi dividido em 3 etapas, cobrindo o ciclo de vida dos dados (Coleta, Armazenamento e Operações). A seguir, serão descritas as etapas do projeto:

### **Etapa 1: Coleta de Dados**

* **Nome da ferramenta:** **Amazon Kinesis Data Firehose**  
* **Foco da ferramenta:** Ingestão e entrega de dados em tempo real (Streaming).  
* **Descrição de caso de uso:** Implementação para coletar dados de vendas dos PDVs (Pontos de Venda) e logs de sensores IoT (que monitoram a temperatura das geladeiras de vacinas e insulinas) de todas as filiais.  
  **Benefício de Custo:** Substitui a necessidade de servidores de coleta locais ligados 24/7. O serviço é totalmente gerenciado e a farmácia paga apenas pelo volume de dados ingeridos (Gigabytes), eliminando custos de manutenção de infraestrutura de entrada.

### **Etapa 2: Armazenamento de Dados**

* **Nome da ferramenta:** **Amazon S3 (Simple Storage Service)**  
* **Foco da ferramenta:** Armazenamento de objetos (Data Lake) seguro e escalável.  
* **Descrição de caso de uso:** Criação de um repositório centralizado para armazenar histórico de receitas digitalizadas, notas fiscais eletrônicas e backups de inventário. Será configurado o **S3 Intelligent-Tiering**, que move automaticamente arquivos antigos e pouco acessados para camadas de armazenamento mais baratas (Archive).  
  **Benefício de Custo:** Custo muito inferior ao de manter storage físico (SAN/NAS) ou bancos de dados tradicionais para arquivos estáticos. A economia é automática conforme os dados envelhecem.

### **Etapa 3: Operações com Dados**

* **Nome da ferramenta:** **AWS Lambda**  
* **Foco da ferramenta:** Computação Serverless (Execução de código sem servidor).  
* **Descrição de caso de uso:** Processamento automático dos dados de inventário. Quando um arquivo de vendas é salvo no S3 (Etapa 2), uma função Lambda é acionada para atualizar o estoque no sistema central e verificar se há necessidade de reposição de medicamentos, enviando alertas.  
  **Benefício de Custo:** Elimina a necessidade de manter uma Máquina Virtual (EC2) ligada o tempo todo esperando trabalho. A cobrança é feita por milissegundos de execução do código. Se não houver vendas ou processamento no momento, o custo é zero.

## **Conclusão**

A implementação de ferramentas na empresa **Abstergo Industries** tem como esperado **a redução de até 40% nos custos de infraestrutura de TI e a automação do controle de estoque**, o que aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias, como o uso de Inteligência Artificial para previsão de demanda de medicamentos sazonais.

## **Anexos**

* Documento 01 \- Planilha de Comparativo de Custos (TCO: On-Premise vs AWS)

---

**Pedro Canuto,** *Arquiteto de Soluções Cloud*

