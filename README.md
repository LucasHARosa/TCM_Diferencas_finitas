<h1 align="center">TCM Diferencas finitas</h1>

<h3>Trabalho Computacional - Solução de Equações Diferenciais utilizando Diferenças Finitas </h3>

<p>O trabalho computacional a ser realizado possui como objetivo a resolução numérica da equação da difusão de calor em um domínio com uma condição de contorno específica.</p>

<h2>Objetivo</h2>
<p> Esse trabalho consiste em solucionar para a figura abaixo a difusão de calor de forma transiente sem geração de energia interna. </p>  
<p align="center" >
<img  src = "https://user-images.githubusercontent.com/65405310/168137855-69f28887-b315-4a5d-867e-596aca0cb61a.jpg" alt="desafio" class="center">
</p>
<p>A equação transiente da difusão de calor, onde não há geração interna de energia pode ser expressa como:</p>
<p align="center" >
<img  src = "https://user-images.githubusercontent.com/65405310/168138894-3fc0660d-c0f8-4721-b407-1dacb70b6c0c.png" alt="desafio" class="center">
</p>
<p>Em que rho é a massa específica do meio contínuo analisado (seja ele sólido ou fluido), Cp é o calor específico à pressão constante (uma propriedade material do meio analisado), k é a condutividade térmica do meio, T denota o campo de temperatura, t é a variável tempo e nabla^2 representa o operador escalar Laplaciano

Utilizaremos um método numérico para aproximar um resultado da equação diferencial apresentada, que se chama "Método das diferenças finitas", para utilizarmos esse método na figura precisamos discretizar o domínio através de uma malha. Olhando para essa malha discretizada é possível obter uma expressão mais fácil de se trabalhar, tendo em conta os nós da malha é possível chegar a:</p>
<p align="center" >
<img  src = "https://user-images.githubusercontent.com/65405310/168155938-c7ae2cda-96b0-4eaf-95c7-42ef08c108c3.png" alt="desafio" class="center">
</p>
<p>Sendo o índice (p) o instante de tempo anterior, logo (p+1) o instante atual, (m,n) nesse caso é o nó em questão, T é a temperatura e Fo é expresso por:</p>
<p align="center" >
<img  src = "https://user-images.githubusercontent.com/65405310/168157581-81d739e9-b7c8-492c-935e-49173196d164.png" alt="desafio" class="center">
<img  src = "https://user-images.githubusercontent.com/65405310/168157591-b8dab0b9-021e-4e21-a1b1-abce04891fab.png" alt="desafio" class="center">
</p>
<h2> Resultados </h2>
