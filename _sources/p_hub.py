import json, re
from partials import ico, page, head
from p_index import faq_item
from p_formations import INCENDIE, SST, REG, FAQ_INC, FAQ_SST, FAQ_REG

def cat_card(href, icon, titre, texte, sessions, feature=False):
    rows = ''.join(f'<li><b>{s["court"]}</b><span>{s["tag"]}</span></li>' for s in sessions)
    cls = 'card cat-card' + (' card--feature' if feature else '')
    return f'''<a class="{cls}" href="{href}"><span class="ico-tile">{ico(icon)}</span><h3>{titre}</h3><p>{texte}</p><ul class="sessions">{rows}</ul><span class="link-arrow">Voir les programmes {ico('arrow')}</span></a>'''

CAT = f'''
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><span>Formations</span></nav>
    <h1 class="h-anim">Le catalogue des <span class="accent">formations</span></h1>
    <p class="lead">Toutes mes formations se déroulent dans vos locaux, en Île-de-France et partout en France selon les conditions de la mission, avec attestations individuelles. Choisissez un domaine pour voir les programmes détaillés.</p>
  </div>
</section>
<section class="section">
  <h2 class="sr-only">Domaines de formation</h2>
  <div class="wrap">
    <div class="grid-3" data-stagger>
      {cat_card('formation-incendie.html', 'flame', 'Sécurité incendie', "Du réflexe de base à l'organisation de l'évacuation.", INCENDIE, True)}
      {cat_card('formation-sst.html', 'heart', 'SST et secourisme', "Selon le référentiel national de l'INRS.", SST)}
      {cat_card('formations-reglementaires.html', 'clipboard', 'Formations réglementaires', 'Construites à partir de vos risques réels.', REG)}
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Sur mesure</span>
      <h2>Un besoin qui ne rentre dans aucune case ?</h2>
      <p class="lead">Horaires décalés, équipes multilingues, risques propres à votre activité : je construis le programme avec vous.</p>
      <a class="btn btn-primary" style="align-self:flex-start" href="contact.html?univers=formation&amp;sujet=Programme%20sur%20mesure">Demander un programme sur mesure {ico('arrow', extra=' ico-arrow')}</a>
    </div>
    <div class="media reveal">
      <img src="assets/photo-formation.jpg" alt="Préparation des extincteurs avant une formation incendie" width="1200" height="895" loading="lazy">
    </div>
  </div>
</section>
'''

GROUPS = [
 ('faq-incendie', 'formation', 'flame', 'Formation incendie', FAQ_INC),
 ('faq-sst', 'formation', 'heart', 'SST et secourisme', FAQ_SST + [("Qui peut former des SST ?", "La formation SST doit être dispensée par un formateur certifié par l'INRS, au sein d'une structure habilitée. Je suis formateur SST agréé INRS.")]),
 ('faq-reglementaire', 'formation', 'clipboard', 'Formations réglementaires', FAQ_REG),
 ('faq-conseil', 'conseil', 'scale', 'Conseil et interventions', [
   ("Intervenez-vous hors d'Île-de-France ?", "Oui, selon les conditions de la mission : durée, nombre de sessions et frais de déplacement."),
   ("Proposez-vous aussi du conseil (DUERP, audit, RPS) ?", "Oui, avec mon cabinet MAKE Consulting. Les missions et leurs questions fréquentes sont détaillées sur <a href='https://make-consulting.fr/faq.html' target='_blank' rel='noopener'>make-consulting.fr</a>."),
 ]),
 ('faq-firetraining', 'firetraining', 'headset', 'FireTraining MS', [
   ("Qu'est-ce que FireTraining MS ?", "Une application de réalité mixte pour casques Meta Quest, que j'ai développée pour les formations incendie. Le stagiaire voit un départ de feu apparaître dans la salle et s'exerce à le traiter."),
   ("L'application remplace-t-elle la formation pratique ?", "Non. C'est un complément pédagogique. Les attestations délivrées correspondent à des formations conformes, avec la manipulation réelle d'extincteurs."),
   ("Existe-t-il une offre pour les organismes de formation ?", "Oui : une licence annuelle avec accès complet, support technique, mises à jour, nouveaux scénarios et tableau de bord formateur."),
   ("Et pour les formateurs indépendants ?", "Un achat unique du fichier d'installation, sans abonnement, avec un scénario tronc commun. Des scénarios supplémentaires sont disponibles à l'unité."),
 ]),
]

def strip(t):
    return re.sub('<[^>]+>', '', t)

def build_faq():
    blocks = ''
    for gid, u, icon, titre, items in GROUPS:
        fq = ''.join(faq_item(q, a) for q, a in items)
        blocks += f'<div class="faq-group" id="{gid}" data-u="{u}"><h2><span class="ico-tile">{ico(icon)}</span>{titre}</h2><div class="faq">{fq}</div></div>'
    nav = ''.join(f'<a href="#{g[0]}">{g[3]}</a>' for g in GROUPS)
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><span>Questions fréquentes</span></nav>
    <h1 class="h-anim">Questions <span class="accent">fréquentes</span></h1>
    <p class="lead">Vos obligations en formation, en prévention et en sécurité incendie, et tout ce qu'il faut savoir sur FireTraining MS.</p>
  </div>
</section>
<nav class="subnav" aria-label="Thèmes"><div class="wrap">{nav}</div></nav>
<section class="section"><div class="wrap">{blocks}</div></section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta-band reveal">
      <div><h2>Votre question n'y est pas ?</h2><p>Posez-la directement. Je réponds sous 24 h ouvrées.</p></div>
      <div class="btns"><a class="btn btn-light" href="contact.html">Me contacter {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a></div>
    </div>
  </div>
</section>'''
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
        for g in GROUPS for q, a in g[4]]}
    return page('Questions fréquentes | Formation incendie, SST, DUERP, FireTraining MS',
                "Réponses sur les obligations de formation incendie et SST, le DUERP, l'IPRP, la prévention des RPS et l'application FireTraining MS.",
                'faq.html', 'formation', body,
                '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', current='faq.html')

def build_catalogue():
    return page('Catalogue des formations incendie, SST et réglementaires | Paris',
                "Toutes les formations en intra-entreprise à Paris et en Île-de-France : incendie, SST et secourisme, risques chimiques, travail en hauteur, RPS, amiante.",
                'formations.html', 'formation', CAT, current='formations.html')

def build_references_redirect():
    return '''<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><title>Références | MAKE Consulting</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://www.formation-incendie-paris.com/#references">
<meta http-equiv="refresh" content="0; url=index.html#references">
<script>location.replace('index.html#references');</script>
</head><body><p>Cette page a déménagé : <a href="index.html#references">voir les références</a>.</p></body></html>'''
