import json
from partials import ico, page
from p_index import faq_item

BASE = 'https://www.formation-incendie-paris.com/'

def facts(f):
    rows = [('clock', 'Durée', f['duree']), ('users', 'Public', f['public']), ('usercheck', 'Effectif', f['effectif']),
            ('target', 'Prérequis', f.get('prerequis', 'Aucun')), ('file', 'Validation', f['validation'])]
    return '<ul class="facts">' + ''.join(f'<li>{ico(i)}<div><small>{l}</small><b>{v}</b></div></li>' for i, l, v in rows) + '</ul>'

def fiche(s, sujet):
    obj = ''.join(f'<li>{ico("check")}{o}</li>' for o in s['objectifs'])
    prog = ''.join(f'<li><div><strong>{t}</strong><span>{d}</span></div></li>' for t, d in s['programme'])
    extra = f'<div class="legal-note">{ico("layers")}<p>{s["note"]}</p></div>' if s.get('note') else ''
    return f'''<article class="fiche" id="{s['id']}">
  <div class="fiche-side">
    <span class="pill pill--acc" style="align-self:flex-start">{s['tag']}</span>
    <h2>{s['titre']}</h2>
    {facts(s)}
    <a class="btn btn-primary" href="contact.html?univers=formation&amp;sujet={sujet}">Demander un devis {ico('arrow', extra=' ico-arrow')}</a>
  </div>
  <div class="fiche-main">
    <p class="lead">{s['intro']}</p>
    <div class="fiche-block"><h3>Objectifs</h3><ul class="checks">{obj}</ul></div>
    <div class="fiche-block"><h3>Programme</h3><ol class="prog">{prog}</ol></div>
    {extra}
  </div>
</article>'''

MODALITES = f'''<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Modalités communes</span><h2>Comment se passent mes formations</h2></div>
    <div class="modal-grid" data-stagger>
      <div class="modal-item"><span class="ico-tile">{ico('building')}</span><h4>Dans vos locaux</h4><p>Intra-entreprise en Île-de-France, et partout en France selon les conditions de la mission. Je m'adapte à vos horaires et à vos équipes postées.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('box')}</span><h4>Matériel fourni</h4><p>Extincteurs, mannequins, défibrillateur de formation, supports pédagogiques : j'apporte tout.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('chart')}</span><h4>Évaluation</h4><p>Évaluation des acquis en fin de session, questionnaire de satisfaction, feuille d'émargement et attestations individuelles.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('usercheck')}</span><h4>Accessibilité</h4><p>Un stagiaire en situation de handicap ? Prévenez-moi avant la session pour que j'adapte le déroulé.</p></div>
    </div>
  </div>
</section>'''

def cta(titre, texte, sujet):
    return f'''<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <canvas data-embers="30" aria-hidden="true"></canvas>
      <div><h2>{titre}</h2><p>{texte}</p></div>
      <div class="btns">
        <a class="btn btn-light" href="contact.html?univers=formation&amp;sujet={sujet}">Demander un devis {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a>
      </div>
    </div>
  </div>
</section>'''

def jsonld(slug, nom, sessions):
    courses = [{"@type": "Course", "name": s['titre'], "description": s['intro'].replace('&#39;', "'"),
                "url": f"{BASE}{slug}#{s['id']}", "inLanguage": "fr",
                "provider": {"@type": "Organization", "name": "MAKE Consulting", "url": BASE},
                "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "onsite", "location": "Île-de-France"}} for s in sessions]
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Formations", "item": BASE + "formations.html"},
        {"@type": "ListItem", "position": 3, "name": nom, "item": BASE + slug}]}
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": courses + [crumbs]}, ensure_ascii=False) + '</script>'

def theme_page(slug, nom, h1, lead, keyfacts, sessions, sujet, faqs, cta_t, cta_x, title, desc):
    kf = ''.join(f'<span class="pill">{ico(i)}{t}</span>' for i, t in keyfacts)
    sub = ''.join(f'<a href="#{s["id"]}">{s["court"]}</a>' for s in sessions)
    fiches = ''.join(fiche(s, sujet) for s in sessions)
    fq = ''.join(faq_item(q, a, k == 0) for k, (q, a) in enumerate(faqs))
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><a href="formations.html">Formations</a><span aria-hidden="true">/</span><span>{nom}</span></nav>
    <h1 class="h-anim">{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="keyfacts">{kf}</div>
  </div>
</section>
<nav class="subnav" aria-label="Sessions de cette page"><div class="wrap">{sub}</div></nav>
<div class="wrap">{fiches}</div>
{MODALITES}
<section class="section" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal"><span class="eyebrow">Questions fréquentes</span><h2>{nom} : vos questions</h2></div>
    <div class="faq reveal">{fq}</div>
    <p style="text-align:center;margin-top:28px"><a class="link-arrow" href="faq.html">Toutes les questions {ico('arrow')}</a></p>
  </div>
</section>
{cta(cta_t, cta_x, sujet)}'''
    return page(title, desc, slug, 'formation', body, jsonld(slug, nom, sessions), current=slug)

# ─── Formation incendie ─────────────────────────────────
INCENDIE = [
 dict(id='sensibilisation', court='Sensibilisation', tag='½ journée', titre='Sensibilisation incendie',
  intro="La formation de base pour tous vos salariés : comprendre comment naît un feu, réagir à l'alarme et utiliser un extincteur sans hésiter.",
  duree='½ journée (3 h 30)', public='Tous les salariés', effectif='10 à 12 personnes conseillées', validation='Attestation de formation individuelle',
  objectifs=["Comprendre la naissance et la propagation d'un incendie", "Connaître les consignes de sécurité de l'établissement", "Réagir correctement à l'alarme et évacuer", "Choisir et utiliser l'extincteur adapté"],
  programme=[('Le feu', 'Triangle du feu, classes de feux, modes de propagation.'), ("Les causes d'incendie", "Risques électriques, stockage, travaux par points chauds, comportements."), ("Alarme et consignes", "Signal d'alarme, consignes affichées, conduite à tenir."), ("Les moyens d'extinction", "Types d'extincteurs et agents extincteurs, robinets d'incendie armés s'il y en a."), ('Mise en pratique', "Manipulation d'extincteurs par chaque stagiaire.")]),
 dict(id='epi', court='Équipier de première intervention', tag='½ journée', titre='Équipier de première intervention (EPI)',
  intro="Pour les salariés désignés qui doivent intervenir sur un début d'incendie en attendant les secours.",
  duree='½ journée (3 h 30)', public='Salariés désignés équipiers', effectif='10 à 12 personnes conseillées', validation='Attestation de formation individuelle',
  objectifs=["Donner l'alerte et déclencher l'alarme", "Intervenir rapidement sur un début de feu", "Mettre en œuvre extincteurs et RIA en sécurité", "Participer à l'évacuation et accueillir les secours"],
  programme=[("Le rôle de l'EPI", "Place de l'équipier dans l'organisation de sécurité."), ('Détection et alerte', 'Qui prévenir, comment, avec quelles informations.'), ("Moyens d'extinction", "Choix de l'agent selon la classe de feu, distances et techniques d'attaque."), ('Conduite à tenir', "Désenfumage, fermeture des portes, coupures d'énergie."), ('Exercice pratique', "Extinction par chaque stagiaire et mise en situation.")]),
 dict(id='guide-serre-file', court='Guide et serre-file', tag='½ journée', titre='Guide et serre-file',
  intro="Former les personnes qui encadrent l'évacuation : guider les occupants, vérifier les locaux, ne laisser personne derrière.",
  duree='½ journée (3 h 30)', public="Salariés désignés pour l'évacuation", effectif='10 à 12 personnes conseillées', validation='Attestation de formation individuelle',
  objectifs=["Organiser et encadrer une évacuation", "Vérifier que les locaux sont vides", "Prendre en charge les personnes à mobilité réduite", "Rendre compte au point de rassemblement"],
  programme=[("L'organisation de l'évacuation", "Chaîne d'alerte, rôles et responsabilités."), ('Le rôle du guide', 'Ouvrir la marche, choisir le cheminement, rassurer.'), ('Le rôle du serre-file', "Fermer la marche, vérifier les locaux, fermer les portes."), ('Personnes à mobilité réduite', "Espaces d'attente sécurisés, binômes d'accompagnement."), ("Exercice et retour d'expérience", "Évacuation réelle ou simulée puis débriefing.")]),
 dict(id='realite-mixte', court='Module réalité mixte', tag='En option', titre='Module réalité mixte FireTraining MS',
  intro="À ajouter à une sensibilisation ou une formation EPI : chaque stagiaire traite un départ de feu virtuel dans son propre environnement de travail.",
  duree='Intégré à la session', public='Stagiaires des sessions incendie', effectif='Selon la session', validation="Rapport individuel des réactions",
  objectifs=["Vivre un départ de feu avant d'y être confronté", "Choisir le bon extincteur sous pression", "Rejouer le scénario jusqu'au bon geste"],
  programme=[('Briefing', "Rappel des classes de feux et des agents extincteurs."), ('Scénario en casque', "Départ de feu superposé à la salle, grâce à la vidéo en transparence."), ('Débriefing', "Retour sur les gestes et les temps de réaction.")],
  note="Le module complète la manipulation réelle des extincteurs, il ne la remplace pas. <a class=\"link-arrow\" href=\"firetraining-ms.html\">En savoir plus sur FireTraining MS</a>"),
]
FAQ_INC = [
 ("La formation incendie est-elle obligatoire ?", "Oui. Le Code du travail (art. R.4227-28 et suivants) impose à tout employeur de former ses salariés à la prévention incendie et aux consignes d'évacuation, et d'organiser des exercices et essais périodiques."),
 ("Quelle différence entre sensibilisation et EPI ?", "La sensibilisation s'adresse à tous les salariés. La formation EPI est destinée aux personnes désignées pour intervenir sur un début de feu : elle va plus loin sur l'alerte, les techniques d'extinction et la conduite à tenir."),
 ("Faut-il former des guides et serre-files ?", "L'employeur doit organiser l'évacuation. Désigner et former des guides et serre-files est la façon la plus courante d'y répondre, en particulier dans les établissements sur plusieurs niveaux."),
 ("La formation se fait-elle sur feu réel ?", "Chaque stagiaire manipule un extincteur. Les conditions de l'exercice (extérieur, cour, parking) sont définies avec vous avant la session selon la configuration du site."),
]

# ─── SST ────────────────────────────────────────────────
SST = [
 dict(id='sst-initial', court='SST initial', tag='2 jours', titre='Sauveteur secouriste du travail (SST)',
  intro="La formation de référence pour disposer de secouristes dans vos équipes, selon le référentiel national de l'INRS.",
  duree='2 jours (14 h minimum)', public='Tous les salariés', effectif='4 à 10 personnes', validation='Certificat SST valable 24 mois',
  objectifs=["Situer son rôle de SST dans l'entreprise", "Protéger, examiner, faire alerter et secourir une victime", "Repérer les situations dangereuses et en informer", "Contribuer à la prévention dans l'entreprise"],
  programme=[('Le SST dans l\'entreprise', 'Cadre juridique, rôle et limites du sauveteur.'), ('Protéger', 'Repérer les dangers persistants et supprimer ou isoler le danger.'), ('Examiner et faire alerter', "Reconnaître les signes vitaux, transmettre l'alerte."), ('Secourir', "Saignement, étouffement, malaise, brûlure, plaie, victime inconsciente, arrêt cardiaque avec défibrillateur."), ('Prévention', "Du constat d'une situation dangereuse à l'information de la hiérarchie."), ('Évaluation certificative', "Mises en situation selon la grille de l'INRS.")]),
 dict(id='mac-sst', court='Recyclage SST', tag='1 jour', titre='Recyclage SST (MAC)',
  intro="Le maintien et actualisation des compétences, à suivre tous les 24 mois pour conserver le certificat.",
  duree='1 jour (7 h)', public='Titulaires du certificat SST', effectif='4 à 10 personnes', prerequis='Certificat SST en cours de validité', validation='Prolongation du certificat pour 24 mois',
  objectifs=["Actualiser les gestes de secours", "Intégrer les évolutions du référentiel", "Revoir le rôle de prévention du SST"],
  programme=[('Retour d\'expérience', 'Interventions réalisées depuis la dernière formation.'), ('Révision des gestes', 'Mises en situation sur les cas les plus fréquents.'), ('Évolutions', 'Changements du référentiel et de la réglementation.'), ('Évaluation certificative', "Mises en situation selon la grille de l'INRS.")]),
 dict(id='psc', court='PSC', tag='1 jour', titre='Premiers secours civiques (PSC)',
  intro="Les gestes de premiers secours pour tous, au travail comme dans la vie quotidienne.",
  duree='1 jour (7 h)', public='Tout public', effectif='10 personnes maximum', validation='Certificat de compétences PSC',
  objectifs=["Protéger et alerter", "Agir face à une hémorragie ou un étouffement", "Réagir face à un malaise ou une perte de connaissance", "Réaliser une réanimation avec défibrillateur"],
  programme=[('Protection et alerte', 'Sécuriser la zone et appeler les secours.'), ('Obstruction des voies aériennes', 'Désobstruction chez l\'adulte, l\'enfant et le nourrisson.'), ('Hémorragies, plaies, brûlures', 'Gestes adaptés à chaque situation.'), ('Malaise et perte de connaissance', 'Position latérale de sécurité.'), ('Arrêt cardiaque', 'Compressions thoraciques et défibrillateur.')]),
 dict(id='gqs', court='Gestes qui sauvent', tag='2 heures', titre='Gestes qui sauvent (GQS)',
  intro="Une sensibilisation courte, facile à caser dans une journée de travail, pour que chacun sache réagir.",
  duree='2 heures', public='Tout public', effectif='10 personnes maximum', validation='Attestation de sensibilisation',
  objectifs=["Alerter efficacement les secours", "Arrêter une hémorragie", "Mettre une victime en sécurité", "Pratiquer le massage cardiaque avec défibrillateur"],
  programme=[('Protéger et alerter', 'Les bons réflexes et les numéros utiles.'), ('Hémorragie', 'Compression et garrot.'), ('Position latérale de sécurité', 'Pour une victime inconsciente qui respire.'), ('Arrêt cardiaque', 'Compressions et utilisation du défibrillateur.')]),
]
FAQ_SST = [
 ("Combien de SST faut-il dans une entreprise ?", "Le Code du travail (art. R.4224-15) impose un salarié formé aux premiers secours dans chaque atelier où sont réalisés des travaux dangereux, et sur chaque chantier de 20 travailleurs ou plus pendant plus de 15 jours avec travaux dangereux. En pratique, prévoir un SST pour 10 à 20 salariés, présent à chaque horaire, est une bonne base."),
 ("Combien de temps le certificat SST est-il valable ?", "24 mois. Le recyclage (MAC SST) d'une journée permet de le prolonger. Sans recyclage dans ce délai, le salarié doit refaire la formation initiale."),
 ("Quelle différence entre SST, PSC et GQS ?", "Le SST est une formation professionnelle de 2 jours avec un volet prévention. Le PSC dure une journée et s'adresse à tout public. Les GQS sont une sensibilisation de 2 heures."),
]

# ─── Réglementaires ─────────────────────────────────────
REG = [
 dict(id='risques-chimiques', court='Risques chimiques', tag='½ à 1 jour', titre='Prévention des risques chimiques',
  intro="Pour les salariés qui manipulent ou stockent des produits dangereux : lire une étiquette, appliquer les bonnes pratiques, réagir en cas d'incident.",
  duree='½ à 1 jour', public='Salariés exposés à des produits chimiques', effectif='12 personnes maximum', validation='Attestation de formation individuelle',
  objectifs=["Identifier les dangers grâce à l'étiquetage CLP", "Exploiter une fiche de données de sécurité", "Appliquer les règles de stockage et de manipulation", "Choisir et porter les bons équipements de protection"],
  programme=[('Les agents chimiques dangereux', "Voies d'exposition et effets sur la santé."), ('Étiquetage CLP', 'Pictogrammes, mentions de danger et conseils de prudence.'), ('Fiches de données de sécurité', 'Où trouver l\'information utile.'), ('Prévention', 'Stockage, incompatibilités, protections collectives et EPI.'), ('En cas d\'incident', 'Déversement, projection, conduite à tenir.')]),
 dict(id='travail-en-hauteur', court='Travail en hauteur', tag='1 jour', titre='Travail en hauteur et port du harnais',
  intro="Connaître les règles et utiliser correctement un système d'arrêt des chutes.",
  duree='1 jour', public='Salariés amenés à travailler en hauteur', effectif='8 personnes maximum', prerequis='Aptitude médicale au travail en hauteur', validation='Attestation de formation individuelle',
  objectifs=["Connaître la réglementation et la priorité aux protections collectives", "Identifier les risques de chute", "Vérifier et ajuster un harnais antichute", "Choisir un point d'ancrage adapté"],
  programme=[('Réglementation', 'Principes de prévention et hiérarchie des protections.'), ('Analyse des risques', 'Situations de travail et facteurs de chute.'), ('Les équipements', 'Harnais, longes, antichutes, ancrages.'), ('Vérification', 'Contrôles avant utilisation.'), ('Mise en pratique', 'Selon les installations disponibles sur votre site.')]),
 dict(id='rps', court='Prévention des RPS', tag='½ journée', titre='Prévention des risques psychosociaux',
  intro="Donner aux managers, RH et élus du CSE les repères pour identifier et prévenir les risques psychosociaux.",
  duree='½ journée', public='Managers, RH, membres du CSE', effectif='12 personnes maximum', validation='Attestation de formation individuelle',
  objectifs=["Comprendre les facteurs de risques psychosociaux", "Repérer les signaux d'alerte", "Connaître le rôle de chacun dans la prévention", "Adopter des pratiques managériales protectrices"],
  programme=[('Définitions', 'Stress, épuisement professionnel, violences internes et externes.'), ('Les facteurs de risque', "Intensité du travail, exigences émotionnelles, autonomie, rapports sociaux, conflits de valeurs, insécurité."), ('Signaux d\'alerte', 'Indicateurs individuels et collectifs.'), ('Agir', 'Rôles de l\'employeur, du manager, du CSE ; ressources internes et externes.')],
  note="Besoin d'aller plus loin ? Je réalise aussi des diagnostics RPS complets avec plan d'action. <a class=\"link-arrow\" href=\"conseil.html#missions\">Voir la mission de conseil</a>"),
 dict(id='amiante', court='Risque amiante', tag='Sur devis', titre='Risque amiante et modes opératoires',
  intro="Une sensibilisation au risque amiante pour vos équipes et un appui à la rédaction de vos modes opératoires en sous-section 4.",
  duree='Sur devis', public='Donneurs d\'ordre, encadrants, opérateurs', effectif='Selon le besoin', validation='Attestation de sensibilisation',
  objectifs=["Connaître les dangers de l'amiante et la réglementation", "Comprendre le repérage avant travaux", "Structurer un mode opératoire SS4"],
  programme=[('Le risque amiante', 'Matériaux concernés, effets sur la santé.'), ('Réglementation', 'Obligations du donneur d\'ordre et de l\'entreprise.'), ('Repérage avant travaux', 'Documents à exiger avant d\'intervenir.'), ('Modes opératoires', 'Aide à la rédaction, par un encadrant technique SS4.')],
  note="Cette session ne remplace pas la formation amiante SS4 obligatoire, délivrée par un organisme de formation certifié."),
]
FAQ_REG = [
 ("Ces formations sont-elles obligatoires ?", "L'employeur doit former ses salariés à la sécurité en fonction des risques de leur poste (Code du travail, art. L.4141-2). Les risques identifiés dans votre document unique indiquent les formations à prévoir."),
 ("Pouvez-vous adapter le programme ?", "Oui. Chaque formation réglementaire part de vos postes de travail, de vos produits et de votre DUERP. Je vous envoie un programme ajusté avec le devis."),
 ("Faites-vous le lien avec le DUERP ?", "Oui. En tant qu'IPRP, je peux aussi réaliser ou mettre à jour votre document unique, et construire le plan de formation qui en découle."),
]

def build_incendie():
    return theme_page('formation-incendie.html', 'Formation incendie',
        'Formation incendie en entreprise <span class="accent">à Paris et en Île-de-France</span>',
        "Sensibilisation, équipier de première intervention, guide et serre-file : trois formations d'une demi-journée, dans vos locaux, avec manipulation d'extincteurs par chaque stagiaire.",
        [('flame', 'Formateur SSIAP 3'), ('clock', '½ journée par session'), ('building', 'Intra-entreprise'), ('file', 'Attestations individuelles')],
        INCENDIE, 'Formation%20incendie%20%2F%20EPI', FAQ_INC, 'Planifions votre formation incendie',
        "Indiquez le nombre de personnes et le lieu. Programme et devis sous 48 h.",
        'Formation incendie en entreprise à Paris | Sensibilisation, EPI, évacuation',
        "Formation incendie dans vos locaux à Paris et en Île-de-France : sensibilisation, équipier de première intervention, guide et serre-file. Formateur SSIAP 3, attestations individuelles.")

def build_sst():
    return theme_page('formation-sst.html', 'SST et secourisme',
        'Formation SST et secourisme <span class="accent">dans vos locaux</span>',
        "SST initial, recyclage, PSC et gestes qui sauvent, par un formateur SST agréé INRS. Des mises en situation concrètes, adaptées à vos postes de travail.",
        [('heart', 'Formateur agréé INRS'), ('users', '4 à 10 stagiaires en SST'), ('building', 'Intra-entreprise'), ('file', 'Certificat valable 24 mois')],
        SST, 'Formation%20SST%20%2F%20Secourisme', FAQ_SST, 'Formez vos sauveteurs secouristes',
        "Session initiale ou recyclage : dites-moi combien de salariés former. Devis sous 48 h.",
        'Formation SST à Paris | Sauveteur secouriste du travail, recyclage, PSC',
        "Formation SST initiale (2 jours) et recyclage MAC SST (1 jour) dans vos locaux à Paris et en Île-de-France. Formateur agréé INRS. Aussi PSC et gestes qui sauvent.")

def build_reg():
    return theme_page('formations-reglementaires.html', 'Formations réglementaires',
        'Formations réglementaires <span class="accent">construites sur vos risques</span>',
        "Risques chimiques, travail en hauteur, prévention des RPS, risque amiante : des formations conçues à partir de vos postes et de votre document unique.",
        [('clipboard', 'Programme sur mesure'), ('scale', 'IPRP déclaré'), ('building', 'Intra-entreprise'), ('file', 'Attestations individuelles')],
        REG, 'Formation%20r%C3%A9glementaire', FAQ_REG, 'Construisons votre plan de formation',
        "Décrivez vos postes et vos risques : je vous propose le programme adapté.",
        'Formations réglementaires en entreprise | Risques chimiques, hauteur, RPS',
        "Formations réglementaires sur mesure en Île-de-France : risques chimiques, travail en hauteur, prévention des RPS, risque amiante. Programmes construits à partir de votre DUERP.")

# ─── QSE ────────────────────────────────────────────────
QSE = [
 dict(id='sensibilisation-qse', court='Sensibilisation QSE', tag='1 jour', titre='Les bases du management QSE',
  intro="Une journée pour que vos managers et vos équipes comprennent ce que recouvre une démarche qualité, sécurité, environnement, et ce qu'elle change dans leur travail quotidien.",
  duree='1 jour (7 h)', public='Managers, référents, salariés impliqués dans la démarche', effectif='12 personnes maximum', validation='Attestation de formation individuelle',
  objectifs=["Comprendre les enjeux d'une démarche QSE", "Connaître les normes ISO 9001, ISO 14001 et ISO 45001 et leur logique commune", "Situer son rôle dans l'amélioration continue", "Utiliser les outils de base : indicateurs, analyse des causes, plan d'action"],
  programme=[('Les trois volets', "Qualité, santé-sécurité au travail, environnement : ce que chacun apporte à l'entreprise."), ('Les normes de référence', "ISO 9001, ISO 14001, ISO 45001 : structure commune, exigences clés, certification."), ("L'amélioration continue", "Le cycle PDCA, les processus, les indicateurs."), ('Les outils', "Analyse des causes, traitement des non-conformités, plan d'action."), ('Cas pratique', "Application à une situation de votre entreprise.")]),
 dict(id='audit-interne', court='Audit interne', tag='2 jours', titre='Auditeur interne QSE',
  intro="Former vos collaborateurs à préparer, conduire et restituer un audit interne de votre système de management qualité, sécurité ou environnement.",
  duree='2 jours (14 h)', public='Futurs auditeurs internes, responsables et animateurs QSE', effectif='10 personnes maximum', prerequis="Connaître le fonctionnement de l'entreprise", validation='Attestation de formation individuelle',
  objectifs=["Connaître les principes de l'audit selon la norme ISO 19011", "Préparer un audit : périmètre, critères, plan et grille", "Conduire les entretiens et collecter des preuves", "Rédiger les constats et restituer l'audit"],
  programme=[("Les principes de l'audit", "Rôle de l'audit interne, ISO 19011, posture de l'auditeur."), ('Préparer', "Programme d'audit, périmètre, critères, plan et grille d'audit."), ('Conduire', "Réunion d'ouverture, entretiens, observation, preuves d'audit."), ('Conclure', "Constats, non-conformités, points forts, réunion de clôture, rapport."), ('Mise en situation', "Audit d'un processus de votre entreprise, puis retour d'expérience.")],
  note="L'audit interne prépare les audits de certification, qui sont réalisés par un organisme certificateur. Besoin d'un audit réalisé par un intervenant extérieur ? <a class=\"link-arrow\" href=\"conseil.html#missions\">Voir l'audit QSE en conseil</a>"),
 dict(id='amdec', court='AMDEC', tag='1 jour', titre="AMDEC : analyser les modes de défaillance",
  intro="Une méthode structurée pour repérer ce qui peut mal tourner sur un produit, un procédé ou un équipement, et traiter d'abord les risques les plus critiques.",
  duree='1 jour (7 h)', public='Équipes qualité, méthodes, maintenance, production', effectif='10 personnes maximum', validation='Attestation de formation individuelle',
  objectifs=["Comprendre la démarche AMDEC et ses usages", "Identifier modes de défaillance, causes et effets", "Coter gravité, occurrence et détection", "Hiérarchiser les risques et bâtir le plan d'action"],
  programme=[("La démarche", "Principe de l'AMDEC produit, procédé et moyen."), ("L'analyse fonctionnelle", "Décomposer le système étudié."), ('Les défaillances', "Modes, causes, effets."), ('La cotation', "Gravité, occurrence, détection, criticité."), ('Atelier', "AMDEC menée en groupe sur un cas de votre entreprise.")]),
 dict(id='referent-securite', court='Référent sécurité', tag='2 jours', titre='Référent santé-sécurité : évaluer les risques',
  intro="Pour le salarié désigné par l'employeur pour s'occuper de la prévention des risques professionnels : évaluer les risques, tenir le document unique, suivre le plan d'action.",
  duree='2 jours (14 h)', public='Salariés désignés compétents en prévention, dirigeants de TPE et PME', effectif='10 personnes maximum', validation='Attestation de formation individuelle',
  objectifs=["Connaître les obligations de l'employeur et le rôle du référent", "Évaluer les risques d'une unité de travail", "Rédiger et mettre à jour le document unique (DUERP)", "Construire et suivre le plan de prévention"],
  programme=[('Le cadre', "Principes généraux de prévention, acteurs de la prévention, rôle du salarié compétent."), ("L'évaluation des risques", "Unités de travail, dangers, cotation, mesures existantes."), ('Le document unique', "Contenu, mise à jour, conservation."), ("Le plan d'action", "Priorités, responsables, échéances, suivi."), ('Atelier', "Évaluation d'une unité de travail de votre entreprise.")],
  note="En tant qu'IPRP, je peux aussi réaliser ou mettre à jour votre DUERP. <a class=\"link-arrow\" href=\"conseil.html#missions\">Voir la mission DUERP</a>"),
]
FAQ_QSE = [
 ("Qu'est-ce qu'une formation QSE ?", "Une formation qualité, sécurité, environnement apprend à vos équipes à organiser et améliorer le travail selon les normes ISO 9001 (qualité), ISO 45001 (santé-sécurité au travail) et ISO 14001 (environnement) : maîtriser les processus, prévenir les risques, réduire les impacts et progresser en continu."),
 ("Ces formations délivrent-elles un diplôme ?", "Non. Ce sont des formations professionnelles courtes pour les entreprises, réalisées dans vos locaux, avec une attestation individuelle. Elles ne remplacent pas un diplôme en management QSE."),
 ("Préparez-vous à la certification ISO ?", "Je forme vos équipes et vos auditeurs internes, et je peux vous accompagner dans la démarche en conseil. La certification elle-même est délivrée par un organisme certificateur accrédité, à l'issue de son propre audit."),
 ("Faut-il désigner un référent sécurité ?", "Oui. Le Code du travail (art. L.4644-1) impose à l'employeur de désigner un ou plusieurs salariés compétents pour s'occuper de la prévention des risques professionnels. À défaut de compétences en interne, il peut faire appel à un IPRP enregistré."),
]

def build_qse():
    return theme_page('formation-qse.html', 'Formations QSE',
        'Formations QSE en entreprise <span class="accent">à Paris et en Île-de-France</span>',
        "Management qualité, sécurité, environnement, audit interne, AMDEC, évaluation des risques : des formations courtes dans vos locaux, par un formateur titulaire d'un Master QSE et IPRP déclaré.",
        [('award', 'Master QSE'), ('scale', 'IPRP déclaré'), ('building', 'Intra-entreprise'), ('file', 'Attestations individuelles')],
        QSE, 'Formation%20QSE', FAQ_QSE, 'Formons vos équipes à la démarche QSE',
        "Dites-moi où en est votre démarche et combien de personnes former. Programme et devis sous 48 h.",
        'Formation QSE en entreprise à Paris | Audit interne, AMDEC, ISO',
        "Formations QSE dans vos locaux en Île-de-France : management qualité, sécurité, environnement, auditeur interne ISO 9001, 14001 et 45001, AMDEC, référent sécurité.")
