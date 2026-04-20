# Carvalhaes Comercial - Orçamentos

Este repositório gerencia a geração de orçamentos profissionais para a Carvalhaes Comércio e Serviços.

## Identidade Visual
As cores utilizadas nos documentos seguem a paleta oficial extraída do logo:
- **Azul Primário**: `#0054A6` (Títulos e Tabelas)
- **Vermelho Secundário**: `#E30613` (Destaques e Seções)

## Como Criar um Orçamento
1. Crie uma pasta em `orcamentos/clientes/nome-do-cliente/`.
2. Adicione um arquivo `.md` com os itens do orçamento.
3. Se houver fotos dos produtos ou do local, coloque-as na mesma pasta.
4. O script de geração converterá o Markdown em um PDF elegante com as fotos ao final.

## Requisitos
- Python 3.x
- `weasyprint` (para conversão de HTML/CSS para PDF)
