# Bootcamp de Dados Blue Edtech

## Projeto ValorA.i

### Sobre o Problema Apresentado

O problema que nos foi apresentado foi acerca deste datset do kaggle (que pode ser acessado [aqui](https://www.kaggle.com/c/mercari-price-suggestion-challenge)) e a partir disso resolver problema relacionado com precificação dinâmica.

Precificar um produto fica ainda mais difícil em escala, considerando quantos produtos são vendidos online. As roupas têm fortes tendências de preços sazonais e são fortemente influenciadas por marcas, enquanto os eletrônicos têm preços flutuantes com base nas especificações do produto. Seja criativo e apresente o seu projeto como um produto que será oferecido a sites de e-commerce.

Com esses Problemas apresentados, foi feita a análise inicial e formulado as hipóteses do problema.

### Sobre o Dataset

O Dataset contém informações dos produtos da empresa japonesa mercari, no qual, tem os seguintes atributos (sendo 8 atributos no total):

- **train_id**: identificado único de cada anúncio;
- **name**: título do anúncio. Foram removidas as informações de preços dos anúncios para evitar vazamento de informação. Os preços removidos foram preenchidos com [rm];
- **item_condition_id**: condição do item fornecido pelo vendedor. Têm valores variados entre 1 e 5 com a seguinte descrição: 1 - ótimo; 2 - bom; 3 - regular; 4 - ruim; 5 - Péssimo;
- **brand_name** : nome da marca do produto;
- **category**: Lista de categoria ao que o produto pertence;
- **price**: preço do produto em dólar;
- **shipping**: 1 - caso a taxa de envio seja paga pelo vendedor. 0 - caso a taxa de envio seja paga pelo consumidor.
- **item_description**: deve conter descrição detalhada do produto. Foram removidas as informações de preços das descrições para evitar vazamento de informação. Os preços removidos foram preenchidos com [rm].

### Formulação de Hipoteses

Diante disso, foram formulados as seguintes hipoteses:
- **Hipótese 1**: o tempo influencia nos preços? Podem existir produtos com sazonalidade de demanda e oferta que influenciem nos preços. Nesse caso um modelo baseado em séries temporais pode apresentar bons resultados.

- **Hipótese 2**: as características influenciam nos preços? Produtos com características diferentes, podem possuir uma faixa de preços diferentes. Para esse caso um modelo baseado em agrupamento pode apresentar bons resultados.

- **Hipótese 3**: tanto as características quanto o tempo influenciam nos preços? É possível que as hipóteses 1 e 2 sejam verdadeiras, nesse caso seria interessante testar um modelo híbrido com agrupamento e séries temporais pode trazes bons resultados.

- **Hipótese 4**: a marca é relevante na definição de preço? É possível que produtos com características semelhantes possuam faixas de preços bem distintas por causa do atributo marca. Caso afirmativo, separar as marcas que agregam mais valor aos produtos antes de aplicar outros processos pode trazer bons resultados.

- **Hipótese 5**: as condições do produto são relevantes na determinação do preço? É possível que as condições do item usado tenham um peso grande na determinação dos preços de venda dos produtos. Caso afirmativo, dar um maior peso a este atributo pode melhorar os resultados.


Esse projeto contém muitas partes, se quiser acessar, clique no link apontado no sumário abaixo

Versão resumida do Projeto dos processos mais importante:
 
 1 - [Análise Inicial](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/Analise%20Inicial.md)
 
 2 - [Análise de Cluster](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/Analise%20Cluster.md)
 
 3 - [Analise de Cluster no Atributo Título](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/analise%20texto%20titulo.md)
 
 4 - [Análise de Cluster da Descrição do Produto](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/Analise%20descri%C3%A7%C3%A3o%20Produto.md)
 
 5 - [Modelagem](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/Modelagem.md)
 
 6 - [Avaliação do Modelo](https://github.com/duartejr/bootcamp_blue/blob/Gustavo/docs/documenta%C3%A7%C3%A3o/Avalia%C3%A7%C3%A3o%20do%20Modelo.md)
 
 Se quiser ler uma análise mais aprofundada, leia os relatórios:
 
 - [Sprint 1](https://drive.google.com/file/d/1TYEvaB1KXBTU2dMf3ChPgLqYfC2oPxOs/view?usp=sharing)
 
 - [Sprint 2](https://drive.google.com/file/d/18ULRXou3CRGTwraWi-mvnriWqvR80X8f/view?usp=sharing)
 
 - [Sprint 3](https://drive.google.com/file/d/1iMXBcRsYIz6kcgF3kfO-4USL-vdIE3wt/view)
 
 - [Sprint 4](https://drive.google.com/file/d/1gHbDv3Md9hKpFFfxP9Q04awTf96t0AoV/view?usp=sharing)
 



