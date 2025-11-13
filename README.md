# Img Seg 🚀

Img Seg é um aplicativo simples em Gradio para remoção de fundos em imagens usando um pipeline de segmentação do Hugging Face. O app carrega um modelo remoto e aplica uma máscara para gerar uma imagem PNG com fundo transparente pronta para download.

## Demo (deploy)
Você pode testar o app imediatamente no Hugging Face Spaces (deploy público):

[👉 Abrir Img Seg no Hugging Face Spaces](https://huggingface.co/spaces/ka-yas/img_seg)

Use este link para abrir a interface web já hospedada — basta fazer upload da sua imagem, aguardar a segmentação e baixar o PNG resultante.

## Como usar

1) Usar o deploy (recomendado — mais simples)

- Acesse o link acima.
- Clique em "Upload" ou arraste a sua imagem para a área indicada.
- Aguarde o processamento (pode levar alguns segundos dependendo do modelo e da imagem).
- Baixe a imagem resultante em PNG (com fundo transparente).

2) Executar localmente (opcional)

Se preferir rodar o app na sua máquina:

```bash
pip install -r requirements.txt
python app.py
```

Após executar, o Gradio exibirá uma URL local (e possivelmente um link público temporário) para abrir a interface no navegador.

## Principais arquivos

- `app.py` — interface Gradio e função principal `remove_background`.
- `requirements.txt` — dependências do projeto.
- `pyproject.toml` — metadados do projeto.
- `.gitattributes` — configuração de LFS para arquivos grandes.

## Observações técnicas

- A função principal é `remove_background` em `app.py`, que inicializa um pipeline `image-segmentation` do Hugging Face e aplica a máscara para gerar o PNG com transparência.
- Modelo usado (no deploy): `briaai/RMBG-1.4`.

## Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request para sugestões, correções ou melhorias. Exemplos de melhorias úteis: adicionar testes, otimizar processamento, adicionar upload em lote ou salvar configurações.

## Licença

Adicione aqui a licença do projeto (ex.: MIT) conforme preferir.

---

Se quiser, posso também:

- Adicionar um badge de status ou um GIF demonstrativo.
- Incluir instruções para deploy automático no Hugging Face (se desejar automatizar o CI/CD).
- Traduzir o README ao inglês.

