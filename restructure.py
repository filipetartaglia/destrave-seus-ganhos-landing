import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero CTA
html = html.replace(
    '<a href="#vsl" id="descobrir-btn" class="btn btn-ghost">Descobrir Como Funciona</a>',
    '<a href="#vsl" id="descobrir-btn" class="btn btn-ghost" style="padding-left:24px;padding-right:24px;">▶ Assistir ao vídeo</a>'
)

# Extract VSL
vsl_match = re.search(r'  <!-- VSL -->\n  <section class="vsl-section" id="vsl">.*?</section>\n', html, re.DOTALL)
if vsl_match:
    vsl_content = vsl_match.group(0)
    html = html.replace(vsl_content, '')
    
    # Update VSL microcopy
    vsl_content = vsl_content.replace(
        '<span class="eyebrow mono center">Assista antes de continuar</span>',
        '<span class="eyebrow mono center">Se preferir assistir</span>'
    )
    vsl_content = vsl_content.replace(
        '<h2 style="font-size:clamp(24px,3.4vw,34px);">Em poucos minutos, você vai entender exatamente por que parou de evoluir.</h2>',
        '<h2 style="font-size:clamp(24px,3.4vw,34px);">Entenda em poucos minutos por que você pode ter parado de evoluir.</h2>'
    )

# Extract Depoimentos
depoimentos_match = re.search(r'  <!-- PROVAS SOCIAIS -->\n  <section id="depoimentos">.*?</section>\n', html, re.DOTALL)
if depoimentos_match:
    depoimentos_content = depoimentos_match.group(0)
    html = html.replace(depoimentos_content, '')

# Now insert them after HERO
hero_end = '  </section>\n'
hero_end_idx = html.find(hero_end, html.find('<!-- HERO -->')) + len(hero_end)

new_html = html[:hero_end_idx] + '\n' + vsl_content + '\n' + depoimentos_content + html[hero_end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

# Update js/main.js
with open("js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace(
    "trackPixel('VSL_Click', { source: 'hero_button' });",
    "trackPixel('video_cta_click', { source: 'hero_button' });"
)

# Remove the play() call to prevent autoplay with sound when scrolling
js = js.replace(
    "if (window.vslVimeoPlayer) {\n        window.vslVimeoPlayer.play();\n      }",
    "// Autoplay prevented as per rules"
)

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Restructure complete")
