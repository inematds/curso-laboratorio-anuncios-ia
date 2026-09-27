# Laboratório de Anúncios com IA v6.2

Curso aberto INEMA.CLUB. 24 aulas em 8 módulos, estilo OSWork v6.2. Seis casos originais e fictícios: Lume, Vento, Senda, Pulso, Arquivo do Vento e Dobra.

Estimativa completa: 28–40 horas de estudo e produção, além de filas. Requer saber gerar imagens, clipes e editar, ou cursar previamente Prompting, Kling e CapCut.

Ilustrações geradas pelo recurso nativo de imagens do Codex. A ferramenta não expõe seletor ou confirmação de uma versão chamada 2.5; não foi substituída por serviço externo. O curso fornece roteiros, referências, pedidos e faixa licenciada. Não fornece seis campanhas renderizadas nem alega execução de testes de vídeo nos serviços externos. As atividades exigem arquivos produzidos pelo aluno; pendência não equivale a conclusão.

O kit reutiliza trecho de Carefree, Kevin MacLeod, CC BY 4.0, obtido pelo INEMAVOX e creditado. Não publica material privado do acervo de análise.

Reconstrução: python3 montar.py. Evidências em context/.

## English / Español

[English](https://inematds.github.io/curso-laboratorio-anuncios-ia/en/) · [Español](https://inematds.github.io/curso-laboratorio-anuncios-ia/es/)

Textos traduzidos com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa. Ilustrações originais compartilhadas; progresso e anotações separados por idioma.

Após montar o português, reaplique os catálogos salvos:

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/curso-i18n-checks
```

Requer Python/BeautifulSoup e os pacotes locais Babel/Playwright indicados nos scripts. A montagem não chama modelos nem redes. Mudanças na fonte PT exigem revisar os catálogos `i18n/`. O motor oficial `assets/curso.js` é preservado; a proteção de importação é gerada em `assets/curso-i18n.js` e nas edições traduzidas.

Evidências em `context/validacao-i18n.md`. Revisões por agentes são simuladas, não testes com alunos reais.
