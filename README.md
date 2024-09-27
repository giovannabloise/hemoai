# hemoAI :microscope:

Uma ferramenta de machine learning para identificação de lâminas de sangue utilizando o Teachable Machine (https://teachablemachine.withgoogle.com/).

O script permite a identificação de algumas condições hematológicas da série eritrocítica, como hemácias normais, anemia falciforme, malária e tripanossomíase, a partir de esfregaço sanguíneo.

## Treinamento do modelo

Para treinamento, foram utilizadas bases do kaggle + curadoria manual de fotos de esfregaço sanguíneo contendo hemácias normais, sangue infectado com tripanossoma, hemácias infectadas com plasmodium (anel de bacharel) e lâminas de anemia falciforme (drepanócitos).

![image](https://github.com/user-attachments/assets/369a598f-9e2e-4fe6-874b-aff13e45c6ac)

## Requisitos
- **Bibliotecas necessárias**:
  - `numpy`
  - `click`
  - `tensorflow`
  - `keras`
  - `Pillow`

## Instalação

1. **Crie um ambiente Conda**:

   ```bash
   conda create --name hemoAI python=3.10
   
   conda activate hemoAI

2. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>
   pip install .
   ```

## Modo de Uso

```
python hemoai.py --image-path path/to/your/image.jpg
```
