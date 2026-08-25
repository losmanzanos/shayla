#!/usr/bin/env python3
"""Page content + writer. Run:  python3 build_content.py"""
import io, json
from build_pages import page, head_block, cta, SITE

W = lambda slug, html: io.open(slug, "w", encoding="utf-8").write(html)
OUT = []

def emit(slug, **kw):
    W(slug, page(slug, **kw)); OUT.append(slug)

# ─────────────────────────────────────────────── ABOUT
emit("about.html",
  title="About | Golden Hour Wellness Colorado",
  desc="A therapist-owned counseling practice in Colorado specializing in trauma, EMDR and addiction counseling. Founded by Shayla Martinez-O'Brien, LPC, LAC.",
  body=head_block("About", "A practice built around the person in the room.",
       "Golden Hour Wellness Colorado, LLC is a small, therapist-owned counseling practice serving clients across the state.") + '''
<section class="section">
  <div class="wrap prose">
    <p>The practice was founded by <a href="shayla.html">Shayla Martinez-O&rsquo;Brien</a>, a Licensed Professional Counselor and Licensed Addiction Counselor with 11 years of clinical practice. What began as one clinician is now a small, hand-picked team.</p>

    <p>We believe true healing comes from an increased ability to tolerate challenging emotion, paired with a clearer understanding of your own value system. That work is slow, human, and worth it, and you don&rsquo;t have to do it alone.</p>

    <h2>How we work</h2>
    <p>Therapy here is collaborative rather than prescriptive. You set the pace. We bring the training, the structure, and an honest read on what seems to be helping.</p>
    <p>Sessions are available in person and by telehealth anywhere in Colorado. If you&rsquo;re not sure what you need yet, that&rsquo;s a normal place to start, and a free consultation is the right first step.</p>

    <h2>Who we work with</h2>
    <p>Adults navigating trauma, anxiety, depression, substance use, relationship strain and major life transitions. We also run <a href="mamas-golden-hour.html">Mama&rsquo;s Golden Hour</a>, a virtual therapy group for Colorado mothers.</p>

    <div class="callout">
      <p><strong>If we&rsquo;re not the right fit, we&rsquo;ll say so.</strong> Part of a first conversation is working out whether this practice is the right place for you. Sometimes the honest answer is a referral elsewhere, and that&rsquo;s a good outcome too.</p>
    </div>

    <h2>Insurance</h2>
    <p>We&rsquo;re in-network with <strong>Aetna</strong>, <strong>United Healthcare</strong> and <strong>Cigna</strong>. If your plan isn&rsquo;t one of those, get in touch anyway and we can talk through out-of-network reimbursement and self-pay rates. You&rsquo;re also entitled to a <a href="good-faith-estimate.html">Good Faith Estimate</a> before your first session.</p>
    <p class="callout warn"><strong>Please note:</strong> insurance is not accepted for Mama&rsquo;s Golden Hour. Group sessions are self-pay.</p>
  </div>
</section>''' + cta())

# ─────────────────────────────────────────────── TEAM
emit("team.html",
  title="Our Team | Golden Hour Wellness Colorado",
  desc="Meet the clinicians at Golden Hour Wellness Colorado: Shayla Martinez-O'Brien LPC LAC, Chrissie Flynn-Weirich LAC, and Ashley LeRossignol LPC.",
  body=head_block("Our team", "Three clinicians. Roughly 34 years of practice between them.") + '''
<section class="section">
  <div class="wrap">
    <div class="cards">
      <a class="card" href="shayla.html">
        <h3>Shayla Martinez-O&rsquo;Brien</h3>
        <p><strong>LPC, LAC &middot; Founder</strong><br>Trauma, EMDR and addiction. Accepting individual clients.</p>
        <span class="more">Read profile &rarr;</span>
      </a>
      <a class="card" href="chrissie.html">
        <h3>Chrissie Flynn-Weirich</h3>
        <p><strong>LAC &middot; Wellness Facilitator</strong><br>Substance use, anxiety and life transitions. Accepting individual clients.</p>
        <span class="more">Read profile &rarr;</span>
      </a>
      <a class="card" href="ashley.html">
        <h3>Ashley LeRossignol</h3>
        <p><strong>LPC &middot; Consultant &amp; group facilitator</strong><br>Co-facilitates Mama&rsquo;s Golden Hour. Does not take individual clients here.</p>
        <span class="more">Read profile &rarr;</span>
      </a>
    </div>

    <div class="callout" style="margin-top:2.5rem; max-width:44rem">
      <p><strong>Scheduling.</strong> Individual sessions are available with Shayla and Chrissie. Ashley&rsquo;s work with the practice is limited to co-facilitating <a href="mamas-golden-hour.html">Mama&rsquo;s Golden Hour</a> and clinical consultation.</p>
    </div>
  </div>
</section>''' + cta())

# ─────────────────────────────────────────────── PROFILES
def profile(slug, name, cred, img, w, h, tags, lead, paras, bookable, extra_meta):
    person = {"@context":"https://schema.org","@type":"Person","name":name,
              "jobTitle":cred,"worksFor":{"@type":"MedicalBusiness","name":"Golden Hour Wellness Colorado, LLC"},
              "url":f"{SITE}/{slug}"}
    book = ('<a class="btn btn-primary" href="index.html#book">Book with ' + name.split()[0] + '</a>'
            if bookable else
            '<a class="btn btn-outline" href="mamas-golden-hour.html">About the group</a>')
    meta = "".join(f"<li><b>{k}</b><span>{v}</span></li>" for k, v in extra_meta)
    body = head_block("Our team", name, cred) + f'''
<section class="section">
  <div class="wrap bio-grid">
    <div class="bio-photo">
      <img src="assets/img/{img}" width="{w}" height="{h}" alt="Portrait of {name}">
      <ul class="meta-list">{meta}</ul>
    </div>
    <div class="prose" style="max-width:none">
      <p class="lede">{lead}</p>
      {"".join(f"<p>{p}</p>" for p in paras)}
      <p style="margin-top:2rem">{book}</p>
    </div>
  </div>
</section>'''
    emit(slug, title=f"{name} | Golden Hour Wellness Colorado",
         desc=lead[:180], body=body, active="team.html",
         extra_head=f'<script type="application/ld+json">{json.dumps(person)}</script>')

profile("shayla.html", "Shayla Martinez-O&rsquo;Brien", "LPC, LAC &middot; Founder",
  "shayla.jpg", 1086, 1357, [],
  "A Licensed Professional Counselor and Licensed Addiction Counselor in Colorado, specializing in trauma therapy, with 11 years of practice.",
  ["I use Eye Movement Desensitization and Reprocessing (EMDR) among other trauma-focused approaches to help clients better tolerate emotion related to past and present traumas and stressors.",
   "I believe true healing comes from an increased ability to tolerate challenging emotion along with a better understanding of one&rsquo;s own value system. I would love the opportunity to walk alongside you in your journey to improved self-awareness, strengthened positive neural pathways, and deeper connection with who you are.",
   "I&rsquo;m a Colorado native and do my very best to live up to the stereotype. I&rsquo;m married, a mother of two, with two lab mixes at home.",
   "I founded Golden Hour Wellness Colorado and work as both clinician and business manager. I also co-facilitate <a href=\"mamas-golden-hour.html\">Mama&rsquo;s Golden Hour</a>."],
  True,
  [("Licence", "LPC, LAC (Colorado)"), ("Experience", "11 years"),
   ("Focus", "Trauma, EMDR, addiction"), ("Sessions", "In person &amp; telehealth")])

profile("chrissie.html", "Chrissie Flynn-Weirich", "LAC &middot; Wellness Facilitator",
  "chrissie.jpg", 1086, 1357, [],
  "A Licensed Addiction Counselor and Wellness Facilitator with over 13 years supporting people living with substance use disorders.",
  ["Together we will identify your strengths and your passions. Side by side we will assess what&rsquo;s working, what&rsquo;s not, and set meaningful goals that align with your vision of your best self. Each session will envelop empathy and unconditional regard.",
   "I&rsquo;ll support and empower your narrative through mindfulness and compassion as we explore challenges and discover solutions for navigating major life changes with greater clarity and sense of purpose, reconnecting with yourself and others.",
   "I believe in the healing powers of self-reflection, curiosity, self-compassion and connection. Outside of sessions I enjoy baking, reading, music and dance, and my own wellness comes from meditation, yoga and poetry."],
  True,
  [("Licence", "LAC (Colorado)"), ("Experience", "13+ years"),
   ("Focus", "Substance use, anxiety"), ("Sessions", "Telehealth")])

profile("ashley.html", "Ashley LeRossignol", "LPC &middot; Consultant &amp; group facilitator",
  "ashley.jpg", 1103, 1378, [],
  "Ashley co-facilitates Mama&rsquo;s Golden Hour alongside Shayla and consults on clinical practice. She does not take individual clients through Golden Hour Wellness.",
  ["Working from a solution-oriented framework, Ashley brings over 10 years of experience treating anxiety, depression, relationship challenges, and family and work stressors. She utilizes Cognitive Behavioral Therapy, highlighting the ways mood, thoughts and behaviors shape one another, and emphasising self-compassion along the way.",
   "She received her master&rsquo;s degree in counseling psychology from the University of San Francisco. Outside of therapy you&rsquo;ll find her outdoors, traveling, cooking and exploring new restaurants, places, cultures and communities.",
   "<strong>Scheduling note:</strong> individual sessions at Golden Hour Wellness are available with Shayla and Chrissie. Ashley&rsquo;s role here is the group and consultation."],
  False,
  [("Licence", "LPC"), ("Experience", "10+ years"),
   ("Role", "Group &amp; consulting"), ("Individual clients", "Not through this practice")])

print("wrote:", len(OUT), "pages")
for o in OUT: print("  ", o)
