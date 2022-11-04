# EDA Análise de Clusters

Para explorar melhor a análise, foi feita a análise de cluster para explorar melhor o dataset, desta forma foi aplicado o algoritmo kmeans, aplicado o metodo do cotovelo, no qual indicou a divisão em cinco clusters, mas a análise mostrou que quatro seria melhor.

Feito a clusterização em quatro clusters, a divisão ficou, principalmente, entre os preços dos produtos, que ficou da seguinte forma

- **Cluster 0**: Produtos entre 3 e 42 dólares;
- **Cluster 1**: Produtos entre 42,50 a 141 dólares;
- **Cluster 2**: Produtos acima de 482 dólares;
- **Cluster 3**: Produtos de 142 a 481 dólares

Quanto às categorias, “Women” é a que possui a maioria dos produtos em  
todos  os  clusters,  seguida  pela  categoria  “Eletronics”,  que  se  destaca com a  segunda maior quantidade de produtos nos clusters 3 e 2.

![image](https://user-images.githubusercontent.com/39843884/199980495-756fc004-dd55-4d6a-adb5-cd1ebf1d67d9.png)
![image](https://user-images.githubusercontent.com/39843884/199980716-8c674527-e791-48bc-a6b5-6e693f0c4ed6.png)
![image](https://user-images.githubusercontent.com/39843884/199981037-660c0b9b-0571-429d-a80a-4ccf8ff21673.png)
Interessante notar também a distribuição de produtos por marca dentro de  
cada cluster. Os produtos sem marca (“No brand”) possuem as maiores quantidades  nos clusters 0, 1 e 3, já no cluster 2, a marca que mais possui produtos é a Louis Vuitton.

![image](https://user-images.githubusercontent.com/39843884/199982591-280e2bc0-31f1-4b42-8877-391595770afd.png)
![image](https://user-images.githubusercontent.com/39843884/199982767-a2b102d1-4b8b-42ad-b006-e5fedf4aaa9b.png)
![image](https://user-images.githubusercontent.com/39843884/199982973-409ca15c-301f-49cd-9d44-16c522744d9a.png)
![image](https://user-images.githubusercontent.com/39843884/199983297-9dc692bd-4a05-4359-94f6-4ea2a4233219.png)
Para ler uma análise mais aprofundada, veja esse relatório [aqui](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d9f2f2d5-6be4-4723-8959-26bafb1a4950/relatorio_sprint_2-1.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221104T125353Z&X-Amz-Expires=86400&X-Amz-Signature=3bdfbbd07449fe09571d9500eb28d0a4d4746cc934dd318644a794b81a7355c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22relatorio_sprint_2-1.pdf%22&x-id=GetObject)
