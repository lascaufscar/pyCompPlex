**CompPlex Tools: Ferramenta para cálculo de medidas de complexidade em imagens
de sensoriamento remoto acoplada em SIG livre**

**1 Introdução**

O conceito de entropia da informação é especialmente interessante quando se
estudam paisagens a partir de imagens de sensores remotos, como satélites e
veículos aéreos não tripulados (VANTs). A variabilidade nos valores de pixels em
uma imagem de sensor remoto representa a diversidade de informações presentes em
uma paisagem e suas unidades e pode servir, por exemplo, para estimar a mudança
na quantidade de informações no sistema causada pela fragmentação.

Os scripts CompPlex Tools foram criados para permitir o cálculo da entropia da
informação (He), variabilidade (He/Hmax) e medidas de López-Ruiz, Mancini e
Calbet (LMC) e Shiner, Davison e Landsberg (SDL). O CompPlex HeROI possibilita o
cálculo dessas medidas para diferentes regiões de interesse (ROIs) selecionadas
em uma imagem de satélite da área de estudo, seguida da comparação da
complexidade de seus padrões, além de possibilitar a geração de assinaturas de
complexidade para cada ROI. O CompPlex Janus possibilita espacializar os
resultados dessas quatro medidas em mapas de complexidade da paisagem enquanto
que o CompPlex Chronos possibilita uma análise multitemporal das métricas, pixel
a pixel, em imagens de diferentes datas.

**2 Cálculos das medidas de complexidade**

Aplicando-se a teoria informacional de Shannon (1949) aos dados de reflectância
em uma banda de uma imagem de SR, e estes sendo representados por sua
discretização em números digitais (DN) à medida que a ocorrência de um
determinado grupo de valores de DN se torna mais provável do que outros valores,
a entropia da imagem decresce. O valor máximo da entropia da imagem neste caso
somente seria atingido quando a ocorrência dos valores de DN na imagem é
equiprovável, não havendo tendência de concentração de probabilidades de um
determinado valor.

Sendo N o número de estados de DN (quantidade de valores de DN sem repetições)
em uma amostra de pixel selecionados na imagem temos que a entropia máxima
admitida para esta amostra é:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image002.png?raw=true)

Dividindo-se o total de valores de um determinado estado de DN pelo total de
pixel da amostra temos a probabilidade P(DN) de ocorrência deste valor dentro da
amostra. A entropia de Shannon para a amostra é então calculada como:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image003.png?raw=true)

Outras medidas de complexidade utilizadas baseiam-se na percepção do
desequilíbrio entre os estados de informação.

Segundo apresentam Lopez-Ruiz, Mancini e Calbet (2010) o desequilíbrio D pode
ser mensurado segundo uma distância entre o estado atual do sistema e a condição
de equilíbrio que é calculada como:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image005.png?raw=true)

Sendo:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image007.png?raw=true)

Temos que:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image009.png?raw=true)

Shiner, Davison, and Landsberg Shiner, Davison, and Landsberg Shiner, Davison e Landsberg (1999) já haviam proposto calcular o desequilíbrio
D’ como o complemento do equilíbrio, sendo:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image011.png?raw=true)

E assim, temos que:

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image013.png?raw=true)


**3 A Ferramenta CompPlex Tools**

A ferramenta CompPlex foi desenvolvida com a linguagem de script Python na forma
de um Plugin para o software livre de SIG QGIS 3. Foram utilizadas, e assim são
requisitos para a sua utilização, as bibliotecas Python GDAL, NUMPY, NUMBA,
RASTERIO e PANDAS. A inclusão da ferramenta ao QGIS se dá por meio de um plugin
criado pela ferramenta Plugin Builder, em que todos os arquivos python
necessários são armazenados num diretório, que deve ser copiado para o
diretórios de plugins do QGIS para o perfil padrão.

Este plugin insere à interface do QGIS uma nova toolbar de onde pode-se acessar
as três ferramentas para cálculo das métricas de complexidade.

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image015.png?raw=true)

Barra de ferramentas CompPlex Tools

A ferramenta possui três funções principais. Uma para o cálculo das métricas a
partir de regiões de interesse (HeROI), outra para cálculo das métricas para a
imagem completa a partir de Kernels (Janus) e outra para a análise multitemporal
das métricas, pixel a pixel, em imagens de diferentes datas (Chronos).

**3.1 CompPlex HeROI**

O objetivo da ferramenta é apresentar os resultados dos cálculos de complexidade
em uma imagem de sensoriamento remoto para determinadas regiões de interesse
(ROIs). As ROIs são feições do tipo polígono que delimitam as áreas de interesse
para os cálculos. Os resultados são armazenados num arquivo de texto CSV e
incluídos ao projeto QGIS na forma de uma tabela.

Os cálculos são realizados para todas as bandas de uma imagem, no caso desta ser
multibanda, e cada ROI é identificada por meio de um identificador escolhido da
tabela de atributos do plano de informação ROI Layer.

A utilização da ferramenta se dá por meio de uma caixa de diálogo que é acessada
pela ToolBar CompPlex Tools na área de ferramentas do QGIS .

Nesta caixa de diálogo tem-se acesso a três caixas de seleção (CS). As duas
primeiras CS permitem selecionar layers presentes no projeto. A primeira CS
possui um filtro para layers do tipo imagem e a segunda CS um filtro para layers
vetoriais do tipo polígonos. A terceira CS está vinculada a segunda e permite
selecionar um dos campos da tabela de atributos da layer selecionada na segunda
CS.

Um botão abre uma caixa de diálogo para escolher o diretório e nome de arquivo,
com um filtro para arquivos texto do tipo CSV, para salvar o resultado do
processamento.

Depois da seleção dos parâmetros a ferramenta é executada clicando-se no botão
OK, os cálculos são realizados e salvos no arquivo selecionado e uma tabela com
o nome Resultados é adicionada ao projeto ficando visível no painel de layers,
podendo ser aberta com o comando Open Attribute Table.

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image017.png?raw=true)

Caixa de diálogo para seleção de parâmetros da ferramenta HeROI

O algoritmo possui duas funções principais. A primeira delas seleciona os pixels
que se sobrepõem a uma feição (polígono) e armazena seus valores num array e,
além disso, já calcula para esta feição os valores de estatísticas descritivas
(count, min, max, mean e std) para os pixels selecionados. A segunda usa o array
de saída da primeira função para calcular os valores de complexidade (He, Hmax,
He/Hmax, N, SDL e LMC) referentes àquela feição.

Para realizar o cálculo para todas as bandas e todas as feições são utilizados
dois loopings encadeados, o primeiro para o número de bandas da imagem e o
segundo para o número de feições da ROI Layer.

Os resultados dos cálculos de cada feição vão sendo armazenados numa estrutura
de dados do tipo tabela da biblioteca Pandas do Python e ao final do looping
esta tabela é convertida e salva para um arquivo texto CSV.

**3.2 CompPlex Janus**

No caso da ferramenta para o cálculo das métricas de complexidade para toda uma
imagem (Janus) e que o resultado seja também uma imagem com os valores da
métrica selecionada o algoritmo funciona como os algoritmos tradicionais de
filtragem. O usuário seleciona o tamanho de uma janela móvel para realizar os
cálculos por meio de uma convolução.

Neste caso a convolução tem o papel de fazer uma filtragem para extração de
informações de interesse na imagem aos quais são aplicados a função da métrica
selecionada. Mais especificamente, o uso desse filtro é feito através de
matrizes denominadas máscaras ou kernels - como são mais conhecidos na prática.

Durante a aplicação da convolução em uma imagem, o kernel vai se deslocando ao
longo da imagem, como uma janela móvel, que vai selecionando os valores de DN
aos quais se aplica a função da métrica selecionada e o resultado deste cálculo
vai formando uma nova imagem com o seu valor ocupando a posição central do
kernel.

Na figura podemos ver a seleção de DNs por meio do Kernel e o valor da função de
complexidade formando uma imagem de saída.

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image019.jpg?raw=true)

Princípio da janela móvel para a convolução

A utilização da ferramenta se dá por meio de uma caixa de diálogo que é acessada
pela ToolBar CompPlex Tools na área de ferramentas do QGIS .

Nesta caixa de diálogo tem-se acesso a três caixas de seleção (CS). A primeira
CS permite selecionar rasters presentes no projeto, esta CS possui um filtro
para layers do tipo imagem. A segunda CS possui tamanhos pré determinados de
janelas móveis que podem ser selecionados para os cálculos. A terceira CS
permite selecionar qual a métrica de complexidade será utilizada para calcular a
nova imagem.

Um botão abre uma caixa de diálogo para escolher o diretório e nome de arquivo,
com um filtro para arquivos texto do tipo tiff, para salvar o resultado do
processamento.

Depois da seleção dos parâmetros a ferramenta é executada clicando-se no botão
OK, os cálculos são realizados e a imagem é salva no arquivo selecionado.

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image021.jpg?raw=true)

Caixa de diálogo para seleção de parâmetros da ferramenta Janus

O algoritmo lê a imagem raster e a coverte num array (rows x cols). Inicia então
uma convolução com dois loopings encadeados percorrendo linhas e colunas do
array onde aplica a máscara de acordo com o tamanho da janela móvel selecionada
e chama uma função principal que calcula a métrica de complexidade selecionada
para os DN contidos na mácara e armazena o resultado num novo array na mesma
posição. Ao final da convolução o novo array é convertido numa imagem raster e
salvo no arquivo selecionado.

**3.3 CompPlex Chronos**

A ferramenta Chronos destina-se à uma análise multitemporal das métricas de
complexidade. Para isso é necessário imagens de diferentes épocas para um mesmo
local, com a mesma resolução espacial, o mesmo sistema de referência, para que
cada pixel nas diferentes imagens representem o mesmo local. Além disso, seria
interessante que o sensor também fosse o mesmo a fim de evitar-se problemas
decorrentes de calibração.

A utilização da ferramenta se dá por meio de uma caixa de diálogo que é acessada
pela ToolBar CompPlex Tools na área de ferramentas do QGIS.

Nesta caixa de diálogo tem-se acesso a dois botões que abrem uma caixa de
diálogo para escolher um diretório de dados de entrada e um diretório de dados
de saída. Nesta ferramenta basta selecionar o diretório onde estão contidos os
arquivos rasters do formato tiff, e todos os arquivos com este formatos serão
utilizados como dados de entrada para a análise multitemporal. Da mesma forma
para os arquivos de saída basta-se escolher o diretório e nele serão salvos
quatro arquivos tiff, um para cada métrica (He, He/HMax, SDL e LMC), como
resultados da análise.

![fig1](https://github.com/bielenki/pyCompPlex/blob/main/CompPlex_arquivos/image023.jpg?raw=true)

Caixa de diálogo para seleção de parâmetros da ferramenta Chronos

O algoritmo lê cada imagem raster de formato tiff contido no diretório
selecionado para os dados de entrada e as coverte em arrays (rows x cols) e os
salva numa lista de arrays. É como se tivéssemos um array de N dimensões sendo N
o número de imagens tiff contidas no diretório.

Com três loopings encadeados (rows, cols e arrays nas lista) percorre-se todos
os pixels das imagens, a cada rodada no looping os pixels da posição (row, col)
de todas as imagens são armazenados num vetor, que é repassado a uma função
principal que calcula as quatros métricas de complexidade com base nos valores
de DN contidos nesse vetor. O valor de cada uma delas é armazenado em um novo
array exatamente na posição (row x col). Ao final da convolução os quatro novos
arrays são convertidos em imagens e salvos no diretório de dados de saída
escolhido.
