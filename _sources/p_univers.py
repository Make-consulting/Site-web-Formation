from partials import ico, page
from p_index import faq_item

DEMO = 'contact.html?univers=firetraining&amp;sujet=D%C3%A9mo%20FireTraining%20MS'

def feat(icon, t, d, tag=''):
    tg = f'<span class="pill pill--acc" style="position:absolute;top:28px;right:28px">{tag}</span>' if tag else ''
    return f'<article class="card"><span class="ico-tile">{ico(icon)}</span>{tg}<h3>{t}</h3><p>{d}</p></article>'

def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{ico("check")}{i}</li>' for i in items) + '</ul>'

FT = f'''
<section class="hero hero--night">
  <canvas data-embers="60" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <span class="eyebrow">Réalité mixte · Formation incendie</span>
      <h1 class="h-anim">FireTraining MS, <span class="accent">le feu sans le danger.</span></h1>
      <p class="lead">Une application de réalité mixte pour Meta Quest, conçue par un formateur SSIAP 3 et sapeur-pompier volontaire. Le départ de feu apparaît dans la salle, le stagiaire agit, le formateur observe et débriefe.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="{DEMO}">Demander une démo {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="#formules">Voir les formules</a>
      </div>
      <div class="hero-proof">
        <span>{ico('headset')}Meta Quest</span>
        <span>{ico('layers')}Complément du terrain</span>
        <span>{ico('users')}Équipes, OF, formateurs</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="media video" data-video="-pCvWiTv1ec">
        <img src="assets/firetraining-screenshot.jpg" alt="" width="1200" height="799" fetchpriority="high">
        <button class="video-play" type="button" aria-label="Lire la vidéo de démonstration de FireTraining MS"><span class="video-btn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg></span><span class="video-label">Voir la démo vidéo</span></button>
      </div>
      <p class="video-note">La lecture charge la vidéo depuis YouTube (Google).</p>
    </div>
  </div>
</section>

<section class="section" id="apports">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Apports pédagogiques</span>
      <h2>Ce que la réalité mixte ajoute à vos sessions</h2>
      <p class="lead">Le stagiaire reste dans la salle et voit ses collègues. Le feu, la fumée et la propagation sont superposés à l'environnement réel.</p>
    </div>
    <div class="grid-3" data-stagger>
      {feat('flame', 'Scénarios réalistes', 'Départ de feu, fumée, propagation : le stagiaire vit la situation avant d&#39;y être confronté.')}
      {feat('gauge', 'Évaluation objective', 'Temps de réaction, choix de l&#39;agent extincteur, prise de décision : mesurés pendant l&#39;exercice.')}
      {feat('repeat', 'Scénarios rejouables', 'Chaque stagiaire refait le scénario autant de fois que nécessaire, sans consommer d&#39;extincteur.')}
      {feat('usercheck', 'Accessible à tous', 'Utile pour les stagiaires qui ne peuvent pas pratiquer physiquement, avec moins de prise de risque.')}
      {feat('box', 'Vos locaux modélisés', 'Reproduire votre bâtiment dans l&#39;application pour un exercice au plus près du réel.', 'En développement')}
      {feat('layers', 'Complément du terrain', 'L&#39;application complète la manipulation réelle des extincteurs. Les attestations restent conformes à la réglementation.')}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">En session</span>
      <h2>Comment se déroule un exercice</h2>
    </div>
    <ol class="steps steps--4" data-stagger>
      <li><h4>Briefing</h4><p>Rappel du triangle du feu, des classes de feu et du choix de l&#39;extincteur.</p></li>
      <li><h4>Mise en casque</h4><p>Le stagiaire garde la vue sur la salle grâce à la vidéo en transparence du Quest.</p></li>
      <li><h4>Scénario</h4><p>Le formateur lance le départ de feu. Le stagiaire alerte, choisit l&#39;agent et intervient.</p></li>
      <li><h4>Débriefing</h4><p>Retour immédiat sur les gestes et les temps de réaction, puis passage au suivant.</p></li>
    </ol>
  </div>
</section>

<section class="section" id="formules">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Formules</span>
      <h2>Trois façons d&#39;utiliser FireTraining MS</h2>
      <p class="lead">Selon que vous formez vos propres équipes, que vous êtes un organisme de formation ou un formateur indépendant.</p>
    </div>
    <div class="grid-3" data-stagger>
      <article class="card offer">
        <span class="offer-for">Pour vos équipes</span>
        <h3>Formation avec FireTraining MS</h3>
        <p>J&#39;interviens dans vos locaux avec l&#39;application intégrée à la formation incendie. Le matériel est fourni.</p>
        {checks(['Intra-entreprise, en Île-de-France et en France selon conditions', 'Formation incendie et module réalité mixte', 'Casques fournis', 'Rapport individuel des stagiaires', 'Attestations conformes'])}
        <p class="price">Devis selon vos effectifs</p>
        <a class="btn btn-ghost" href="contact.html?univers=firetraining&amp;sujet=Formation%20avec%20FireTraining%20MS%20(mes%20%C3%A9quipes)">Demander un devis {ico('arrow', extra=' ico-arrow')}</a>
      </article>
      <article class="card card--feature offer">
        <span class="offer-for">Pour les organismes de formation</span>
        <h3>Licence annuelle</h3>
        <p>Intégrez FireTraining MS à votre catalogue, avec support, mises à jour et nouveaux scénarios.</p>
        {checks(['Accès complet à l&#39;application', 'Prise en main formateur (2 h)', 'Support technique inclus', 'Mises à jour et nouveaux scénarios', 'Tableau de bord formateur'])}
        <p class="price" style="color:rgba(255,255,255,.7)">Tarif annuel sur devis</p>
        <a class="btn btn-primary" href="firetraining-pro.html#of">Découvrir la licence {ico('arrow', extra=' ico-arrow')}</a>
      </article>
      <article class="card offer">
        <span class="offer-for">Pour les formateurs indépendants</span>
        <h3>Achat de l&#39;application</h3>
        <p>Un achat unique, sans abonnement. Des scénarios supplémentaires sont disponibles à l&#39;unité.</p>
        {checks(['Fichier d&#39;installation livré', 'Scénario tronc commun inclus', 'Sans abonnement annuel', 'Scénarios additionnels à l&#39;unité', 'Utilisation en autonomie'])}
        <p class="price">Tarif sur demande</p>
        <a class="btn btn-ghost" href="firetraining-pro.html#formateur">Découvrir l&#39;achat {ico('arrow', extra=' ico-arrow')}</a>
      </article>
    </div>
  </div>
</section>

<section class="section section--tint" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Avant de vous lancer</h2>
    </div>
    <div class="faq reveal">
      {faq_item("Quel matériel faut-il ?", "FireTraining MS fonctionne sur les casques Meta Quest. Pour la formule formation, je fournis le matériel. Pour la licence ou l&#39;achat, je vous conseille sur les équipements compatibles.", True)}
      {faq_item("L&#39;application remplace-t-elle la formation pratique ?", "Non. C&#39;est un complément pédagogique. Les attestations délivrées correspondent à des formations conformes au référentiel réglementaire, avec les éléments pratiques obligatoires, dont la manipulation réelle d&#39;extincteurs.")}
      {faq_item("Puis-je tester avant de m&#39;engager ?", "Oui. Je propose des démonstrations sur rendez-vous, à Paris ou chez vous en Île-de-France.")}
      {faq_item("L&#39;offre est-elle disponible hors Île-de-France ?", "La formule formation est proposée en Île-de-France, et ailleurs en France selon les conditions de la mission. La licence et l&#39;achat sont disponibles partout en France.")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band reveal" style="background:var(--night)">
      <canvas data-embers="40" aria-hidden="true"></canvas>
      <div>
        <h2>Voyez l&#39;application en conditions réelles</h2>
        <p>Une démonstration de 30 minutes, dans vos locaux ou à Paris, pour juger par vous-même.</p>
      </div>
      <div class="btns">
        <a class="btn btn-primary" href="{DEMO}">Demander une démo {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a>
      </div>
    </div>
  </div>
</section>
'''

DIAG = 'contact.html?univers=conseil&amp;sujet=Diagnostic%20initial%20offert%20(30%20min)'

def mission(icon, tag, t, d, items, sujet):
    return f'''<article class="card"><span class="ico-tile">{ico(icon)}</span><span class="pill">{tag}</span><h3>{t}</h3><p>{d}</p>{checks(items)}<a class="link-arrow" href="contact.html?univers=conseil&amp;sujet={sujet}">En parler {ico('arrow')}</a></article>'''

CO = f'''
<section class="hero hero--conseil">
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <span class="eyebrow">Conseil en prévention · IPRP déclaré</span>
      <h1 class="h-anim">Le conseil, avec <span class="accent">MAKE Consulting.</span></h1>
      <p class="lead">Document unique, audits QSE et ISO, prévention des RPS, sécurité incendie : mes missions de conseil sont présentées sur le site de mon cabinet, make-consulting.fr.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="https://make-consulting.fr/" target="_blank" rel="noopener">Aller sur make-consulting.fr {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-ghost" href="https://make-consulting.fr/contact.html?sujet=Diagnostic%20initial%20offert%20(30%20min)" target="_blank" rel="noopener">Diagnostic offert (30 min)</a>
      </div>
      <div class="hero-proof">
        <span>{ico('scale')}IPRP, art. L.4644-1</span>
        <span>{ico('shield')}Sapeur-pompier volontaire</span>
        <span>{ico('clock')}Devis sous 48 h</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="diag-card">
        <span class="eyebrow">Formation et conseil</span>
        <div class="big">Un seul interlocuteur</div>
        <p style="color:var(--ink-2)">Le diagnostic identifie les risques, la formation prépare vos équipes. Les deux se complètent et se commandent auprès de la même personne.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="missions">
  <div class="wrap">
    <div class="legal-note reveal" id="iprp" style="margin-bottom:56px">{ico('scale')}<p><strong>IPRP : Intervenant en Prévention des Risques Professionnels.</strong> Statut reconnu par le Code du travail (art. L.4644-1). Mes interventions s&#39;inscrivent dans votre obligation légale d&#39;évaluation et de prévention des risques.</p></div>
    <div class="sec-head reveal"><span class="eyebrow">Missions</span><h2>Les missions de conseil</h2><p class="lead">Chaque mission est détaillée sur make-consulting.fr : déroulé, livrables, références et tarifs.</p></div>
    <div class="grid-3" data-stagger>
      <a class="card cat-card" href="https://make-consulting.fr/duerp.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('clipboard')}</span><h3>DUERP clé en main</h3><p>Document unique réalisé de A à Z, plan d&#39;action priorisé.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a><a class="card cat-card" href="https://make-consulting.fr/audit-qse.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('award')}</span><h3>Audit QSE et normes ISO</h3><p>Audit de conformité, audit interne, ISO 9001, 14001, 45001.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a><a class="card cat-card" href="https://make-consulting.fr/prevention-rps.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('activity')}</span><h3>Prévention des RPS</h3><p>Diagnostic, restitution anonymisée et plan d&#39;action.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a><a class="card cat-card" href="https://make-consulting.fr/securite-incendie.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('flame')}</span><h3>Sécurité incendie</h3><p>Audit de conformité et plans de défense incendie pour sites ICPE.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a><a class="card cat-card" href="https://make-consulting.fr/diagnostic-ssiap.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('radio')}</span><h3>Diagnostic des services SSIAP</h3><p>Évaluation en situation des agents de sécurité incendie.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a><a class="card cat-card" href="https://make-consulting.fr/continuite-activite.html" target="_blank" rel="noopener"><span class="ico-tile">{ico('refresh')}</span><h3>PCA et PCS</h3><p>Continuité d&#39;activité et plan communal de sauvegarde.</p><span class="link-arrow">Voir sur make-consulting.fr {ico('arrow')}</span></a>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Après le diagnostic</span>
      <h2>Former vos équipes</h2>
      <p class="lead">Un document unique ou un audit débouche souvent sur un plan de formation : incendie, SST, risques chimiques, travail en hauteur, prévention des RPS.</p>
      <a class="link-arrow" href="formations.html">Voir le catalogue des formations {ico('arrow')}</a>
    </div>
    <figure class="quote reveal" style="margin:0"><blockquote>Le DUERP que Maxence a réalisé pour notre mairie est d&#39;une qualité remarquable. Complet, opérationnel, et présenté de façon limpide au conseil municipal.</blockquote><figcaption><strong>Directrice générale des services</strong>Commune de 12 000 habitants, Val-de-Marne</figcaption></figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <div><h2>Faisons le point en 30 minutes</h2><p>Un échange offert, sans engagement, pour savoir où vous en êtes et par quoi commencer.</p></div>
      <div class="btns">
        <a class="btn btn-light" href="https://make-consulting.fr/contact.html?sujet=Diagnostic%20initial%20offert%20(30%20min)" target="_blank" rel="noopener">Réserver le diagnostic {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a>
      </div>
    </div>
  </div>
</section>
'''

def build_ft():
    return page('FireTraining MS | Réalité mixte pour la formation incendie',
                'FireTraining MS : application de réalité mixte pour Meta Quest, en complément de la formation incendie. Formation de vos équipes, licence pour organismes de formation, achat pour formateurs.',
                'firetraining-ms.html', 'firetraining', FT)

def build_co():
    return page('Conseil en prévention et QSE avec MAKE Consulting | IPRP',
                'DUERP clé en main, prévention des RPS, audit sécurité, normes ISO, PCA et PCS. Maxence Soileux, IPRP déclaré en Île-de-France. Diagnostic initial offert de 30 minutes.',
                'conseil.html', 'conseil', CO)
