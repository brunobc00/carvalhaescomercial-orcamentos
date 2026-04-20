import sys
import os
import markdown
import json
from weasyprint import HTML, CSS
from pathlib import Path

def gerar_pdf(md_path):
    # Caminhos base
    base_dir = Path(md_path).parent
    repo_root = Path(__file__).parent.parent
    output_pdf = base_dir / f"{Path(md_path).stem}.pdf"
    
    # Carrega dados da empresa
    with open(repo_root / "dados_empresa.json", "r") as f:
        empresa = json.load(f)
    
    # Lê o Markdown
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Converte MD para HTML
    html_content = markdown.markdown(md_content, extensions=['tables'])
    
    # Procura imagens na pasta do cliente
    images_html = ""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = [f for f in os.listdir(base_dir) if f.lower().endswith(valid_extensions)]
    
    if image_files:
        images_html = '<div class="gallery"><h2>Galeria de Fotos</h2>'
        for img in image_files:
            img_path = (base_dir / img).as_uri()
            images_html += f'<div class="gallery-item"><img src="{img_path}"><p>{img}</p></div>'
        images_html += '</div>'

    # Template HTML final
    full_html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Orçamento</title>
    </head>
    <body>
        <div class="header-logo">
            <!-- Espaço para o logo via CSS @page ou img -->
        </div>
        
        {html_content}
        
        {images_html}
    </body>
    </html>
    """
    
    # Aplica o CSS
    css_path = repo_root / "templates" / "orcamento.css"
    
    # Gera o PDF
    HTML(string=full_html, base_url=str(base_dir)).write_pdf(
        str(output_pdf),
        stylesheets=[CSS(filename=str(css_path))]
    )
    
    print(f"✅ PDF gerado com sucesso: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python gerar_orcamento.py <caminho_do_arquivo.md>")
    else:
        gerar_pdf(sys.argv[1])
