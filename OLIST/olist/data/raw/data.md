# Brazilian E-Commerce Public Dataset by Olist

## Bases de Dados

Este projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist**,
disponibilizado pela Olist no Kaggle.

O conjunto de dados contém informações anonimizadas de aproximadamente
**100 mil pedidos realizados entre 2016 e 2018**, envolvendo clientes,
vendedores, produtos, pagamentos, avaliações e informações geográficas.

As bases disponíveis são:

  -----------------------------------------------------------------------------
  Arquivo                                   Descrição
  ----------------------------------------- -----------------------------------
  `olist_orders_dataset.csv`                Informações dos pedidos realizados
                                            pelos clientes, incluindo status,
                                            datas de compra, aprovação, entrega
                                            e previsão de entrega.

  `olist_customers_dataset.csv`             Dados dos clientes, contendo
                                            identificadores, localização (CEP,
                                            cidade e estado) e informações
                                            relacionadas ao consumidor.

  `olist_order_items_dataset.csv`           Relação dos produtos associados aos
                                            pedidos, contendo vendedor,
                                            produto, quantidade, preço e
                                            informações de frete.

  `olist_products_dataset.csv`              Informações dos produtos
                                            comercializados, incluindo
                                            categoria, dimensões, peso e
                                            características do item.

  `olist_sellers_dataset.csv`               Dados dos vendedores presentes na
                                            plataforma, incluindo localização e
                                            identificação do vendedor.

  `olist_order_payments_dataset.csv`        Informações dos pagamentos
                                            realizados nos pedidos, como tipo
                                            de pagamento, quantidade de
                                            parcelas e valor pago.

  `olist_order_reviews_dataset.csv`         Avaliações dos clientes sobre os
                                            pedidos, incluindo nota,
                                            comentários e datas de criação e
                                            resposta da avaliação.

  `olist_geolocation_dataset.csv`           Dados geográficos relacionando CEPs
                                            brasileiros com coordenadas e
                                            localidades.

  `product_category_name_translation.csv`   Tradução dos nomes das categorias
                                            de produtos do português para o
                                            inglês.
  -----------------------------------------------------------------------------

## Relacionamento Geral das Bases

A estrutura principal do dataset segue o fluxo:

    Clientes
       |
       ↓
    Pedidos
       |
       ↓
    Itens do Pedido
       |
       ↓
    Produtos / Vendedores

    Pedidos
       |
       ↓
    Pagamentos

    Pedidos
       |
       ↓
    Avaliações

## Observações

-   Os dados são anonimizados.
-   Os identificadores presentes nas tabelas permitem o relacionamento
    entre diferentes bases.
-   A análise inicial será realizada utilizando principalmente a base:

`olist_orders_dataset.csv`

Esta tabela será utilizada como ponto inicial para análise exploratória
e geração de relatórios de qualidade dos dados.
