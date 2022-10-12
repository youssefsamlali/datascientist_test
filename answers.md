## Question 1)
pour détecter les anomalies je regarde df.info et df.describe ça me donne une première idée sur le type de données que je possède
et leur distribution afin de voir les valeurs nulls et abbérantes
par exemple :
?? transaction 680_4_43277 avec montant négatif (ça peut être lié à un remboursement ? )
les produits 43;44;45 n'ont pas de marque

## Question 3)
A seasonal product category is a category of products saled in a specific season it could be a specific day or days of the week or a month or months in a year etc
for example 'sapin/calendrier/chocolat de noel' / 'plage en été'
a seasonality can increase or decrease turnover
other exogenous characteristics that can affect the sales performance of a product are climate / political mondial situation etc
For example the actual situation with oil because of the war in ukraine

## Question 4)
le biais qu'il peut y avoir est un biais de selection les stores ou des produits séléctionnées ne sont pas représentatifs de la catégorie
et en plus nous avons pas d'historique (uniquement 3 mois de données)
pour corriger le biais nous devons selectionner plus de transactions dans différents stores et avoir un historique plus élargis

## Question 8)
on remarque que le turnover a baissé d'environ 26% entre P1 et P2, ce qui reste stable c'est la moyenne des chekout par client
donc les clients continuent d'acheter le meme nombre de fois mais avec des quantitées moins, le nombre de client a aussi connu une baisse de 12%

## Question 1O)
Pour la première campagne de réactivation, on peut regarder si les clients perdus dans la periode 2 revienent après la camapgne
Concernant la deuxième campagne, on peut regarder si les clients fidèles ont augementé leur quantité achetés par période et donc leur turnover


