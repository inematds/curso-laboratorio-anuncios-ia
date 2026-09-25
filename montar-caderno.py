from pathlib import Path
from html import escape as E
import json,zipfile
R=Path(__file__).resolve().parent
cases=[]
def C(slug,title,seconds,img,fixed,rows,voice,check):
 cases.append(dict(slug=slug,title=title,duration=seconds,image=img,fixed=fixed,rows=[dict(time=t,scene=s,image_prompt=ip,motion=mo,review=rv) for t,s,ip,mo,rv in rows],voice=voice,check=check))
C('lume','Lume · anúncio narrado',18,2,'Lanterna cilíndrica magenta, alça preta e uma lente frontal. Pedra escura e ambiente azul. Não representa desempenho real.',[
('0–2','Produto na penumbra','Lanterna inteira sobre pedra escura; contorno magenta visível, espaço para texto no editor.','Câmera fixa; névoa leve.','O produto pode ser reconhecido pelo contorno.'),
('2–4','Feixe aparece','Mesma lanterna acesa; feixe suave na névoa azul.','A névoa se move sem alterar a lente.','Uma lente, uma alça, forma preservada.'),
('4–6','Apresentação inteira','Mesma lanterna totalmente visível sobre a pedra.','Aproximação pequena e lenta.','Nenhuma parte desaparece.'),
('6–8','Textura do corpo','Detalhe do corpo magenta, mesma proporção e material.','Luz varia suavemente; produto parado.','Textura não vira letras ou marca.'),
('8–10','Alça','Detalhe da alça preta presa ao corpo, apoio natural.','Câmera estável.','Alça continua presa e não se multiplica.'),
('10–12','Escala no ambiente','Produto inteiro na mesma pedra, mais espaço azul ao redor.','Névoa passa ao fundo.','A escala não muda durante o clipe.'),
('12–14','Luz e matéria','Lente e corpo visíveis, brilho controlado.','Pequena mudança de luz.','Brilho não apaga a forma do produto.'),
('14–16','Retorno ao conjunto','Mesma composição principal com produto inteiro.','Movimento reduz até parar.','Alça, lente e corpo mantidos.'),
('16–18','Encerramento','Produto inteiro, fundo limpo para frase adicionada no editor.','Câmera fixa.','Nome e identificação cabem sem cobrir o objeto.')],
'Quando tudo parece igual, uma pausa muda o olhar. Lume: imagine outro caminho. Grave em ritmo natural, ouça e distribua a frase pelos 18 segundos. Não corte palavras para caber.',
'Nove cenas, 18 segundos, produto coerente e voz compreensível. Identificação: conceito fictício com IA.')
C('vento','Vento · sequência musical',20,5,'Pessoa adulta de roupa coral, corredor de vidro verde, mesma luz e direção. Quatro clipes editados; não é tomada real única.',[
('0–5','Começar','Pessoa inteira no começo do corredor, braços relaxados.','Começa a caminhar devagar; câmera acompanha.','Corpo, roupa e pilares estáveis.'),
('5–10','Avançar','Use o último quadro limpo anterior; mesma pessoa alguns passos adiante.','Continua na mesma direção.','Posição e escala encaixam na passagem.'),
('10–15','Faixa de luz','Mesma pessoa atravessa uma faixa de sol no piso.','Caminhada pequena, sem giro.','Luz pertence ao espaço, não muda a roupa.'),
('15–20','Parar','Mesmo corredor; pessoa encerra o passo.','Movimento desacelera até parar.','Pés não deslizam e música termina de forma deliberada.')],
'Instrumental do kit ao longo dos 20 segundos. Ouça antes de decidir as emendas. Os intervalos são uma estrutura de estudo, não uma análise de batidas da faixa.',
'Quatro trechos, três emendas conferidas, som contínuo e créditos preservados. Identificação: estudo fictício com IA.')
C('senda','Senda · produto com cinco planos',15,8,'Armação âmbar translúcida, duas lentes escuras, ponte e duas hastes. Papel creme. Sem alegações de proteção ou saúde.',[
('0–3','Inteiro','Óculos inteiros sobre papel creme, margem para as hastes.','Aproximação lenta.','Conjunto reconhecível.'),
('3–6','Papel','Mesma armação, dobra de papel em primeiro plano.','Dobra se move suavemente.','Papel não transforma o produto.'),
('6–9','Material','Detalhe da armação âmbar e da dobradiça.','Câmera quase parada.','Material e junções coerentes.'),
('9–12','Ângulo','Mesma referência, ângulo levemente diferente.','Movimento mínimo, sem giro completo.','Duas hastes sem atravessar lentes.'),
('12–15','Encerramento','Produto inteiro com fundo limpo.','Câmera fixa.','Frase Senda: observe os detalhes legível.')],
'Música autorizada opcional. A peça funciona sem voz. Se usar o trecho do kit, recorte conscientemente para 15 segundos e preserve o crédito.',
'Cinco cenas, 15 segundos, construção coerente e frase legível. Identificação: conceito fictício com IA.')
C('pulso','Pulso · anúncio esportivo reduzido',12,11,'Tênis coral, sola creme, cadarços corais; roupa azul marinho e pista azul. Não promete desempenho nem saúde.',[
('0–4','Produto','Tênis lateral apoiado na pista azul.','Câmera fixa ou aproximação pequena.','Contato com a pista e solado coerentes.'),
('4–8','Preparação','Pessoa adulta parada em pé, braços soltos, roupa azul marinho, calçando a referência.','Pequena mudança de peso.','Duas pernas, dois pés, equilíbrio.'),
('8–12','Um passo','Mesma pessoa e direção, espaço para avançar um pé.','Um passo curto e apoio na pista.','Pé não atravessa chão; corpo não se multiplica.')],
'Três batidas leves gravadas por você podem marcar a edição. São um recurso de ritmo, não um registro cardíaco. Alternativa: primeiro montar em silêncio.',
'Três cenas, 12 segundos, apoio e anatomia conferidos. Identificação: conceito fictício com IA.')
C('arquivo','Arquivo do Vento · primeira pessoa',16,14,'Quatro referências: sala terracota, instrumento astronômico de latão, luvas cinza e luz do teto circular. Não representa local existente.',[
('0–4','Entrada','Visão da entrada para a mesa; luz da abertura circular.','Avanço lento.','Mesa e teto correspondem ao mapa.'),
('4–8','Aproximação','Mesma sala, mesa mais próxima; objeto permanece no centro da ação.','Avanço pequeno, sem atravessar mesa.','Aproximação coerente com a escala.'),
('8–12','Observação','Instrumento de latão próximo; luvas na base do quadro.','Mãos estáveis; leve ajuste do olhar.','Mãos e objeto sem deformação.'),
('12–16','Encerramento','Mesmo ponto de vista, instrumento e sala reconhecíveis.','Movimento termina com calma.','Portas, teto e mesa permanecem no lugar.')],
'Som ambiente próprio ou autorizado, discreto. Pode começar em silêncio para conferir o espaço. Música e susto não são obrigatórios.',
'Quatro cenas, 16 segundos, três passagens espaciais conferidas. Identificação: universo fictício com IA.')
C('dobra','Dobra · demonstração em sete cenas',21,17,'Jo: pele morena, cabelo preto curto, blusa creme. Bolsa retangular de lona oliva com duas alças creme. Personagem e produto fictícios.',[
('0–3','Apresentação','Jo de meio corpo segurando a bolsa inteira.','Fala curta, gestos mínimos.','Veja o formato. Boca e voz conferidas, ou narração identificada.'),
('3–6','Inteiro','Bolsa inteira, mesma referência.','Câmera fixa.','A bolsa por inteiro. Forma retangular preservada.'),
('6–9','Alças','Detalhe das alças creme presas ao corpo da bolsa.','Mão segura sem torcer.','Observe as alças. Mão e tecido não se fundem.'),
('9–12','Tecido','Detalhe da lona oliva.','Aproximação pequena.','Detalhe do tecido. Textura não muda de material.'),
('12–15','Abertura','Bolsa aberta, sem alegação de capacidade ou objetos surgindo.','Movimento mínimo.','Veja a abertura. Bordas e alças coerentes.'),
('15–18','Conjunto','Jo e bolsa inteiras no enquadramento de meio corpo.','Pose simples.','Compare o conjunto. Rosto, roupa e produto preservados.'),
('18–21','Encerramento','Produto visível e espaço para identificação.','Câmera fixa.','Conheça o conceito Dobra. Frase inteira e legível.')],
'Use as sete frases curtas indicadas, com pausas. Voz própria ou sintética permitida. Narração sobre detalhes reduz a necessidade de sincronização. Não invente experiência de compra.',
'Sete cenas, 21 segundos, fala, personagem e bolsa coerentes. Identificação visível: Demonstração fictícia com IA.')
(R/'context/casos.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
head='''<!doctype html><html lang="pt-BR" data-theme="papel"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Caderno de produção · Laboratório de Anúncios</title><link rel="stylesheet" href="assets/aula.css"><style>main{padding-top:28px;padding-bottom:50px}h1{font-family:var(--serif);font-size:clamp(36px,7vw,58px);line-height:1.1}h2{font-family:var(--serif);font-size:32px}section{padding:24px 0;scroll-margin-top:24px}article{padding:20px;border:1px solid var(--line);border-radius:12px;margin:16px 0;background:var(--panel)}article h3{font-size:22px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;background:var(--panel);padding:18px;border:1px solid var(--line)}img{max-width:100%;height:auto;border-radius:12px}audio{width:100%}.small{font-size:16px}a{overflow-wrap:anywhere}</style></head><body><main class="wrap">'''
intro='''<p><a href="curso.html#trilha">← voltar ao curso</a> · <a href="galeria.html">referências didáticas</a></p><h1>Caderno de <em>produção</em></h1><p>Seis casos originais para estudar roteiro, continuidade e montagem. As imagens são referências didáticas criadas no Codex. Não há seis campanhas renderizadas neste kit. Os exercícios pedem que você produza e confira seus próprios arquivos.</p><p><a href="assets/kit-laboratorio.zip" download>Salvar roteiros, referências e faixa de estudo</a> · <a href="assets/roteiros.txt" download>Salvar roteiros em texto</a></p><p>Formato dos seis estudos: vertical 9:16, exportação MP4 em 1080 por 1920 quando seus arquivos permitirem. Não amplie material ruim esperando recuperar detalhe. No editor, confira enquadramento e leitura. As referências do curso são horizontais para leitura; gere suas próprias referências no formato planejado.</p><p>Acrescente identificação legível de conceito ou demonstração fictícia com IA. Confira custos e recursos na conta antes de gerar. Para a produção completa, reserve 28–40 horas, além de filas. A prática de dez minutos é um recorte da etapa, frequentemente a revisão de arquivos já produzidos.</p>'''
nav='<nav aria-label="Casos">'+' · '.join(f'<a href="#{c["slug"]}">{E(c["title"].split(" · ")[0])}</a>' for c in cases)+'</nav>'
parts=[];txt=['LABORATÓRIO DE ANÚNCIOS — ROTEIROS AUTORAIS','Casos fictícios, sem campanhas reais ou resultados alegados.','Formato vertical 9:16. Identifique a ficção com IA na peça.']
for c in cases:
 rows=''.join(f'<article><h3>{i}. {E(x["scene"])} · {x["time"]} s</h3><p><b>Imagem:</b> {E(x["image_prompt"])}</p><p><b>Movimento:</b> {E(x["motion"])}</p><p><b>Conferência:</b> {E(x["review"])}</p></article>' for i,x in enumerate(c['rows'],1))
 parts.append(f'<section id="{c["slug"]}"><h2>{E(c["title"])}</h2><p><b>Ficha fixa:</b> {E(c["fixed"])}</p><img src="assets/img/aula-{c["image"]}.webp" width="1280" height="720" alt="Referência ilustrativa do caso {E(c["title"])}"><p class="small">Imagem didática do Codex; não é quadro extraído de campanha produzida.</p>{rows}<p><b>Som:</b> {E(c["voice"])}</p><p><b>Pronto:</b> {E(c["check"])}</p></section>')
 txt+=['\n'+c['title'],c['fixed']]+[f'{i}. {x["time"]}s — {x["scene"]}\nImagem: {x["image_prompt"]}\nMovimento: {x["motion"]}\nConferência: {x["review"]}' for i,x in enumerate(c['rows'],1)]+['Som: '+c['voice'],'Pronto: '+c['check']]
credit='Carefree — Kevin MacLeod (incompetech.com). Licença CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. Trecho inicial de 20 segundos, convertido para MP3. Fonte: https://incompetech.com/music/royalty-free/index.html?gt=&isrc=USUAN1400037. Obtido pelo INEMAVOX em 25/09/2026. Se alterar volume, duração ou aplicar fades, acrescente essa informação ao crédito.'
process='''CASO:
CENA:
ARQUIVO E TENTATIVA:
REFERÊNCIA USADA:
PEDIDO:
SITUAÇÃO: aprovado / corrigir / pendente
TEMPO DO PROBLEMA:
O QUE OBSERVEI:
ALTERAÇÃO A TESTAR:
TRABALHO ATIVO: medido / estimado / não medido
ESPERA DE PROCESSAMENTO:
TENTATIVAS E CONSUMO CONHECIDO:
LIMITE E ALTERNATIVA:
'''
final='''CASO ESCOLHIDO:
PÚBLICO:
MENSAGEM:
FORMATO:
DURAÇÃO E CENAS:
ARQUIVOS ESPERADOS:
CRITÉRIOS: sequência / identidade / som / leitura / identificação
VERSÃO ANTERIOR:
VERSÃO REVISADA:
MUDANÇA E EFEITO OBSERVADO:
DECISÃO:
ÍNDICE DOS SEIS ESTUDOS:
Lume — 18s — arquivo e situação:
Vento — 20s — arquivo e situação:
Senda — 15s — arquivo e situação:
Pulso — 12s — arquivo e situação:
Arquivo do Vento — 16s — arquivo e situação:
Dobra — 21s — arquivo e situação:
ACABAMENTO FINAL — arquivo e situação:
FONTES E CRÉDITOS:
PENDÊNCIAS REAIS:
'''
end=f'''<section id="musica"><h2>Faixa de estudo · 20 segundos</h2><audio controls preload="metadata" src="assets/audio/carefree-20s.mp3"></audio><p><a href="assets/audio/carefree-20s.mp3" download>Salvar a faixa</a></p><pre>{E(credit)}</pre><p><a href="https://incompetech.com/music/royalty-free/index.html?gt=&amp;isrc=USUAN1400037">Fonte da música</a> · <a href="https://creativecommons.org/licenses/by/4.0/">Licença CC BY 4.0</a></p></section><section id="processo"><h2>Ficha de processo</h2><pre>{E(process)}</pre></section><section id="final"><h2>Ficha de acabamento e índice</h2><pre>{E(final)}</pre></section><p><a href="curso.html#trilha">Voltar à trilha</a></p></main></body></html>'''
(R/'caderno.html').write_text(head+intro+nav+''.join(parts)+end)
(R/'assets/roteiros.txt').write_text('\n\n'.join(txt)+'\n\n'+process+'\n'+final+'\n\nCRÉDITO\n'+credit+'\n')
(R/'assets/CREDITOS.txt').write_text(credit+'\n\nImagens: ilustrações originais geradas pelo recurso nativo do Codex. Não representam pessoas, produtos, locais ou campanhas reais. Diagramas e textos: autoria INEMA.CLUB.\n')
with zipfile.ZipFile(R/'assets/kit-laboratorio.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in ['assets/roteiros.txt','assets/CREDITOS.txt','assets/audio/carefree-20s.mp3']:z.write(R/f,f.removeprefix('assets/'))
 for c in cases:z.write(R/f'assets/img/aula-{c["image"]}.webp','referencias/'+c['slug']+'.webp')
# Full named sequence is shown in the lesson's second teaching visual.
extra={}
for i,c in enumerate(cases):
 rows=''.join(f'<div class="item doc"><span class="pin">{j}</span><div><b>{E(x["scene"])} · {x["time"]} s</b><br>{E(x["review"])}</div></div>' for j,x in enumerate(c['rows'],1))
 extra[str(i*3+1)]=f'<figure class="largo"><div class="janela"><div class="tela-top">Roteiro preenchido · {E(c["title"])}</div><div class="janela-body">{rows}</div></div><figcaption>Plano autoral de {c["duration"]} segundos. O caderno detalha imagem, movimento e som de cada cena.</figcaption></figure>'
(R/'context/visuais-extras.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2)+'\n')
# Gallery distinguishes didactic images from unproduced video.
gallery=head.replace('Caderno de produção','Galeria didática')+'<p><a href="curso.html#trilha">← curso</a> · <a href="caderno.html">caderno</a></p><h1>Referências <em>didáticas</em></h1><p>Imagens criadas no Codex para ensinar escolhas. Não são quadros extraídos de seis anúncios produzidos. As atividades de geração exigem seus próprios arquivos. Os pares 2/3, 5/6, 8/9, 14/15 e 17/18 usam referência anterior, mas ainda exigem comparação.</p>'
ls=json.loads((R/'context/aulas-editoriais.json').read_text())
for n,d in enumerate(ls,1):gallery+=f'<section id="imagem-{n}"><h2>{n}. {E(d["titulo"])}</h2><img src="assets/img/aula-{n}.webp" width="1280" height="720" loading="lazy" alt="{E(d["observacao"])}"><p>{E(d["observacao"])}</p><p><a href="assets/img/aula-{n}.webp" download>Salvar referência didática</a> · <a href="curso.html#aula-{n}">Abrir aula</a></p></section>'
(R/'galeria.html').write_text(gallery+'</main></body></html>')
