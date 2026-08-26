import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero
html = html.replace(
'''      <div class="hero-content">
        <span class="eyebrow mono">Por que você parou de crescer?</span>
        <h1>Você faz 4 séries de 10 há semanas, sempre com <span class="accent-text">o mesmo peso</span>, e chama isso de treino.</h1>
        <p class="lead">Não é. É manutenção. Existe uma diferença técnica entre os dois — e ela é o motivo exato pelo qual você parou de crescer. Descubra qual é, hoje.</p>
        <div class="hero-ctas">
          <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary">Quero Destravar Meus Ganhos</a>''',
'''      <div class="hero-content">
        <span class="eyebrow mono">Por que você parou de evoluir?</span>
        <h1>Você treina há meses, mas seu corpo parece ter parado de <span class="accent-text">evoluir?</span></h1>
        <p class="lead">O Método Destrave foi criado para quem já treina, mas sente que parou de progredir — organizando treino, progressão, nutrição e recuperação em um método claro de aplicação.</p>
        <div class="hero-ctas">
          <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary">Quero Destravar Minha Evolução</a>'''
)

# 2. Identificação
html = html.replace(
'''      <div class="section-head reveal">
        <span class="eyebrow mono">Diagnóstico</span>
        <h2>Antes de responder "por que parei de crescer", veja se isso é você.</h2>
        <p>A maioria dos homens que procura a Destrave Pro chega exatamente neste ponto.</p>
      </div>
      <div class="id-grid">
        <div class="id-card reveal"><span class="id-check">✓</span><p>Treina há meses e simplesmente não cresce mais.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Não consegue aumentar carga, mesmo treinando pesado.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Vive trocando de treino na esperança de "destravar".</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Já tentou suplementos esperando que resolvessem o problema.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Faz tudo "certo" — dieta, treino, descanso — e continua estagnado.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Você aumenta o peso, mas sabe — no fundo — que não fez a última repetição até a falha de verdade.</p></div>
      </div>''',
'''      <div class="section-head reveal">
        <span class="eyebrow mono">Diagnóstico</span>
        <h2>O problema pode não ser falta de esforço.</h2>
        <p>A maioria das pessoas que procura a Destrave Pro chega exatamente neste ponto.</p>
      </div>
      <div class="id-grid">
        <div class="id-card reveal"><span class="id-check">✓</span><p>Você treina há meses e sente que o físico não muda.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Aumenta a carga, mas não percebe evolução proporcional.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Troca de exercícios constantemente na esperança de ver resultados.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Segue dicas diferentes de vários influenciadores na internet.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Sente que está treinando muito, mas evoluindo pouco.</p></div>
        <div class="id-card reveal"><span class="id-check">✓</span><p>Não sabe exatamente quando aumentar carga ou mudar a estratégia.</p></div>
      </div>'''
)

# 3. Add Mechanism & Differentiation and move Depoimentos after VSL
old_depoimentos = '''  <!-- PROVAS SOCIAIS -->
  <section id="depoimentos">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow mono">Quem já leu</span>
        <h2>O que dizem quem já aplicou o método</h2>
      </div>
      <div class="testimonials-grid">
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">O que mais me chamou atenção foi a parte que explica por que a gente entra em platô. Eu treinava há meses fazendo sempre a mesma coisa e nunca tinha parado pra pensar nisso. A parte de RPE, TUT e progressão ficou bem fácil de entender. Já comecei a aplicar algumas mudanças no treino.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">L</span>
            <span class="testimonial-name">Lucas M.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Achei muito legal que ele não fala só de treino. A parte sobre recuperação, alimentação e principalmente disciplina fez bastante sentido pra mim. Percebi que meu erro não era só dentro da academia. É um material bem completo.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">M</span>
            <span class="testimonial-name">Matheus A.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Eu já acompanho bastante conteúdo de musculação, mas mesmo assim aprendi algumas estratégias que nunca tinha usado, como controlar o tempo das repetições e aplicar as técnicas de intensidade da forma certa. A leitura é simples e bem organizada.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">J</span>
            <span class="testimonial-name">João P.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Gostei porque o ebook não fica enrolando. Vai direto ao ponto e explica exatamente o que fazer quando você para de evoluir. O plano de treino de 4 semanas foi o que mais gostei. Dá vontade de colocar em prática na hora.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">R</span>
            <span class="testimonial-name">Rafael S.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">O que mais gostei foi que tudo parece aplicável. Não é aquele monte de teoria difícil. Você termina um capítulo e já sabe exatamente o que testar no treino seguinte. Pra quem sente que estagnou, vale muito a leitura.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">G</span>
            <span class="testimonial-name">Guilherme R.</span>
          </div>
        </div>
      </div>
    </div>
  </section>

'''
html = html.replace(old_depoimentos, "")

vsl_end = '''      <p class="vsl-caption">Vídeo · Como o Destrave Seus Ganhos funciona na prática</p>
      <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary vsl-cta">Quero Destravar Meus Ganhos</a>
    </div>
  </section>'''

new_sections_after_vsl = '''      <p class="vsl-caption">Vídeo · Como o Destrave Seus Ganhos funciona na prática</p>
      <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary vsl-cta">Quero Destravar Minha Evolução</a>
    </div>
  </section>

  <!-- PROVAS SOCIAIS -->
  <section id="depoimentos">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow mono">Quem já aplicou o método</span>
        <h2>Veja o que quem já aplicou está dizendo</h2>
      </div>
      <div class="testimonials-grid">
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">O que mais me chamou atenção foi a parte que explica por que a gente entra em platô. Eu treinava há meses fazendo sempre a mesma coisa e nunca tinha parado pra pensar nisso. A parte de RPE, TUT e progressão ficou bem fácil de entender. Já comecei a aplicar algumas mudanças no treino.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">L</span>
            <span class="testimonial-name">Lucas M.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Achei muito legal que ele não fala só de treino. A parte sobre recuperação, alimentação e principalmente disciplina fez bastante sentido pra mim. Percebi que meu erro não era só dentro da academia. É um material bem completo.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">M</span>
            <span class="testimonial-name">Matheus A.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Eu já acompanho bastante conteúdo de musculação, mas mesmo assim aprendi algumas estratégias que nunca tinha usado, como controlar o tempo das repetições e aplicar as técnicas de intensidade da forma certa. A leitura é simples e bem organizada.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">J</span>
            <span class="testimonial-name">João P.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">Gostei porque o ebook não fica enrolando. Vai direto ao ponto e explica exatamente o que fazer quando você para de evoluir. O plano de treino de 4 semanas foi o que mais gostei. Dá vontade de colocar em prática na hora.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">R</span>
            <span class="testimonial-name">Rafael S.</span>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="testimonial-quote-icon">"</div>
          <p class="testimonial-text">O que mais gostei foi que tudo parece aplicável. Não é aquele monte de teoria difícil. Você termina um capítulo e já sabe exatamente o que testar no treino seguinte. Pra quem sente que estagnou, vale muito a leitura.</p>
          <div class="testimonial-footer">
            <span class="testimonial-avatar">G</span>
            <span class="testimonial-name">Guilherme R.</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MECANISMO E DIFERENCIAÇÃO -->
  <section style="background:var(--bg-elevated);border-top:1px solid var(--border);border-bottom:1px solid var(--border);">
    <div class="container explain-flow">
      <div class="explain-step reveal">
        <span class="eyebrow mono">O Problema</span>
        <h2>Você não precisa de mais uma dica de treino.</h2>
        <p>Você provavelmente já viu de tudo: treinos no Instagram, vídeos no YouTube, dicas de hipertrofia, diferentes métodos e exercícios.</p>
        <p>O problema não é falta de informação. O problema é ter <strong>informação fragmentada</strong> sem uma estrutura clara de como aplicar.</p>
      </div>
      <div class="explain-step reveal">
        <span class="eyebrow mono">A Solução</span>
        <h2>O Destrave organiza isso em um método.</h2>
        <p>Você encontra informação de graça. O que falta é uma estrutura para saber o que aplicar, quando aplicar e como acompanhar sua evolução.</p>
        <p>Não é mais um treino. Não é uma coleção de dicas. É uma estrutura para entender o que está limitando sua evolução e organizar o que fazer a partir disso, integrando diagnóstico, treino, progressão, intensidade, nutrição, recuperação e disciplina.</p>
      </div>
      <div class="plateau-card reveal" style="text-align: center;">
        <div class="plateau-labels" style="justify-content: space-around; font-size: 14px; margin-top: 0;">
          <div style="color:var(--text-secondary);">
            <strong>CONTEÚDO GRATUITO:</strong><br><br>
            Dicas isoladas<br>
            Informações espalhadas<br>
            Diferentes opiniões<br>
            Dificuldade de aplicar
          </div>
          <div style="color:var(--cta-bright);">
            <strong>MÉTODO DESTRAVE:</strong><br><br>
            Estrutura<br>
            Sequência<br>
            Aplicação<br>
            Acompanhamento
          </div>
        </div>
      </div>
    </div>
  </section>'''

html = html.replace(vsl_end, new_sections_after_vsl)

# 4. Metodos Correction
html = html.replace(
'''        <div class="module-row reveal">
          <div class="module-col"><span class="module-num">MÓDULO 03</span><div class="module-icon"><img src="images/modulo-03-choque.webp" alt="Plano de choque"></div></div>
          <div><h3>Plano de Choque</h3><p>Semana 1-4 prepara o músculo. Semana 5-8 é intensidade máxima com técnicas de choque. Depois vem uma semana inteira de Deload — reduzir carga de propósito. Ignorar essa parte é o erro nº1 de quem tenta sozinho.</p></div>
        </div>
        <div class="module-row reveal">
          <div class="module-col"><span class="module-num">MÓDULO 04</span><div class="module-icon"><img src="images/ilustra-nutricao.webp" alt="Nutrição estratégica"></div></div>
          <div><h3>Nutrição Estratégica</h3><p>Não é sobre cortar carboidrato. É sobre saber que seu corpo só absorve 30-40g de proteína por refeição — o resto é desperdiçado. A distribuição importa mais que o total.</p></div>
        </div>''',
'''        <div class="module-row reveal">
          <div class="module-col"><span class="module-num">MÓDULO 03</span><div class="module-icon"><img src="images/modulo-03-choque.webp" alt="Plano de choque"></div></div>
          <div><h3>Plano de Choque</h3><p>Protocolo prático de 4 semanas. Prepara o músculo, aplica intensidade máxima com técnicas de choque e finaliza com o Deload — reduzir carga de propósito para recuperar. Ignorar a recuperação é o erro nº1 de quem tenta sozinho.</p></div>
        </div>
        <div class="module-row reveal">
          <div class="module-col"><span class="module-num">MÓDULO 04</span><div class="module-icon"><img src="images/ilustra-nutricao.webp" alt="Nutrição estratégica"></div></div>
          <div><h3>Nutrição Estratégica</h3><p>Não basta olhar apenas para a quantidade total de proteína. A organização da ingestão ao longo do dia também pode fazer parte de uma estratégia nutricional consistente para apoiar o seu objetivo.</p></div>
        </div>'''
)

# 5. Stack / Oferta
html = html.replace(
'''      <div class="receive-checklist reveal">
        <span class="receive-check-item">✅ Método</span>
        <span class="receive-check-item">✅ Plano de Choque</span>
        <span class="receive-check-item">✅ Nutrição</span>
        <span class="receive-check-item">✅ Atualizações</span>
        <span class="receive-check-item">✅ Garantia</span>
      </div>
      <div class="receive-grid">
        <div class="receive-card reveal">
          <div class="book-cover"><img src="images/capa-ebook.webp" alt="Capa do ebook Destrave Seus Ganhos"></div>
          <div class="receive-info"><h4>Livro Principal</h4><p>O método completo, módulo a módulo.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#2a1414,#161f30);"><img src="images/capa-plano-choque.webp" alt="Capa Plano de Choque"></div>
          <div class="receive-info"><h4>Plano de Choque</h4><p>Protocolo prático de 4 semanas.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#0d1a2e,#161f30);"><img src="images/capa-guia-nutricional.webp" alt="Capa Guia Nutricional"></div>
          <div class="receive-info"><h4>Guia Nutricional</h4><p>Estratégia alimentar para sustentar o estímulo.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-mock" style="background:linear-gradient(145deg,#e53131,#161f30);"><span>Garantia<br>Hotmart</span></div>
          <div class="receive-info"><h4>Garantia</h4><p>Risco zero na sua decisão.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#0d1420,#111827);"><img src="images/icone-atualizacoes.webp" alt="Atualizações futuras" style="height:70%;box-shadow:none;"></div>
          <div class="receive-info"><h4>Atualizações Futuras</h4><p>O método evolui — seu acesso evolui junto.</p></div>
        </div>
      </div>''',
'''      <div class="receive-checklist reveal">
        <span class="receive-check-item">✅ Método</span>
        <span class="receive-check-item">✅ Plano de Aplicação</span>
        <span class="receive-check-item">✅ Nutrição</span>
        <span class="receive-check-item">✅ Mentalidade</span>
        <span class="receive-check-item">✅ Comunidade</span>
      </div>
      <div class="receive-grid">
        <div class="receive-card reveal">
          <div class="book-cover"><img src="images/capa-ebook.webp" alt="Capa do ebook Destrave Seus Ganhos"></div>
          <div class="receive-info"><h4>01 — Método Destrave Seus Ganhos</h4><p>O conteúdo principal estruturado.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#2a1414,#161f30);"><img src="images/capa-plano-choque.webp" alt="Capa Plano de Choque"></div>
          <div class="receive-info"><h4>02 — Plano de Aplicação</h4><p>Para transformar conhecimento em execução (protocolo de 4 semanas).</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#0d1a2e,#161f30);"><img src="images/capa-guia-nutricional.webp" alt="Capa Guia Nutricional"></div>
          <div class="receive-info"><h4>03 — Guia de Nutrição</h4><p>Orientações para organizar a alimentação dentro da proposta do produto.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#0d1420,#111827);"><img src="images/modulo-05-mentalidade.webp" alt="Mentalidade" style="height:70%;box-shadow:none;"></div>
          <div class="receive-info"><h4>04 — Mentalidade e Disciplina</h4><p>Conteúdo para sustentar consistência e aderência.</p></div>
        </div>
        <div class="receive-card reveal">
          <div class="book-cover" style="background:linear-gradient(160deg,#0d1420,#111827);"><img src="images/icone-atualizacoes.webp" alt="Comunidade" style="height:70%;box-shadow:none;"></div>
          <div class="receive-info"><h4>05 — Comunidade</h4><p>Espaço para acompanhamento, troca e suporte conforme disponibilidade atual.</p></div>
        </div>
      </div>'''
)

# 6. Beneficios Correction
html = html.replace(
'''      <div class="benefits-grid">
        <div class="benefit-card reveal"><div class="ico">→</div><p>Saiba por que 80% das suas séries precisam estar em esforço quase máximo — e o que fazer com os outros 20%.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Aplique o ritmo exato (3 segundos descendo, 1 de pausa, 2 subindo, 1 de contração) que transforma qualquer série em um novo estímulo pro músculo.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Descubra exatamente por que seu corpo parou de evoluir.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Identifique exatamente quando fazer um Deload.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Saiba quando aplicar técnicas avançadas — e quando não.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Aprenda a utilizar progressão de carga corretamente.</p></div>
      </div>''',
'''      <div class="benefits-grid">
        <div class="benefit-card reveal"><div class="ico">→</div><p>Entenda como usar a proximidade da falha de forma estratégica, sem transformar toda série em uma guerra.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Aprenda a controlar execução, amplitude e ritmo para tornar suas séries mais consistentes e mensuráveis.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Descubra exatamente por que seu corpo parou de evoluir e o que fazer a respeito.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Identifique o momento certo para organizar sua recuperação e fazer um Deload.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Saiba quando aplicar técnicas avançadas de intensidade — e quando evitá-las.</p></div>
        <div class="benefit-card reveal"><div class="ico">→</div><p>Aprenda a organizar a progressão de carga de forma inteligente.</p></div>
      </div>'''
)

# 7. Garantia
html = html.replace(
'''  <!-- GARANTIA -->
  <section id="garantia">
    <div class="container">
      <div class="guarantee-box reveal">
        <div class="guarantee-seal">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l7 3v6c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V5l7-3z"/><path d="M9 12l2 2 4-4"/></svg>
        </div>
        <div>
          <h3>Garantia incondicional</h3>
          <p>Sua compra é protegida pela garantia da Hotmart. Se o método não fizer sentido pra você, é só pedir o reembolso dentro do prazo — sem perguntas, sem burocracia. O risco é todo nosso.</p>
        </div>
      </div>
    </div>
  </section>''',
'''  <!-- GARANTIA -->
  <section id="garantia">
    <div class="container">
      <div class="guarantee-box reveal">
        <div class="guarantee-seal">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l7 3v6c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V5l7-3z"/><path d="M9 12l2 2 4-4"/></svg>
        </div>
        <div>
          <h3>Garantia de 7 dias</h3>
          <p>Você tem 7 dias para conhecer o método e decidir se ele faz sentido para você. Sua compra é protegida pela garantia da Hotmart. Se não for o que você esperava, é só pedir o reembolso dentro do prazo, de forma simples e direta.</p>
        </div>
      </div>
    </div>
  </section>'''
)

# 8. FAQ and CTA FINAL
html = html.replace(
'''        <div class="faq-item">
          <button class="faq-q">Serve para iniciantes? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">O método funciona melhor para quem já treina há alguns meses e sente que parou de evoluir — platô só existe pra quem já vinha progredindo. Se você está começando agora, o foco inicial deve ser aprender o básico antes de aplicar as técnicas de quebra de platô.</div></div>
        </div>''',
'''        <div class="faq-item">
          <button class="faq-q">Isso é um treino? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">Não, é um método estruturado que organiza treino, nutrição e recuperação. Ele te dá as ferramentas para entender sua estagnação e aplicar estratégias, incluindo um protocolo prático de 4 semanas.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q">Por que não seguir conteúdo gratuito? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">Conteúdo gratuito oferece informações isoladas e opiniões diversas. O Método Destrave organiza tudo em uma estrutura lógica, mostrando o que aplicar, quando e como acompanhar sua progressão de verdade.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q">É para iniciantes? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">O método funciona melhor para quem já treina há alguns meses e sente que parou de evoluir — platô só existe pra quem já vinha progredindo. Se você está começando agora, o foco inicial deve ser aprender o básico antes de aplicar as técnicas de quebra de platô.</div></div>
        </div>'''
)

html = html.replace(
'''        <div class="faq-item">
          <button class="faq-q">Como recebo o acesso? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">Imediatamente após a confirmação da compra, por e-mail, com login direto na plataforma da Destrave Pro.</div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA FINAL -->
  <section class="final-cta" id="oferta">
    <video class="final-cta-video" autoplay muted loop playsinline poster="images/final-cta-bg-poster.jpg">
      <source src="videos/final-cta-bg.mp4" type="video/mp4">
    </video>
    <div class="final-cta-video-overlay"></div>
    <div class="container reveal">
      <span class="eyebrow mono center">Destrave Pro</span>
      <p class="final-cta-lead">Daqui a 4 semanas, você vai abrir seu app de treino e ver: mais peso, mais repetição, ou menos descanso entre séries. Não importa qual dos três — qualquer um significa que o platô acabou.</p>
      <h2>Você pode continuar repetindo o mesmo treino esperando um resultado diferente... <span>ou entender por que ele parou de funcionar e voltar a evoluir ainda esta semana.</span></h2>
      <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary" style="padding:18px 36px;font-size:16px;">Quero Destravar Meus Ganhos Agora</a>
    </div>
  </section>''',
'''        <div class="faq-item">
          <button class="faq-q">Como recebo o material? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">Imediatamente após a confirmação da compra, por e-mail, com login direto na plataforma.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q">E se eu comprar e perceber que não é para mim? <span class="plus">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">Você tem 7 dias de garantia incondicional. Se não gostar, basta solicitar o reembolso na plataforma Hotmart e devolveremos seu investimento integralmente.</div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA FINAL -->
  <section class="final-cta" id="oferta">
    <video class="final-cta-video" autoplay muted loop playsinline poster="images/final-cta-bg-poster.jpg">
      <source src="videos/final-cta-bg.mp4" type="video/mp4">
    </video>
    <div class="final-cta-video-overlay"></div>
    <div class="container reveal">
      <span class="eyebrow mono center">Acesso imediato + garantia de 7 dias</span>
      <p class="final-cta-lead">Organize sua rotina com uma estrutura que faz sentido. Em poucas semanas, você terá clareza sobre o que está limitando sua evolução e como ajustar o seu estímulo.</p>
      <h2>Você pode continuar repetindo o mesmo treino esperando um milagre... <span>ou criar uma estrutura sólida e voltar a buscar sua progressão.</span></h2>
      <a href="https://pay.hotmart.com/Y102348799D?checkoutMode=10" target="_blank" rel="noopener" class="btn btn-primary" style="padding:18px 36px;font-size:16px;">Quero Começar o Método Destrave</a>
    </div>
  </section>'''
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML update complete.")
