# Redução de amostragem em imagens monocromáticas

Esse projeto aplica 3 técnicas de redução de amostragem. Abaixo estão as instruções de como executar o código e uma explicação da estrutura das pastas e parâmetros.

## Parâmetros

O script aceita três parâmetros:

### Parâmetro 1: Nome do Arquivo

Este parâmetro espera um arquivo do tipo imagem. Os tipos de imagem válidos são:

- `.png`
- `.jpg`
- `.jpeg`
- `.gif`
- `.bmp`

Se o arquivo não for um dos tipos acima, uma mensagem de erro será exibida e o script será encerrado.

### Parâmetro 2: Porcentagem de Redução

Este parâmetro espera um valor numérico entre 0 e 100. O valor será dividido por 100, já que se assume que está sendo passada uma porcentagem.

Se o valor não estiver entre 0 à 100, uma mensagem de erro será exibida e o script será encerrado.

### Parâmetro 3: Técnica

Este parâmetro espera um dos seguintes valores:

- `moda`
- `mediana`
- `média`

Se a técnica não for uma das acima, uma mensagem de erro será exibida e o script será encerrado.

## Exemplo de Uso

Para executar o código, use o seguinte comando:

```
python3 main.py x.png 70 média
```

## Estrutura das Pastas

### `constants`

Este módulo contém valores constantes que são usados em todo o projeto.

### `param_utils`

Este módulo é responsável por tratar e verificar erros relacionados aos parâmetros.

### `image_utils`

Este módulo lida com a exibição e abertura da imagem. Também lança um erro se a imagem não puder ser aberta.

### `sampling_techniques`

Este módulo aplica a técnica de redução de amostragem especificada à imagem e retorna a imagem processada.

### `main`

Este é o código principal que une tudo. Ele executa as seguintes tarefas:

- Abre a imagem em escala de cinza
- Lê e verifica os parâmetros
- Aplica a técnica de amostragem especificada à imagem
- Exibe a imagem resultante na tela.
