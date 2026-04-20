# Carvalhaes Comercial - Gestão de Orçamentos

Repositório dedicado à criação e gerenciamento de orçamentos da Carvalhaes Comércio e Serviços.

## Estrutura do Projeto
- `assets/`: Logo e elementos visuais da empresa.
- `orcamentos/clientes/`: Pastas organizadas por cliente contendo arquivos Markdown de orçamento.
- `scripts/`: Scripts para automação de exportação e processamento.
- `templates/`: Modelos de orçamento e estilos CSS.

## Regras de Negócio e Processos

### 1. Dados da Empresa
Os dados oficiais (CNPJ, Endereço, Contato) estão centralizados no arquivo `dados_empresa.json` na raiz do projeto.

### 2. Gerenciamento de Imagens nos Orçamentos
Sempre que um orçamento possuir imagens comprobatórias ou técnicas:
- Elas devem ser salvas na pasta do cliente específico.
- O script de geração de PDF deve ser configurado para anexar automaticamente todas as imagens encontradas na pasta ao final do documento.

### 3. Padrão de Nomenclatura
- Clientes: `nome-do-cliente` (kebab-case).
- Arquivos: `YYYY-MM-DD-orcamento-descrição.md`.

## Comandos Úteis
- Gerar PDF: `python scripts/gerar_orcamento.py <caminho_do_arquivo>`
